using System.Net.Sockets;
using Polly;

const string Hostname = "localhost";
const string UnixSocketPath = "/tmp/foo.sock";

// We are using Polly here to ensure our backend is available.
var policy = Policy.Handle<Exception>().RetryForever();
policy.Execute(() =>
{
    if (!File.Exists(UnixSocketPath))
    {
        throw new InvalidOperationException($"Foo API socket {UnixSocketPath} not available.");
    }
});

// Request data from Unix socket before, the hard way...
using var socket = new Socket(AddressFamily.Unix, SocketType.Stream, ProtocolType.IP);

var endpoint = new UnixDomainSocketEndPoint(UnixSocketPath);
socket.Connect(endpoint);

var requestBytes = System.Text.Encoding.UTF8.GetBytes($"GET / HTTP/1.0\r\nHost: {Hostname}\r\nAccept: */*\r\n\r\n");
socket.Send(requestBytes);

byte[] receivedBytes = new byte[1024];
socket.Receive(receivedBytes, 1024, SocketFlags.None);

Console.WriteLine(System.Text.Encoding.UTF8.GetString(receivedBytes));

// Using SocketsHttpHandler to request data from Unix socket.  
// https://docs.microsoft.com/de-de/dotnet/api/system.net.http.socketshttphandler?view=net-6.0
var httpHandler  = new SocketsHttpHandler
{
    ConnectCallback = async (context, token) =>
    {
        var socket = new Socket(AddressFamily.Unix, SocketType.Stream, ProtocolType.IP);
        var endpoint = new UnixDomainSocketEndPoint(UnixSocketPath);
        await socket.ConnectAsync(endpoint).ConfigureAwait(false);

        return new NetworkStream(socket, ownsSocket: false);
    }
    //SslOptions = new SslClientAuthenticationOptions
    //{
    //    EnabledSslProtocols = SslProtocols.Tls12 | SslProtocols.Tls13,
    //    RemoteCertificateValidationCallback = new RemoteCertificateValidationCallback((message, cert, chain, sslPolicyErrors) =>
    //    {
    //        // Custom server certificate validation logic...
    //        return true;
    //    })
    //}
};

var client = new HttpClient(httpHandler);
client.BaseAddress = new Uri($"http://{Hostname}");

var response = await client.GetAsync("/").ConfigureAwait(false);
var content = await response.Content.ReadAsStringAsync().ConfigureAwait(false);

Console.WriteLine(content);
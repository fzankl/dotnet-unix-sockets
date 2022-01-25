using System.Net.Sockets;
using Refit;

const string Hostname = "localhost";
const string UnixSocketPath = "/tmp/foo.sock";

var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddRefitClient<IFooApi>()
    .ConfigurePrimaryHttpMessageHandler((_) =>
    {
        return new SocketsHttpHandler
        {
            ConnectCallback = async (_, _) =>
            {
                var socket = new Socket(AddressFamily.Unix, SocketType.Stream, ProtocolType.Unspecified);
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
    })
    .ConfigureHttpClient((_, client) =>
    {
        client.BaseAddress = new Uri($"http://{Hostname}");
    });

var app = builder.Build();

app.MapGet("/", (IFooApi fooApi) =>
{
    return fooApi.GetFoo();
});

app.Run();

internal interface IFooApi
{
    [Get("/")]
    Task<string> GetFoo();
}
using System.Net.Sockets;
using Grpc.Net.Client;

var app = WebApplication.CreateBuilder(args).Build();

app.MapGet("/", async () =>
{
    var socketsHttpHandler = new SocketsHttpHandler
    {
        ConnectCallback = async (_, cancellationToken) =>
        {
            var endpoint = new UnixDomainSocketEndPoint("/tmp/foo.sock");
            var socket = new Socket(AddressFamily.Unix, SocketType.Stream, ProtocolType.Unspecified);

            try
            {
                await socket.ConnectAsync(endpoint, cancellationToken).ConfigureAwait(false);
                return new NetworkStream(socket, false);
            }
            catch
            {
                socket.Dispose();
                throw;
            }
        }
    };
    
    var channel = GrpcChannel.ForAddress("http://localhost", new GrpcChannelOptions
    {
        HttpHandler = socketsHttpHandler
    });
    
    var foo = new UnixSocketDemo.Foo.FooClient(channel);

    var response = await foo.GetFooAsync(new UnixSocketDemo.FooRequest
    {
        Message = "Hello from .NET"
    });

    return response.Message;
});

app.Run();
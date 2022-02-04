using System.Net.Sockets;
using Refit;

const string BaseAddress = "http://localhost";
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
        };
    })
    .ConfigureHttpClient((_, client) =>
    {
        client.BaseAddress = new Uri(BaseAddress);
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
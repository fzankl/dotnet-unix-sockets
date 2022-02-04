const string UnixSocketPath = "/tmp/foo.sock";

if (File.Exists(UnixSocketPath))
{
    File.Delete(UnixSocketPath);
}

var builder = WebApplication.CreateBuilder(args);
builder.WebHost.ConfigureKestrel(options =>
{
    options.ListenUnixSocket(UnixSocketPath);
});

var app = builder.Build();
app.MapGet("/", () => "Hello from Foo API served via Unix Socket.");

app.Run();
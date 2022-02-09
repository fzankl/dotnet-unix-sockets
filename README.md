# Unix Sockets in .NET 6 / ASP.NET 6

Example how to use and interact with Unix Domain Sockets using .NET 6

-----------------------------------

This example shows how to work with Unix Domain Sockets in .NET 6. The implementation shows the basic setup to serve and consume applications. In addition, inter-process communication between services written in .NET and Python is demonstrated.

Detailed information:

  * English: https://www.fzankl.de/en/blog/unix-domain-sockets-in-dotnet-basics-and-real-world-examples
  * German: https://www.fzankl.de/de/blog/unix-domain-sockets-in-dotnet-grundlagen-und-praktische-beispiele

## How to run this sample

To run this code you have to install and configure WSL 2. Then you can use Visual Studio Code using a WSL 2 remote session.

In [another post](https://www.fzankl.de/en/blog/using-wsl2-in-enterprises) you can learn how to configure and run WSL 2 within a corporate environment.

### Basics

Then you are able to start the `Server` project which will host an .NET 6 minimal API and serves it via a Unix Socket within the WSL 2 distro.

After that you can start either the `ClientConsole` or `ClientWeb` project, both demonstrating different client side implementations. Detailed explenation can be found in the blog posts mentioned above.

### Demo

An additional demo shows how to exchange data between .NET and Python with gRPC over Unix Domain Sockets. To run the demo, you have to execute the Python script. Afterwards, the .NET-based client can be used to execute a request against this server.

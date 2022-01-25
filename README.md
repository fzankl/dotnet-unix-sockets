# Unix Sockets in .NET 6 / ASP.NET 6

Example how to use and interact with Unix Sockets using .NET 6

-----------------------------------

This example shows how to work with Unix Sockets in .NET 6. The implementation shows the basic setup to serve and consume applications via sockets.

Detailed information:

 * English: TBD
 * German: TBD

## How to run this sample

To run this sample you have to install and configure WSL2.
In [another post](https://www.fzankl.de/en/blog/using-wsl2-in-enterprises) you can learn how to configure and run WSL2 within a corporate environment.


Then you are able to start the `Server` project which will host an .NET 6 minimal API and serves it via a Unix Socket within the WSL2 distro.

After that you can start either the `ClientConsole` or `ClientWeb` project, both demonstrating different client side implementations. Detailed explenation can be found in the blog posts mentioned above.
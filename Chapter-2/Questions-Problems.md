# Review-Questions Chapter 2

## SECTION 1.1

### R1

1. Web -- HTTP, HTTPS
2. BitTorrent -- BitTorrent
3. E-mail -- SMTP
4. File transfer -- FTP
5. Remote terminal -- Telnet

### R2

Network provides information exchange services between applications on different or the same host.

The application architecture determines the format of information and the behavior sending and receiving information, which is the application layer protocol.

By using the services provided by the network layer, applications can implement many functions, including sending emails, browsing the web, downloading\exchanging files, and remote control.

### R3

The process waiting/checking the information send by other process is the server.

### R4

The process waiting/checking the information send by other process is the server.

As in Page 116:
> In the context of a communication session between a pair of processes, the pro-
> cess that initiates the communication (that is, initially contacts the other process
> at the beginning of the session) is labeled as the client. The process that waits to
> be contacted to begin the session is the server.

### R5

IP address and port

### R6

The protocol defines communication with Web Servers.

Without it, a web application has no way of knowing how to send a page request, nor how to render a page from an html file.

A browser to send/receive message with servers and renders pages according to the behavior and message format defined by the HTTP protocol.

### R7

Instant messaging software.

Such as: Twitter, Telegram, Wechat

Stock trading software. Requires no data loss and timing.

### R8

* Reliable data transfer: Only TCP
* Error checking(Included in Reliable data transfer): Both
* Multiplexing Demultiplexing: Both
* Congestion Control: Only TCP

### R9

TLS operate at the application layer.

First establish a TCP connection. A TLS handshake then occurs, and finally the data is transferred using the TLS-exposed socket.

The server must support TLS protocol.

## SECTIONS 2.2–2.5

### R10

Just like greeting, first indicate your identity and purpose, then start conversation.
Also, when someone wants to end a conversation and says something tactful.

First request to establish a connection, give some replies and reach some consensus - set parameters, allocate resources, and then start the conversation.

When ending the connection, send request confirm and release related resources.

### R11

A stateless protocol maintains no information about the clients. IMAP and SMTP are stateful.

### R12

Cookies, also account with password.

### R13

Browser caching can render pages as fast as no network delays.

Caching in Web cache server usually more closer to user.

Some objects may not stored in Web cache and must get from higher server.

### R14

```bash
sudo pacman -S inetutils
telnet gaia.cs.umass.edu 80
```

```input
GET / HTTP/1.1
Host: gaia.cs.umass.edu
IF-modified-since: Tue, 01 Mar 2016 18:57:50 GMT
```

```output
HTTP/1.1 304 Not Modified
Date: Tue, 17 Dec 2024 15:41:15 GMT
Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips PHP/7.4.33 mod_perl/2.0.11 Perl/v5.16.3
ETag: "a5b-52d015789ee9e"
```

### R15

No strict constraints for HTTP body.

`Content-Type` that client sends to server maybe one but not enforced.

SMTP message body has constraints: must ASCII text

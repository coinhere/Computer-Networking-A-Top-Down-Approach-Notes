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

### R16

1. Alice's host to Gmail web server: HTTPS
2. Gmail web server to Gmail SMTP server: SMTP
3. Gmail SMTP server to Bob's SMTP server: SMTP
4. Bob's SMTP server to Bob's host: IMAP

### R17
>
>Delivered-To:
Received:
X-Google-Smtp-Source:
X-Received:
ARC-Seal:
ARC-Message-Signature:
ARC-Authentication-Results:
Return-Path:
Received:
Received-SPF:
Authentication-Results:
DKIM-Signature:
DKIM-Signature:
Received:
Received:
Date:
From:
Message-ID:
Subject:
Mime-Version:
Reply-To:
X-Feedback-ID:
X-SG-EID:
X-SG-ID:
To:
X-Entity-ID:
Content-Type:
Content-Transfer-Encoding:

### R18

In page 144:

>by opening multiple parallel TCP connections, thereby having objects in the
same web page sent in parallel to the browser. This way, the small objects can arrive
at and be rendered in the browser much faster, thereby reducing user-perceived delay.

### R19

In page 162:

>MX records allow the hostnames of mail servers to have simple
aliases. Note that by using the MX record, a company can have the same aliased
name for its mail server and for one of its other servers (such as its Web server).
To obtain the canonical name for the mail server, a DNS client would query for
an MX record; to obtain the canonical name for the other server, the DNS client
would query for the CNAME record

### R20

Recursive DNS queries is let the DNS server do all the DNS quering thing, typically used in a local DNS server, while iterative queries the DNS server just told you where to get the address.

Recursive DNS queries are a thing where the DNS server does all the DNS queries and finally returns the ip address to you, this is usually used in local DNS servers.

While in an iterative query, the DNS server simply tells you which DNS server you should get the address from. And you may ask multiple times.

In page 160:
>The example shown in Figure 2.19 makes use of both recursive queries and
iterative queries. The query sent from cse.nyu.edu to dns.nyu.edu is a
recursive query, since the query asks dns.nyu.edu to obtain the mapping on its
behalf. However, the subsequent three queries are iterative since all of the replies
are directly returned to dns.nyu.edu. In theory, any DNS query can be itera-
tive or recursive. For example, Figure 2.20 shows a DNS query chain for which all
of the queries are recursive. In practice, the queries typically follow the pattern in
Figure 2.19: The query from the requesting host to the local DNS server is recursive,
and the remaining queries are iterative

## SECTION 2.5

### R21

When the number of downloading users far exceeds the server's carrying capacity.
And the network is blocked.

The scalability of P2P architecture can meet the growth of download volume.

### R22

In page 172:

>Importantly, every 30 seconds, she also picks one additional neighbor at
random and sends it chunk

So Alice will receive a chunk from a user that randomly selects her.

### R23

Peers already in the swarm and connected to others can continue sharing files without issue.

New peers trying to join the swarm via the tracker won't receive the list of other peers, making it harder to start downloading the file.

## SECTION 2.6

### R24

| Server Placement | Description | Advantages | Drawbacks |
|-|-|-|-|
| Enter Deep | lots of small servers closer to users | low delays and congestion | higher maintenance |
| Bring Home | large data centers at key location | easier to maintain and low cost | higher delays for far users |

### R25

Where to locate and What to locate(Hardware and Content).

Concerns including:

Location closer to users. Minimize latency.

Cost of Maintenance. If it easy to maintain.

Load Balancing. Ensure that no individual server becomes overloaded.

Content utilization. Is the content the most popular?

Reliance. Services still available if several severs broken.

Security.

## SECTION 2.7

### R26

UDP only requires a socket because it is connectionless. UDP server sockets use different addresses to distinguish messages sent by different clients and use these addresses when communicating with them.

TCP uses connections instead, It uses `serverSocket` as a welcoming socket to establish connections with different clients and assigns a `connectionSocket` to each client. The `connectionSocket` is used to communicate with different clients.

n+1 sockets would need. 1 for welcome, n for connection.

### R27

TCP requires a connection to be established before communication can occur.
The TCP server program must first execute to create a listening socket, enabling it to accept incoming connection requests.
If The TCP server is not running, the client's connection attempt will fail as there is no process to accept the connection.

UDP, on the other hand, is connectionless, and messages sent by the client to the server may be lost if the server is not started at first. But once the server is started, it can receive the subsequent messages sent by the client and reply to it.

# Problems

### P1

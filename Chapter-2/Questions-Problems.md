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

#### a

False, 1 for html file and 3 for images

#### b

True

#### c

False

#### d

False, Date is time when the response was generated.

#### e

False, `204 No Content`, `304 Not Modified` and HEAD requests.

### P2

SMS (Short Message Service) is a widely used messaging protocol that enables the exchange of text messages up to 160 characters between mobile devices. It operates over cellular networks and does not require an internet connection, making it accessible on virtually all mobile phones. However, SMS lacks advanced features such as end-to-end encryption, multimedia support, and group chat capabilities.

iMessage is Apple's proprietary messaging service that allows users to send text messages, photos, videos, and more over the internet. It utilizes Apple's own protocols and infrastructure, providing end-to-end encryption for secure communication. iMessage supports features like read receipts, typing indicators, and group chats, enhancing the messaging experience for Apple device users.

WeChat, developed by Tencent, is a multifaceted messaging platform that combines text messaging, voice and video calls, social media, and payment services. It employs proprietary protocols tailored to its diverse functionalities, enabling seamless integration of various services within a single application. WeChat's protocols are not publicly disclosed, and the platform operates primarily within China's internet ecosystem.

WhatsApp uses the Extensible Messaging and Presence Protocol (XMPP) for real-time messaging. XMPP is an open standard application layer protocol based on TCP, utilizing XML to represent messages, statuses, and user requests. In WhatsApp's implementation, user messages are sent to WhatsApp servers, which then forward them to the target user's smartphone.

The primary differences among these messaging systems lie in their underlying protocols, features, and operational models. SMS is a basic text messaging service operating over cellular networks without internet dependency, lacking advanced features like encryption and multimedia support. iMessage and WhatsApp both offer internet-based messaging with end-to-end encryption, but iMessage is exclusive to Apple devices, while WhatsApp is cross-platform. WeChat distinguishes itself by integrating a wide range of services beyond messaging, including social media and payment functionalities, and operates primarily within China's internet ecosystem. Additionally, WhatsApp's use of XMPP allows for decentralized communication, whereas iMessage and WeChat rely on centralized servers.

### P3

When you enter <http://yourbusiness.com/about.html> into your browser's address bar, several steps occur to display the webpage:

1. DNS Resolution: The browser first resolves the domain name yourbusiness.com to an IP address using the Domain Name System (DNS). This involves sending a DNS query to a DNS server, which returns the corresponding IP address.

2. TCP Connection: With the IP address obtained, the browser establishes a Transmission Control Protocol (TCP) connection to the web server on port 80, the default port for HTTP. This involves a three-way handshake:

* SYN: The browser sends a synchronization request to the server.
* SYN-ACK: The server acknowledges the request.
* ACK: The browser acknowledges the server's response, completing the handshake.

3. HTTP Request: Once the connection is established, the browser sends an HTTP GET request to the server for the resource /about.html. This request includes headers such as Host: yourbusiness.com to specify the target domain.

4. Server Response: The server processes the request and responds with an HTTP response message. If the resource is found, the response includes a 200 OK status code and the HTML content of about.html. If the resource is not found, the server returns a 404 Not Found status code.

5. Rendering the Page: The browser receives the HTML content and begins rendering the page. It may need to make additional HTTP requests to fetch other resources referenced in the HTML, such as images, stylesheets, or scripts. Each of these resources involves similar steps: DNS resolution, TCP connection, HTTP request, server response, and rendering.

6. Closing the Connection: After all resources are loaded, the browser may close the TCP connection, or it may keep it open for reuse in future requests, depending on the HTTP version and connection settings.

Throughout this process, the primary protocols used are DNS for domain name resolution, TCP for reliable data transmission, and HTTP for requesting and delivering web content. The messages exchanged include DNS queries and responses, TCP packets for connection establishment and data transfer, and HTTP request and response messages containing headers and content.

### P4

#### a

/cs453/index.html

#### b

HTTP/1.1

#### c

Persistent

Connection:keep-alive

#### d

The IP address of the host is not specified in the HTTP request message. To determine the IP address, one would need to perform a DNS lookup for the domain gaia.cs.umass.edu.

#### e

The browser initiating this message is Netscape version 7.2. The browser type is specified in the User-Agent header: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.2) Gecko/20040804 Netscape/7.2 (ax).

The browser type is needed in an HTTP request message to inform the server about the client's software and capabilities. This information allows the server to tailor its response to the specific requirements and limitations of the client's browser, such as content formatting, supported features, and compatibility considerations.

### P5

#### a

Yes.

Date: Tue, 07 Mar 2008 12:39:45GMT

#### b

Last-Modified: Sat, 10 Dec2005 18:27:46 GMT

#### c

Content-Length: 3874

#### d

The first 5 bytes of the document are not explicitly provided in the response headers. To determine the exact content, one would need to access the document's content.
The server agreed to a persistent connection, as indicated by the Connection: Keep-Alive header.

### P6

#### a

Both, By include the Connection: close header

#### b

No encryption

#### c

Yes

#### d

Yes

### P7

After n queries for DNS. One $RTT_0$ for TCP Connection, One for Request and Response also 0.002 for transmission.

$$
RTT_1+...+RTT_n+RTT_0+1.002\times RTT_0
$$

### P8

#### a

$$
n \times RTT + 2\times RTT + 2\times RTT \times 9
$$

#### b

$$
n \times RTT + 2\times RTT + 2\times RTT \times 2
$$

#### c

With no parallel
$$
n \times RTT + 2\times RTT + RTT \times 9
$$

With parallel
$$
n \times RTT + 2\times RTT + RTT \times 2
$$

### P9

#### a

$$
\begin{align*}
\Delta &= 1.6Mbit/54Mbps \\
\beta &= 24 \\
delay &= \Delta/(1-\Delta\beta) + 3
\end{align*}
$$

#### b

$$
\begin{align*}
\Delta &= 1.6Mbit/54Mbps \\
\beta &= 24\times 0.3 \\
delay &= (\Delta/(1-\Delta\beta)+3)\times 0.3
\end{align*}
$$

### P10

$$
\begin{align*}
t_{initial} &=  RTT\times 2 + (100000+200*3)/300 \\
t_{noparallel} &= t_{initial} + N \times t_{initial} \\
t_{nopersistent} &= t_{initial} + RTT\times 2 + (100000+200*3)N/300 \\
t_{persistent} &= t_{initial} + RTT + (100000+200)N/300 \\
\end{align*}
$$

As the link is 30-meter, The RTT is slow, So parallel downloads via parallel instances of non-persistent HTTP make no sense.
While the parallel downloads via parallel instances of persistent HTTP is little faster than non-persistent HTTP.

### P11

#### a

Yes, because Bob has more connections, he can get a larger share of the link bandwidth.

#### b

Yes, Bob still needs to perform parallel downloads; otherwise he will get less bandwidth than the other four users.

### P12

```python
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
connectionSocket, addr = serverSocket.accept()

while True:
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)
connectionSocket.close()
```

### P13

#### a

5000 + 3*4 = 5012

#### b

4*4 = 16

### P14

2*4

### P15

Key Difference:

MAIL FROM: is used by mail servers for message routing and error handling.
From: is what the recipient sees in their email client and can be modified for display purposes.

### P16

SMTP uses a line containing only a period to mark the end of a message body.
HTTP uses “Content-Length header field” to indicate the length of a message body.
No, HTTP cannot use the method used by SMTP, because HTTP message could be binary
data, whereas in SMTP, the message body must be in 7-bit ASCII format.

### P17

asusus-4b96 ([58.88.21.177])

### P18

#### a

A WHOIS database is a publicly accessible database that contains information about registered domain names and their owners. It is maintained by domain registrars and registries and is used to store details.

#### b

<https://who.is/> : ns1.baidu.com ns2.baidu.com

#### c

```bash
nslookup  # 进入交互模式后输入`server`查看当前的DNS服务器
nslookup -type=A www.baidu.com
nslookup -type=NS www.baidu.com ns1.baidu.com
nslookup -type=MX www.baidu.com ns2.baidu.com
```

```bash
❯ nslookup -type=NS www.baidu.com ns1.baidu.com
Server:   ns1.baidu.com
Address:  110.242.68.134#53

Non-authoritative answer:
www.baidu.com canonical name = www.a.shifen.com.

Authoritative answers can be found from:
a.shifen.com
  origin = ns1.a.shifen.com
  mail addr = baidu_dns_master.baidu.com
  serial = 2503300020
  refresh = 5
  retry = 5
  expire = 2592000
  minimum = 3600
```

#### d

```bash
❯ nslookup www.baidu.com

Server:   192.168.31.1
Address:  192.168.31.1#53

Non-authoritative answer:
www.baidu.com canonical name = www.a.shifen.com.
Name: www.a.shifen.com
Address: 183.240.99.169
Name: www.a.shifen.com
Address: 183.240.99.58
Name: www.a.shifen.com
Address: 2409:8c54:870:310:0:ff:b0ed:40ac
Name: www.a.shifen.com
Address: 2409:8c54:870:187:0:ff:b0d9:bb1c
```

#### e

according to <https://whois.arin.net/rest/customer/C10991933>:
baidu.com: 69.30.242.152 - 69.30.242.159

#### f

n attacker can use the whois database and nslookup tool to determine the IP address
ranges, DNS server addresses, etc., for the target institution.

#### g

To see if a address is owned by a specific organization.
Businesses can use WHOIS to detect trademark infringement and domain squatting.

### P19

```bash
❯ dig baidu.com NS

; <<>> DiG 9.20.7 <<>> baidu.com NS
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26206
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;baidu.com.     IN  NS

;; ANSWER SECTION:
baidu.com.    1 IN  NS  ns7.baidu.com.
baidu.com.    1 IN  NS  dns.baidu.com.
baidu.com.    1 IN  NS  ns4.baidu.com.
baidu.com.    1 IN  NS  ns3.baidu.com.
baidu.com.    1 IN  NS  ns2.baidu.com.

;; Query time: 34 msec
;; SERVER: 192.168.31.1#53(192.168.31.1) (UDP)
;; WHEN: Sun Mar 30 22:45:36 CST 2025
;; MSG SIZE  rcvd: 128
```

### P20

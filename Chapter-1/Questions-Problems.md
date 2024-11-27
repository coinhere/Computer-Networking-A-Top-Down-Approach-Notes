# Review-Questions

## SECTION 1.1

### R1

No defference.  
In page 41:

> Throughout this book we will use the terms hosts and end systems interchangeably;
> that is, host = end system.

End systems:

- PC
- Phone, Laptop
- Wearable Device
- Workstation, Server
- Game console

Yes.

### R2

1. The Caller enter the phone number of the person he wants to talk and calls.
2. Waiting for the call to go through. If not, check the phone number and wait a few minutes to try again.
3. The Callee says "hello" -- inform the Caller that he is listening.
4. The Caller ask the Callee if he is the person he wants to talk to.
5. If the answer is "yes" -- the Caller tell his name and start the conversation.
6. Conversation continues until the either of the Caller or Callee says the words to end the conversation.
7. Say "bye" to the other person and end the conversation.

### R3

It the rules that govern the way hosts communicate. If the standards is not specific or vary from host to host, then communication will not be successful. Because machines are not as smart as humans.

## SECTION 1.2

### R4

Home Access: DSL, Cable, FTTH, and 5G Fixed Wireless.
Access in the Enterprise (and the Home): Ethernet and WiFi.
Wide-Area Wireless Access: 3G and LTE 4G and 5G.

### R5

shared among users. No.

In page 45.

> One important characteristic of cable Internet access is that it is a shared broadcast medium. In
> particular, every packet sent by the head end travels downstream on every link to every home and every
> packet sent by a home travels on the upstream channel to the head end.

### R6

Wide-Area Wireless Access: 3G and LTE 4G and 5G.

### R7

In page 43.

> The home’s DSL modem takes digital data and translates it to high-frequency tones for transmis-sion over telephone wires to the CO.
> The residential telephone line carries both data and traditional telephone signals simultaneously, which are encoded at different frequencies:
> • A high-speed downstream channel, in the 50 kHz to 1 MHz band
> • A medium-speed upstream channel, in the 4 kHz to 50 kHz band
> • An ordinary two-way telephone channel, in the 0 to 4 kHz band

In <https://www.switchful.com/service/internet/resource/dsl-internet-vs-dial-up> `What’s the difference between DSL internet and dial-up?`：

> DSL operates over the same phone lines as dial-up but uses higher frequencies to provide much faster speeds. While dial-up is limited to 56 kbps (0.056 Mbps), even the slowest DSL connections provide 3-5 Mbps—around 100 times faster. DSL also allows simultaneous use of the internet and phone service over the same line, while dial-up ties up the phone line when in use.

### R8

twisted-pair copper wire, coaxial cable, and fiber optic cable, also radio spectrum

In page 48:

> In the previous subsection, we gave an overview of some of the most important
> network access technologies in the Internet. As we described these technologies,
> we also indicated the physical media used. For example, we said that HFC uses a
> combination of fiber cable and coaxial cable. We said that DSL and Ethernet use
> copper wire. And we said that mobile access networks use the radio spectrum. In this
> subsection, we provide a brief overview of these and other transmission media that
> are commonly used in the Internet.

### R9

| Types | Downstream     | Upstream       | shared/ dedicated |
| ----- | -------------- | -------------- | ----------------- |
| DSL   | 24Mbps~52Mbps  | 3.5Mbps~16Mbps | dedicated         |
| HFC   | 40Mbps~1.2Gbps | 30Mbps~100Mbps | shared            |
| FTTH  | 1Gbps~10Gbps   | 1Gbps~10Gbps   | shared            |

For DSL, in page 44:

> The DSL standards define multiple transmission rates, including downstream
> transmission rates of 24 Mbs and 52 Mbs, and upstream rates of 3.5 Mbps and
> 16 Mbps; the newest standard provides for aggregate upstream plus downstream
> rates of 1 Gbps [ITU 2014].

For HFC, in page 45:

> The DOCSIS 2.0 and 3.0 standards
> define downstream bitrates of 40 Mbps and 1.2 Gbps, and upstream rates
> of 30 Mbps and 100 Mbps, respectively.
> ...
> One important characteristic of cable Internet access is that it is a shared broadcast medium.
> In particular, every packet sent by the head end travels downstream on
> every link to every home and every packet sent by a home travels on the upstream
> channel to the head end.

For FTTH, in page 45:

> FTTH can potentially provide Internet access rates in
> the gigabits per second range.

In [Wikipedia](https://en.wikipedia.org/wiki/Fiber_to_the_x):

> FTTH (fiber-to-the-home): Fiber reaches the boundary of the living space, such as a box on the outside wall of a home. Passive optical networks and point-to-point Ethernet are architectures that are capable of delivering triple-play services over FTTH networks directly from an operator's central office.[4][5] Typically providing between 1 and 10 Gbit/s

In page 46:

> Each home has
> an optical network terminator (ONT), which is connected by dedicated optical
> fiber to a neighborhood splitter. The splitter combines a number of homes (typically less than 100) onto a single, shared optical fiber, which connects to an optical
> line terminator (OLT) in the telco’s CO.

### R10

WiFi, In page 46:

> In a wireless LAN setting, wireless
> users transmit/receive packets to/from an access point that is connected into the
> enterprise’s network (most likely using wired Ethernet), which in turn is connected
> to the wired Internet.
> A wireless LAN user must typically be within a few tens of
> meters of the access point. Wireless LAN access based on IEEE 802.11 technology, more colloquially known as WiFi, is now just about everywhere—universities,
> business offices, cafes, airports, homes, and even in airplanes. As discussed in detail
> in Chapter 7, 802.11 today provides a shared transmission rate of up to more than
> 100 Mbps.

5G, In page 47:

> These devices employ the same wireless infrastructure
> used for cellular telephony to send/receive packets through a base station that is operated by the cellular network provider. Unlike WiFi, a user need only be within a few
> tens of kilometers (as opposed to a few tens of meters) of the base station.
> Telecommunications companies have made enormous investments in so-called
> fourth-generation (4G) wireless, which provides real-world download speeds of up to
> 60 Mbps

I prefer WiFi over 5G. As WIFI has no traffic limit and charges a fixed monthly fee, while 5G has a certain traffic limit and additional fees will be charged after exceeding it.
Also there is often free WI-FI in public places.

But if the WI-FI connection speed is too slow due to too many people connecting or other reasons, then I will choose 5G, provided that the traffic limit is not exceeded.

## SECTION 1.3

### R11

$$
t = L/R_{1} + L/R_{2}
$$

### R12

Lower delay, and guaranteed constant rate.

In page 57:

> In circuit-switched networks, the resources needed along a path (buffers, link
> transmission rate) to provide for communication between the end systems are
> reserved for the duration of the communication session between the end systems.
> In packet-switched networks, these resources are not reserved; a session’s messages
> use the resources on demand and, as a consequence, may have to wait (that is, queue)
> for access to a communication link
> ...
> Since a given
> transmission rate has been reserved for this sender-to-receiver connection, the sender
> can transfer the data to the receiver at the guaranteed constant rate.

In <https://www.tutorialspoint.com/difference-between-tdm-and-fdm>:

There are two major disadvantages in using FDM −

- The frequency bands must be separated by guard bands to avoid noise and disruption. This results in bandwidth wastage.
- FDM uses analog signals, which are more prone to noise disruptions than digital signals. So, if there are significant nonlinearities in the transmission link, there could be crosstalk among the different signals, resulting in communication errors.

### R13

#### a

$$
2Mbps/1Mbps = 2
$$

#### b

Since the maximum transmission for two or fewer users is 2Mbps which is equal to the link's rate, each packet can be sent in time without queuing delays.

#### c

0.2

#### d

$$
0.2*0.2*0.2 = 0.008
$$

### R14

Avoid paying ISP for sending traffic to each other.

By charging ISPs that connect to the IXP based on the mount of traffic.

### R15

A content provider may has lots of data centers distributed around the world which are connected to each other via a private network.

In page 64:

> Google is currently one of the leading examples of such a content-provider network. As of this writing, it Google has 19 major data
> centers distributed across North America, Europe, Asia, South America, and Australia
> with each data center having tens or hundreds of thousands of servers. Additionally,
> Google has smaller data centers, each with a few hundred servers; these smaller data
> centers are often located within IXPs. The Google data centers are all interconnected
> via Google’s private TCP/IP network, which spans the entire globe but is nevertheless separate from the public Internet. Importantly, the Google private network only
> carries traffic to/from Google servers.

## SECTION 1.4

### R16

- processing delay -- constant
- queuing delay -- variable
- transmission delay -- variable, $=L/R$
- propagationa delay -- variable, $=d/s$

### R17

### R18

- wireless nodal delay: $1500\times 8/2\times 10^6 + 1000/3\times 10^8=0.006003$
- wired nodal delay: $1500\times 8/100\times 10^6 + 1000/2\times 10^8=0.000125$

### R19

#### a

$$
throughput=R1 = 500 kbps
$$

#### b

$$
time = 4 \times 8 \times 10^6 / 0.5 \times 10^6 = 64
$$

#### c

$$
throughput = R2 = 100 kbps\\
time = 4 \times 8 \times 10^6 / 0.1 \times 10^6 = 320
$$

### R20

1. Dividing the file to several packets, each has a header.
2. Process the packet, forward the packet according to It header and congestion of links.3. Queuing.
4. Transmit the packet

- A packet is analogous to a car carries passengers.
- A router is analogous to a city where the car can stop and find the way to destination.
- A link is analogous to highway from a city to another city.
- The packet switching is analogous to a driver has no certain route but just a destination, once he arrives a city, he ask someone the way to his destination, and when he follow the way and arrives another city, he do this again until he arrives the destination.

### R21

## SECTION 1.5

### R22

Not necessary, but a transport protocol that supply the service of multiplexing is still needed, As this is necessary to application communication.

### R23

- application layer -- supply the transmission protocol between application.
- transport layer -- supply the communication between application and other services.
- network layer -- supply the service of transport routes a datagram from the source to destination
- data-link layer -- supply the service of transport packet from a node to another.
- physical layer -- supply the service of transport a bit

### R24

So that the developer doesn't need known the detail of the bottom protocol stack, only need known the services it provided and how to use it.

### R25

network layer, link-layer, application layer

## SECTION 1.6

### R26

In page 85:
>Much of the malware out there today is self-replicating: once it infects one host,
from that host it seeks entry into other hosts over the Internet, and from the newly
infected hosts, it seeks entry into yet more hosts. In this manner, self-replicating mal-
ware can spread exponentially fast

### R27

By infecting devices with malware, which is a malicious program running in the devices.
It can be controlled by bad guys to launch DDOS attack by sending specified packet.

### R28

- Read all the packets Alice send to Bob and packets Bob send to Alice.
- Change or drop the packets.
- Pretend as Alice and send packets to Bob, same for Bob.

# Problems

### P1

Using a http protocol:

| addr |   method   | argument       |return value|
| ----- | -------------- | -------------- | ----------------- |
| /login   | post | username,password | success/reject, Cookies |
| /query-balance   | get | | amount |
| /withdrawl   | post | amount | success/reject |
| /logout  |get|    | |

### P2

$$
P \times L/R + (N-1) \times L/R
$$

### P3

#### a

circuit-switched is more appropriate. As this application transmits data at a steady rate and continue running for a relatively long period of time.

#### b

No

### P4

#### a

16

#### b

8

#### c

yes

### P5

#### a

$$
(10 cars)/(5 cars/min) = 2 min \\
3 \times 2 + 175/100 \times 60 = 111min
$$

#### b

$$
(8 cars)/(5 cars/min) = 1.6 min \\
3 \times 1.6 + 175/100 \times 60 = 109.8min
$$

### P6

#### a

$$
d_prop = m/s
$$

#### b

$$
d_trans = L/R
$$

#### c

$$
m/s + L/R
$$

#### d

just leaving host A.

#### e

in the link.

#### f

in the host B.

#### g

$$
m = s \times L/R = 2.5 \times 10^8 \cdot \frac{1500 \times 8}{10^7} = 300 km
$$

### P7

$$
\frac{56\times 8}{64\times 10^3} + \frac{56\times 8}{10^7} + 10^{-2}
$$

### P8

#### a

$$
\frac{10^7 }{ 200\times 10^3 }= 50
$$

#### b

0.1

#### c

$$
\binom{120}{n} \cdot 0.1^n \cdot 0.9^{120-n}
$$

#### d

$$
1- \sum_{n=1}^{50} \binom{120}{n} \cdot (0.1)^n \cdot (0.9)^{120-n}
$$

### P9

#### a

$$
\frac{10^9}{100 \times 10^3} = 10000
$$

#### b

$$
\sum_{n=N+1}^{M} \binom{M}{N} \cdot (p)^N \cdot (1-p)^{M-N}
$$

### P10

$$
\frac{1500 \times 8}{4 \times 10^6} = 3 ms
$$

Depend on the transmit rate between Route A to Route B.

### 11

$$
|\frac{L}{R_1} + d_1 - \frac{L}{R_2} - d_2 |>= \frac{L}{R_{AB}}
$$

### 12

$$
\frac{h}{R} + \frac{L}{R} \\
N \cdot \frac{h}{R} + \frac{L}{R}
$$

### 13

#### a

$$
\frac{\sum_{i=0}^{N-1} \frac{i \cdot L}{R}}{N} = \frac{(N-1)L}{2R}
$$

#### b

$$
\frac{(N-1)L}{2R}
$$

### 14

#### a

$$
I = \frac{La}{R} \\
\frac{L}{R} + \frac{IL}{R(1-I)} = \frac{L}{R(1-I)} \\
x = \frac{L}{R} \\
$$

#### b

$$
f(x) = \frac{x}{1-ax}
$$

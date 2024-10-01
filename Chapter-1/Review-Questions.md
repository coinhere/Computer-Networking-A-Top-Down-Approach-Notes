# Review-Questions

## SECTION 1.1

### R1. What is the difference between a host and an end system? List several different types of end systems. Is a Web server an end system?

No defference.  
In page 41:

> Throughout this book we will use the terms hosts and end systems interchangeably; that is, host = end system.

End systems:

- PC
- Phone, Laptop
- Wearable Device
- Workstation, Server
- Game console

Yes.

### R2. Describe the protocol that might be used by two people having a telephonic conversation to initiate and end the conversation, i.e., the way that they talk

1. The Caller enter the phone number of the person he wants to talk and calls.
2. Waiting for the call to go through. If not, check the phone number and wait a few minutes to try again.
3. The Callee says "hello" -- inform the Caller that he is listening.
4. The Caller ask the Callee if he is the person he wants to talk to.
5. If the answer is "yes" -- the Caller tell his name and start the conversation.
6. Conversation continues until the either of the Caller or Callee says the words to end the conversation.
7. Say "bye" to the other person and end the conversation.

### R3. Why are standards important for protocols?

It the rules that govern the way hosts communicate. If the standards is not specific or vary from host to host, then communication will not be successful. Because machines are not as smart as humans.

## SECTION 1.2

### R4. List four access technologies. Classify each one as home access, enterprise access, or wide-area wireless access

Home Access: DSL, Cable, FTTH, and 5G Fixed Wireless.
Access in the Enterprise (and the Home): Ethernet and WiFi.
Wide-Area Wireless Access: 3G and LTE 4G and 5G.

### R5. Is HFC transmission rate dedicated or shared among users? Are collisions possible in a downstream HFC channel? Why or why not?

shared among users. No.

In page 45.

> One important characteristic of cable Internet access is that it is a shared broadcast medium. In
> particular, every packet sent by the head end travels downstream on every link to every home and every
> packet sent by a home travels on the upstream channel to the head end.

### R6. What access network technologies would be most suitable for providing internet access in rural areas?

Wide-Area Wireless Access: 3G and LTE 4G and 5G.

### R7. Dial-up modems and DSL both use the telephone line (a twisted-pair coppercable) as their transmission medium. Why then is DSL much faster than dial-up access?

In page 43.

> The home’s DSL modem takes digital data and translates it to high-frequency tones for transmis-sion over telephone wires to the CO.
> The residential telephone line carries both data and traditional telephone signals simultaneously, which are encoded at different frequencies:
> • A high-speed downstream channel, in the 50 kHz to 1 MHz band
> • A medium-speed upstream channel, in the 4 kHz to 50 kHz band
> • An ordinary two-way telephone channel, in the 0 to 4 kHz band

In <https://www.switchful.com/service/internet/resource/dsl-internet-vs-dial-up> `What’s the difference between DSL internet and dial-up?`：

> DSL operates over the same phone lines as dial-up but uses higher frequencies to provide much faster speeds. While dial-up is limited to 56 kbps (0.056 Mbps), even the slowest DSL connections provide 3-5 Mbps—around 100 times faster. DSL also allows simultaneous use of the internet and phone service over the same line, while dial-up ties up the phone line when in use.

### R8. What are some of the physical media that Ethernet can run over?

twisted-pair copper wire, coaxial cable, and fiber optic cable, also radio spectrum

In page 48:

> In the previous subsection, we gave an overview of some of the most important
> network access technologies in the Internet. As we described these technologies,
> we also indicated the physical media used. For example, we said that HFC uses a
> combination of fiber cable and coaxial cable. We said that DSL and Ethernet use
> copper wire. And we said that mobile access networks use the radio spectrum. In this
> subsection, we provide a brief overview of these and other transmission media that
> are commonly used in the Internet.

### HFC, DSL, and FTTH are all used for residential access. For each of these access technologies, provide a range of transmission rates and comment on whether the transmission rate is shared or dedicated

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

### R10. Describe the different wireless technologies you use during the day and their characteristics. If you have a choice between multiple technologies, why do you prefer one over another?

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

### R11. Suppose there is exactly one packet switch between a sending host and a receiving host. The transmission rates between the sending host and the switch and between the switch and the receiving host are R1 and R2, respectively. Assuming that the switch uses store-and-forward packet switching, what is the total end-to-end delay to send a packet of length L? (Ignore queuing, propagation delay, and processing delay.)

$$
t = L/R_{1} + L/R_{2}
$$

### R12. What advantage does a circuit-switched network have over a packet-switched network? What advantages does TDM have over FDM in a circuit-switched network?

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

### R13. Suppose users share a 2 Mbps link. Also suppose each user transmits continuously at 1 Mbps when transmitting, but each user transmits only 20 percent of the time. (See the discussion of statistical multiplexing in Section 1.3.)

#### a. When circuit switching is used, how many users can be supported?

$$
2Mbps/1Mbps = 2
$$

#### b. For the remainder of this problem, suppose packet switching is used. Why will there be essentially no queuing delay before the link if two or fewer users transmit at the same time? Why will there be a queuing delay if three users transmit at the same time?

Since the maximum transmission for two or fewer users is 2Mbps which is equal to the link's rate, each packet can be sent in time without queuing delays.

#### c. Find the probability that a given user is transmitting

0.2

#### d. Suppose now there are three users. Find the probability that at any given time, all three users are transmitting simultaneously. Find the fraction of time during which the queue grows

$$
0.2*0.2*0.2 = 0.008
$$

### R14. Why will two ISPs at the same level of the hierarchy often peer with each other? How does an IXP earn money?

Avoid paying ISP for sending traffic to each other.

By charging ISPs that connect to the IXP based on the mount of traffic.

### R15. Why is a content provider considered a different Internet entity today? How does a content provider connect to other ISPs? Why?

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

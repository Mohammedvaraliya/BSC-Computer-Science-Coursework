#### Aim: 
    Using Packet Tracer to create a network with three routers with RIPv1 and
    each router associated network will have minimum three PC and show the
    connectivity

#### Theory:

    RIP is one of the dynamic routing protocols and the first distance-vector routing
    protocol that uses the hop count as a routing metric. A lower hop count is
    preferred.

    Each router between the source and destination network is counted as one hop. RIP
    prevents routing loops by imposing a maximum number of hops on the path
    between source and destination.

    In RIP, Every 30 seconds, each router broadcasts its entire routing table to its
    nearest neighbors.

    Pros and Cons of RIP Protocol

    Pros:

    1. The RIP protocol is ideal for small networks since it is simple to learn and
       configure.
    2. RIP routing is guaranteed to work with nearly all routers.
    3. When the network topology changes, RIP does not require an update.
    
    Cons:

    1. RIP does not support variable length subnet masks
    2. RIP transmits updates every 30 seconds, which cause traffic and consumes
       bandwidth.
    3. RIP hop counts are restricted to 15, hence any router beyond that distance is
       deemed infinity and becomes unreachable.
    4. The rate of convergence is slow in RIP compared to other routing protocols.
       When a link fails, finding alternate network paths takes a long time.
    5. RIP does not support multiple paths on the same route, which may result in
       extra routing loops.

1. `Configuring Router 0 (using the CLI mode)`

    ```bash
    Router>en
    Router>enable
    Router#
    Router#configure terminal
    Enter configuration commands, one per line. End with CNTL/Z.
    Router(config)#interface gigabitEthernet 0/0
    Router(config-if)#ip address 10.0.0.1 255.0.0.0
    Router(config-if)#no shutdown
    Router(config-if)#exit
    Router(config)#interface serial 0/1/0
    Router(config-if)#ip address 192.168.0.1 255.255.255.0
    Router(config-if)#no shutdown
    Router(config-if)#exit
    Router(config)#
    Router
    ```

2. `Configuring Router 1 (using the CLI mode)`

    ```bash
    Router>enable
    Router#configure terminal
    Router(config)#interface gigabitEthernet 0/0
    Router(config-if)#ip address 20.0.0.1 255.0.0.0
    Router(config-if)#no shutdown
    Router(config-if)#exit
    Router(config)#interface serial 0/1/0
    Router(config-if)#ip address 192.168.0.2 255.255.255.0
    Router(config-if)#no shutdown
    Router(config-if)#exit
    Router(config)#interface serial 0/1/1
    Router(config-if)#ip address 192.168.1.1 255.255.255.0
    Router(config-if)#no shutdown 
    ```

3. `Configuring Router 2 (using the CLI mode)`

    ```bash
    Router>enable
    Router#configure terminal
    Router(config)#interface gigabitEthernet 0/0
    Router(config-if)#ip address 30.0.0.1 255.0.0.0
    Router(config-if)#no shutdown
    Router(config-if)#exit
    Router(config)#interface serial 0/1/1
    Router(config-if)#ip address 192.168.1.2 255.255.255.0
    Router(config-if)#no shutdown
    ```

4. `Setting the RIPv1 on Router 0`

    ```bash
    Router>enable
    Router#configure terminal
    Router(config)#router rip
    Router(config-router)#network 10.0.0.0
    Router(config-router)#network 192.168.0.0
    Router(config-router)#exit
    ```

5. `Setting the RIPv1 on Router 1`

    ```bash
    Router>enable
    Router#configure terminal
    Enter configuration commands, one per line. End with CNTL/Z.
    Router(config)#router rip
    Router(config-router)#network 192.168.0.0
    Router(config-router)#network 20.0.0.0
    Router(config-router)#network 192.168.1.0
    Router(config-router)#exit
    Router(config)#
    Router#
    ```
6. `Setting the RIPv1 on Router 2`

    ```bash
    Router>enable
    Router#configure terminal
    Router(config)#router rip
    Router(config-router)#network 192.168.1.0
    Router(config-router)#network 30.0.0.0
    Router(config-router)#exit
    Router(config)#
    ```
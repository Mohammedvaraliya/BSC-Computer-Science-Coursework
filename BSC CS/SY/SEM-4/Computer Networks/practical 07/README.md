#### Aim: 
    Using Packet Tracer, create a network with three routers with OSPF and
    each router associated network will have minimum three PC and show
    Connectivity

#### Theory:

    Open shortest path first (OSPF) is a link-state routing protocol that is used to find
    the best path between the source and the destination router using its own shortest
    path first (SPF) algorithm. A link-state routing protocol is a protocol that uses the
    concept of triggered updates, i.e., if there is a change observed in the learned
    routing table then the updates are triggered only, not like the distance-vector
    routing protocol where the routing table is exchanged at a period of time.

    Open shortest path first (OSPF) is developed by Internet Engineering Task Force
    (IETF) as one of the Interior Gateway Protocol (IGP), i.e., the protocol which aims
    at moving the packet within a large autonomous system or routing domain.

    OSPF advantages –

        1. Both IPv4 and IPv6 routed protocols
        2. Load balancing with equal-cost routes for the same destination
        3. Unlimited hop counts
        4. Trigger updates for fast convergence
        5. A loop-free topology using SPF algorithm
        6. Run-on most routers
        7. Classless protocol

    There are some disadvantages of OSPF like, it requires an extra CPU process to
    run the SPF algorithm, requiring more RAM to store adjacency topology, and
    being more complex to set up and hard to troubleshoot.

1. `Configuring Router 0 for OSPF (using the CLI mode)`

    ```bash
    Router(config)#
    Router(config)#router ospf 1
    Router(config-router)#network 10.0.0.0 0.0.0.255 area 1
    Router(config-router)#network 40.0.0.0 0.0.0.255 area 1
    Router(config-router)#exit
    Router(config)#
    ```

2. `Configuring Router 1 for OSPF (using the CLI mode)`

    ```bash
    Router(config)#
    Router(config)#router ospf 1
    Router(config-router)#
    Router(config-router)#network 40.0.0.0 0.0.0.255 area 1
    Router(config-router)#network 40.0.0.0 0.0.0.255 area 1
    Router(config-router)#network 50.0.0.0 0.0.0.255 area 1
    Router(config-router)#exit
    Router(config)#
    ```

3. `Configuring Router 2 for OSPF (using the CLI mode)`

    ```bash
    Router(config)#
    Router(config)#router ospf 1
    Router(config-router)#
    Router(config-router)#network 30.0.0.0 0.0.0.255 area 1
    Router(config-router)#network 50.0.0.0 0.0.0.255 area 1
    Router(config-router)# exit
    Router(config)#
    ```

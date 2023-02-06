#### Aim: 
    Using Packet Tracer to create a network with three routers with RIPv2 and
    each router associated network will have minimum three PC and show the
    connectivity

#### Theory:

    RIPv2 is an enhancement to the original RIP protocol developed in 1994. RIPv2 is
    also a distance vector routing protocol but has a few enhancements to make it more
    efficient than RIPv1.

    RIPv2 is more efficient than RIPv1, but is not suitable for larger, more complex
    networks. It simply provides more flexibility on smaller networks.

    RIPv2 uses the same routing metric as RIPv1, the hop count. Updates with RIPv2
    are sent via multicasts and not broadcasts. RIPv2 can also be configured to do
    classless routing. When configured for classless routing, RIPv2 will transmit
    submit masks when it sends routing updates. This allows for the use of subnetting
    and discontiguous networks.

    RIPv2 allows for authentication to be required for updates. When authentication is
    enabled, each router is configured with the RIP update password. The password
    sent with the RIP update must match the password configured on the destination
    router. If the passwords do not match, then the receiving router will not process the
    update.

    Advantages of RIPv2

    1) It’s a standardized protocol.
    2) It’s VLSM compliant.
    3) Provides fast convergence.
    4) It sends triggered updates when the network changes.
    5) Works with snapshot routing – making it ideal for dial networks.
       Disadvantage of RIPv2
    1) Max hop count of 15, due to the ‘count-to-infinity’ vulnerability.
    2) No concept of neighbors.
    3) Exchanges entire table with all neighbors every 30 seconds (except in the
       case of a triggered update).

1. `Configuring Router 0 for RIPv2 (using the CLI mode)`

    ```bash
    Router>enable
    Router#configure terminal
    Router(config)#router rip
    Router(config-router)#version 2
    Router(config-router)#network 10.10.0.0
    Router(config-router)#network 192.168.0.0
    Router(config-router)#exit
    Router(config)#
    ```

2. `Configuring Router 1 for RIPv2 (using the CLI mode)`

    ```bash
    Router>enable
    Router#configure terminal
    Router(config)#router rip
    Router(config-router)#version 2
    Router(config-router)#network 10.20.0.0
    Router(config-router)#network 192.168.0.0
    Router(config-router)#network 192.168.1.0
    Router(config-router)#exit
    Router(config)#
    ```

3. `Configuring Router 2 for RIPv2 (using the CLI mode)`

    ```bash
    Router>enable
    Router#configure terminal
    Router(config)#router rip
    Router(config-router)#version 2
    Router(config-router)#network 10.30.0.0
    Router(config-router)#network 192.168.1.0
    Router(config-router)#exit
    Router(config)#
    ```

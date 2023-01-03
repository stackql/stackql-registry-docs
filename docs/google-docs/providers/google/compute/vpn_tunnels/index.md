---
title: vpn_tunnels
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_tunnels
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_tunnels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.vpn_tunnels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `ikeVersion` | `integer` | IKE protocol version to use when establishing the VPN tunnel with the peer VPN gateway. Acceptable IKE versions are 1 or 2. The default version is 2. |
| `region` | `string` | [Output Only] URL of the region where the VPN tunnel resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `status` | `string` | [Output Only] The status of the VPN tunnel, which can be one of the following: - PROVISIONING: Resource is being allocated for the VPN tunnel. - WAITING_FOR_FULL_CONFIG: Waiting to receive all VPN-related configs from the user. Network, TargetVpnGateway, VpnTunnel, ForwardingRule, and Route resources are needed to setup the VPN tunnel. - FIRST_HANDSHAKE: Successful first handshake with the peer VPN. - ESTABLISHED: Secure session is successfully established with the peer VPN. - NETWORK_ERROR: Deprecated, replaced by NO_INCOMING_PACKETS - AUTHORIZATION_ERROR: Auth error (for example, bad shared secret). - NEGOTIATION_FAILURE: Handshake failed. - DEPROVISIONING: Resources are being deallocated for the VPN tunnel. - FAILED: Tunnel creation has failed and the tunnel is not ready to be used. - NO_INCOMING_PACKETS: No incoming packets from peer. - REJECTED: Tunnel configuration was rejected, can be result of being denied access. - ALLOCATING_RESOURCES: Cloud VPN is in the process of allocating all required resources. - STOPPED: Tunnel is stopped due to its Forwarding Rules being deleted for Classic VPN tunnels or the project is in frozen state. - PEER_IDENTITY_MISMATCH: Peer identity does not match peer IP, probably behind NAT. - TS_NARROWING_NOT_ALLOWED: Traffic selector narrowing not allowed for an HA-VPN tunnel.  |
| `localTrafficSelector` | `array` | Local traffic selector to use when establishing the VPN tunnel with the peer VPN gateway. The value should be a CIDR formatted string, for example: 192.168.0.0/16. The ranges must be disjoint. Only IPv4 is supported. |
| `peerIp` | `string` | IP address of the peer VPN gateway. Only IPv4 is supported. |
| `vpnGatewayInterface` | `integer` | The interface ID of the VPN gateway with which this VPN tunnel is associated. |
| `sharedSecret` | `string` | Shared secret used to set the secure session between the Cloud VPN gateway and the peer VPN gateway. |
| `peerGcpGateway` | `string` | URL of the peer side HA GCP VPN gateway to which this VPN tunnel is connected. Provided by the client when the VPN tunnel is created. This field can be used when creating highly available VPN from VPC network to VPC network, the field is exclusive with the field peerExternalGateway. If provided, the VPN tunnel will automatically use the same vpnGatewayInterface ID in the peer GCP VPN gateway. |
| `router` | `string` | URL of the router resource to be used for dynamic routing. |
| `vpnGateway` | `string` | URL of the VPN gateway with which this VPN tunnel is associated. Provided by the client when the VPN tunnel is created. This must be used (instead of target_vpn_gateway) if a High Availability VPN gateway resource is created. |
| `targetVpnGateway` | `string` | URL of the Target VPN gateway with which this VPN tunnel is associated. Provided by the client when the VPN tunnel is created. |
| `peerExternalGateway` | `string` | URL of the peer side external VPN gateway to which this VPN tunnel is connected. Provided by the client when the VPN tunnel is created. This field is exclusive with the field peerGcpGateway. |
| `peerExternalGatewayInterface` | `integer` | The interface ID of the external VPN gateway to which this VPN tunnel is connected. Provided by the client when the VPN tunnel is created. |
| `sharedSecretHash` | `string` | Hash of the shared secret. |
| `detailedStatus` | `string` | [Output Only] Detailed status message for the VPN tunnel. |
| `kind` | `string` | [Output Only] Type of resource. Always compute#vpnTunnel for VPN tunnels. |
| `remoteTrafficSelector` | `array` | Remote traffic selectors to use when establishing the VPN tunnel with the peer VPN gateway. The value should be a CIDR formatted string, for example: 192.168.0.0/16. The ranges should be disjoint. Only IPv4 is supported. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vpnTunnels_aggregatedList` | `SELECT` | `project` | Retrieves an aggregated list of VPN tunnels. |
| `vpnTunnels_get` | `SELECT` | `project, region, vpnTunnel` | Returns the specified VpnTunnel resource. Gets a list of available VPN tunnels by making a list() request. |
| `vpnTunnels_list` | `SELECT` | `project, region` | Retrieves a list of VpnTunnel resources contained in the specified project and region. |
| `vpnTunnels_insert` | `INSERT` | `project, region` | Creates a VpnTunnel resource in the specified project and region using the data included in the request. |
| `vpnTunnels_delete` | `DELETE` | `project, region, vpnTunnel` | Deletes the specified VpnTunnel resource. |

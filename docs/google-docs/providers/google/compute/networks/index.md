---
title: networks
hide_title: false
hide_table_of_contents: false
keywords:
  - networks
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
<tr><td><b>Name</b></td><td><code>networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. The first character must be a lowercase letter, and all following characters (except for the last character) must be a dash, lowercase letter, or digit. The last character must be a lowercase letter or digit. |
| `description` | `string` | An optional description of this resource. Provide this field when you create the resource. |
| `firewallPolicy` | `string` | [Output Only] URL of the firewall policy the network is associated with. |
| `enableUlaInternalIpv6` | `boolean` | Enable ULA internal ipv6 on this network. Enabling this feature will assign a /48 from google defined ULA prefix fd20::/20. . |
| `gatewayIPv4` | `string` | [Output Only] The gateway address for default routing out of the network, selected by GCP. |
| `internalIpv6Range` | `string` | When enabling ula internal ipv6, caller optionally can specify the /48 range they want from the google defined ULA prefix fd20::/20. The input must be a valid /48 ULA IPv6 address and must be within the fd20::/20. Operation will fail if the speficied /48 is already in used by another resource. If the field is not speficied, then a /48 range will be randomly allocated from fd20::/20 and returned via this field. . |
| `subnetworks` | `array` | [Output Only] Server-defined fully-qualified URLs for all subnetworks in this VPC network. |
| `routingConfig` | `object` | A routing configuration attached to a network resource. The message includes the list of routers associated with the network, and a flag indicating the type of routing behavior to enforce network-wide. |
| `mtu` | `integer` | Maximum Transmission Unit in bytes. The minimum value for this field is 1460 and the maximum value is 1500 bytes. If unspecified, defaults to 1460. |
| `networkFirewallPolicyEnforcementOrder` | `string` | The network firewall policy enforcement order. Can be either AFTER_CLASSIC_FIREWALL or BEFORE_CLASSIC_FIREWALL. Defaults to AFTER_CLASSIC_FIREWALL if the field is not specified. |
| `selfLinkWithId` | `string` | [Output Only] Server-defined URL for this resource with the resource id. |
| `peerings` | `array` | [Output Only] A list of network peerings for the resource. |
| `autoCreateSubnetworks` | `boolean` | Must be set to create a VPC network. If not set, a legacy network is created. When set to true, the VPC network is created in auto mode. When set to false, the VPC network is created in custom mode. An auto mode VPC network starts with one subnet per region. Each subnet has a predetermined range as described in Auto mode VPC network IP ranges. For custom mode VPC networks, you can add subnets using the subnetworks insert method. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#network for networks. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `IPv4Range` | `string` | Deprecated in favor of subnet mode networks. The range of internal addresses that are legal on this network. This range is a CIDR specification, for example: 192.168.0.0/16. Provided by the client when the network is created. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `network, project` | Returns the specified network. Gets a list of available networks by making a list() request. |
| `list` | `SELECT` | `project` | Retrieves the list of networks available to the specified project. |
| `insert` | `INSERT` | `project` | Creates a network in the specified project using the data included in the request. |
| `delete` | `DELETE` | `network, project` | Deletes the specified network. |
| `patch` | `EXEC` | `network, project` | Patches the specified network with the data included in the request. Only the following fields can be modified: routingConfig.routingMode. |
| `switchToCustomMode` | `EXEC` | `network, project` | Switches the network mode from auto subnet mode to custom subnet mode. |
| `updatePeering` | `EXEC` | `network, project` | Updates the specified network peering with the data included in the request. You can only modify the NetworkPeering.export_custom_routes field and the NetworkPeering.import_custom_routes field. |

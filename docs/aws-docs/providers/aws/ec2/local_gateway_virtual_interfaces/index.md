---
title: local_gateway_virtual_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_virtual_interfaces
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_gateway_virtual_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.local_gateway_virtual_interfaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `vlan` | `integer` | The ID of the VLAN. |
| `peerAddress` | `string` | The peer address. |
| `localAddress` | `string` | The local address. |
| `localBgpAsn` | `integer` | The Border Gateway Protocol (BGP) Autonomous System Number (ASN) of the local gateway. |
| `peerBgpAsn` | `integer` | The peer BGP ASN. |
| `localGatewayVirtualInterfaceId` | `string` | The ID of the virtual interface. |
| `localGatewayId` | `string` | The ID of the local gateway. |
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the local gateway virtual interface. |
| `tagSet` | `array` | The tags assigned to the virtual interface. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `local_gateway_virtual_interfaces_Describe` | `SELECT` |  |

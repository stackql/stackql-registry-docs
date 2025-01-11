---
title: vpn_connection_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_connection_tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>vpn_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_connection_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a VPN connection between a virtual private gateway and a VPN customer gateway or a transit gateway and a VPN customer gateway.<br />To specify a VPN connection between a transit gateway and customer gateway, use the <code>TransitGatewayId</code> and <code>CustomerGatewayId</code> properties.<br />To specify a VPN connection between a virtual private gateway and customer gateway, use the <code>VpnGatewayId</code> and <code>CustomerGatewayId</code> properties.<br />For more information, see &#91;&#93;(https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpn_connection_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="remote_ipv6_network_cidr" /></td><td><code>string</code></td><td>The IPv6 CIDR on the AWS side of the VPN connection.<br />Default: <code>::/0</code></td></tr>
<tr><td><CopyableCode code="remote_ipv4_network_cidr" /></td><td><code>string</code></td><td>The IPv4 CIDR on the AWS side of the VPN connection.<br />Default: <code>0.0.0.0/0</code></td></tr>
<tr><td><CopyableCode code="vpn_tunnel_options_specifications" /></td><td><code>array</code></td><td>The tunnel options for the VPN connection.</td></tr>
<tr><td><CopyableCode code="customer_gateway_id" /></td><td><code>string</code></td><td>The ID of the customer gateway at your end of the VPN connection.</td></tr>
<tr><td><CopyableCode code="outside_ip_address_type" /></td><td><code>string</code></td><td>The type of IPv4 address assigned to the outside interface of the customer gateway device.<br />Valid values: <code>PrivateIpv4</code> | <code>PublicIpv4</code> <br />Default: <code>PublicIpv4</code></td></tr>
<tr><td><CopyableCode code="static_routes_only" /></td><td><code>boolean</code></td><td>Indicates whether the VPN connection uses static routes only. Static routes must be used for devices that don't support BGP.<br />If you are creating a VPN connection for a device that does not support Border Gateway Protocol (BGP), you must specify <code>true</code>.</td></tr>
<tr><td><CopyableCode code="enable_acceleration" /></td><td><code>boolean</code></td><td>Indicate whether to enable acceleration for the VPN connection.<br />Default: <code>false</code></td></tr>
<tr><td><CopyableCode code="transit_gateway_id" /></td><td><code>string</code></td><td>The ID of the transit gateway associated with the VPN connection.<br />You must specify either <code>TransitGatewayId</code> or <code>VpnGatewayId</code>, but not both.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of VPN connection.</td></tr>
<tr><td><CopyableCode code="local_ipv4_network_cidr" /></td><td><code>string</code></td><td>The IPv4 CIDR on the customer gateway (on-premises) side of the VPN connection.<br />Default: <code>0.0.0.0/0</code></td></tr>
<tr><td><CopyableCode code="vpn_gateway_id" /></td><td><code>string</code></td><td>The ID of the virtual private gateway at the AWS side of the VPN connection.<br />You must specify either <code>TransitGatewayId</code> or <code>VpnGatewayId</code>, but not both.</td></tr>
<tr><td><CopyableCode code="transport_transit_gateway_attachment_id" /></td><td><code>string</code></td><td>The transit gateway attachment ID to use for the VPN tunnel.<br />Required if <code>OutsideIpAddressType</code> is set to <code>PrivateIpv4</code>.</td></tr>
<tr><td><CopyableCode code="local_ipv6_network_cidr" /></td><td><code>string</code></td><td>The IPv6 CIDR on the customer gateway (on-premises) side of the VPN connection.<br />Default: <code>::/0</code></td></tr>
<tr><td><CopyableCode code="vpn_connection_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tunnel_inside_ip_version" /></td><td><code>string</code></td><td>Indicate whether the VPN tunnels process IPv4 or IPv6 traffic.<br />Default: <code>ipv4</code></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>vpn_connections</code> in a region.
```sql
SELECT
region,
remote_ipv6_network_cidr,
remote_ipv4_network_cidr,
vpn_tunnel_options_specifications,
customer_gateway_id,
outside_ip_address_type,
static_routes_only,
enable_acceleration,
transit_gateway_id,
type,
local_ipv4_network_cidr,
vpn_gateway_id,
transport_transit_gateway_attachment_id,
local_ipv6_network_cidr,
vpn_connection_id,
tunnel_inside_ip_version,
tag_key,
tag_value
FROM aws.ec2.vpn_connection_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>vpn_connection_tags</code> resource, see <a href="/providers/aws/ec2/vpn_connections/#permissions"><code>vpn_connections</code></a>


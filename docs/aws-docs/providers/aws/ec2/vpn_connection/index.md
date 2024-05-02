---
title: vpn_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_connection
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
Gets an individual <code>vpn_connection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPNConnection</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpn_connection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>vpn_connection_id</code></td><td><code>string</code></td><td>The provider-assigned unique ID for this managed resource</td></tr>
<tr><td><code>customer_gateway_id</code></td><td><code>string</code></td><td>The ID of the customer gateway at your end of the VPN connection.</td></tr>
<tr><td><code>static_routes_only</code></td><td><code>boolean</code></td><td>Indicates whether the VPN connection uses static routes only.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Any tags assigned to the VPN connection.</td></tr>
<tr><td><code>transit_gateway_id</code></td><td><code>string</code></td><td>The ID of the transit gateway associated with the VPN connection.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of VPN connection.</td></tr>
<tr><td><code>vpn_gateway_id</code></td><td><code>string</code></td><td>The ID of the virtual private gateway at the AWS side of the VPN connection.</td></tr>
<tr><td><code>vpn_tunnel_options_specifications</code></td><td><code>array</code></td><td>The tunnel options for the VPN connection.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
vpn_connection_id,
customer_gateway_id,
static_routes_only,
tags,
transit_gateway_id,
type,
vpn_gateway_id,
vpn_tunnel_options_specifications
FROM aws.ec2.vpn_connection
WHERE data__Identifier = '<VpnConnectionId>';
```

## Permissions

To operate on the <code>vpn_connection</code> resource, the following permissions are required:

### Delete
```json
ec2:DescribeVpnConnections,
ec2:DeleteVpnConnection,
ec2:DeleteTags
```

### Update
```json
ec2:DescribeVpnConnections,
ec2:CreateTags,
ec2:DeleteTags
```

### Read
```json
ec2:DescribeVpnConnections
```


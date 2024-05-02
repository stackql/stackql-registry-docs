---
title: local_gateway_route
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_route
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
Gets an individual <code>local_gateway_route</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_gateway_route</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes a route for a local gateway route table.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.local_gateway_route</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>destination_cidr_block</code></td><td><code>string</code></td><td>The CIDR block used for destination matches.</td></tr>
<tr><td><code>local_gateway_route_table_id</code></td><td><code>string</code></td><td>The ID of the local gateway route table.</td></tr>
<tr><td><code>local_gateway_virtual_interface_group_id</code></td><td><code>string</code></td><td>The ID of the virtual interface group.</td></tr>
<tr><td><code>network_interface_id</code></td><td><code>string</code></td><td>The ID of the network interface.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of the route.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The route type.</td></tr>
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
destination_cidr_block,
local_gateway_route_table_id,
local_gateway_virtual_interface_group_id,
network_interface_id,
state,
type
FROM aws.ec2.local_gateway_route
WHERE data__Identifier = '<DestinationCidrBlock>|<LocalGatewayRouteTableId>';
```

## Permissions

To operate on the <code>local_gateway_route</code> resource, the following permissions are required:

### Read
```json
ec2:SearchLocalGatewayRoutes
```

### Delete
```json
ec2:DeleteLocalGatewayRoute,
ec2:SearchLocalGatewayRoutes
```

### Update
```json
ec2:ModifyLocalGatewayRoute,
ec2:SearchLocalGatewayRoutes
```


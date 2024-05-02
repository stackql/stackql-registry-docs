---
title: local_gateway_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_routes
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
Retrieves a list of <code>local_gateway_routes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_gateway_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes a route for a local gateway route table.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.local_gateway_routes</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>destination_cidr_block</code></td><td><code>string</code></td><td>The CIDR block used for destination matches.</td></tr>
<tr><td><code>local_gateway_route_table_id</code></td><td><code>string</code></td><td>The ID of the local gateway route table.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
destination_cidr_block,
local_gateway_route_table_id
FROM aws.ec2.local_gateway_routes
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>local_gateway_routes</code> resource, the following permissions are required:

### Create
```json
ec2:CreateLocalGatewayRoute,
ec2:SearchLocalGatewayRoutes
```

### List
```json
ec2:DescribeLocalGatewayRouteTables,
ec2:SearchLocalGatewayRoutes
```


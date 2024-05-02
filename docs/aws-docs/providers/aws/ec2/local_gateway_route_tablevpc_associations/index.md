---
title: local_gateway_route_tablevpc_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_route_tablevpc_associations
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
Used to retrieve a list of <code>local_gateway_route_tablevpc_associations</code> in a region or create a <code>local_gateway_route_tablevpc_associations</code> resource, use <code>local_gateway_route_tablevpc_association</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_gateway_route_tablevpc_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes an association between a local gateway route table and a VPC.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.local_gateway_route_tablevpc_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>local_gateway_route_table_vpc_association_id</code></td><td><code>string</code></td><td>The ID of the association.</td></tr>
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
local_gateway_route_table_vpc_association_id
FROM aws.ec2.local_gateway_route_tablevpc_associations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>local_gateway_route_tablevpc_associations</code> resource, the following permissions are required:

### Create
```json
ec2:CreateLocalGatewayRouteTableVpcAssociation,
ec2:DescribeLocalGatewayRouteTableVpcAssociations,
ec2:CreateTags
```

### List
```json
ec2:DescribeLocalGatewayRouteTableVpcAssociations
```


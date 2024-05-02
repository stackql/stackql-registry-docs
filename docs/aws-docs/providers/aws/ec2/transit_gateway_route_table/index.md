---
title: transit_gateway_route_table
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_route_table
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
Gets or operates on an individual <code>transit_gateway_route_table</code> resource, use <code>transit_gateway_route_tables</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_route_table</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::TransitGatewayRouteTable</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_route_table</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>transit_gateway_route_table_id</code></td><td><code>string</code></td><td>Transit Gateway Route Table primary identifier</td></tr>
<tr><td><code>transit_gateway_id</code></td><td><code>string</code></td><td>The ID of the transit gateway.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags are composed of a Key&#x2F;Value pair. You can use tags to categorize and track each parameter group. The tag value null is permitted.</td></tr>
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
transit_gateway_route_table_id,
transit_gateway_id,
tags
FROM aws.ec2.transit_gateway_route_table
WHERE data__Identifier = '<TransitGatewayRouteTableId>';
```

## Permissions

To operate on the <code>transit_gateway_route_table</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeTransitGatewayRouteTables
```

### Delete
```json
ec2:DeleteTransitGatewayRouteTable,
ec2:DescribeTransitGatewayRouteTables,
ec2:GetTransitGatewayRouteTableAssociations,
ec2:DisassociateTransitGatewayRouteTable
```


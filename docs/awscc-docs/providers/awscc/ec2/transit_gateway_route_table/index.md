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
Gets an individual <code>transit_gateway_route_table</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_route_table</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>transit_gateway_route_table</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.transit_gateway_route_table</code></td></tr>
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
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
transit_gateway_route_table_id,
transit_gateway_id,
tags
FROM awscc.ec2.transit_gateway_route_table
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


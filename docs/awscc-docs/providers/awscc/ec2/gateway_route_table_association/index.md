---
title: gateway_route_table_association
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_route_table_association
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
Gets an individual <code>gateway_route_table_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway_route_table_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>gateway_route_table_association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.gateway_route_table_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>route_table_id</code></td><td><code>string</code></td><td>The ID of the route table.</td></tr>
<tr><td><code>gateway_id</code></td><td><code>string</code></td><td>The ID of the gateway.</td></tr>
<tr><td><code>association_id</code></td><td><code>string</code></td><td>The route table association ID.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
route_table_id,
gateway_id,
association_id
FROM awscc.ec2.gateway_route_table_association
WHERE data__Identifier = '<GatewayId>';
```

## Permissions

To operate on the <code>gateway_route_table_association</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeRouteTables
```

### Update
```json
ec2:DescribeRouteTables,
ec2:ReplaceRouteTableAssociation
```

### Delete
```json
ec2:DescribeRouteTables,
ec2:DisassociateRouteTable
```


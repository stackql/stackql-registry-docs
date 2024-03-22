---
title: local_gateway_route_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_route_tables
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
Retrieves a list of <code>local_gateway_route_tables</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_gateway_route_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>local_gateway_route_tables</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.local_gateway_route_tables</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>local_gateway_route_table_id</code></td><td><code>string</code></td><td>The ID of the local gateway route table.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
local_gateway_route_table_id
FROM awscc.ec2.local_gateway_route_tables
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>local_gateway_route_tables</code> resource, the following permissions are required:

### Create
```json
ec2:CreateLocalGatewayRouteTable,
ec2:DescribeLocalGatewayRouteTables,
ec2:CreateTags
```

### List
```json
ec2:DescribeLocalGatewayRouteTables
```


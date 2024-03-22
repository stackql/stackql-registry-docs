---
title: route_table
hide_title: false
hide_table_of_contents: false
keywords:
  - route_table
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
Gets an individual <code>route_table</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route_table</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>route_table</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.route_table</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>route_table_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Any tags assigned to the route table.</td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
route_table_id,
tags,
vpc_id
FROM awscc.ec2.route_table
WHERE data__Identifier = '<RouteTableId>';
```

## Permissions

To operate on the <code>route_table</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeRouteTables
```

### Update
```json
ec2:CreateTags,
ec2:DeleteTags,
ec2:DescribeRouteTables
```

### Delete
```json
ec2:DescribeRouteTables,
ec2:DeleteRouteTable
```


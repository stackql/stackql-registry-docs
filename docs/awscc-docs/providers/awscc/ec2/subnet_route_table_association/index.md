---
title: subnet_route_table_association
hide_title: false
hide_table_of_contents: false
keywords:
  - subnet_route_table_association
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
Gets an individual <code>subnet_route_table_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_route_table_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>subnet_route_table_association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.subnet_route_table_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>route_table_id</code></td><td><code>string</code></td><td>The ID of the route table.&lt;br&#x2F;&gt; The physical ID changes when the route table ID is changed.</td></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td>The ID of the subnet.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
route_table_id,
subnet_id
FROM awscc.ec2.subnet_route_table_association
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>subnet_route_table_association</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeRouteTables
```

### Delete
```json
ec2:DisassociateRouteTable,
ec2:DescribeSubnets,
ec2:DescribeRouteTables
```


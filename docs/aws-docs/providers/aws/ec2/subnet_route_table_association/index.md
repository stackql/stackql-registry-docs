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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>subnet_route_table_association</code> resource, use <code>subnet_route_table_associations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_route_table_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates a subnet with a route table. The subnet and route table must be in the same VPC. This association causes traffic originating from the subnet to be routed according to the routes in the route table. A route table can be associated with multiple subnets. To create a route table, see &#91;AWS::EC2::RouteTable&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-ec2-routetable.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.subnet_route_table_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="route_table_id" /></td><td><code>string</code></td><td>The ID of the route table.&lt;br&#x2F;&gt; The physical ID changes when the route table ID is changed.</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The ID of the subnet.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id,
route_table_id,
subnet_id
FROM aws.ec2.subnet_route_table_association
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


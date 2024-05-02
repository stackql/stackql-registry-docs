---
title: db_subnet_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - db_subnet_groups
  - rds
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>db_subnet_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_subnet_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::RDS::DBSubnetGroup`` resource creates a database subnet group. Subnet groups must contain at least two subnets in two different Availability Zones in the same region. &lt;br&#x2F;&gt; For more information, see &#91;Working with DB subnet groups&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonRDS&#x2F;latest&#x2F;UserGuide&#x2F;USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Subnets) in the *Amazon RDS User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rds.db_subnet_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>db_subnet_group_name</code></td><td><code>string</code></td><td>The name for the DB subnet group. This value is stored as a lowercase string.&lt;br&#x2F;&gt; Constraints: Must contain no more than 255 lowercase alphanumeric characters or hyphens. Must not be "Default".&lt;br&#x2F;&gt; Example: ``mysubnetgroup``</td></tr>
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
db_subnet_group_name
FROM aws.rds.db_subnet_groups
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>db_subnet_groups</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
rds:CreateDBSubnetGroup,
rds:DescribeDBSubnetGroups,
rds:AddTagsToResource,
rds:RemoveTagsFromResource,
rds:ListTagsForResource
```

### List
```json
rds:DescribeDBSubnetGroups
```


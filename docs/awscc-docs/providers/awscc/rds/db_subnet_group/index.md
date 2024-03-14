---
title: db_subnet_group
hide_title: false
hide_table_of_contents: false
keywords:
  - db_subnet_group
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
Gets an individual <code>db_subnet_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_subnet_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_subnet_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rds.db_subnet_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>db_subnet_group_description</code></td><td><code>string</code></td><td>The description for the DB subnet group.</td></tr>
<tr><td><code>db_subnet_group_name</code></td><td><code>string</code></td><td>The name for the DB subnet group. This value is stored as a lowercase string.&lt;br&#x2F;&gt; Constraints: Must contain no more than 255 lowercase alphanumeric characters or hyphens. Must not be "Default".&lt;br&#x2F;&gt; Example: ``mysubnetgroup``</td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td>The EC2 Subnet IDs for the DB subnet group.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An optional array of key-value pairs to apply to this DB subnet group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
db_subnet_group_description,
db_subnet_group_name,
subnet_ids,
tags
FROM awscc.rds.db_subnet_group
WHERE data__Identifier = '<DBSubnetGroupName>';
```

## Permissions

To operate on the <code>db_subnet_group</code> resource, the following permissions are required:

### Read
```json
rds:DescribeDBSubnetGroups,
rds:ListTagsForResource
```

### Update
```json
rds:ModifyDBSubnetGroup,
rds:DescribeDBSubnetGroups,
rds:AddTagsToResource,
rds:RemoveTagsFromResource,
rds:ListTagsForResource
```

### Delete
```json
rds:DeleteDBSubnetGroup,
rds:DescribeDBSubnetGroups,
rds:ListTagsForResource
```


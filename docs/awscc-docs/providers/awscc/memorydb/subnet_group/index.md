---
title: subnet_group
hide_title: false
hide_table_of_contents: false
keywords:
  - subnet_group
  - memorydb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>subnet_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>subnet_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.memorydb.subnet_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>subnet_group_name</code></td><td><code>string</code></td><td>The name of the subnet group. This value must be unique as it also serves as the subnet group identifier.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>An optional description of the subnet group.</td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td>A list of VPC subnet IDs for the subnet group.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this subnet group.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the subnet group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
subnet_group_name,
description,
subnet_ids,
tags,
a_rn
FROM awscc.memorydb.subnet_group
WHERE region = 'us-east-1'
AND data__Identifier = '{SubnetGroupName}';
```

## Permissions

To operate on the <code>subnet_group</code> resource, the following permissions are required:

### Read
```json
memorydb:DescribeSubnetGroups,
memorydb:ListTags
```

### Update
```json
memorydb:UpdateSubnetGroup,
memorydb:DescribeSubnetGroups,
memorydb:ListTags,
memorydb:TagResource,
memorydb:UntagResource
```

### Delete
```json
memorydb:DeleteSubnetGroup,
memorydb:DescribeSubnetGroups
```


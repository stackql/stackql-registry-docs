---
title: db_parameter_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - db_parameter_groups
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
Retrieves a list of <code>db_parameter_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_parameter_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_parameter_groups</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rds.db_parameter_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>db_parameter_group_name</code></td><td><code>string</code></td><td>The name of the DB parameter group.&lt;br&#x2F;&gt; Constraints:&lt;br&#x2F;&gt;  +  Must be 1 to 255 letters, numbers, or hyphens.&lt;br&#x2F;&gt;  +  First character must be a letter&lt;br&#x2F;&gt;  +  Can't end with a hyphen or contain two consecutive hyphens&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; If you don't specify a value for ``DBParameterGroupName`` property, a name is automatically created for the DB parameter group.&lt;br&#x2F;&gt;  This value is stored as a lowercase string.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
d_bparameter_group_name
FROM awscc.rds.db_parameter_groups
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>db_parameter_groups</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
rds:AddTagsToResource,
rds:CreateDBParameterGroup,
rds:DescribeDBParameterGroups,
rds:DescribeDBParameters,
rds:DescribeEngineDefaultParameters,
rds:ListTagsForResource,
rds:ModifyDBParameterGroup,
rds:RemoveTagsFromResource
```

### List
```json
rds:DescribeDBParameterGroups
```


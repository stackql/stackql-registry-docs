---
title: role_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - role_aliases
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>role_aliases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>role_aliases</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.role_aliases</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>role_alias</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>role_aliases</code> resource, the following permissions are required:

### Create
```json
iam:GetRole,
iam:PassRole,
iot:CreateRoleAlias,
iot:DescribeRoleAlias,
iot:TagResource,
iot:ListTagsForResource
```

### List
```json
iot:ListRoleAliases
```


## Example
```sql
SELECT
region,
role_alias
FROM awscc.iot.role_aliases
WHERE region = 'us-east-1'
```

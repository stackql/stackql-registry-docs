---
title: role_alias
hide_title: false
hide_table_of_contents: false
keywords:
  - role_alias
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
Gets an individual <code>role_alias</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>role_alias</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.role_alias</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>role_alias</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_alias_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>credential_duration_seconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
role_alias,
role_alias_arn,
role_arn,
credential_duration_seconds,
tags
FROM awscc.iot.role_alias
WHERE region = 'us-east-1'
AND data__Identifier = '{RoleAlias}';
```

## Permissions

To operate on the <code>role_alias</code> resource, the following permissions are required:

### Read
```json
iam:GetRole,
iam:PassRole,
iot:DescribeRoleAlias,
iot:ListTagsForResource
```

### Update
```json
iam:GetRole,
iam:PassRole,
iot:UpdateRoleAlias,
iot:DescribeRoleAlias,
iot:TagResource,
iot:UntagResource,
iot:ListTagsForResource
```

### Delete
```json
iot:DeleteRoleAlias,
iot:DescribeRoleAlias
```


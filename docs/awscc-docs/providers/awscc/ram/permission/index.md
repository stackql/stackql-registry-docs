---
title: permission
hide_title: false
hide_table_of_contents: false
keywords:
  - permission
  - ram
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>permission</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permission</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>permission</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ram.permission</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the permission.</td></tr>
<tr><td><code>version</code></td><td><code>string</code></td><td>Version of the permission.</td></tr>
<tr><td><code>is_resource_type_default</code></td><td><code>boolean</code></td><td>Set to true to use this as the default permission.</td></tr>
<tr><td><code>permission_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_type</code></td><td><code>string</code></td><td>The resource type this permission can be used with.</td></tr>
<tr><td><code>policy_template</code></td><td><code>object</code></td><td>Policy template for the permission.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>permission</code> resource, the following permissions are required:

### Read
```json
ram:GetPermission
```

### Update
```json
ram:CreatePermissionVersion,
ram:DeletePermissionVersion,
ram:SetDefaultPermissionVersion,
ram:GetPermission,
ram:ReplacePermissionAssociations,
ram:ListReplacePermissionAssociationsWork,
ram:ListPermissionVersions,
ram:UntagResource,
ram:TagResource
```

### Delete
```json
ram:DeletePermissionVersion,
ram:DeletePermission
```


## Example
```sql
SELECT
region,
arn,
name,
version,
is_resource_type_default,
permission_type,
resource_type,
policy_template,
tags
FROM awscc.ram.permission
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```

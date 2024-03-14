---
title: identity_pool_role_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_pool_role_attachment
  - cognito
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>identity_pool_role_attachment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_pool_role_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>identity_pool_role_attachment</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cognito.identity_pool_role_attachment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>identity_pool_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>roles</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_mappings</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
identity_pool_id,
roles,
id,
role_mappings
FROM awscc.cognito.identity_pool_role_attachment
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>identity_pool_role_attachment</code> resource, the following permissions are required:

### Read
```json
cognito-identity:GetIdentityPoolRoles
```

### Update
```json
cognito-identity:GetIdentityPoolRoles,
cognito-identity:SetIdentityPoolRoles,
iam:PassRole
```

### Delete
```json
cognito-identity:GetIdentityPoolRoles,
cognito-identity:SetIdentityPoolRoles
```


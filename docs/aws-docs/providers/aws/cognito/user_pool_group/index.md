---
title: user_pool_group
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_group
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
Gets or operates on an individual <code>user_pool_group</code> resource, use <code>user_pool_groups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolGroup</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cognito.user_pool_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>precedence</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>user_pool_id</code></td><td><code>string</code></td><td></td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
description,
group_name,
precedence,
role_arn,
user_pool_id
FROM aws.cognito.user_pool_group
WHERE data__Identifier = '<UserPoolId>|<GroupName>';
```

## Permissions

To operate on the <code>user_pool_group</code> resource, the following permissions are required:

### Read
```json
cognito-idp:GetGroup
```

### Update
```json
cognito-idp:UpdateGroup,
iam:PassRole,
iam:PutRolePolicy
```

### Delete
```json
cognito-idp:DeleteGroup,
cognito-idp:GetGroup,
iam:PutRolePolicy
```


---
title: security_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - security_policy
  - opensearchserverless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>security_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon OpenSearchServerless security policy resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.opensearchserverless.security_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the policy</td></tr>
<tr><td><code>policy</code></td><td><code>string</code></td><td>The JSON policy document that is the content for the policy</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the policy</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
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
policy,
name,
type
FROM aws.opensearchserverless.security_policy
WHERE data__Identifier = '<Type>|<Name>';
```

## Permissions

To operate on the <code>security_policy</code> resource, the following permissions are required:

### Update
```json
aoss:GetSecurityPolicy,
aoss:UpdateSecurityPolicy,
kms:DescribeKey,
kms:CreateGrant
```

### Delete
```json
aoss:GetSecurityPolicy,
aoss:DeleteSecurityPolicy
```

### Read
```json
aoss:GetSecurityPolicy,
kms:DescribeKey
```


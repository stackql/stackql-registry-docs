---
title: policy
hide_title: false
hide_table_of_contents: false
keywords:
  - policy
  - verifiedpermissions
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.verifiedpermissions.policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>definition</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>policy_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy_store_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
definition,
policy_id,
policy_store_id,
policy_type
FROM awscc.verifiedpermissions.policy
WHERE data__Identifier = '<PolicyId>|<PolicyStoreId>';
```

## Permissions

To operate on the <code>policy</code> resource, the following permissions are required:

### Read
```json
verifiedpermissions:CreatePolicy,
verifiedpermissions:GetPolicy,
verifiedpermissions:UpdatePolicy,
verifiedpermissions:DeletePolicy
```

### Update
```json
verifiedpermissions:CreatePolicy,
verifiedpermissions:GetPolicy,
verifiedpermissions:UpdatePolicy,
verifiedpermissions:DeletePolicy
```

### Delete
```json
verifiedpermissions:CreatePolicy,
verifiedpermissions:GetPolicy,
verifiedpermissions:UpdatePolicy,
verifiedpermissions:DeletePolicy
```


---
title: policy_store
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_store
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
Gets an individual <code>policy_store</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_store</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>policy_store</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.verifiedpermissions.policy_store</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy_store_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>validation_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>schema</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
description,
policy_store_id,
validation_settings,
schema
FROM awscc.verifiedpermissions.policy_store
WHERE data__Identifier = '<PolicyStoreId>';
```

## Permissions

To operate on the <code>policy_store</code> resource, the following permissions are required:

### Read
```json
verifiedpermissions:CreatePolicyStore,
verifiedpermissions:GetPolicyStore,
verifiedpermissions:UpdatePolicyStore,
verifiedpermissions:DeletePolicyStore,
verifiedpermissions:GetSchema
```

### Update
```json
verifiedpermissions:CreatePolicyStore,
verifiedpermissions:GetPolicyStore,
verifiedpermissions:UpdatePolicyStore,
verifiedpermissions:DeletePolicyStore,
verifiedpermissions:GetSchema,
verifiedpermissions:PutSchema
```

### Delete
```json
verifiedpermissions:CreatePolicyStore,
verifiedpermissions:GetPolicyStore,
verifiedpermissions:UpdatePolicyStore,
verifiedpermissions:DeletePolicyStore
```


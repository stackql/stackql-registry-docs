---
title: policy_template
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_template
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
Gets an individual <code>policy_template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>policy_template</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.verifiedpermissions.policy_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy_store_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy_template_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>statement</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
policy_store_id,
policy_template_id,
statement
FROM awscc.verifiedpermissions.policy_template
WHERE region = 'us-east-1'
AND data__Identifier = '{PolicyStoreId}';
AND data__Identifier = '{PolicyTemplateId}';
```

## Permissions

To operate on the <code>policy_template</code> resource, the following permissions are required:

### Read
```json
verifiedpermissions:CreatePolicyTemplate,
verifiedpermissions:GetPolicyTemplate,
verifiedpermissions:UpdatePolicyTemplate,
verifiedpermissions:DeletePolicyTemplate
```

### Update
```json
verifiedpermissions:CreatePolicyTemplate,
verifiedpermissions:GetPolicyTemplate,
verifiedpermissions:UpdatePolicyTemplate,
verifiedpermissions:DeletePolicyTemplate
```

### Delete
```json
verifiedpermissions:CreatePolicyTemplate,
verifiedpermissions:GetPolicyTemplate,
verifiedpermissions:UpdatePolicyTemplate,
verifiedpermissions:DeletePolicyTemplate
```


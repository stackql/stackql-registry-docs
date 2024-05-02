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
<tr><td><b>Description</b></td><td>Definition of AWS::VerifiedPermissions::PolicyTemplate Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.verifiedpermissions.policy_template</code></td></tr>
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
policy_store_id,
policy_template_id,
statement
FROM aws.verifiedpermissions.policy_template
WHERE data__Identifier = '<PolicyStoreId>|<PolicyTemplateId>';
```

## Permissions

To operate on the <code>policy_template</code> resource, the following permissions are required:

### Read
```json
verifiedpermissions:GetPolicyTemplate
```

### Update
```json
verifiedpermissions:UpdatePolicyTemplate,
verifiedpermissions:GetPolicyTemplate
```

### Delete
```json
verifiedpermissions:DeletePolicyTemplate,
verifiedpermissions:GetPolicyTemplate
```


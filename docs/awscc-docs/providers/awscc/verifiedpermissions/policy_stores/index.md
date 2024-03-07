---
title: policy_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_stores
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
Retrieves a list of <code>policy_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>policy_stores</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.verifiedpermissions.policy_stores</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>policy_store_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>policy_stores</code> resource, the following permissions are required:

### Create
<pre>
verifiedpermissions:CreatePolicyStore,
verifiedpermissions:GetPolicyStore,
verifiedpermissions:UpdatePolicyStore,
verifiedpermissions:DeletePolicyStore,
verifiedpermissions:PutSchema</pre>

### List
<pre>
verifiedpermissions:CreatePolicyStore,
verifiedpermissions:GetPolicyStore,
verifiedpermissions:UpdatePolicyStore,
verifiedpermissions:DeletePolicyStore,
verifiedpermissions:ListPolicyStores,
verifiedpermissions:GetSchema</pre>


## Example
```sql
SELECT
region,
policy_store_id
FROM awscc.verifiedpermissions.policy_stores
WHERE region = 'us-east-1'
```

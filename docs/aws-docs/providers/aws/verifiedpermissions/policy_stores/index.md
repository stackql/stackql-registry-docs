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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>policy_stores</code> in a region or create a <code>policy_stores</code> resource, use <code>policy_store</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a policy store that you can place schema, policies, and policy templates in to validate authorization requests</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.verifiedpermissions.policy_stores" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="policy_store_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
policy_store_id
FROM aws.verifiedpermissions.policy_stores
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>policy_stores</code> resource, the following permissions are required:

### Create
```json
verifiedpermissions:CreatePolicyStore,
verifiedpermissions:GetPolicyStore,
verifiedpermissions:PutSchema
```

### List
```json
verifiedpermissions:ListPolicyStores,
verifiedpermissions:GetPolicyStore,
verifiedpermissions:GetSchema
```

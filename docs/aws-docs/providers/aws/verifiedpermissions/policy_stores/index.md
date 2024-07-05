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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>policy_store</code> resource or lists <code>policy_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a policy store that you can place schema, policies, and policy templates in to validate authorization requests</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.verifiedpermissions.policy_stores" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_store_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="validation_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="schema" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="ValidationSettings, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>policy_stores</code> in a region.
```sql
SELECT
region,
arn,
description,
policy_store_id,
validation_settings,
schema
FROM aws.verifiedpermissions.policy_stores
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>policy_store</code>.
```sql
SELECT
region,
arn,
description,
policy_store_id,
validation_settings,
schema
FROM aws.verifiedpermissions.policy_stores
WHERE region = 'us-east-1' AND data__Identifier = '<PolicyStoreId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policy_store</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.verifiedpermissions.policy_stores (
 ValidationSettings,
 region
)
SELECT 
'{{ ValidationSettings }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.verifiedpermissions.policy_stores (
 Description,
 ValidationSettings,
 Schema,
 region
)
SELECT 
 '{{ Description }}',
 '{{ ValidationSettings }}',
 '{{ Schema }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: policy_store
    props:
      - name: Description
        value: '{{ Description }}'
      - name: ValidationSettings
        value:
          Mode: '{{ Mode }}'
      - name: Schema
        value:
          CedarJson: '{{ CedarJson }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.verifiedpermissions.policy_stores
WHERE data__Identifier = '<PolicyStoreId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>policy_stores</code> resource, the following permissions are required:

### Create
```json
verifiedpermissions:CreatePolicyStore,
verifiedpermissions:GetPolicyStore,
verifiedpermissions:PutSchema
```

### Read
```json
verifiedpermissions:GetPolicyStore,
verifiedpermissions:GetSchema
```

### Update
```json
verifiedpermissions:UpdatePolicyStore,
verifiedpermissions:GetPolicyStore,
verifiedpermissions:GetSchema,
verifiedpermissions:PutSchema
```

### Delete
```json
verifiedpermissions:DeletePolicyStore,
verifiedpermissions:GetPolicyStore
```

### List
```json
verifiedpermissions:ListPolicyStores,
verifiedpermissions:GetPolicyStore,
verifiedpermissions:GetSchema
```


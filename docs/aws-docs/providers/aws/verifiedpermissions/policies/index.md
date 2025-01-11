---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
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

Creates, updates, deletes or gets a <code>policy</code> resource or lists <code>policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::VerifiedPermissions::Policy Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.verifiedpermissions.policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="definition" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_store_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policy.html"><code>AWS::VerifiedPermissions::Policy</code></a>.

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
    <td><CopyableCode code="Definition, PolicyStoreId, region" /></td>
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
Gets all <code>policies</code> in a region.
```sql
SELECT
region,
definition,
policy_id,
policy_store_id,
policy_type
FROM aws.verifiedpermissions.policies
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>policy</code>.
```sql
SELECT
region,
definition,
policy_id,
policy_store_id,
policy_type
FROM aws.verifiedpermissions.policies
WHERE region = 'us-east-1' AND data__Identifier = '<PolicyId>|<PolicyStoreId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.verifiedpermissions.policies (
 Definition,
 PolicyStoreId,
 region
)
SELECT 
'{{ Definition }}',
 '{{ PolicyStoreId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.verifiedpermissions.policies (
 Definition,
 PolicyStoreId,
 region
)
SELECT 
 '{{ Definition }}',
 '{{ PolicyStoreId }}',
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
  - name: policy
    props:
      - name: Definition
        value: null
      - name: PolicyStoreId
        value: '{{ PolicyStoreId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.verifiedpermissions.policies
WHERE data__Identifier = '<PolicyId|PolicyStoreId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>policies</code> resource, the following permissions are required:

### Create
```json
verifiedpermissions:CreatePolicy,
verifiedpermissions:GetPolicy
```

### Read
```json
verifiedpermissions:GetPolicy
```

### Update
```json
verifiedpermissions:UpdatePolicy,
verifiedpermissions:GetPolicy
```

### Delete
```json
verifiedpermissions:DeletePolicy,
verifiedpermissions:GetPolicy
```

### List
```json
verifiedpermissions:ListPolicies,
verifiedpermissions:GetPolicy
```

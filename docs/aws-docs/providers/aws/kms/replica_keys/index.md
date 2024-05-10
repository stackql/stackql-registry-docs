---
title: replica_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - replica_keys
  - kms
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


Used to retrieve a list of <code>replica_keys</code> in a region or to create or delete a <code>replica_keys</code> resource, use <code>replica_key</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replica_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::KMS::ReplicaKey resource specifies a multi-region replica AWS KMS key in AWS Key Management Service (AWS KMS).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kms.replica_keys" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="key_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
key_id
FROM aws.kms.replica_keys
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>replica_key</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- replica_key.iql (required properties only)
INSERT INTO aws.kms.replica_keys (
 KeyPolicy,
 PrimaryKeyArn,
 region
)
SELECT 
'{{ KeyPolicy }}',
 '{{ PrimaryKeyArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- replica_key.iql (all properties)
INSERT INTO aws.kms.replica_keys (
 Description,
 PendingWindowInDays,
 KeyPolicy,
 PrimaryKeyArn,
 Enabled,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ PendingWindowInDays }}',
 '{{ KeyPolicy }}',
 '{{ PrimaryKeyArn }}',
 '{{ Enabled }}',
 '{{ Tags }}',
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
  - name: replica_key
    props:
      - name: Description
        value: '{{ Description }}'
      - name: PendingWindowInDays
        value: '{{ PendingWindowInDays }}'
      - name: KeyPolicy
        value: {}
      - name: PrimaryKeyArn
        value: '{{ PrimaryKeyArn }}'
      - name: Enabled
        value: '{{ Enabled }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.kms.replica_keys
WHERE data__Identifier = '<KeyId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>replica_keys</code> resource, the following permissions are required:

### Create
```json
kms:ReplicateKey,
kms:CreateKey,
kms:DescribeKey,
kms:DisableKey,
kms:TagResource
```

### List
```json
kms:ListKeys,
kms:DescribeKey
```

### Delete
```json
kms:DescribeKey,
kms:ScheduleKeyDeletion
```


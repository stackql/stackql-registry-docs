---
title: farms
hide_title: false
hide_table_of_contents: false
keywords:
  - farms
  - deadline
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

Creates, updates, deletes or gets a <code>farm</code> resource or lists <code>farms</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>farms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::Farm Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.deadline.farms" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="farm_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="DisplayName, region" /></td>
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
Gets all <code>farms</code> in a region.
```sql
SELECT
region,
description,
display_name,
farm_id,
kms_key_arn,
arn
FROM aws.deadline.farms
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>farm</code>.
```sql
SELECT
region,
description,
display_name,
farm_id,
kms_key_arn,
arn
FROM aws.deadline.farms
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>farm</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.deadline.farms (
 DisplayName,
 region
)
SELECT 
'{{ DisplayName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.deadline.farms (
 Description,
 DisplayName,
 KmsKeyArn,
 region
)
SELECT 
 '{{ Description }}',
 '{{ DisplayName }}',
 '{{ KmsKeyArn }}',
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
  - name: farm
    props:
      - name: Description
        value: '{{ Description }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: KmsKeyArn
        value: '{{ KmsKeyArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.deadline.farms
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>farms</code> resource, the following permissions are required:

### Create
```json
deadline:CreateFarm,
deadline:GetFarm,
kms:Encrypt,
kms:Decrypt,
kms:CreateGrant,
kms:GenerateDataKey
```

### Read
```json
deadline:GetFarm,
identitystore:ListGroupMembershipsForMember,
kms:Encrypt,
kms:Decrypt,
kms:CreateGrant,
kms:GenerateDataKey
```

### Update
```json
deadline:UpdateFarm,
deadline:GetFarm,
identitystore:ListGroupMembershipsForMember,
kms:Encrypt,
kms:Decrypt,
kms:CreateGrant,
kms:GenerateDataKey
```

### Delete
```json
deadline:DeleteFarm,
deadline:GetFarm,
identitystore:ListGroupMembershipsForMember,
kms:Encrypt,
kms:Decrypt,
kms:CreateGrant,
kms:GenerateDataKey
```

### List
```json
deadline:ListFarms,
identitystore:ListGroupMembershipsForMember
```


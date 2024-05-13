---
title: studios
hide_title: false
hide_table_of_contents: false
keywords:
  - studios
  - nimblestudio
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


Used to retrieve a list of <code>studios</code> in a region or to create or delete a <code>studios</code> resource, use <code>studio</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studios</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a studio that contains other Nimble Studio resources</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.studios" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="DisplayName, UserRoleArn, AdminRoleArn, StudioName, region" /></td>
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
studio_id
FROM aws.nimblestudio.studios
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>studio</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.nimblestudio.studios (
 AdminRoleArn,
 DisplayName,
 StudioName,
 UserRoleArn,
 region
)
SELECT 
'{{ AdminRoleArn }}',
 '{{ DisplayName }}',
 '{{ StudioName }}',
 '{{ UserRoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.nimblestudio.studios (
 AdminRoleArn,
 DisplayName,
 StudioEncryptionConfiguration,
 StudioName,
 Tags,
 UserRoleArn,
 region
)
SELECT 
 '{{ AdminRoleArn }}',
 '{{ DisplayName }}',
 '{{ StudioEncryptionConfiguration }}',
 '{{ StudioName }}',
 '{{ Tags }}',
 '{{ UserRoleArn }}',
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
  - name: studio
    props:
      - name: AdminRoleArn
        value: '{{ AdminRoleArn }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: StudioEncryptionConfiguration
        value:
          KeyType: '{{ KeyType }}'
          KeyArn: '{{ KeyArn }}'
      - name: StudioName
        value: '{{ StudioName }}'
      - name: Tags
        value: {}
      - name: UserRoleArn
        value: '{{ UserRoleArn }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.nimblestudio.studios
WHERE data__Identifier = '<StudioId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>studios</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
nimble:CreateStudio,
nimble:GetStudio,
nimble:TagResource,
sso:CreateManagedApplicationInstance,
kms:Encrypt,
kms:Decrypt,
kms:CreateGrant,
kms:ListGrants,
kms:GenerateDataKey
```

### Delete
```json
nimble:DeleteStudio,
nimble:GetStudio,
nimble:UntagResource,
kms:Encrypt,
kms:Decrypt,
kms:ListGrants,
kms:RetireGrant,
kms:GenerateDataKey,
sso:DeleteManagedApplicationInstance,
sso:GetManagedApplicationInstance
```

### List
```json
nimble:ListStudios
```


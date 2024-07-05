---
title: dataset_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset_groups
  - personalize
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

Creates, updates, deletes or gets a <code>dataset_group</code> resource or lists <code>dataset_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::Personalize::DatasetGroup.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.personalize.dataset_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="dataset_group_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the dataset group.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the new dataset group.</td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name(ARN) of a AWS Key Management Service (KMS) key used to encrypt the datasets.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the AWS Identity and Access Management (IAM) role that has permissions to access the AWS Key Management Service (KMS) key. Supplying an IAM role is only valid when also specifying a KMS key.</td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td>The domain of a Domain dataset group.</td></tr>
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
    <td><CopyableCode code="Name, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>dataset_groups</code> in a region.
```sql
SELECT
region,
dataset_group_arn,
name,
kms_key_arn,
role_arn,
domain
FROM aws.personalize.dataset_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>dataset_group</code>.
```sql
SELECT
region,
dataset_group_arn,
name,
kms_key_arn,
role_arn,
domain
FROM aws.personalize.dataset_groups
WHERE region = 'us-east-1' AND data__Identifier = '<DatasetGroupArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dataset_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.personalize.dataset_groups (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.personalize.dataset_groups (
 Name,
 KmsKeyArn,
 RoleArn,
 Domain,
 region
)
SELECT 
 '{{ Name }}',
 '{{ KmsKeyArn }}',
 '{{ RoleArn }}',
 '{{ Domain }}',
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
  - name: dataset_group
    props:
      - name: Name
        value: '{{ Name }}'
      - name: KmsKeyArn
        value: '{{ KmsKeyArn }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Domain
        value: '{{ Domain }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.personalize.dataset_groups
WHERE data__Identifier = '<DatasetGroupArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>dataset_groups</code> resource, the following permissions are required:

### Create
```json
personalize:CreateDatasetGroup,
personalize:DescribeDatasetGroup,
iam:PassRole
```

### Read
```json
personalize:DescribeDatasetGroup
```

### Delete
```json
personalize:DescribeDatasetGroup,
personalize:DeleteDatasetGroup
```

### List
```json
personalize:ListDatasetGroups
```


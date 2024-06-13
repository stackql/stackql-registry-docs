---
title: model_package_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - model_package_groups
  - sagemaker
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

Creates, updates, deletes or gets a <code>model_package_group</code> resource or lists <code>model_package_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_package_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ModelPackageGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.model_package_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="model_package_group_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the model package group.</td></tr>
<tr><td><CopyableCode code="model_package_group_name" /></td><td><code>string</code></td><td>The name of the model package group.</td></tr>
<tr><td><CopyableCode code="model_package_group_description" /></td><td><code>string</code></td><td>The description of the model package group.</td></tr>
<tr><td><CopyableCode code="model_package_group_policy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time at which the model package group was created.</td></tr>
<tr><td><CopyableCode code="model_package_group_status" /></td><td><code>string</code></td><td>The status of a modelpackage group job.</td></tr>
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
    <td><CopyableCode code="ModelPackageGroupName, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>model_package_groups</code> in a region.
```sql
SELECT
region,
model_package_group_arn
FROM aws.sagemaker.model_package_groups
WHERE region = 'us-east-1';
```
Gets all properties from a <code>model_package_group</code>.
```sql
SELECT
region,
tags,
model_package_group_arn,
model_package_group_name,
model_package_group_description,
model_package_group_policy,
creation_time,
model_package_group_status
FROM aws.sagemaker.model_package_groups
WHERE region = 'us-east-1' AND data__Identifier = '<ModelPackageGroupArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>model_package_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.model_package_groups (
 ModelPackageGroupName,
 region
)
SELECT 
'{{ ModelPackageGroupName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.model_package_groups (
 Tags,
 ModelPackageGroupName,
 ModelPackageGroupDescription,
 ModelPackageGroupPolicy,
 region
)
SELECT 
 '{{ Tags }}',
 '{{ ModelPackageGroupName }}',
 '{{ ModelPackageGroupDescription }}',
 '{{ ModelPackageGroupPolicy }}',
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
  - name: model_package_group
    props:
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: ModelPackageGroupName
        value: '{{ ModelPackageGroupName }}'
      - name: ModelPackageGroupDescription
        value: '{{ ModelPackageGroupDescription }}'
      - name: ModelPackageGroupPolicy
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.model_package_groups
WHERE data__Identifier = '<ModelPackageGroupArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>model_package_groups</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateModelPackageGroup,
sagemaker:DescribeModelPackageGroup,
sagemaker:GetModelPackageGroupPolicy,
sagemaker:PutModelPackageGroupPolicy,
sagemaker:ListTags,
sagemaker:AddTags
```

### Delete
```json
sagemaker:DeleteModelPackageGroup,
sagemaker:DescribeModelPackageGroup,
sagemaker:GetModelPackageGroupPolicy,
sagemaker:DeleteModelPackageGroupPolicy
```

### List
```json
sagemaker:ListModelPackageGroups
```

### Read
```json
sagemaker:DescribeModelPackageGroup,
sagemaker:GetModelPackageGroupPolicy,
sagemaker:PutModelPackageGroupPolicy,
sagemaker:ListTags
```

### Update
```json
sagemaker:DescribeModelPackageGroup,
sagemaker:GetModelPackageGroupPolicy,
sagemaker:DeleteModelPackageGroupPolicy,
sagemaker:PutModelPackageGroupPolicy,
sagemaker:ListTags,
sagemaker:AddTags,
sagemaker:DeleteTags
```


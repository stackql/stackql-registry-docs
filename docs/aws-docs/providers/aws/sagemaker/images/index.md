---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
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

Creates, updates, deletes or gets an <code>image</code> resource or lists <code>images</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::Image</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.images" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="image_name" /></td><td><code>string</code></td><td>The name of the image this version belongs to.</td></tr>
<tr><td><CopyableCode code="image_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the parent image.</td></tr>
<tr><td><CopyableCode code="image_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to perform tasks on behalf of the customer.</td></tr>
<tr><td><CopyableCode code="image_display_name" /></td><td><code>string</code></td><td>The display name of the image.</td></tr>
<tr><td><CopyableCode code="image_description" /></td><td><code>string</code></td><td>A description of the image.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="ImageName, ImageRoleArn, region" /></td>
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
List all <code>images</code> in a region.
```sql
SELECT
region,
image_arn
FROM aws.sagemaker.images
WHERE region = 'us-east-1';
```
Gets all properties from an <code>image</code>.
```sql
SELECT
region,
image_name,
image_arn,
image_role_arn,
image_display_name,
image_description,
tags
FROM aws.sagemaker.images
WHERE region = 'us-east-1' AND data__Identifier = '<ImageArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>image</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.images (
 ImageName,
 ImageRoleArn,
 region
)
SELECT 
'{{ ImageName }}',
 '{{ ImageRoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.images (
 ImageName,
 ImageRoleArn,
 ImageDisplayName,
 ImageDescription,
 Tags,
 region
)
SELECT 
 '{{ ImageName }}',
 '{{ ImageRoleArn }}',
 '{{ ImageDisplayName }}',
 '{{ ImageDescription }}',
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
  - name: image
    props:
      - name: ImageName
        value: '{{ ImageName }}'
      - name: ImageRoleArn
        value: '{{ ImageRoleArn }}'
      - name: ImageDisplayName
        value: '{{ ImageDisplayName }}'
      - name: ImageDescription
        value: '{{ ImageDescription }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.images
WHERE data__Identifier = '<ImageArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>images</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateImage,
sagemaker:DescribeImage,
iam:PassRole,
sagemaker:AddTags,
sagemaker:ListTags
```

### Read
```json
sagemaker:DescribeImage,
sagemaker:ListTags
```

### Update
```json
sagemaker:UpdateImage,
sagemaker:DescribeImage,
sagemaker:ListTags,
sagemaker:AddTags,
sagemaker:DeleteTags,
iam:PassRole
```

### Delete
```json
sagemaker:DeleteImage,
sagemaker:DescribeImage
```

### List
```json
sagemaker:ListImages
```


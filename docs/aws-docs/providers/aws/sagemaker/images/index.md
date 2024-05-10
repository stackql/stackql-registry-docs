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


Used to retrieve a list of <code>images</code> in a region or to create or delete a <code>images</code> resource, use <code>image</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::Image</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.images" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="image_arn" /></td><td><code>undefined</code></td><td></td></tr>
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
image_arn
FROM aws.sagemaker.images
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "ImageName": "{{ ImageName }}",
 "ImageRoleArn": "{{ ImageRoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.sagemaker.images (
 ImageName,
 ImageRoleArn,
 region
)
SELECT 
{{ ImageName }},
 {{ ImageRoleArn }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ImageName": "{{ ImageName }}",
 "ImageRoleArn": "{{ ImageRoleArn }}",
 "ImageDisplayName": "{{ ImageDisplayName }}",
 "ImageDescription": "{{ ImageDescription }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.sagemaker.images (
 ImageName,
 ImageRoleArn,
 ImageDisplayName,
 ImageDescription,
 Tags,
 region
)
SELECT 
 {{ ImageName }},
 {{ ImageRoleArn }},
 {{ ImageDisplayName }},
 {{ ImageDescription }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
sagemaker:DeleteImage,
sagemaker:DescribeImage
```

### List
```json
sagemaker:ListImages
```


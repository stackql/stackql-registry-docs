---
title: image
hide_title: false
hide_table_of_contents: false
keywords:
  - image
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


Gets or updates an individual <code>image</code> resource, use <code>images</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::Image</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.image" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="image_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="image_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="image_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="image_display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="image_description" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
image_name,
image_arn,
image_role_arn,
image_display_name,
image_description,
tags
FROM aws.sagemaker.image
WHERE region = 'us-east-1' AND data__Identifier = '<ImageArn>';
```


## Permissions

To operate on the <code>image</code> resource, the following permissions are required:

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


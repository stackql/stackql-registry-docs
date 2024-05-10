---
title: model_package_group
hide_title: false
hide_table_of_contents: false
keywords:
  - model_package_group
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


Gets or updates an individual <code>model_package_group</code> resource, use <code>model_package_groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_package_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ModelPackageGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.model_package_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="model_package_group_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_package_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_package_group_description" /></td><td><code>string</code></td><td></td></tr>
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
tags,
model_package_group_arn,
model_package_group_name,
model_package_group_description,
model_package_group_policy,
creation_time,
model_package_group_status
FROM aws.sagemaker.model_package_group
WHERE region = 'us-east-1' AND data__Identifier = '<ModelPackageGroupArn>';
```


## Permissions

To operate on the <code>model_package_group</code> resource, the following permissions are required:

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


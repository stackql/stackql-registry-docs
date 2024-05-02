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
Gets or operates on an individual <code>model_package_group</code> resource, use <code>model_package_groups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_package_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ModelPackageGroup</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.model_package_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>model_package_group_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>model_package_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>model_package_group_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>model_package_group_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>The time at which the model package group was created.</td></tr>
<tr><td><code>model_package_group_status</code></td><td><code>string</code></td><td>The status of a modelpackage group job.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
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
WHERE data__Identifier = '<ModelPackageGroupArn>';
```

## Permissions

To operate on the <code>model_package_group</code> resource, the following permissions are required:

### Delete
```json
sagemaker:DeleteModelPackageGroup,
sagemaker:DescribeModelPackageGroup,
sagemaker:GetModelPackageGroupPolicy,
sagemaker:DeleteModelPackageGroupPolicy
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


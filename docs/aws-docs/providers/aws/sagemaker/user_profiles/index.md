---
title: user_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - user_profiles
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
Retrieves a list of <code>user_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::UserProfile</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.user_profiles</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>user_profile_name</code></td><td><code>string</code></td><td>A name for the UserProfile.</td></tr>
<tr><td><code>domain_id</code></td><td><code>string</code></td><td>The ID of the associated Domain.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
user_profile_name,
domain_id
FROM aws.sagemaker.user_profiles
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>user_profiles</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateUserProfile,
sagemaker:DescribeUserProfile,
sagemaker:DescribeImage,
sagemaker:DescribeImageVersion,
iam:PassRole
```

### List
```json
sagemaker:ListUserProfiles
```


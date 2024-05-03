---
title: user_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - user_profile
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

Gets or operates on an individual <code>user_profile</code> resource, use <code>user_profiles</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::UserProfile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.user_profile" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="user_profile_arn" /></td><td><code>string</code></td><td>The user profile Amazon Resource Name (ARN).</td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the associated Domain.</td></tr>
<tr><td><CopyableCode code="single_sign_on_user_identifier" /></td><td><code>string</code></td><td>A specifier for the type of value specified in SingleSignOnUserValue. Currently, the only supported value is "UserName". If the Domain's AuthMode is SSO, this field is required. If the Domain's AuthMode is not SSO, this field cannot be specified.</td></tr>
<tr><td><CopyableCode code="single_sign_on_user_value" /></td><td><code>string</code></td><td>The username of the associated AWS Single Sign-On User for this UserProfile. If the Domain's AuthMode is SSO, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not SSO, this field cannot be specified.</td></tr>
<tr><td><CopyableCode code="user_profile_name" /></td><td><code>string</code></td><td>A name for the UserProfile.</td></tr>
<tr><td><CopyableCode code="user_settings" /></td><td><code>object</code></td><td>A collection of settings.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags to apply to the user profile.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
user_profile_arn,
domain_id,
single_sign_on_user_identifier,
single_sign_on_user_value,
user_profile_name,
user_settings,
tags
FROM aws.sagemaker.user_profile
WHERE data__Identifier = '<UserProfileName>|<DomainId>';
```

## Permissions

To operate on the <code>user_profile</code> resource, the following permissions are required:

### Read
```json
sagemaker:DescribeUserProfile
```

### Update
```json
sagemaker:UpdateUserProfile,
sagemaker:DescribeUserProfile,
sagemaker:DescribeImage,
sagemaker:DescribeImageVersion,
iam:PassRole
```

### Delete
```json
sagemaker:DeleteUserProfile,
sagemaker:DescribeUserProfile
```


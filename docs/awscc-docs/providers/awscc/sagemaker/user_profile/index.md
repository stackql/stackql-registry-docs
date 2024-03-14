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
Gets an individual <code>user_profile</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user_profile</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.user_profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>user_profile_arn</code></td><td><code>string</code></td><td>The user profile Amazon Resource Name (ARN).</td></tr>
<tr><td><code>domain_id</code></td><td><code>string</code></td><td>The ID of the associated Domain.</td></tr>
<tr><td><code>single_sign_on_user_identifier</code></td><td><code>string</code></td><td>A specifier for the type of value specified in SingleSignOnUserValue. Currently, the only supported value is "UserName". If the Domain's AuthMode is SSO, this field is required. If the Domain's AuthMode is not SSO, this field cannot be specified.</td></tr>
<tr><td><code>single_sign_on_user_value</code></td><td><code>string</code></td><td>The username of the associated AWS Single Sign-On User for this UserProfile. If the Domain's AuthMode is SSO, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not SSO, this field cannot be specified.</td></tr>
<tr><td><code>user_profile_name</code></td><td><code>string</code></td><td>A name for the UserProfile.</td></tr>
<tr><td><code>user_settings</code></td><td><code>object</code></td><td>A collection of settings.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of tags to apply to the user profile.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.sagemaker.user_profile
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


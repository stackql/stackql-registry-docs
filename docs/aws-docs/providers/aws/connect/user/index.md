---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>user</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::User</td></tr>
<tr><td><b>Id</b></td><td><code>aws.connect.user</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><code>directory_user_id</code></td><td><code>string</code></td><td>The identifier of the user account in the directory used for identity management.</td></tr>
<tr><td><code>hierarchy_group_arn</code></td><td><code>string</code></td><td>The identifier of the hierarchy group for the user.</td></tr>
<tr><td><code>username</code></td><td><code>string</code></td><td>The user name for the account.</td></tr>
<tr><td><code>password</code></td><td><code>string</code></td><td>The password for the user account. A password is required if you are using Amazon Connect for identity management. Otherwise, it is an error to include a password.</td></tr>
<tr><td><code>routing_profile_arn</code></td><td><code>string</code></td><td>The identifier of the routing profile for the user.</td></tr>
<tr><td><code>identity_info</code></td><td><code>object</code></td><td>The information about the identity of the user.</td></tr>
<tr><td><code>phone_config</code></td><td><code>object</code></td><td>The phone settings for the user.</td></tr>
<tr><td><code>security_profile_arns</code></td><td><code>array</code></td><td>One or more security profile arns for the user</td></tr>
<tr><td><code>user_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the user.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><code>user_proficiencies</code></td><td><code>array</code></td><td>One or more predefined attributes assigned to a user, with a level that indicates how skilled they are.</td></tr>
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
instance_arn,
directory_user_id,
hierarchy_group_arn,
username,
password,
routing_profile_arn,
identity_info,
phone_config,
security_profile_arns,
user_arn,
tags,
user_proficiencies
FROM aws.connect.user
WHERE data__Identifier = '<UserArn>';
```

## Permissions

To operate on the <code>user</code> resource, the following permissions are required:

### Read
```json
connect:DescribeUser,
connect:ListUserProficiencies
```

### Delete
```json
connect:DeleteUser,
connect:UntagResource
```

### Update
```json
connect:UpdateUserIdentityInfo,
connect:UpdateUserPhoneConfig,
connect:UpdateUserRoutingProfile,
connect:UpdateUserSecurityProfiles,
connect:UpdateUserHierarchy,
connect:TagResource,
connect:UntagResource,
connect:AssociateUserProficiencies,
connect:DisassociateUserProficiencies,
connect:UpdateUserProficiencies
```


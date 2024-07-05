---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>user</code> resource or lists <code>users</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::User</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.users" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="directory_user_id" /></td><td><code>string</code></td><td>The identifier of the user account in the directory used for identity management.</td></tr>
<tr><td><CopyableCode code="hierarchy_group_arn" /></td><td><code>string</code></td><td>The identifier of the hierarchy group for the user.</td></tr>
<tr><td><CopyableCode code="username" /></td><td><code>string</code></td><td>The user name for the account.</td></tr>
<tr><td><CopyableCode code="password" /></td><td><code>string</code></td><td>The password for the user account. A password is required if you are using Amazon Connect for identity management. Otherwise, it is an error to include a password.</td></tr>
<tr><td><CopyableCode code="routing_profile_arn" /></td><td><code>string</code></td><td>The identifier of the routing profile for the user.</td></tr>
<tr><td><CopyableCode code="identity_info" /></td><td><code>object</code></td><td>The information about the identity of the user.</td></tr>
<tr><td><CopyableCode code="phone_config" /></td><td><code>object</code></td><td>The phone settings for the user.</td></tr>
<tr><td><CopyableCode code="security_profile_arns" /></td><td><code>array</code></td><td>One or more security profile arns for the user</td></tr>
<tr><td><CopyableCode code="user_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the user.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><CopyableCode code="user_proficiencies" /></td><td><code>array</code></td><td>One or more predefined attributes assigned to a user, with a level that indicates how skilled they are.</td></tr>
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
    <td><CopyableCode code="InstanceArn, PhoneConfig, RoutingProfileArn, SecurityProfileArns, Username, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>users</code> in a region.
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
FROM aws.connect.users
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>user</code>.
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
FROM aws.connect.users
WHERE region = 'us-east-1' AND data__Identifier = '<UserArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.users (
 InstanceArn,
 Username,
 RoutingProfileArn,
 PhoneConfig,
 SecurityProfileArns,
 region
)
SELECT 
'{{ InstanceArn }}',
 '{{ Username }}',
 '{{ RoutingProfileArn }}',
 '{{ PhoneConfig }}',
 '{{ SecurityProfileArns }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.users (
 InstanceArn,
 DirectoryUserId,
 HierarchyGroupArn,
 Username,
 Password,
 RoutingProfileArn,
 IdentityInfo,
 PhoneConfig,
 SecurityProfileArns,
 Tags,
 UserProficiencies,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ DirectoryUserId }}',
 '{{ HierarchyGroupArn }}',
 '{{ Username }}',
 '{{ Password }}',
 '{{ RoutingProfileArn }}',
 '{{ IdentityInfo }}',
 '{{ PhoneConfig }}',
 '{{ SecurityProfileArns }}',
 '{{ Tags }}',
 '{{ UserProficiencies }}',
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
  - name: user
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: DirectoryUserId
        value: '{{ DirectoryUserId }}'
      - name: HierarchyGroupArn
        value: '{{ HierarchyGroupArn }}'
      - name: Username
        value: '{{ Username }}'
      - name: Password
        value: '{{ Password }}'
      - name: RoutingProfileArn
        value: '{{ RoutingProfileArn }}'
      - name: IdentityInfo
        value:
          FirstName: '{{ FirstName }}'
          LastName: '{{ LastName }}'
          Email: '{{ Email }}'
          SecondaryEmail: '{{ SecondaryEmail }}'
          Mobile: '{{ Mobile }}'
      - name: PhoneConfig
        value:
          AfterContactWorkTimeLimit: '{{ AfterContactWorkTimeLimit }}'
          AutoAccept: '{{ AutoAccept }}'
          DeskPhoneNumber: '{{ DeskPhoneNumber }}'
          PhoneType: '{{ PhoneType }}'
      - name: SecurityProfileArns
        value:
          - '{{ SecurityProfileArns[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: UserProficiencies
        value:
          - AttributeName: '{{ AttributeName }}'
            AttributeValue: '{{ AttributeValue }}'
            Level: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.connect.users
WHERE data__Identifier = '<UserArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>users</code> resource, the following permissions are required:

### Create
```json
connect:CreateUser,
connect:TagResource,
connect:AssociateUserProficiencies
```

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

### List
```json
connect:ListUsers
```


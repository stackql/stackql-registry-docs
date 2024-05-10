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


Used to retrieve a list of <code>users</code> in a region or to create or delete a <code>users</code> resource, use <code>user</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::User</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.users" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="user_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the user.</td></tr>
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
user_arn
FROM aws.connect.users
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- user.iql (required properties only)
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
-- user.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
connect:DeleteUser,
connect:UntagResource
```

### List
```json
connect:ListUsers
```


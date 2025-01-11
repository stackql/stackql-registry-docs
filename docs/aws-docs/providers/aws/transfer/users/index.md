---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - transfer
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
<tr><td><b>Description</b></td><td>Definition of AWS::Transfer::User Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.users" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="home_directory" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="home_directory_mappings" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="home_directory_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="posix_profile" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="role" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="server_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ssh_public_keys" /></td><td><code>array</code></td><td>This represents the SSH User Public Keys for CloudFormation resource</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="user_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html"><code>AWS::Transfer::User</code></a>.

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
    <td><CopyableCode code="Role, ServerId, UserName, region" /></td>
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
arn,
home_directory,
home_directory_mappings,
home_directory_type,
policy,
posix_profile,
role,
server_id,
ssh_public_keys,
tags,
user_name
FROM aws.transfer.users
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>user</code>.
```sql
SELECT
region,
arn,
home_directory,
home_directory_mappings,
home_directory_type,
policy,
posix_profile,
role,
server_id,
ssh_public_keys,
tags,
user_name
FROM aws.transfer.users
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
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
INSERT INTO aws.transfer.users (
 Role,
 ServerId,
 UserName,
 region
)
SELECT 
'{{ Role }}',
 '{{ ServerId }}',
 '{{ UserName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.transfer.users (
 HomeDirectory,
 HomeDirectoryMappings,
 HomeDirectoryType,
 Policy,
 PosixProfile,
 Role,
 ServerId,
 SshPublicKeys,
 Tags,
 UserName,
 region
)
SELECT 
 '{{ HomeDirectory }}',
 '{{ HomeDirectoryMappings }}',
 '{{ HomeDirectoryType }}',
 '{{ Policy }}',
 '{{ PosixProfile }}',
 '{{ Role }}',
 '{{ ServerId }}',
 '{{ SshPublicKeys }}',
 '{{ Tags }}',
 '{{ UserName }}',
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
      - name: HomeDirectory
        value: '{{ HomeDirectory }}'
      - name: HomeDirectoryMappings
        value:
          - Entry: '{{ Entry }}'
            Target: '{{ Target }}'
            Type: '{{ Type }}'
      - name: HomeDirectoryType
        value: '{{ HomeDirectoryType }}'
      - name: Policy
        value: '{{ Policy }}'
      - name: PosixProfile
        value:
          Uid: null
          Gid: null
          SecondaryGids:
            - null
      - name: Role
        value: '{{ Role }}'
      - name: ServerId
        value: '{{ ServerId }}'
      - name: SshPublicKeys
        value:
          - '{{ SshPublicKeys[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: UserName
        value: '{{ UserName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.transfer.users
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>users</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
transfer:CreateUser,
transfer:DescribeUser,
transfer:ImportSshPublicKey,
transfer:TagResource
```

### Read
```json
transfer:DescribeUser
```

### Update
```json
iam:PassRole,
transfer:DeleteSshPublicKey,
transfer:DescribeUser,
transfer:ImportSshPublicKey,
transfer:TagResource,
transfer:UnTagResource,
transfer:UpdateUser
```

### Delete
```json
transfer:DeleteUser
```

### List
```json
transfer:ListUsers
```

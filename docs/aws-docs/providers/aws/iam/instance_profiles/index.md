---
title: instance_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_profiles
  - iam
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

Creates, updates, deletes or gets an <code>instance_profile</code> resource or lists <code>instance_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a new instance profile. For information about instance profiles, see &#91;Using instance profiles&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html).<br />For information about the number of instance profiles you can create, see &#91;object quotas&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.instance_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="path" /></td><td><code>string</code></td><td>The path to the instance profile. For more information about paths, see &#91;IAM Identifiers&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.<br />This parameter is optional. If it is not included, it defaults to a slash (/).<br />This parameter allows (through its &#91;regex pattern&#93;(https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the ! (<code>\u0021</code>) through the DEL character (<code>\u007F</code>), including most punctuation characters, digits, and upper and lowercased letters.</td></tr>
<tr><td><CopyableCode code="roles" /></td><td><code>array</code></td><td>The name of the role to associate with the instance profile. Only one role can be assigned to an EC2 instance at a time, and all applications on the instance share the same role and permissions.</td></tr>
<tr><td><CopyableCode code="instance_profile_name" /></td><td><code>string</code></td><td>The name of the instance profile to create.<br />This parameter allows (through its &#91;regex pattern&#93;(https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html"><code>AWS::IAM::InstanceProfile</code></a>.

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
    <td><CopyableCode code="Roles, region" /></td>
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
Gets all <code>instance_profiles</code> in a region.
```sql
SELECT
region,
path,
roles,
instance_profile_name,
arn
FROM aws.iam.instance_profiles
;
```
Gets all properties from an individual <code>instance_profile</code>.
```sql
SELECT
region,
path,
roles,
instance_profile_name,
arn
FROM aws.iam.instance_profiles
WHERE data__Identifier = '<InstanceProfileName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instance_profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iam.instance_profiles (
 Roles,
 region
)
SELECT 
'{{ Roles }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iam.instance_profiles (
 Path,
 Roles,
 InstanceProfileName,
 region
)
SELECT 
 '{{ Path }}',
 '{{ Roles }}',
 '{{ InstanceProfileName }}',
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
  - name: instance_profile
    props:
      - name: Path
        value: '{{ Path }}'
      - name: Roles
        value:
          - '{{ Roles[0] }}'
      - name: InstanceProfileName
        value: '{{ InstanceProfileName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iam.instance_profiles
WHERE data__Identifier = '<InstanceProfileName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>instance_profiles</code> resource, the following permissions are required:

### Create
```json
iam:CreateInstanceProfile,
iam:PassRole,
iam:AddRoleToInstanceProfile,
iam:GetInstanceProfile
```

### Read
```json
iam:GetInstanceProfile
```

### Update
```json
iam:PassRole,
iam:RemoveRoleFromInstanceProfile,
iam:AddRoleToInstanceProfile,
iam:GetInstanceProfile
```

### Delete
```json
iam:GetInstanceProfile,
iam:RemoveRoleFromInstanceProfile,
iam:DeleteInstanceProfile
```

### List
```json
iam:ListInstanceProfiles
```

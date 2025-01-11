---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - rolesanywhere
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

Creates, updates, deletes or gets a <code>profile</code> resource or lists <code>profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RolesAnywhere::Profile Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rolesanywhere.profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="duration_seconds" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="managed_policy_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="profile_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="profile_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="require_instance_properties" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="session_policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="attribute_mappings" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="accept_role_session_name" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html"><code>AWS::RolesAnywhere::Profile</code></a>.

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
    <td><CopyableCode code="Name, RoleArns, region" /></td>
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
Gets all <code>profiles</code> in a region.
```sql
SELECT
region,
duration_seconds,
enabled,
managed_policy_arns,
name,
profile_arn,
profile_id,
require_instance_properties,
role_arns,
session_policy,
tags,
attribute_mappings,
accept_role_session_name
FROM aws.rolesanywhere.profiles
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>profile</code>.
```sql
SELECT
region,
duration_seconds,
enabled,
managed_policy_arns,
name,
profile_arn,
profile_id,
require_instance_properties,
role_arns,
session_policy,
tags,
attribute_mappings,
accept_role_session_name
FROM aws.rolesanywhere.profiles
WHERE region = 'us-east-1' AND data__Identifier = '<ProfileId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.rolesanywhere.profiles (
 Name,
 RoleArns,
 region
)
SELECT 
'{{ Name }}',
 '{{ RoleArns }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.rolesanywhere.profiles (
 DurationSeconds,
 Enabled,
 ManagedPolicyArns,
 Name,
 RequireInstanceProperties,
 RoleArns,
 SessionPolicy,
 Tags,
 AttributeMappings,
 AcceptRoleSessionName,
 region
)
SELECT 
 '{{ DurationSeconds }}',
 '{{ Enabled }}',
 '{{ ManagedPolicyArns }}',
 '{{ Name }}',
 '{{ RequireInstanceProperties }}',
 '{{ RoleArns }}',
 '{{ SessionPolicy }}',
 '{{ Tags }}',
 '{{ AttributeMappings }}',
 '{{ AcceptRoleSessionName }}',
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
  - name: profile
    props:
      - name: DurationSeconds
        value: null
      - name: Enabled
        value: '{{ Enabled }}'
      - name: ManagedPolicyArns
        value:
          - '{{ ManagedPolicyArns[0] }}'
      - name: Name
        value: '{{ Name }}'
      - name: RequireInstanceProperties
        value: '{{ RequireInstanceProperties }}'
      - name: RoleArns
        value:
          - '{{ RoleArns[0] }}'
      - name: SessionPolicy
        value: '{{ SessionPolicy }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: AttributeMappings
        value:
          - MappingRules:
              - Specifier: '{{ Specifier }}'
            CertificateField: '{{ CertificateField }}'
      - name: AcceptRoleSessionName
        value: '{{ AcceptRoleSessionName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.rolesanywhere.profiles
WHERE data__Identifier = '<ProfileId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>profiles</code> resource, the following permissions are required:

### Create
```json
iam:GetRole,
iam:GetPolicy,
iam:PassRole,
rolesanywhere:CreateProfile,
rolesanywhere:TagResource,
rolesanywhere:ListTagsForResource,
rolesanywhere:PutAttributeMapping,
rolesanywhere:DeleteAttributeMapping
```

### Read
```json
rolesanywhere:GetProfile,
rolesanywhere:ListTagsForResource
```

### Update
```json
iam:GetRole,
iam:GetPolicy,
iam:PassRole,
rolesanywhere:GetProfile,
rolesanywhere:UpdateProfile,
rolesanywhere:EnableProfile,
rolesanywhere:DisableProfile,
rolesanywhere:TagResource,
rolesanywhere:UntagResource,
rolesanywhere:ListTagsForResource,
rolesanywhere:PutAttributeMapping,
rolesanywhere:DeleteAttributeMapping
```

### Delete
```json
rolesanywhere:DeleteProfile
```

### List
```json
rolesanywhere:ListProfiles,
rolesanywhere:ListTagsForResource
```

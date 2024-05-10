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


Used to retrieve a list of <code>profiles</code> in a region or to create or delete a <code>profiles</code> resource, use <code>profile</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RolesAnywhere::Profile Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rolesanywhere.profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="profile_id" /></td><td><code>string</code></td><td></td></tr>
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
profile_id
FROM aws.rolesanywhere.profiles
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "RoleArns": [
  "{{ RoleArns[0] }}"
 ]
}
>>>
--required properties only
INSERT INTO aws.rolesanywhere.profiles (
 Name,
 RoleArns,
 region
)
SELECT 
{{ .Name }},
 {{ .RoleArns }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DurationSeconds": null,
 "Enabled": "{{ Enabled }}",
 "ManagedPolicyArns": [
  "{{ ManagedPolicyArns[0] }}"
 ],
 "Name": "{{ Name }}",
 "RequireInstanceProperties": "{{ RequireInstanceProperties }}",
 "RoleArns": [
  "{{ RoleArns[0] }}"
 ],
 "SessionPolicy": "{{ SessionPolicy }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.rolesanywhere.profiles (
 DurationSeconds,
 Enabled,
 ManagedPolicyArns,
 Name,
 RequireInstanceProperties,
 RoleArns,
 SessionPolicy,
 Tags,
 region
)
SELECT 
 {{ .DurationSeconds }},
 {{ .Enabled }},
 {{ .ManagedPolicyArns }},
 {{ .Name }},
 {{ .RequireInstanceProperties }},
 {{ .RoleArns }},
 {{ .SessionPolicy }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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
rolesanywhere:ListTagsForResource
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


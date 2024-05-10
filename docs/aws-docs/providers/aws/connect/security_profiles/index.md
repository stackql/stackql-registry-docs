---
title: security_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - security_profiles
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


Used to retrieve a list of <code>security_profiles</code> in a region or to create or delete a <code>security_profiles</code> resource, use <code>security_profile</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::SecurityProfile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.security_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="security_profile_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the security profile.</td></tr>
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
security_profile_arn
FROM aws.connect.security_profiles
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
 "InstanceArn": "{{ InstanceArn }}",
 "SecurityProfileName": "{{ SecurityProfileName }}"
}
>>>
--required properties only
INSERT INTO aws.connect.security_profiles (
 InstanceArn,
 SecurityProfileName,
 region
)
SELECT 
{{ .InstanceArn }},
 {{ .SecurityProfileName }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AllowedAccessControlTags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "Description": "{{ Description }}",
 "InstanceArn": "{{ InstanceArn }}",
 "Permissions": [
  "{{ Permissions[0] }}"
 ],
 "SecurityProfileName": "{{ SecurityProfileName }}",
 "TagRestrictedResources": [
  "{{ TagRestrictedResources[0] }}"
 ],
 "HierarchyRestrictedResources": [
  null
 ],
 "AllowedAccessControlHierarchyGroupId": "{{ AllowedAccessControlHierarchyGroupId }}",
 "Applications": [
  {
   "ApplicationPermissions": [
    "{{ ApplicationPermissions[0] }}"
   ],
   "Namespace": "{{ Namespace }}"
  }
 ],
 "Tags": [
  null
 ]
}
>>>
--all properties
INSERT INTO aws.connect.security_profiles (
 AllowedAccessControlTags,
 Description,
 InstanceArn,
 Permissions,
 SecurityProfileName,
 TagRestrictedResources,
 HierarchyRestrictedResources,
 AllowedAccessControlHierarchyGroupId,
 Applications,
 Tags,
 region
)
SELECT 
 {{ .AllowedAccessControlTags }},
 {{ .Description }},
 {{ .InstanceArn }},
 {{ .Permissions }},
 {{ .SecurityProfileName }},
 {{ .TagRestrictedResources }},
 {{ .HierarchyRestrictedResources }},
 {{ .AllowedAccessControlHierarchyGroupId }},
 {{ .Applications }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.connect.security_profiles
WHERE data__Identifier = '<SecurityProfileArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>security_profiles</code> resource, the following permissions are required:

### Create
```json
connect:CreateSecurityProfile,
connect:TagResource
```

### Delete
```json
connect:DeleteSecurityProfile,
connect:UntagResource
```

### List
```json
connect:ListSecurityProfiles
```


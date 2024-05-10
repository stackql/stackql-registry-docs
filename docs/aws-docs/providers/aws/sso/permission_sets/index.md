---
title: permission_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - permission_sets
  - sso
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


Used to retrieve a list of <code>permission_sets</code> in a region or to create or delete a <code>permission_sets</code> resource, use <code>permission_set</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permission_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for SSO PermissionSet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sso.permission_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The sso instance arn that the permission set is owned.</td></tr>
<tr><td><CopyableCode code="permission_set_arn" /></td><td><code>string</code></td><td>The permission set that the policy will be attached to</td></tr>
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
instance_arn,
permission_set_arn
FROM aws.sso.permission_sets
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
 "InstanceArn": "{{ InstanceArn }}"
}
>>>
--required properties only
INSERT INTO aws.sso.permission_sets (
 Name,
 InstanceArn,
 region
)
SELECT 
{{ .Name }},
 {{ .InstanceArn }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "InstanceArn": "{{ InstanceArn }}",
 "SessionDuration": "{{ SessionDuration }}",
 "RelayStateType": "{{ RelayStateType }}",
 "ManagedPolicies": [
  "{{ ManagedPolicies[0] }}"
 ],
 "InlinePolicy": {},
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "CustomerManagedPolicyReferences": [
  {
   "Name": "{{ Name }}",
   "Path": "{{ Path }}"
  }
 ],
 "PermissionsBoundary": {
  "CustomerManagedPolicyReference": null,
  "ManagedPolicyArn": null
 }
}
>>>
--all properties
INSERT INTO aws.sso.permission_sets (
 Name,
 Description,
 InstanceArn,
 SessionDuration,
 RelayStateType,
 ManagedPolicies,
 InlinePolicy,
 Tags,
 CustomerManagedPolicyReferences,
 PermissionsBoundary,
 region
)
SELECT 
 {{ .Name }},
 {{ .Description }},
 {{ .InstanceArn }},
 {{ .SessionDuration }},
 {{ .RelayStateType }},
 {{ .ManagedPolicies }},
 {{ .InlinePolicy }},
 {{ .Tags }},
 {{ .CustomerManagedPolicyReferences }},
 {{ .PermissionsBoundary }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.sso.permission_sets
WHERE data__Identifier = '<InstanceArn|PermissionSetArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>permission_sets</code> resource, the following permissions are required:

### Create
```json
sso:CreatePermissionSet,
sso:PutInlinePolicyToPermissionSet,
sso:AttachManagedPolicyToPermissionSet,
sso:AttachCustomerManagedPolicyReferenceToPermissionSet,
sso:PutPermissionsBoundaryToPermissionSet,
sso:TagResource,
sso:DescribePermissionSet,
sso:ListTagsForResource,
sso:ListManagedPoliciesInPermissionSet,
sso:ListCustomerManagedPolicyReferencesInPermissionSet,
sso:GetInlinePolicyForPermissionSet,
sso:GetPermissionsBoundaryForPermissionSet
```

### Delete
```json
sso:DeletePermissionSet
```

### List
```json
sso:DescribePermissionSet
```


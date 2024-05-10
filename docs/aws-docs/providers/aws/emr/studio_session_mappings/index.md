---
title: studio_session_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - studio_session_mappings
  - emr
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


Used to retrieve a list of <code>studio_session_mappings</code> in a region or to create or delete a <code>studio_session_mappings</code> resource, use <code>studio_session_mapping</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio_session_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emr.studio_session_mappings" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td>The ID of the Amazon EMR Studio to which the user or group will be mapped.</td></tr>
<tr><td><CopyableCode code="identity_type" /></td><td><code>string</code></td><td>Specifies whether the identity to map to the Studio is a user or a group.</td></tr>
<tr><td><CopyableCode code="identity_name" /></td><td><code>string</code></td><td>The name of the user or group. For more information, see UserName and DisplayName in the AWS SSO Identity Store API Reference. Either IdentityName or IdentityId must be specified.</td></tr>
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
studio_id,
identity_type,
identity_name
FROM aws.emr.studio_session_mappings
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
 "IdentityName": "{{ IdentityName }}",
 "IdentityType": "{{ IdentityType }}",
 "SessionPolicyArn": "{{ SessionPolicyArn }}",
 "StudioId": "{{ StudioId }}"
}
>>>
--required properties only
INSERT INTO aws.emr.studio_session_mappings (
 IdentityName,
 IdentityType,
 SessionPolicyArn,
 StudioId,
 region
)
SELECT 
{{ .IdentityName }},
 {{ .IdentityType }},
 {{ .SessionPolicyArn }},
 {{ .StudioId }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "IdentityName": "{{ IdentityName }}",
 "IdentityType": "{{ IdentityType }}",
 "SessionPolicyArn": "{{ SessionPolicyArn }}",
 "StudioId": "{{ StudioId }}"
}
>>>
--all properties
INSERT INTO aws.emr.studio_session_mappings (
 IdentityName,
 IdentityType,
 SessionPolicyArn,
 StudioId,
 region
)
SELECT 
 {{ .IdentityName }},
 {{ .IdentityType }},
 {{ .SessionPolicyArn }},
 {{ .StudioId }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.emr.studio_session_mappings
WHERE data__Identifier = '<StudioId|IdentityType|IdentityName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>studio_session_mappings</code> resource, the following permissions are required:

### Create
```json
elasticmapreduce:CreateStudioSessionMapping,
sso-directory:SearchUsers,
sso-directory:SearchGroups,
sso-directory:DescribeUser,
sso-directory:DescribeGroup,
sso:GetManagedApplicationInstance,
sso:ListDirectoryAssociations,
sso:GetProfile,
sso:ListProfiles,
sso:AssociateProfile
```

### Delete
```json
elasticmapreduce:GetStudioSessionMapping,
elasticmapreduce:DeleteStudioSessionMapping,
sso-directory:SearchUsers,
sso-directory:SearchGroups,
sso-directory:DescribeUser,
sso-directory:DescribeGroup,
sso:GetManagedApplicationInstance,
sso:DescribeInstance,
sso:ListDirectoryAssociations,
sso:GetProfile,
sso:ListProfiles,
sso:DisassociateProfile
```

### List
```json
elasticmapreduce:ListStudioSessionMappings
```


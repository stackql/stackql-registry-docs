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

Creates, updates, deletes or gets a <code>studio_session_mapping</code> resource or lists <code>studio_session_mappings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio_session_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emr.studio_session_mappings" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="identity_name" /></td><td><code>string</code></td><td>The name of the user or group. For more information, see UserName and DisplayName in the AWS SSO Identity Store API Reference. Either IdentityName or IdentityId must be specified.</td></tr>
<tr><td><CopyableCode code="identity_type" /></td><td><code>string</code></td><td>Specifies whether the identity to map to the Studio is a user or a group.</td></tr>
<tr><td><CopyableCode code="session_policy_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the session policy that will be applied to the user or group. Session policies refine Studio user permissions without the need to use multiple IAM user roles.</td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td>The ID of the Amazon EMR Studio to which the user or group will be mapped.</td></tr>
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
    <td><CopyableCode code="StudioId, IdentityName, IdentityType, SessionPolicyArn, region" /></td>
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
Gets all <code>studio_session_mappings</code> in a region.
```sql
SELECT
region,
identity_name,
identity_type,
session_policy_arn,
studio_id
FROM aws.emr.studio_session_mappings
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>studio_session_mapping</code>.
```sql
SELECT
region,
identity_name,
identity_type,
session_policy_arn,
studio_id
FROM aws.emr.studio_session_mappings
WHERE region = 'us-east-1' AND data__Identifier = '<StudioId>|<IdentityType>|<IdentityName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>studio_session_mapping</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.emr.studio_session_mappings (
 IdentityName,
 IdentityType,
 SessionPolicyArn,
 StudioId,
 region
)
SELECT 
'{{ IdentityName }}',
 '{{ IdentityType }}',
 '{{ SessionPolicyArn }}',
 '{{ StudioId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.emr.studio_session_mappings (
 IdentityName,
 IdentityType,
 SessionPolicyArn,
 StudioId,
 region
)
SELECT 
 '{{ IdentityName }}',
 '{{ IdentityType }}',
 '{{ SessionPolicyArn }}',
 '{{ StudioId }}',
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
  - name: studio_session_mapping
    props:
      - name: IdentityName
        value: '{{ IdentityName }}'
      - name: IdentityType
        value: '{{ IdentityType }}'
      - name: SessionPolicyArn
        value: '{{ SessionPolicyArn }}'
      - name: StudioId
        value: '{{ StudioId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
elasticmapreduce:GetStudioSessionMapping,
sso-directory:SearchUsers,
sso-directory:SearchGroups,
sso-directory:DescribeUser,
sso-directory:DescribeGroup,
sso:GetManagedApplicationInstance,
sso:DescribeInstance
```

### Update
```json
elasticmapreduce:GetStudioSessionMapping,
elasticmapreduce:UpdateStudioSessionMapping,
sso-directory:SearchUsers,
sso-directory:SearchGroups,
sso-directory:DescribeUser,
sso-directory:DescribeGroup,
sso:GetManagedApplicationInstance,
sso:DescribeInstance
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


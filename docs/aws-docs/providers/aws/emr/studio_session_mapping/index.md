---
title: studio_session_mapping
hide_title: false
hide_table_of_contents: false
keywords:
  - studio_session_mapping
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

Gets or operates on an individual <code>studio_session_mapping</code> resource, use <code>studio_session_mappings</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio_session_mapping</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emr.studio_session_mapping" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="identity_name" /></td><td><code>string</code></td><td>The name of the user or group. For more information, see UserName and DisplayName in the AWS SSO Identity Store API Reference. Either IdentityName or IdentityId must be specified.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
identity_name,
identity_type,
session_policy_arn,
studio_id
FROM aws.emr.studio_session_mapping
WHERE data__Identifier = '<StudioId>|<IdentityType>|<IdentityName>';
```

## Permissions

To operate on the <code>studio_session_mapping</code> resource, the following permissions are required:

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


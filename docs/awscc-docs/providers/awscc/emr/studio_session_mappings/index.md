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
Retrieves a list of <code>studio_session_mappings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio_session_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>studio_session_mappings</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.emr.studio_session_mappings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>studio_id</code></td><td><code>string</code></td><td>The ID of the Amazon EMR Studio to which the user or group will be mapped.</td></tr>
<tr><td><code>identity_type</code></td><td><code>string</code></td><td>Specifies whether the identity to map to the Studio is a user or a group.</td></tr>
<tr><td><code>identity_name</code></td><td><code>string</code></td><td>The name of the user or group. For more information, see UserName and DisplayName in the AWS SSO Identity Store API Reference. Either IdentityName or IdentityId must be specified.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>studio_session_mappings</code> resource, the following permissions are required:

### Create
```json
elasticmapreduce:CreateStudioSessionMapping,
sso-directory:SearchUsers,
sso-directory:SearchGroups,
sso-directory:DescribeUser,
sso-directory:DescribeGroup,
sso:ListDirectoryAssociations,
sso:GetProfile,
sso:ListProfiles,
sso:AssociateProfile
```

### List
```json
elasticmapreduce:ListStudioSessionMappings
```


## Example
```sql
SELECT
region,
studio_id,
identity_type,
identity_name
FROM awscc.emr.studio_session_mappings
WHERE region = 'us-east-1'
```

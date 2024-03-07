---
title: directory_config
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_config
  - appstream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>directory_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directory_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>directory_config</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appstream.directory_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>organizational_unit_distinguished_names</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>service_account_credentials</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>directory_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>certificate_based_auth_properties</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>directory_config</code> resource, the following permissions are required:

### Update
```json
appstream:CreateDirectoryConfig,
appstream:DeleteDirectoryConfig,
appstream:DescribeDirectoryConfig,
appstream:UpdateDirectoryConfig,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

### Read
```json
appstream:CreateDirectoryConfig,
appstream:DeleteDirectoryConfig,
appstream:DescribeDirectoryConfig,
appstream:UpdateDirectoryConfig,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

### Delete
```json
appstream:CreateDirectoryConfig,
appstream:DeleteDirectoryConfig,
appstream:DescribeDirectoryConfig,
appstream:UpdateDirectoryConfig,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```


## Example
```sql
SELECT
region,
organizational_unit_distinguished_names,
service_account_credentials,
directory_name,
certificate_based_auth_properties
FROM awscc.appstream.directory_config
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DirectoryName&gt;'
```

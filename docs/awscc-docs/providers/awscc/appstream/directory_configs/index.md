---
title: directory_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_configs
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
Retrieves a list of <code>directory_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directory_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>directory_configs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appstream.directory_configs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>directory_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>directory_configs</code> resource, the following permissions are required:

### Create
```json
appstream:CreateDirectoryConfig,
appstream:DeleteDirectoryConfig,
appstream:DescribeDirectoryConfig,
appstream:UpdateDirectoryConfig,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

### List
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
directory_name
FROM awscc.appstream.directory_configs
WHERE region = 'us-east-1'
```

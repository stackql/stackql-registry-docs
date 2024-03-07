---
title: file_systems
hide_title: false
hide_table_of_contents: false
keywords:
  - file_systems
  - efs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>file_systems</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>file_systems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>file_systems</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.efs.file_systems</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>file_system_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>file_systems</code> resource, the following permissions are required:

### Create
```json
elasticfilesystem:CreateFileSystem,
elasticfilesystem:DescribeReplicationConfigurations,
elasticfilesystem:TagResource,
elasticfilesystem:CreateReplicationConfiguration,
elasticfilesystem:DescribeFileSystems,
elasticfilesystem:PutBackupPolicy,
elasticfilesystem:PutFileSystemPolicy,
elasticfilesystem:PutLifecycleConfiguration,
elasticfilesystem:UpdateFileSystemProtection,
kms:DescribeKey,
kms:GenerateDataKeyWithoutPlaintext,
kms:CreateGrant
```

### List
```json
elasticfilesystem:DescribeBackupPolicy,
elasticfilesystem:DescribeFileSystemPolicy,
elasticfilesystem:DescribeFileSystems,
elasticfilesystem:DescribeLifecycleConfiguration,
elasticfilesystem:DescribeReplicationConfigurations
```


## Example
```sql
SELECT
region,
file_system_id
FROM awscc.efs.file_systems
WHERE region = 'us-east-1'
```

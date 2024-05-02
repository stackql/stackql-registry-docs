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
<tr><td><b>Description</b></td><td>The ``AWS::EFS::FileSystem`` resource creates a new, empty file system in EFSlong (EFS). You must create a mount target (&#91;AWS::EFS::MountTarget&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-efs-mounttarget.html)) to mount your EFS file system on an EC2 or other AWS cloud compute resource.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.efs.file_systems</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>file_system_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
file_system_id
FROM aws.efs.file_systems
WHERE region = 'us-east-1'
```

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


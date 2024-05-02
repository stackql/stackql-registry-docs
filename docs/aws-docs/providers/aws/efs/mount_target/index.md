---
title: mount_target
hide_title: false
hide_table_of_contents: false
keywords:
  - mount_target
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
Gets an individual <code>mount_target</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mount_target</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::EFS::MountTarget`` resource is an Amazon EFS resource that creates a mount target for an EFS file system. You can then mount the file system on Amazon EC2 instances or other resources by using the mount target.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.efs.mount_target</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ip_address</code></td><td><code>string</code></td><td>Valid IPv4 address within the address range of the specified subnet.</td></tr>
<tr><td><code>file_system_id</code></td><td><code>string</code></td><td>The ID of the file system for which to create the mount target.</td></tr>
<tr><td><code>security_groups</code></td><td><code>array</code></td><td>Up to five VPC security group IDs, of the form ``sg-xxxxxxxx``. These must be for the same VPC as subnet specified.</td></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td>The ID of the subnet to add the mount target in. For One Zone file systems, use the subnet that is associated with the file system's Availability Zone.</td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id,
ip_address,
file_system_id,
security_groups,
subnet_id
FROM aws.efs.mount_target
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>mount_target</code> resource, the following permissions are required:

### Read
```json
elasticfilesystem:DescribeMountTargets,
elasticfilesystem:DescribeMountTargetSecurityGroups
```

### Update
```json
elasticfilesystem:DescribeMountTargets,
elasticfilesystem:DescribeMountTargetSecurityGroups,
elasticfilesystem:ModifyMountTargetSecurityGroups
```

### Delete
```json
elasticfilesystem:DescribeMountTargets,
elasticfilesystem:DeleteMountTarget
```


---
title: mount_targets_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - mount_targets_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>mount_targets</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/mount_targets/"><code>mount_targets</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mount_targets_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::EFS::MountTarget</code> resource is an Amazon EFS resource that creates a mount target for an EFS file system. You can then mount the file system on Amazon EC2 instances or other resources by using the mount target.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.efs.mount_targets_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ip_address" /></td><td><code>string</code></td><td>Valid IPv4 address within the address range of the specified subnet.</td></tr>
<tr><td><CopyableCode code="file_system_id" /></td><td><code>string</code></td><td>The ID of the file system for which to create the mount target.</td></tr>
<tr><td><CopyableCode code="security_groups" /></td><td><code>array</code></td><td>Up to five VPC security group IDs, of the form <code>sg-xxxxxxxx</code>. These must be for the same VPC as subnet specified.</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The ID of the subnet to add the mount target in. For One Zone file systems, use the subnet that is associated with the file system's Availability Zone.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>mount_targets</code> in a region.
```sql
SELECT
region,
id
FROM aws.efs.mount_targets_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>mount_targets_list_only</code> resource, see <a href="/providers/aws/efs/mount_targets/#permissions"><code>mount_targets</code></a>



---
title: file_systems_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - file_systems_list_only
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

Lists <code>file_systems</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/file_systems/"><code>file_systems</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>file_systems_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::EFS::FileSystem</code> resource creates a new, empty file system in EFSlong (EFS). You must create a mount target (&#91;AWS::EFS::MountTarget&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html)) to mount your EFS file system on an EC2 or other AWS cloud compute resource.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.efs.file_systems_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="file_system_id" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>file_systems</code> in a region.
```sql
SELECT
region,
file_system_id
FROM aws.efs.file_systems_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>file_systems_list_only</code> resource, see <a href="/providers/aws/efs/file_systems/#permissions"><code>file_systems</code></a>


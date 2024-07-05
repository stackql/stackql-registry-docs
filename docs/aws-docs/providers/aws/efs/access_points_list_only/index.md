---
title: access_points_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - access_points_list_only
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

Lists <code>access_points</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/access_points/"><code>access_points</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_points_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::EFS::AccessPoint</code> resource creates an EFS access point. An access point is an application-specific view into an EFS file system that applies an operating system user and group, and a file system path, to any file system request made through the access point. The operating system user and group override any identity information provided by the NFS client. The file system path is exposed as the access point's root directory. Applications using the access point can only access data in its own directory and below. To learn more, see &#91;Mounting a file system using EFS access points&#93;(https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html).<br />This operation requires permissions for the <code>elasticfilesystem:CreateAccessPoint</code> action.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.efs.access_points_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_point_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="client_token" /></td><td><code>string</code></td><td>The opaque string specified in the request to ensure idempotent creation.</td></tr>
<tr><td><CopyableCode code="access_point_tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.<br />For more information, see &#91;Tag&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).</td></tr>
<tr><td><CopyableCode code="file_system_id" /></td><td><code>string</code></td><td>The ID of the EFS file system that the access point applies to. Accepts only the ID format for input when specifying a file system, for example <code>fs-0123456789abcedf2</code>.</td></tr>
<tr><td><CopyableCode code="posix_user" /></td><td><code>object</code></td><td>The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point that is used for all file operations by NFS clients using the access point.</td></tr>
<tr><td><CopyableCode code="root_directory" /></td><td><code>object</code></td><td>The directory on the EFS file system that the access point exposes as the root directory to NFS clients using the access point.</td></tr>
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
Lists all <code>access_points</code> in a region.
```sql
SELECT
region,
access_point_id
FROM aws.efs.access_points_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>access_points_list_only</code> resource, see <a href="/providers/aws/efs/access_points/#permissions"><code>access_points</code></a>



---
title: location_nfs_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - location_nfs_tags
  - datasync
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

Expands all tag keys and values for <code>location_nfs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_nfs_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationNFS</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.location_nfs_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="mount_options" /></td><td><code>object</code></td><td>The mount options used by DataSync to access the SMB server.</td></tr>
<tr><td><CopyableCode code="on_prem_config" /></td><td><code>object</code></td><td>Contains a list of Amazon Resource Names (ARNs) of agents that are used to connect an NFS server.</td></tr>
<tr><td><CopyableCode code="server_hostname" /></td><td><code>string</code></td><td>The name of the NFS server. This value is the IP address or DNS name of the NFS server.</td></tr>
<tr><td><CopyableCode code="subdirectory" /></td><td><code>string</code></td><td>The subdirectory in the NFS file system that is used to read data from the NFS source location or write data to the NFS destination.</td></tr>
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the NFS location.</td></tr>
<tr><td><CopyableCode code="location_uri" /></td><td><code>string</code></td><td>The URL of the NFS location that was described.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>location_nfs</code> in a region.
```sql
SELECT
region,
mount_options,
on_prem_config,
server_hostname,
subdirectory,
location_arn,
location_uri,
tag_key,
tag_value
FROM aws.datasync.location_nfs_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>location_nfs_tags</code> resource, see <a href="/providers/aws/datasync/location_nfs/#permissions"><code>location_nfs</code></a>


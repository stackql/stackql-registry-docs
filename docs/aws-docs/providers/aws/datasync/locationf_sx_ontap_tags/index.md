---
title: locationf_sx_ontap_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - locationf_sx_ontap_tags
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

Expands all tag keys and values for <code>locationf_sx_ontaps</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locationf_sx_ontap_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationFSxONTAP.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.locationf_sx_ontap_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="storage_virtual_machine_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the FSx ONTAP SVM.</td></tr>
<tr><td><CopyableCode code="fsx_filesystem_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the FSx ONAP file system.</td></tr>
<tr><td><CopyableCode code="security_group_arns" /></td><td><code>array</code></td><td>The ARNs of the security groups that are to use to configure the FSx ONTAP file system.</td></tr>
<tr><td><CopyableCode code="protocol" /></td><td><code>object</code></td><td>Configuration settings for an NFS or SMB protocol, currently only support NFS</td></tr>
<tr><td><CopyableCode code="subdirectory" /></td><td><code>string</code></td><td>A subdirectory in the location's path.</td></tr>
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon FSx ONTAP file system location that is created.</td></tr>
<tr><td><CopyableCode code="location_uri" /></td><td><code>string</code></td><td>The URL of the FSx ONTAP file system that was described.</td></tr>
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
Expands tags for all <code>locationf_sx_ontaps</code> in a region.
```sql
SELECT
region,
storage_virtual_machine_arn,
fsx_filesystem_arn,
security_group_arns,
protocol,
subdirectory,
location_arn,
location_uri,
tag_key,
tag_value
FROM aws.datasync.locationf_sx_ontap_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>locationf_sx_ontap_tags</code> resource, see <a href="/providers/aws/datasync/locationf_sx_ontaps/#permissions"><code>locationf_sx_ontaps</code></a>



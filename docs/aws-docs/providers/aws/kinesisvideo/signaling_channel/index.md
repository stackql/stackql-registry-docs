---
title: signaling_channel
hide_title: false
hide_table_of_contents: false
keywords:
  - signaling_channel
  - kinesisvideo
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


Gets or updates an individual <code>signaling_channel</code> resource, use <code>signaling_channels</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>signaling_channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::KinesisVideo::SignalingChannel</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kinesisvideo.signaling_channel" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Kinesis Video Signaling Channel.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the Kinesis Video Signaling Channel.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the Kinesis Video Signaling Channel to create. Currently, SINGLE_MASTER is the only supported channel type.</td></tr>
<tr><td><CopyableCode code="message_ttl_seconds" /></td><td><code>integer</code></td><td>The period of time a signaling channel retains undelivered messages before they are discarded.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
name,
type,
message_ttl_seconds,
tags
FROM aws.kinesisvideo.signaling_channel
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## Permissions

To operate on the <code>signaling_channel</code> resource, the following permissions are required:

### Read
```json
kinesisvideo:DescribeSignalingChannel
```

### Update
```json
kinesisvideo:UpdateSignalingChannel,
kinesisvideo:DescribeSignalingChannel
```


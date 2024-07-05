---
title: origin_endpoint_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_endpoint_tags
  - mediapackage
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

Expands all tag keys and values for <code>origin_endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_endpoint_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaPackage::OriginEndpoint</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackage.origin_endpoint_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) assigned to the OriginEndpoint.</td></tr>
<tr><td><CopyableCode code="url" /></td><td><code>string</code></td><td>The URL of the packaged OriginEndpoint for consumption.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the OriginEndpoint.</td></tr>
<tr><td><CopyableCode code="channel_id" /></td><td><code>string</code></td><td>The ID of the Channel the OriginEndpoint is associated with.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A short text description of the OriginEndpoint.</td></tr>
<tr><td><CopyableCode code="whitelist" /></td><td><code>array</code></td><td>A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.</td></tr>
<tr><td><CopyableCode code="startover_window_seconds" /></td><td><code>integer</code></td><td>Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.</td></tr>
<tr><td><CopyableCode code="time_delay_seconds" /></td><td><code>integer</code></td><td>Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.</td></tr>
<tr><td><CopyableCode code="manifest_name" /></td><td><code>string</code></td><td>A short string appended to the end of the OriginEndpoint URL.</td></tr>
<tr><td><CopyableCode code="origination" /></td><td><code>string</code></td><td>Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination</td></tr>
<tr><td><CopyableCode code="authorization" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="hls_package" /></td><td><code>object</code></td><td>An HTTP Live Streaming (HLS) packaging configuration.</td></tr>
<tr><td><CopyableCode code="dash_package" /></td><td><code>object</code></td><td>A Dynamic Adaptive Streaming over HTTP (DASH) packaging configuration.</td></tr>
<tr><td><CopyableCode code="mss_package" /></td><td><code>object</code></td><td>A Microsoft Smooth Streaming (MSS) PackagingConfiguration.</td></tr>
<tr><td><CopyableCode code="cmaf_package" /></td><td><code>object</code></td><td>A CMAF packaging configuration.</td></tr>
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
Expands tags for all <code>origin_endpoints</code> in a region.
```sql
SELECT
region,
arn,
url,
id,
channel_id,
description,
whitelist,
startover_window_seconds,
time_delay_seconds,
manifest_name,
origination,
authorization,
hls_package,
dash_package,
mss_package,
cmaf_package,
tag_key,
tag_value
FROM aws.mediapackage.origin_endpoint_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>origin_endpoint_tags</code> resource, see <a href="/providers/aws/mediapackage/origin_endpoints/#permissions"><code>origin_endpoints</code></a>



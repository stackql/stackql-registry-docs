---
title: origin_endpoint_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_endpoint_tags
  - mediapackagev2
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
<tr><td><b>Description</b></td><td><p>Represents an origin endpoint that is associated with a channel, offering a dynamically repackaged version of its content through various streaming media protocols. The content can be efficiently disseminated to end-users via a Content Delivery Network (CDN), like Amazon CloudFront.</p></td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackagev2.origin_endpoint_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) associated with the resource.</p></td></tr>
<tr><td><CopyableCode code="channel_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="channel_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="container_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td><p>The date and time the origin endpoint was created.</p></td></tr>
<tr><td><CopyableCode code="dash_manifests" /></td><td><code>array</code></td><td><p>A DASH manifest configuration.</p></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td><p>Enter any descriptive text that helps you to identify the origin endpoint.</p></td></tr>
<tr><td><CopyableCode code="force_endpoint_error_configuration" /></td><td><code>object</code></td><td><p>The failover settings for the endpoint.</p></td></tr>
<tr><td><CopyableCode code="hls_manifests" /></td><td><code>array</code></td><td><p>An HTTP live streaming (HLS) manifest configuration.</p></td></tr>
<tr><td><CopyableCode code="low_latency_hls_manifests" /></td><td><code>array</code></td><td><p>A low-latency HLS manifest configuration.</p></td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td><p>The date and time the origin endpoint was modified.</p></td></tr>
<tr><td><CopyableCode code="origin_endpoint_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="segment" /></td><td><code>object</code></td><td><p>The segment configuration, including the segment name, duration, and other configuration values.</p></td></tr>
<tr><td><CopyableCode code="startover_window_seconds" /></td><td><code>integer</code></td><td><p>The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days).</p></td></tr>
<tr><td><CopyableCode code="dash_manifest_urls" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="hls_manifest_urls" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="low_latency_hls_manifest_urls" /></td><td><code>array</code></td><td></td></tr>
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
channel_group_name,
channel_name,
container_type,
created_at,
dash_manifests,
description,
force_endpoint_error_configuration,
hls_manifests,
low_latency_hls_manifests,
modified_at,
origin_endpoint_name,
segment,
startover_window_seconds,
dash_manifest_urls,
hls_manifest_urls,
low_latency_hls_manifest_urls,
tag_key,
tag_value
FROM aws.mediapackagev2.origin_endpoint_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>origin_endpoint_tags</code> resource, see <a href="/providers/aws/mediapackagev2/origin_endpoints/#permissions"><code>origin_endpoints</code></a>


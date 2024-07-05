---
title: origin_endpoints_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_endpoints_list_only
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

Lists <code>origin_endpoints</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/origin_endpoints/"><code>origin_endpoints</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_endpoints_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td><p>Represents an origin endpoint that is associated with a channel, offering a dynamically repackaged version of its content through various streaming media protocols. The content can be efficiently disseminated to end-users via a Content Delivery Network (CDN), like Amazon CloudFront.</p></td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackagev2.origin_endpoints_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) associated with the resource.</p></td></tr>
<tr><td><CopyableCode code="channel_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="channel_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="container_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td><p>The date and time the origin endpoint was created.</p></td></tr>
<tr><td><CopyableCode code="dash_manifests" /></td><td><code>array</code></td><td><p>A DASH manifest configuration.</p></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td><p>Enter any descriptive text that helps you to identify the origin endpoint.</p></td></tr>
<tr><td><CopyableCode code="hls_manifests" /></td><td><code>array</code></td><td><p>An HTTP live streaming (HLS) manifest configuration.</p></td></tr>
<tr><td><CopyableCode code="low_latency_hls_manifests" /></td><td><code>array</code></td><td><p>A low-latency HLS manifest configuration.</p></td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td><p>The date and time the origin endpoint was modified.</p></td></tr>
<tr><td><CopyableCode code="origin_endpoint_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="segment" /></td><td><code>object</code></td><td><p>The segment configuration, including the segment name, duration, and other configuration values.</p></td></tr>
<tr><td><CopyableCode code="startover_window_seconds" /></td><td><code>integer</code></td><td><p>The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days).</p></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
Lists all <code>origin_endpoints</code> in a region.
```sql
SELECT
region,
arn
FROM aws.mediapackagev2.origin_endpoints_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>origin_endpoints_list_only</code> resource, see <a href="/providers/aws/mediapackagev2/origin_endpoints/#permissions"><code>origin_endpoints</code></a>



---
title: origin_endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_endpoint
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


Gets or updates an individual <code>origin_endpoint</code> resource, use <code>origin_endpoints</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>&lt;p&gt;Represents an origin endpoint that is associated with a channel, offering a dynamically repackaged version of its content through various streaming media protocols. The content can be efficiently disseminated to end-users via a Content Delivery Network (CDN), like Amazon CloudFront.&lt;&#x2F;p&gt;</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackagev2.origin_endpoint" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) associated with the resource.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="channel_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="channel_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="container_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>&lt;p&gt;The date and time the origin endpoint was created.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>&lt;p&gt;Enter any descriptive text that helps you to identify the origin endpoint.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="hls_manifests" /></td><td><code>array</code></td><td>&lt;p&gt;An HTTP live streaming (HLS) manifest configuration.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="low_latency_hls_manifests" /></td><td><code>array</code></td><td>&lt;p&gt;A low-latency HLS manifest configuration.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td>&lt;p&gt;The date and time the origin endpoint was modified.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="origin_endpoint_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="segment" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="startover_window_seconds" /></td><td><code>integer</code></td><td>&lt;p&gt;The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days).&lt;&#x2F;p&gt;</td></tr>
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
channel_group_name,
channel_name,
container_type,
created_at,
description,
hls_manifests,
low_latency_hls_manifests,
modified_at,
origin_endpoint_name,
segment,
startover_window_seconds,
tags
FROM aws.mediapackagev2.origin_endpoint
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>origin_endpoint</code> resource, the following permissions are required:

### Read
```json
mediapackagev2:GetOriginEndpoint
```

### Update
```json
mediapackagev2:TagResource,
mediapackagev2:UntagResource,
mediapackagev2:ListTagsForResource,
mediapackagev2:UpdateOriginEndpoint,
iam:PassRole
```


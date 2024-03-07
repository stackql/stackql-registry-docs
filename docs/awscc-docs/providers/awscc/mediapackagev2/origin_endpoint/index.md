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
Gets an individual <code>origin_endpoint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>origin_endpoint</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediapackagev2.origin_endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>&lt;p&gt;The Amazon Resource Name (ARN) associated with the resource.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>channel_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>channel_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>container_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>&lt;p&gt;The date and time the origin endpoint was created.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>&lt;p&gt;Enter any descriptive text that helps you to identify the origin endpoint.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>hls_manifests</code></td><td><code>array</code></td><td>&lt;p&gt;An HTTP live streaming (HLS) manifest configuration.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>low_latency_hls_manifests</code></td><td><code>array</code></td><td>&lt;p&gt;A low-latency HLS manifest configuration.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>modified_at</code></td><td><code>string</code></td><td>&lt;p&gt;The date and time the origin endpoint was modified.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>origin_endpoint_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>segment</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>startover_window_seconds</code></td><td><code>integer</code></td><td>&lt;p&gt;The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days).&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>origin_endpoint</code> resource, the following permissions are required:

### Read
<pre>
mediapackagev2:GetOriginEndpoint</pre>

### Update
<pre>
mediapackagev2:TagResource,
mediapackagev2:UntagResource,
mediapackagev2:ListTagsForResource,
mediapackagev2:UpdateOriginEndpoint,
iam:PassRole</pre>

### Delete
<pre>
mediapackagev2:GetOriginEndpoint,
mediapackagev2:DeleteOriginEndpoint</pre>


## Example
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
FROM awscc.mediapackagev2.origin_endpoint
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```

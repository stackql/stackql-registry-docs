---
title: origin_endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_endpoint
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
Gets an individual <code>origin_endpoint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>origin_endpoint</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediapackage.origin_endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) assigned to the OriginEndpoint.</td></tr>
<tr><td><code>url</code></td><td><code>string</code></td><td>The URL of the packaged OriginEndpoint for consumption.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the OriginEndpoint.</td></tr>
<tr><td><code>channel_id</code></td><td><code>string</code></td><td>The ID of the Channel the OriginEndpoint is associated with.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A short text description of the OriginEndpoint.</td></tr>
<tr><td><code>whitelist</code></td><td><code>array</code></td><td>A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.</td></tr>
<tr><td><code>startover_window_seconds</code></td><td><code>integer</code></td><td>Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.</td></tr>
<tr><td><code>time_delay_seconds</code></td><td><code>integer</code></td><td>Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.</td></tr>
<tr><td><code>manifest_name</code></td><td><code>string</code></td><td>A short string appended to the end of the OriginEndpoint URL.</td></tr>
<tr><td><code>origination</code></td><td><code>string</code></td><td>Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination</td></tr>
<tr><td><code>authorization</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>hls_package</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>dash_package</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>mss_package</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>cmaf_package</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>origin_endpoint</code> resource, the following permissions are required:

### Read
```json
mediapackage:DescribeOriginEndpoint
```

### Update
```json
mediapackage:UpdateOriginEndpoint,
iam:PassRole
```

### Delete
```json
mediapackage:DeleteOriginEndpoint
```


## Example
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
tags
FROM awscc.mediapackage.origin_endpoint
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```

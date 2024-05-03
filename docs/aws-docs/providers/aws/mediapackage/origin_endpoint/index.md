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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>origin_endpoint</code> resource, use <code>origin_endpoints</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaPackage::OriginEndpoint</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackage.origin_endpoint" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) assigned to the OriginEndpoint.</td></tr>
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
<tr><td><CopyableCode code="hls_package" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="dash_package" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="mss_package" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="cmaf_package" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
FROM aws.mediapackage.origin_endpoint
WHERE data__Identifier = '<Id>';
```

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


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
<tr><td><b>Id</b></td><td><code>aws.mediapackage.origin_endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) assigned to the OriginEndpoint.</td></tr><tr><td><code>Url</code></td><td><code>string</code></td><td>The URL of the packaged OriginEndpoint for consumption.</td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td>The ID of the OriginEndpoint.</td></tr><tr><td><code>ChannelId</code></td><td><code>string</code></td><td>The ID of the Channel the OriginEndpoint is associated with.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>A short text description of the OriginEndpoint.</td></tr><tr><td><code>Whitelist</code></td><td><code>array</code></td><td>A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.</td></tr><tr><td><code>StartoverWindowSeconds</code></td><td><code>integer</code></td><td>Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.</td></tr><tr><td><code>TimeDelaySeconds</code></td><td><code>integer</code></td><td>Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.</td></tr><tr><td><code>ManifestName</code></td><td><code>string</code></td><td>A short string appended to the end of the OriginEndpoint URL.</td></tr><tr><td><code>Origination</code></td><td><code>string</code></td><td>Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination</td></tr><tr><td><code>Authorization</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>HlsPackage</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DashPackage</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>MssPackage</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>CmafPackage</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.mediapackage.origin_endpoint
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
```

---
title: channel
hide_title: false
hide_table_of_contents: false
keywords:
  - channel
  - ivs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>channel</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ivs.channel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Channel ARN is automatically generated on creation and assigned as the unique identifier.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>Channel</td></tr><tr><td><code>Authorized</code></td><td><code>boolean</code></td><td>Whether the channel is authorized.</td></tr><tr><td><code>LatencyMode</code></td><td><code>string</code></td><td>Channel latency mode.</td></tr><tr><td><code>Type</code></td><td><code>string</code></td><td>Channel type, which determines the allowable resolution and bitrate. If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset model.</td></tr><tr><td><code>PlaybackUrl</code></td><td><code>string</code></td><td>Channel Playback URL.</td></tr><tr><td><code>IngestEndpoint</code></td><td><code>string</code></td><td>Channel ingest endpoint, part of the definition of an ingest server, used when you set up streaming software.</td></tr><tr><td><code>RecordingConfigurationArn</code></td><td><code>string</code></td><td>Recording Configuration ARN. A value other than an empty string indicates that recording is enabled. Default: "" (recording is disabled).</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ivs.channel
WHERE region = 'us-east-1' AND data__Identifier = '{Arn}'
</pre>

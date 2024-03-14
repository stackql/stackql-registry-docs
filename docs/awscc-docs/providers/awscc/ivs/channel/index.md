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
<tr><td><b>Description</b></td><td>channel</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ivs.channel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Channel ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Channel</td></tr>
<tr><td><code>authorized</code></td><td><code>boolean</code></td><td>Whether the channel is authorized.</td></tr>
<tr><td><code>insecure_ingest</code></td><td><code>boolean</code></td><td>Whether the channel allows insecure ingest.</td></tr>
<tr><td><code>latency_mode</code></td><td><code>string</code></td><td>Channel latency mode.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>Channel type, which determines the allowable resolution and bitrate. If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset model.</td></tr>
<tr><td><code>playback_url</code></td><td><code>string</code></td><td>Channel Playback URL.</td></tr>
<tr><td><code>ingest_endpoint</code></td><td><code>string</code></td><td>Channel ingest endpoint, part of the definition of an ingest server, used when you set up streaming software.</td></tr>
<tr><td><code>recording_configuration_arn</code></td><td><code>string</code></td><td>Recording Configuration ARN. A value other than an empty string indicates that recording is enabled. Default: "" (recording is disabled).</td></tr>
<tr><td><code>preset</code></td><td><code>string</code></td><td>Optional transcode preset for the channel. This is selectable only for ADVANCED_HD and ADVANCED_SD channel types. For those channel types, the default preset is HIGHER_BANDWIDTH_DELIVERY. For other channel types (BASIC and STANDARD), preset is the empty string ("").</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
name,
authorized,
insecure_ingest,
latency_mode,
type,
tags,
playback_url,
ingest_endpoint,
recording_configuration_arn,
preset
FROM awscc.ivs.channel
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>channel</code> resource, the following permissions are required:

### Read
```json
ivs:GetChannel,
ivs:ListTagsForResource
```

### Update
```json
ivs:GetChannel,
ivs:UpdateChannel,
ivs:TagResource,
ivs:UnTagResource,
ivs:ListTagsForResource
```

### Delete
```json
ivs:DeleteChannel,
ivs:UnTagResource
```


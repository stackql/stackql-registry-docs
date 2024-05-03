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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>channel</code> resource, use <code>channels</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::Channel</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.channel" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Channel ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Channel</td></tr>
<tr><td><CopyableCode code="authorized" /></td><td><code>boolean</code></td><td>Whether the channel is authorized.</td></tr>
<tr><td><CopyableCode code="insecure_ingest" /></td><td><code>boolean</code></td><td>Whether the channel allows insecure ingest.</td></tr>
<tr><td><CopyableCode code="latency_mode" /></td><td><code>string</code></td><td>Channel latency mode.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>Channel type, which determines the allowable resolution and bitrate. If you exceed the allowable resolution or bitrate, the stream probably will disconnect immediately.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset model.</td></tr>
<tr><td><CopyableCode code="playback_url" /></td><td><code>string</code></td><td>Channel Playback URL.</td></tr>
<tr><td><CopyableCode code="ingest_endpoint" /></td><td><code>string</code></td><td>Channel ingest endpoint, part of the definition of an ingest server, used when you set up streaming software.</td></tr>
<tr><td><CopyableCode code="recording_configuration_arn" /></td><td><code>string</code></td><td>Recording Configuration ARN. A value other than an empty string indicates that recording is enabled. Default: "" (recording is disabled).</td></tr>
<tr><td><CopyableCode code="preset" /></td><td><code>string</code></td><td>Optional transcode preset for the channel. This is selectable only for ADVANCED_HD and ADVANCED_SD channel types. For those channel types, the default preset is HIGHER_BANDWIDTH_DELIVERY. For other channel types (BASIC and STANDARD), preset is the empty string ("").</td></tr>
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
FROM aws.ivs.channel
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


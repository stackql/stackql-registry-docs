---
title: channels_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - channels_list_only
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>channels</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/channels/"><code>channels</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channels_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::Channel</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.channels_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Channel ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>channels</code> in a region.
```sql
SELECT
region,
arn
FROM aws.ivs.channels_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>channels_list_only</code> resource, see <a href="/providers/aws/ivs/channels/#permissions"><code>channels</code></a>



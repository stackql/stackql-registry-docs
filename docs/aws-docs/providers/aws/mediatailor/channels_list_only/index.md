---
title: channels_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - channels_list_only
  - mediatailor
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
<tr><td><b>Description</b></td><td>Definition of AWS::MediaTailor::Channel Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediatailor.channels_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The ARN of the channel.</p></td></tr>
<tr><td><CopyableCode code="audiences" /></td><td><code>array</code></td><td><p>The list of audiences defined in channel.</p></td></tr>
<tr><td><CopyableCode code="channel_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="filler_slate" /></td><td><code>object</code></td><td><p>Slate VOD source configuration.</p></td></tr>
<tr><td><CopyableCode code="log_configuration" /></td><td><code>object</code></td><td><p>The log configuration for the channel.</p></td></tr>
<tr><td><CopyableCode code="outputs" /></td><td><code>array</code></td><td><p>The channel's output properties.</p></td></tr>
<tr><td><CopyableCode code="playback_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to assign to the channel.</td></tr>
<tr><td><CopyableCode code="tier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="time_shift_configuration" /></td><td><code>object</code></td><td><p>The configuration for time-shifted viewing.</p></td></tr>
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
channel_name
FROM aws.mediatailor.channels_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>channels_list_only</code> resource, see <a href="/providers/aws/mediatailor/channels/#permissions"><code>channels</code></a>



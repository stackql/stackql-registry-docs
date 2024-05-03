---
title: channel
hide_title: false
hide_table_of_contents: false
keywords:
  - channel
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

Gets or operates on an individual <code>channel</code> resource, use <code>channels</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaTailor::Channel Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediatailor.channel" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>&lt;p&gt;The ARN of the channel.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="audiences" /></td><td><code>array</code></td><td>&lt;p&gt;The list of audiences defined in channel.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="channel_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="filler_slate" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="log_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="outputs" /></td><td><code>array</code></td><td>&lt;p&gt;The channel's output properties.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="playback_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to assign to the channel.</td></tr>
<tr><td><CopyableCode code="tier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="time_shift_configuration" /></td><td><code>object</code></td><td></td></tr>
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
audiences,
channel_name,
filler_slate,
log_configuration,
outputs,
playback_mode,
tags,
tier,
time_shift_configuration
FROM aws.mediatailor.channel
WHERE data__Identifier = '<ChannelName>';
```

## Permissions

To operate on the <code>channel</code> resource, the following permissions are required:

### Read
```json
mediatailor:DescribeChannel
```

### Update
```json
mediatailor:UpdateChannel,
mediatailor:TagResource,
mediatailor:UntagResource,
iam:CreateServiceLinkedRole,
mediatailor:ConfigureLogsForChannel,
mediatailor:DescribeChannel
```

### Delete
```json
mediatailor:DeleteChannel,
mediatailor:DescribeChannel
```


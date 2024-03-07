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
Gets an individual <code>channel</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>channel</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediatailor.channel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>&lt;p&gt;The ARN of the channel.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>channel_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>filler_slate</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>log_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>outputs</code></td><td><code>array</code></td><td>&lt;p&gt;The channel's output properties.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>playback_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags to assign to the channel.</td></tr>
<tr><td><code>tier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>time_shift_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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


## Example
```sql
SELECT
region,
arn,
channel_name,
filler_slate,
log_configuration,
outputs,
playback_mode,
tags,
tier,
time_shift_configuration
FROM awscc.mediatailor.channel
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ChannelName&gt;'
```

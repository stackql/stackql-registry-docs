---
title: channel_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - channel_policy
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
Gets an individual <code>channel_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>channel_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediatailor.channel_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>channel_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy</code></td><td><code>object</code></td><td>&lt;p&gt;The IAM policy for the channel. IAM policies are used to control access to your channel.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>channel_policy</code> resource, the following permissions are required:

### Read
```json
mediatailor:GetChannelPolicy
```

### Update
```json
mediatailor:PutChannelPolicy,
mediatailor:GetChannelPolicy
```

### Delete
```json
mediatailor:DeleteChannelPolicy,
mediatailor:GetChannelPolicy
```


## Example
```sql
SELECT
region,
channel_name,
policy
FROM awscc.mediatailor.channel_policy
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ChannelName&gt;'
```

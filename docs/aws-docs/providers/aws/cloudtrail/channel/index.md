---
title: channel
hide_title: false
hide_table_of_contents: false
keywords:
  - channel
  - cloudtrail
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
<tr><td><b>Id</b></td><td><code>aws.cloudtrail.channel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source</code></td><td><code>string</code></td><td>The ARN of an on-premises storage solution or application, or a partner event source.</td></tr>
<tr><td><code>destinations</code></td><td><code>array</code></td><td>One or more resources to which events arriving through a channel are logged and stored.</td></tr>
<tr><td><code>channel_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
source,
destinations,
channel_arn,
tags
FROM aws.cloudtrail.channel
WHERE region = 'us-east-1'
AND data__Identifier = '<ChannelArn>'
```

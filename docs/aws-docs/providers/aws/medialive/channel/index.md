---
title: channel
hide_title: false
hide_table_of_contents: false
keywords:
  - channel
  - medialive
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
<tr><td><b>Id</b></td><td><code>aws.medialive.channel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>input_attachments</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>input_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>destinations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>vpc</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>log_level</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>channel_class</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>encoder_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>cdi_input_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>inputs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
input_attachments,
input_specification,
destinations,
vpc,
log_level,
role_arn,
name,
channel_class,
encoder_settings,
cdi_input_specification,
id,
arn,
inputs,
tags
FROM aws.medialive.channel
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```

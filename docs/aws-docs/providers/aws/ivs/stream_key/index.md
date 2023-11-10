---
title: stream_key
hide_title: false
hide_table_of_contents: false
keywords:
  - stream_key
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
Gets an individual <code>stream_key</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stream_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>stream_key</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ivs.stream_key</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Stream Key ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><code>channel_arn</code></td><td><code>string</code></td><td>Channel ARN for the stream.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset model.</td></tr>
<tr><td><code>value</code></td><td><code>string</code></td><td>Stream-key value.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
channel_arn,
tags,
value
FROM aws.ivs.stream_key
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```

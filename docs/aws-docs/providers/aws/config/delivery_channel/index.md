---
title: delivery_channel
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery_channel
  - config
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>delivery_channel</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>delivery_channel</td></tr>
<tr><td><b>Id</b></td><td><code>aws.config.delivery_channel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>s3_key_prefix</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>config_snapshot_delivery_properties</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>s3_bucket_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sns_topic_ar_n</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>s3_kms_key_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
s3_key_prefix,
config_snapshot_delivery_properties,
s3_bucket_name,
sns_topic_ar_n,
id,
s3_kms_key_arn,
name
FROM aws.config.delivery_channel
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```

---
title: delivery_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery_streams
  - kinesisfirehose
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>delivery_streams</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>delivery_streams</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.kinesisfirehose.delivery_streams</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>delivery_stream_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>delivery_streams</code> resource, the following permissions are required:

### Create
<pre>
firehose:CreateDeliveryStream,
firehose:DescribeDeliveryStream,
iam:GetRole,
iam:PassRole,
kms:CreateGrant,
kms:DescribeKey</pre>

### List
<pre>
firehose:ListDeliveryStreams</pre>


## Example
```sql
SELECT
region,
delivery_stream_name
FROM awscc.kinesisfirehose.delivery_streams
WHERE region = 'us-east-1'
```

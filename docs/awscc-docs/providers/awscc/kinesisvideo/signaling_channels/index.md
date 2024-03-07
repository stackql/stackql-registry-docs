---
title: signaling_channels
hide_title: false
hide_table_of_contents: false
keywords:
  - signaling_channels
  - kinesisvideo
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>signaling_channels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>signaling_channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>signaling_channels</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.kinesisvideo.signaling_channels</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the Kinesis Video Signaling Channel.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>signaling_channels</code> resource, the following permissions are required:

### Create
<pre>
kinesisvideo:CreateSignalingChannel,
kinesisvideo:DescribeSignalingChannel</pre>


## Example
```sql
SELECT
region,
name
FROM awscc.kinesisvideo.signaling_channels
WHERE region = 'us-east-1'
```

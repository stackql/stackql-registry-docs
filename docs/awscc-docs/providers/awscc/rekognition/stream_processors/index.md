---
title: stream_processors
hide_title: false
hide_table_of_contents: false
keywords:
  - stream_processors
  - rekognition
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>stream_processors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stream_processors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>stream_processors</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rekognition.stream_processors</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the stream processor. It's an identifier you assign to the stream processor. You can use it to manage the stream processor.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>stream_processors</code> resource, the following permissions are required:

### Create
<pre>
rekognition:CreateStreamProcessor,
iam:PassRole,
rekognition:DescribeStreamProcessor,
rekognition:ListTagsForResource,
rekognition:TagResource</pre>

### List
<pre>
rekognition:ListStreamProcessors</pre>


## Example
```sql
SELECT
region,
name
FROM awscc.rekognition.stream_processors
WHERE region = 'us-east-1'
```

---
title: log_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - log_streams
  - logs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>log_streams</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>log_streams</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.logs.log_streams</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>log_group_name</code></td><td><code>string</code></td><td>The name of the log group where the log stream is created.</td></tr>
<tr><td><code>log_stream_name</code></td><td><code>string</code></td><td>The name of the log stream. The name must be unique wihtin the log group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>log_streams</code> resource, the following permissions are required:

### Create
<pre>
logs:CreateLogStream</pre>

### List
<pre>
logs:DescribeLogStreams</pre>


## Example
```sql
SELECT
region,
log_group_name,
log_stream_name
FROM awscc.logs.log_streams
WHERE region = 'us-east-1'
```

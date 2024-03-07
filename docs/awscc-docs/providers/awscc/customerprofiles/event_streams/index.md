---
title: event_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - event_streams
  - customerprofiles
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>event_streams</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>event_streams</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.customerprofiles.event_streams</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><code>event_stream_name</code></td><td><code>string</code></td><td>The name of the event stream.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>event_streams</code> resource, the following permissions are required:

### Create
<pre>
profile:CreateEventStream,
iam:PutRolePolicy,
kinesis:DescribeStreamSummary,
profile:TagResource</pre>

### List
<pre>
profile:ListEventStreams</pre>


## Example
```sql
SELECT
region,
domain_name,
event_stream_name
FROM awscc.customerprofiles.event_streams
WHERE region = 'us-east-1'
```

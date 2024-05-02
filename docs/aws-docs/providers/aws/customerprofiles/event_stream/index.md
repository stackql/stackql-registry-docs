---
title: event_stream
hide_title: false
hide_table_of_contents: false
keywords:
  - event_stream
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
Gets or operates on an individual <code>event_stream</code> resource, use <code>event_streams</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_stream</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An Event Stream resource of Amazon Connect Customer Profiles</td></tr>
<tr><td><b>Id</b></td><td><code>aws.customerprofiles.event_stream</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><code>event_stream_name</code></td><td><code>string</code></td><td>The name of the event stream.</td></tr>
<tr><td><code>uri</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>event_stream_arn</code></td><td><code>string</code></td><td>A unique identifier for the event stream.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags used to organize, track, or control access for this resource.</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The timestamp of when the export was created.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The operational state of destination stream for export.</td></tr>
<tr><td><code>destination_details</code></td><td><code>object</code></td><td>Details regarding the Kinesis stream.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
domain_name,
event_stream_name,
uri,
event_stream_arn,
tags,
created_at,
state,
destination_details
FROM aws.customerprofiles.event_stream
WHERE data__Identifier = '<DomainName>|<EventStreamName>';
```

## Permissions

To operate on the <code>event_stream</code> resource, the following permissions are required:

### Read
```json
profile:GetEventStream,
kinesis:DescribeStreamSummary
```

### Update
```json
kinesis:DescribeStreamSummary,
profile:GetEventStream,
profile:UntagResource,
profile:TagResource
```

### Delete
```json
profile:DeleteEventStream,
iam:DeleteRolePolicy
```


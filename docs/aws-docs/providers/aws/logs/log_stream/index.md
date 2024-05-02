---
title: log_stream
hide_title: false
hide_table_of_contents: false
keywords:
  - log_stream
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
Gets an individual <code>log_stream</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_stream</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Logs::LogStream</td></tr>
<tr><td><b>Id</b></td><td><code>aws.logs.log_stream</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>log_stream_name</code></td><td><code>string</code></td><td>The name of the log stream. The name must be unique wihtin the log group.</td></tr>
<tr><td><code>log_group_name</code></td><td><code>string</code></td><td>The name of the log group where the log stream is created.</td></tr>
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
log_stream_name,
log_group_name
FROM aws.logs.log_stream
WHERE data__Identifier = '<LogGroupName>|<LogStreamName>';
```

## Permissions

To operate on the <code>log_stream</code> resource, the following permissions are required:

### Read
```json
logs:DescribeLogStreams
```

### Delete
```json
logs:DeleteLogStream
```


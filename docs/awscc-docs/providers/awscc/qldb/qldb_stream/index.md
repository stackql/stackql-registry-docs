---
title: qldb_stream
hide_title: false
hide_table_of_contents: false
keywords:
  - qldb_stream
  - qldb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>qldb_stream</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>qldb_stream</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>qldb_stream</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.qldb.qldb_stream</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ledger_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stream_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>inclusive_start_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>exclusive_end_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kinesis_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
ledger_name,
stream_name,
role_arn,
inclusive_start_time,
exclusive_end_time,
kinesis_configuration,
tags,
arn,
id
FROM awscc.qldb.qldb_stream
WHERE data__Identifier = '<LedgerName>|<Id>';
```

## Permissions

To operate on the <code>qldb_stream</code> resource, the following permissions are required:

### Delete
```json
qldb:CancelJournalKinesisStream,
qldb:DescribeJournalKinesisStream
```

### Read
```json
qldb:DescribeJournalKinesisStream,
qldb:ListTagsForResource
```

### Update
```json
qldb:DescribeJournalKinesisStream,
qldb:UntagResource,
qldb:TagResource
```


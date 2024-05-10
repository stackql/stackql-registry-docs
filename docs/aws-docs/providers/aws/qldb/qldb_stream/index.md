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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>qldb_stream</code> resource, use <code>qldb_streams</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>qldb_stream</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::QLDB::Stream.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.qldb.qldb_stream" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="ledger_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stream_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="inclusive_start_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="exclusive_end_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="kinesis_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.qldb.qldb_stream
WHERE region = 'us-east-1' AND data__Identifier = '<LedgerName>|<Id>';
```


## Permissions

To operate on the <code>qldb_stream</code> resource, the following permissions are required:

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


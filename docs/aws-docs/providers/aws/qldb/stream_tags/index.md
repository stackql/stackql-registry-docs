---
title: stream_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - stream_tags
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

Expands all tag keys and values for <code>streams</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stream_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::QLDB::Stream.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.qldb.stream_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ledger_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stream_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="inclusive_start_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="exclusive_end_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="kinesis_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>streams</code> in a region.
```sql
SELECT
region,
ledger_name,
stream_name,
role_arn,
inclusive_start_time,
exclusive_end_time,
kinesis_configuration,
arn,
id,
tag_key,
tag_value
FROM aws.qldb.stream_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>stream_tags</code> resource, see <a href="/providers/aws/qldb/streams/#permissions"><code>streams</code></a>



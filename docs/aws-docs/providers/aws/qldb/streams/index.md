---
title: streams
hide_title: false
hide_table_of_contents: false
keywords:
  - streams
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


Used to retrieve a list of <code>streams</code> in a region or to create or delete a <code>streams</code> resource, use <code>stream</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::QLDB::Stream.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.qldb.streams" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="ledger_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
ledger_name,
id
FROM aws.qldb.streams
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "LedgerName": "{{ LedgerName }}",
 "StreamName": "{{ StreamName }}",
 "RoleArn": "{{ RoleArn }}",
 "InclusiveStartTime": "{{ InclusiveStartTime }}",
 "KinesisConfiguration": {
  "StreamArn": null,
  "AggregationEnabled": "{{ AggregationEnabled }}"
 }
}
>>>
--required properties only
INSERT INTO aws.qldb.streams (
 LedgerName,
 StreamName,
 RoleArn,
 InclusiveStartTime,
 KinesisConfiguration,
 region
)
SELECT 
{{ .LedgerName }},
 {{ .StreamName }},
 {{ .RoleArn }},
 {{ .InclusiveStartTime }},
 {{ .KinesisConfiguration }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "LedgerName": "{{ LedgerName }}",
 "StreamName": "{{ StreamName }}",
 "RoleArn": "{{ RoleArn }}",
 "InclusiveStartTime": "{{ InclusiveStartTime }}",
 "ExclusiveEndTime": "{{ ExclusiveEndTime }}",
 "KinesisConfiguration": {
  "StreamArn": null,
  "AggregationEnabled": "{{ AggregationEnabled }}"
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.qldb.streams (
 LedgerName,
 StreamName,
 RoleArn,
 InclusiveStartTime,
 ExclusiveEndTime,
 KinesisConfiguration,
 Tags,
 region
)
SELECT 
 {{ .LedgerName }},
 {{ .StreamName }},
 {{ .RoleArn }},
 {{ .InclusiveStartTime }},
 {{ .ExclusiveEndTime }},
 {{ .KinesisConfiguration }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.qldb.streams
WHERE data__Identifier = '<LedgerName|Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>streams</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
qldb:StreamJournalToKinesis,
qldb:DescribeJournalKinesisStream
```

### Delete
```json
qldb:CancelJournalKinesisStream,
qldb:DescribeJournalKinesisStream
```

### List
```json
qldb:listJournalKinesisStreamsForLedger
```


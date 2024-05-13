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
    <td><CopyableCode code="LedgerName, StreamName, RoleArn, KinesisConfiguration, InclusiveStartTime, region" /></td>
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

Use the following StackQL query and manifest file to create a new <code>stream</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.qldb.streams (
 LedgerName,
 StreamName,
 RoleArn,
 InclusiveStartTime,
 KinesisConfiguration,
 region
)
SELECT 
'{{ LedgerName }}',
 '{{ StreamName }}',
 '{{ RoleArn }}',
 '{{ InclusiveStartTime }}',
 '{{ KinesisConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ LedgerName }}',
 '{{ StreamName }}',
 '{{ RoleArn }}',
 '{{ InclusiveStartTime }}',
 '{{ ExclusiveEndTime }}',
 '{{ KinesisConfiguration }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: stream
    props:
      - name: LedgerName
        value: '{{ LedgerName }}'
      - name: StreamName
        value: '{{ StreamName }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: InclusiveStartTime
        value: '{{ InclusiveStartTime }}'
      - name: ExclusiveEndTime
        value: '{{ ExclusiveEndTime }}'
      - name: KinesisConfiguration
        value:
          StreamArn: null
          AggregationEnabled: '{{ AggregationEnabled }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
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


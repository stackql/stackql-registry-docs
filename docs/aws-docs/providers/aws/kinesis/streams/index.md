---
title: streams
hide_title: false
hide_table_of_contents: false
keywords:
  - streams
  - kinesis
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
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Kinesis::Stream</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kinesis.streams" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the Kinesis stream.</td></tr>
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
name
FROM aws.kinesis.streams
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
 "StreamModeDetails": {
  "StreamMode": "{{ StreamMode }}"
 },
 "StreamEncryption": {
  "EncryptionType": "{{ EncryptionType }}",
  "KeyId": "{{ KeyId }}"
 },
 "RetentionPeriodHours": "{{ RetentionPeriodHours }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "Name": "{{ Name }}",
 "ShardCount": "{{ ShardCount }}"
}
>>>
--required properties only
INSERT INTO aws.kinesis.streams (
 StreamModeDetails,
 StreamEncryption,
 RetentionPeriodHours,
 Tags,
 Name,
 ShardCount,
 region
)
SELECT 
{{ StreamModeDetails }},
 {{ StreamEncryption }},
 {{ RetentionPeriodHours }},
 {{ Tags }},
 {{ Name }},
 {{ ShardCount }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "StreamModeDetails": {
  "StreamMode": "{{ StreamMode }}"
 },
 "StreamEncryption": {
  "EncryptionType": "{{ EncryptionType }}",
  "KeyId": "{{ KeyId }}"
 },
 "RetentionPeriodHours": "{{ RetentionPeriodHours }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "Name": "{{ Name }}",
 "ShardCount": "{{ ShardCount }}"
}
>>>
--all properties
INSERT INTO aws.kinesis.streams (
 StreamModeDetails,
 StreamEncryption,
 RetentionPeriodHours,
 Tags,
 Name,
 ShardCount,
 region
)
SELECT 
 {{ StreamModeDetails }},
 {{ StreamEncryption }},
 {{ RetentionPeriodHours }},
 {{ Tags }},
 {{ Name }},
 {{ ShardCount }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.kinesis.streams
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>streams</code> resource, the following permissions are required:

### Create
```json
kinesis:EnableEnhancedMonitoring,
kinesis:DescribeStreamSummary,
kinesis:CreateStream,
kinesis:IncreaseStreamRetentionPeriod,
kinesis:StartStreamEncryption,
kinesis:AddTagsToStream,
kinesis:ListTagsForStream
```

### List
```json
kinesis:ListStreams
```

### Delete
```json
kinesis:DescribeStreamSummary,
kinesis:DeleteStream,
kinesis:RemoveTagsFromStream
```


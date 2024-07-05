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

Creates, updates, deletes or gets a <code>stream</code> resource or lists <code>streams</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Kinesis::Stream</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kinesis.streams" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="stream_mode_details" /></td><td><code>object</code></td><td>The mode in which the stream is running.</td></tr>
<tr><td><CopyableCode code="stream_encryption" /></td><td><code>object</code></td><td>When specified, enables or updates server-side encryption using an AWS KMS key for a specified stream.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon resource name (ARN) of the Kinesis stream</td></tr>
<tr><td><CopyableCode code="retention_period_hours" /></td><td><code>integer</code></td><td>The number of hours for the data records that are stored in shards to remain accessible.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key–value pairs) to associate with the Kinesis stream.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the Kinesis stream.</td></tr>
<tr><td><CopyableCode code="shard_count" /></td><td><code>integer</code></td><td>The number of shards that the stream uses. Required when StreamMode = PROVISIONED is passed.</td></tr>
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
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>streams</code> in a region.
```sql
SELECT
region,
stream_mode_details,
stream_encryption,
arn,
retention_period_hours,
tags,
name,
shard_count
FROM aws.kinesis.streams
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>stream</code>.
```sql
SELECT
region,
stream_mode_details,
stream_encryption,
arn,
retention_period_hours,
tags,
name,
shard_count
FROM aws.kinesis.streams
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

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
'{{ StreamModeDetails }}',
 '{{ StreamEncryption }}',
 '{{ RetentionPeriodHours }}',
 '{{ Tags }}',
 '{{ Name }}',
 '{{ ShardCount }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ StreamModeDetails }}',
 '{{ StreamEncryption }}',
 '{{ RetentionPeriodHours }}',
 '{{ Tags }}',
 '{{ Name }}',
 '{{ ShardCount }}',
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
      - name: StreamModeDetails
        value:
          StreamMode: '{{ StreamMode }}'
      - name: StreamEncryption
        value:
          EncryptionType: '{{ EncryptionType }}'
          KeyId: '{{ KeyId }}'
      - name: RetentionPeriodHours
        value: '{{ RetentionPeriodHours }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: Name
        value: '{{ Name }}'
      - name: ShardCount
        value: '{{ ShardCount }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.kinesis.streams
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>streams</code> resource, the following permissions are required:

### Read
```json
kinesis:DescribeStreamSummary,
kinesis:ListTagsForStream
```

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

### Update
```json
kinesis:EnableEnhancedMonitoring,
kinesis:DisableEnhancedMonitoring,
kinesis:DescribeStreamSummary,
kinesis:UpdateShardCount,
kinesis:UpdateStreamMode,
kinesis:IncreaseStreamRetentionPeriod,
kinesis:DecreaseStreamRetentionPeriod,
kinesis:StartStreamEncryption,
kinesis:StopStreamEncryption,
kinesis:AddTagsToStream,
kinesis:RemoveTagsFromStream,
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


---
title: event_source_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - event_source_mappings
  - lambda
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


Used to retrieve a list of <code>event_source_mappings</code> in a region or to create or delete a <code>event_source_mappings</code> resource, use <code>event_source_mapping</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_source_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::Lambda::EventSourceMapping`` resource creates a mapping between an event source and an LAMlong function. LAM reads items from the event source and triggers the function.&lt;br&#x2F;&gt; For details about each event source type, see the following topics. In particular, each of the topics describes the required and optional parameters for the specific event source. &lt;br&#x2F;&gt;  +  &#91;Configuring a Dynamo DB stream as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-ddb.html#services-dynamodb-eventsourcemapping)&lt;br&#x2F;&gt;  +  &#91;Configuring a Kinesis stream as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-kinesis.html#services-kinesis-eventsourcemapping)&lt;br&#x2F;&gt;  +  &#91;Configuring an SQS queue as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-sqs.html#events-sqs-eventsource)&lt;br&#x2F;&gt;  +  &#91;Configuring an MQ broker as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-mq.html#services-mq-eventsourcemapping)&lt;br&#x2F;&gt;  +  &#91;Configuring MSK as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-msk.html)&lt;br&#x2F;&gt;  +  &#91;Configuring Self-Managed Apache Kafka as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;kafka-smaa.html)&lt;br&#x2F;&gt;  +  &#91;Configuring Amazon DocumentDB as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-documentdb.html)</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.event_source_mappings" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
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
id
FROM aws.lambda.event_source_mappings
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
 "FunctionName": "{{ FunctionName }}"
}
>>>
--required properties only
INSERT INTO aws.lambda.event_source_mappings (
 FunctionName,
 region
)
SELECT 
{{ FunctionName }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "BatchSize": "{{ BatchSize }}",
 "BisectBatchOnFunctionError": "{{ BisectBatchOnFunctionError }}",
 "DestinationConfig": {
  "OnFailure": {
   "Destination": "{{ Destination }}"
  }
 },
 "Enabled": "{{ Enabled }}",
 "EventSourceArn": "{{ EventSourceArn }}",
 "FilterCriteria": {
  "Filters": [
   {
    "Pattern": "{{ Pattern }}"
   }
  ]
 },
 "FunctionName": "{{ FunctionName }}",
 "MaximumBatchingWindowInSeconds": "{{ MaximumBatchingWindowInSeconds }}",
 "MaximumRecordAgeInSeconds": "{{ MaximumRecordAgeInSeconds }}",
 "MaximumRetryAttempts": "{{ MaximumRetryAttempts }}",
 "ParallelizationFactor": "{{ ParallelizationFactor }}",
 "StartingPosition": "{{ StartingPosition }}",
 "StartingPositionTimestamp": null,
 "Topics": [
  "{{ Topics[0] }}"
 ],
 "Queues": [
  "{{ Queues[0] }}"
 ],
 "SourceAccessConfigurations": [
  {
   "Type": "{{ Type }}",
   "URI": "{{ URI }}"
  }
 ],
 "TumblingWindowInSeconds": "{{ TumblingWindowInSeconds }}",
 "FunctionResponseTypes": [
  "{{ FunctionResponseTypes[0] }}"
 ],
 "SelfManagedEventSource": {
  "Endpoints": {
   "KafkaBootstrapServers": [
    "{{ KafkaBootstrapServers[0] }}"
   ]
  }
 },
 "AmazonManagedKafkaEventSourceConfig": {
  "ConsumerGroupId": "{{ ConsumerGroupId }}"
 },
 "SelfManagedKafkaEventSourceConfig": {
  "ConsumerGroupId": null
 },
 "ScalingConfig": {
  "MaximumConcurrency": "{{ MaximumConcurrency }}"
 },
 "DocumentDBEventSourceConfig": {
  "DatabaseName": "{{ DatabaseName }}",
  "CollectionName": "{{ CollectionName }}",
  "FullDocument": "{{ FullDocument }}"
 }
}
>>>
--all properties
INSERT INTO aws.lambda.event_source_mappings (
 BatchSize,
 BisectBatchOnFunctionError,
 DestinationConfig,
 Enabled,
 EventSourceArn,
 FilterCriteria,
 FunctionName,
 MaximumBatchingWindowInSeconds,
 MaximumRecordAgeInSeconds,
 MaximumRetryAttempts,
 ParallelizationFactor,
 StartingPosition,
 StartingPositionTimestamp,
 Topics,
 Queues,
 SourceAccessConfigurations,
 TumblingWindowInSeconds,
 FunctionResponseTypes,
 SelfManagedEventSource,
 AmazonManagedKafkaEventSourceConfig,
 SelfManagedKafkaEventSourceConfig,
 ScalingConfig,
 DocumentDBEventSourceConfig,
 region
)
SELECT 
 {{ BatchSize }},
 {{ BisectBatchOnFunctionError }},
 {{ DestinationConfig }},
 {{ Enabled }},
 {{ EventSourceArn }},
 {{ FilterCriteria }},
 {{ FunctionName }},
 {{ MaximumBatchingWindowInSeconds }},
 {{ MaximumRecordAgeInSeconds }},
 {{ MaximumRetryAttempts }},
 {{ ParallelizationFactor }},
 {{ StartingPosition }},
 {{ StartingPositionTimestamp }},
 {{ Topics }},
 {{ Queues }},
 {{ SourceAccessConfigurations }},
 {{ TumblingWindowInSeconds }},
 {{ FunctionResponseTypes }},
 {{ SelfManagedEventSource }},
 {{ AmazonManagedKafkaEventSourceConfig }},
 {{ SelfManagedKafkaEventSourceConfig }},
 {{ ScalingConfig }},
 {{ DocumentDBEventSourceConfig }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.lambda.event_source_mappings
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>event_source_mappings</code> resource, the following permissions are required:

### Create
```json
lambda:CreateEventSourceMapping,
lambda:GetEventSourceMapping
```

### Delete
```json
lambda:DeleteEventSourceMapping,
lambda:GetEventSourceMapping
```

### List
```json
lambda:ListEventSourceMappings
```


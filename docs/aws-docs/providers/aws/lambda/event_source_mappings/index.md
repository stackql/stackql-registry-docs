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
<tr><td><b>Description</b></td><td>The <code>AWS::Lambda::EventSourceMapping</code> resource creates a mapping between an event source and an LAMlong function. LAM reads items from the event source and triggers the function.&lt;br&#x2F;&gt; For details about each event source type, see the following topics. In particular, each of the topics describes the required and optional parameters for the specific event source. &lt;br&#x2F;&gt;  +  &#91;Configuring a Dynamo DB stream as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-ddb.html#services-dynamodb-eventsourcemapping)&lt;br&#x2F;&gt;  +  &#91;Configuring a Kinesis stream as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-kinesis.html#services-kinesis-eventsourcemapping)&lt;br&#x2F;&gt;  +  &#91;Configuring an SQS queue as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-sqs.html#events-sqs-eventsource)&lt;br&#x2F;&gt;  +  &#91;Configuring an MQ broker as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-mq.html#services-mq-eventsourcemapping)&lt;br&#x2F;&gt;  +  &#91;Configuring MSK as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-msk.html)&lt;br&#x2F;&gt;  +  &#91;Configuring Self-Managed Apache Kafka as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;kafka-smaa.html)&lt;br&#x2F;&gt;  +  &#91;Configuring Amazon DocumentDB as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-documentdb.html)</td></tr>
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
    <td><CopyableCode code="FunctionName, region" /></td>
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

Use the following StackQL query and manifest file to create a new <code>event_source_mapping</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.lambda.event_source_mappings (
 FunctionName,
 region
)
SELECT 
'{{ FunctionName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ BatchSize }}',
 '{{ BisectBatchOnFunctionError }}',
 '{{ DestinationConfig }}',
 '{{ Enabled }}',
 '{{ EventSourceArn }}',
 '{{ FilterCriteria }}',
 '{{ FunctionName }}',
 '{{ MaximumBatchingWindowInSeconds }}',
 '{{ MaximumRecordAgeInSeconds }}',
 '{{ MaximumRetryAttempts }}',
 '{{ ParallelizationFactor }}',
 '{{ StartingPosition }}',
 '{{ StartingPositionTimestamp }}',
 '{{ Topics }}',
 '{{ Queues }}',
 '{{ SourceAccessConfigurations }}',
 '{{ TumblingWindowInSeconds }}',
 '{{ FunctionResponseTypes }}',
 '{{ SelfManagedEventSource }}',
 '{{ AmazonManagedKafkaEventSourceConfig }}',
 '{{ SelfManagedKafkaEventSourceConfig }}',
 '{{ ScalingConfig }}',
 '{{ DocumentDBEventSourceConfig }}',
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
  - name: event_source_mapping
    props:
      - name: BatchSize
        value: '{{ BatchSize }}'
      - name: BisectBatchOnFunctionError
        value: '{{ BisectBatchOnFunctionError }}'
      - name: DestinationConfig
        value:
          OnFailure:
            Destination: '{{ Destination }}'
      - name: Enabled
        value: '{{ Enabled }}'
      - name: EventSourceArn
        value: '{{ EventSourceArn }}'
      - name: FilterCriteria
        value:
          Filters:
            - Pattern: '{{ Pattern }}'
      - name: FunctionName
        value: '{{ FunctionName }}'
      - name: MaximumBatchingWindowInSeconds
        value: '{{ MaximumBatchingWindowInSeconds }}'
      - name: MaximumRecordAgeInSeconds
        value: '{{ MaximumRecordAgeInSeconds }}'
      - name: MaximumRetryAttempts
        value: '{{ MaximumRetryAttempts }}'
      - name: ParallelizationFactor
        value: '{{ ParallelizationFactor }}'
      - name: StartingPosition
        value: '{{ StartingPosition }}'
      - name: StartingPositionTimestamp
        value: null
      - name: Topics
        value:
          - '{{ Topics[0] }}'
      - name: Queues
        value:
          - '{{ Queues[0] }}'
      - name: SourceAccessConfigurations
        value:
          - Type: '{{ Type }}'
            URI: '{{ URI }}'
      - name: TumblingWindowInSeconds
        value: '{{ TumblingWindowInSeconds }}'
      - name: FunctionResponseTypes
        value:
          - '{{ FunctionResponseTypes[0] }}'
      - name: SelfManagedEventSource
        value:
          Endpoints:
            KafkaBootstrapServers:
              - '{{ KafkaBootstrapServers[0] }}'
      - name: AmazonManagedKafkaEventSourceConfig
        value:
          ConsumerGroupId: '{{ ConsumerGroupId }}'
      - name: SelfManagedKafkaEventSourceConfig
        value:
          ConsumerGroupId: null
      - name: ScalingConfig
        value:
          MaximumConcurrency: '{{ MaximumConcurrency }}'
      - name: DocumentDBEventSourceConfig
        value:
          DatabaseName: '{{ DatabaseName }}'
          CollectionName: '{{ CollectionName }}'
          FullDocument: '{{ FullDocument }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
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


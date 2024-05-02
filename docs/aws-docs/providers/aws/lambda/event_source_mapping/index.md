---
title: event_source_mapping
hide_title: false
hide_table_of_contents: false
keywords:
  - event_source_mapping
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
Gets or operates on an individual <code>event_source_mapping</code> resource, use <code>event_source_mappings</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_source_mapping</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::Lambda::EventSourceMapping`` resource creates a mapping between an event source and an LAMlong function. LAM reads items from the event source and triggers the function.&lt;br&#x2F;&gt; For details about each event source type, see the following topics. In particular, each of the topics describes the required and optional parameters for the specific event source. &lt;br&#x2F;&gt;  +  &#91;Configuring a Dynamo DB stream as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-ddb.html#services-dynamodb-eventsourcemapping)&lt;br&#x2F;&gt;  +  &#91;Configuring a Kinesis stream as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-kinesis.html#services-kinesis-eventsourcemapping)&lt;br&#x2F;&gt;  +  &#91;Configuring an SQS queue as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-sqs.html#events-sqs-eventsource)&lt;br&#x2F;&gt;  +  &#91;Configuring an MQ broker as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-mq.html#services-mq-eventsourcemapping)&lt;br&#x2F;&gt;  +  &#91;Configuring MSK as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-msk.html)&lt;br&#x2F;&gt;  +  &#91;Configuring Self-Managed Apache Kafka as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;kafka-smaa.html)&lt;br&#x2F;&gt;  +  &#91;Configuring Amazon DocumentDB as an event source&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-documentdb.html)</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lambda.event_source_mapping</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>batch_size</code></td><td><code>integer</code></td><td>The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).&lt;br&#x2F;&gt;  +   *Amazon Kinesis* – Default 100. Max 10,000.&lt;br&#x2F;&gt;  +   *Amazon DynamoDB Streams* – Default 100. Max 10,000.&lt;br&#x2F;&gt;  +   *Amazon Simple Queue Service* – Default 10. For standard queues the max is 10,000. For FIFO queues the max is 10.&lt;br&#x2F;&gt;  +   *Amazon Managed Streaming for Apache Kafka* – Default 100. Max 10,000.&lt;br&#x2F;&gt;  +   *Self-managed Apache Kafka* – Default 100. Max 10,000.&lt;br&#x2F;&gt;  +   *Amazon MQ (ActiveMQ and RabbitMQ)* – Default 100. Max 10,000.&lt;br&#x2F;&gt;  +   *DocumentDB* – Default 100. Max 10,000.</td></tr>
<tr><td><code>bisect_batch_on_function_error</code></td><td><code>boolean</code></td><td>(Kinesis and DynamoDB Streams only) If the function returns an error, split the batch in two and retry. The default value is false.</td></tr>
<tr><td><code>destination_config</code></td><td><code>object</code></td><td>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka event sources only) A configuration object that specifies the destination of an event after Lambda processes it.</td></tr>
<tr><td><code>enabled</code></td><td><code>boolean</code></td><td>When true, the event source mapping is active. When false, Lambda pauses polling and invocation.&lt;br&#x2F;&gt; Default: True</td></tr>
<tr><td><code>event_source_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the event source.&lt;br&#x2F;&gt;  +   *Amazon Kinesis* – The ARN of the data stream or a stream consumer.&lt;br&#x2F;&gt;  +   *Amazon DynamoDB Streams* – The ARN of the stream.&lt;br&#x2F;&gt;  +   *Amazon Simple Queue Service* – The ARN of the queue.&lt;br&#x2F;&gt;  +   *Amazon Managed Streaming for Apache Kafka* – The ARN of the cluster or the ARN of the VPC connection (for &#91;cross-account event source mappings&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-msk.html#msk-multi-vpc)).&lt;br&#x2F;&gt;  +   *Amazon MQ* – The ARN of the broker.&lt;br&#x2F;&gt;  +   *Amazon DocumentDB* – The ARN of the DocumentDB change stream.</td></tr>
<tr><td><code>filter_criteria</code></td><td><code>object</code></td><td>An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see &#91;Lambda event filtering&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;invocation-eventfiltering.html).</td></tr>
<tr><td><code>function_name</code></td><td><code>string</code></td><td>The name or ARN of the Lambda function.&lt;br&#x2F;&gt;  **Name formats**&lt;br&#x2F;&gt; +   *Function name* – ``MyFunction``.&lt;br&#x2F;&gt;  +   *Function ARN* – ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction``.&lt;br&#x2F;&gt;  +   *Version or Alias ARN* – ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD``.&lt;br&#x2F;&gt;  +   *Partial ARN* – ``123456789012:function:MyFunction``.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.</td></tr>
<tr><td><code>maximum_batching_window_in_seconds</code></td><td><code>integer</code></td><td>The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function.&lt;br&#x2F;&gt; *Default (, , event sources)*: 0&lt;br&#x2F;&gt; *Default (, Kafka, , event sources)*: 500 ms&lt;br&#x2F;&gt; *Related setting:* For SQS event sources, when you set ``BatchSize`` to a value greater than 10, you must set ``MaximumBatchingWindowInSeconds`` to at least 1.</td></tr>
<tr><td><code>maximum_record_age_in_seconds</code></td><td><code>integer</code></td><td>(Kinesis and DynamoDB Streams only) Discard records older than the specified age. The default value is -1, which sets the maximum age to infinite. When the value is set to infinite, Lambda never discards old records.&lt;br&#x2F;&gt;  The minimum valid value for maximum record age is 60s. Although values less than 60 and greater than -1 fall within the parameter's absolute range, they are not allowed</td></tr>
<tr><td><code>maximum_retry_attempts</code></td><td><code>integer</code></td><td>(Kinesis and DynamoDB Streams only) Discard records after the specified number of retries. The default value is -1, which sets the maximum number of retries to infinite. When MaximumRetryAttempts is infinite, Lambda retries failed records until the record expires in the event source.</td></tr>
<tr><td><code>parallelization_factor</code></td><td><code>integer</code></td><td>(Kinesis and DynamoDB Streams only) The number of batches to process concurrently from each shard. The default value is 1.</td></tr>
<tr><td><code>starting_position</code></td><td><code>string</code></td><td>The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB.&lt;br&#x2F;&gt;  +  *LATEST* - Read only new records.&lt;br&#x2F;&gt;  +  *TRIM_HORIZON* - Process all available records.&lt;br&#x2F;&gt;  +  *AT_TIMESTAMP* - Specify a time from which to start reading records.</td></tr>
<tr><td><code>starting_position_timestamp</code></td><td><code>number</code></td><td>With ``StartingPosition`` set to ``AT_TIMESTAMP``, the time from which to start reading, in Unix time seconds. ``StartingPositionTimestamp`` cannot be in the future.</td></tr>
<tr><td><code>topics</code></td><td><code>array</code></td><td>The name of the Kafka topic.</td></tr>
<tr><td><code>queues</code></td><td><code>array</code></td><td>(Amazon MQ) The name of the Amazon MQ broker destination queue to consume.</td></tr>
<tr><td><code>source_access_configurations</code></td><td><code>array</code></td><td>An array of the authentication protocol, VPC components, or virtual host to secure and define your event source.</td></tr>
<tr><td><code>tumbling_window_in_seconds</code></td><td><code>integer</code></td><td>(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.</td></tr>
<tr><td><code>function_response_types</code></td><td><code>array</code></td><td>(Streams and SQS) A list of current response type enums applied to the event source mapping.&lt;br&#x2F;&gt; Valid Values: ``ReportBatchItemFailures``</td></tr>
<tr><td><code>self_managed_event_source</code></td><td><code>object</code></td><td>The self-managed Apache Kafka cluster for your event source.</td></tr>
<tr><td><code>amazon_managed_kafka_event_source_config</code></td><td><code>object</code></td><td>Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source.</td></tr>
<tr><td><code>self_managed_kafka_event_source_config</code></td><td><code>object</code></td><td>Specific configuration settings for a self-managed Apache Kafka event source.</td></tr>
<tr><td><code>scaling_config</code></td><td><code>object</code></td><td>(Amazon SQS only) The scaling configuration for the event source. For more information, see &#91;Configuring maximum concurrency for Amazon SQS event sources&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;lambda&#x2F;latest&#x2F;dg&#x2F;with-sqs.html#events-sqs-max-concurrency).</td></tr>
<tr><td><code>document_db_event_source_config</code></td><td><code>object</code></td><td>Specific configuration settings for a DocumentDB event source.</td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
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
id,
batch_size,
bisect_batch_on_function_error,
destination_config,
enabled,
event_source_arn,
filter_criteria,
function_name,
maximum_batching_window_in_seconds,
maximum_record_age_in_seconds,
maximum_retry_attempts,
parallelization_factor,
starting_position,
starting_position_timestamp,
topics,
queues,
source_access_configurations,
tumbling_window_in_seconds,
function_response_types,
self_managed_event_source,
amazon_managed_kafka_event_source_config,
self_managed_kafka_event_source_config,
scaling_config,
document_db_event_source_config
FROM aws.lambda.event_source_mapping
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>event_source_mapping</code> resource, the following permissions are required:

### Delete
```json
lambda:DeleteEventSourceMapping,
lambda:GetEventSourceMapping
```

### Read
```json
lambda:GetEventSourceMapping
```

### Update
```json
lambda:UpdateEventSourceMapping,
lambda:GetEventSourceMapping
```


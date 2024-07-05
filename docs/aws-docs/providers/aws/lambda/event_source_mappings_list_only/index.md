---
title: event_source_mappings_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - event_source_mappings_list_only
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

Lists <code>event_source_mappings</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/event_source_mappings/"><code>event_source_mappings</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_source_mappings_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::Lambda::EventSourceMapping</code> resource creates a mapping between an event source and an LAMlong function. LAM reads items from the event source and triggers the function.<br />For details about each event source type, see the following topics. In particular, each of the topics describes the required and optional parameters for the specific event source. <br />+ &#91;Configuring a Dynamo DB stream as an event source&#93;(https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-dynamodb-eventsourcemapping) <br />+ &#91;Configuring a Kinesis stream as an event source&#93;(https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-eventsourcemapping) <br />+ &#91;Configuring an SQS queue as an event source&#93;(https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource) <br />+ &#91;Configuring an MQ broker as an event source&#93;(https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-eventsourcemapping) <br />+ &#91;Configuring MSK as an event source&#93;(https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html) <br />+ &#91;Configuring Self-Managed Apache Kafka as an event source&#93;(https://docs.aws.amazon.com/lambda/latest/dg/kafka-smaa.html) <br />+ &#91;Configuring Amazon DocumentDB as an event source&#93;(https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html)</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.event_source_mappings_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="starting_position" /></td><td><code>string</code></td><td>The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB.<br />+ *LATEST* - Read only new records.<br />+ *TRIM_HORIZON* - Process all available records.<br />+ *AT_TIMESTAMP* - Specify a time from which to start reading records.</td></tr>
<tr><td><CopyableCode code="self_managed_event_source" /></td><td><code>object</code></td><td>The self-managed Apache Kafka cluster for your event source.</td></tr>
<tr><td><CopyableCode code="parallelization_factor" /></td><td><code>integer</code></td><td>(Kinesis and DynamoDB Streams only) The number of batches to process concurrently from each shard. The default value is 1.</td></tr>
<tr><td><CopyableCode code="filter_criteria" /></td><td><code>object</code></td><td>An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see &#91;Lambda event filtering&#93;(https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html).</td></tr>
<tr><td><CopyableCode code="function_name" /></td><td><code>string</code></td><td>The name or ARN of the Lambda function.<br />**Name formats**<br />+ *Function name* – <code>MyFunction</code>.<br />+ *Function ARN* – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.<br />+ *Version or Alias ARN* – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD</code>.<br />+ *Partial ARN* – <code>123456789012:function:MyFunction</code>.<br /><br />The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.</td></tr>
<tr><td><CopyableCode code="destination_config" /></td><td><code>object</code></td><td>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka event sources only) A configuration object that specifies the destination of an event after Lambda processes it.</td></tr>
<tr><td><CopyableCode code="amazon_managed_kafka_event_source_config" /></td><td><code>object</code></td><td>Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source.</td></tr>
<tr><td><CopyableCode code="source_access_configurations" /></td><td><code>array</code></td><td>An array of the authentication protocol, VPC components, or virtual host to secure and define your event source.</td></tr>
<tr><td><CopyableCode code="maximum_batching_window_in_seconds" /></td><td><code>integer</code></td><td>The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function.<br />*Default (, , event sources)*: 0<br />*Default (, Kafka, , event sources)*: 500 ms<br />*Related setting:* For SQS event sources, when you set <code>BatchSize</code> to a value greater than 10, you must set <code>MaximumBatchingWindowInSeconds</code> to at least 1.</td></tr>
<tr><td><CopyableCode code="batch_size" /></td><td><code>integer</code></td><td>The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).<br />+ *Amazon Kinesis* – Default 100. Max 10,000.<br />+ *Amazon DynamoDB Streams* – Default 100. Max 10,000.<br />+ *Amazon Simple Queue Service* – Default 10. For standard queues the max is 10,000. For FIFO queues the max is 10.<br />+ *Amazon Managed Streaming for Apache Kafka* – Default 100. Max 10,000.<br />+ *Self-managed Apache Kafka* – Default 100. Max 10,000.<br />+ *Amazon MQ (ActiveMQ and RabbitMQ)* – Default 100. Max 10,000.<br />+ *DocumentDB* – Default 100. Max 10,000.</td></tr>
<tr><td><CopyableCode code="maximum_retry_attempts" /></td><td><code>integer</code></td><td>(Kinesis and DynamoDB Streams only) Discard records after the specified number of retries. The default value is -1, which sets the maximum number of retries to infinite. When MaximumRetryAttempts is infinite, Lambda retries failed records until the record expires in the event source.</td></tr>
<tr><td><CopyableCode code="topics" /></td><td><code>array</code></td><td>The name of the Kafka topic.</td></tr>
<tr><td><CopyableCode code="scaling_config" /></td><td><code>object</code></td><td>(Amazon SQS only) The scaling configuration for the event source. For more information, see &#91;Configuring maximum concurrency for Amazon SQS event sources&#93;(https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency).</td></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td>When true, the event source mapping is active. When false, Lambda pauses polling and invocation.<br />Default: True</td></tr>
<tr><td><CopyableCode code="event_source_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the event source.<br />+ *Amazon Kinesis* – The ARN of the data stream or a stream consumer.<br />+ *Amazon DynamoDB Streams* – The ARN of the stream.<br />+ *Amazon Simple Queue Service* – The ARN of the queue.<br />+ *Amazon Managed Streaming for Apache Kafka* – The ARN of the cluster or the ARN of the VPC connection (for &#91;cross-account event source mappings&#93;(https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#msk-multi-vpc)).<br />+ *Amazon MQ* – The ARN of the broker.<br />+ *Amazon DocumentDB* – The ARN of the DocumentDB change stream.</td></tr>
<tr><td><CopyableCode code="self_managed_kafka_event_source_config" /></td><td><code>object</code></td><td>Specific configuration settings for a self-managed Apache Kafka event source.</td></tr>
<tr><td><CopyableCode code="document_db_event_source_config" /></td><td><code>object</code></td><td>Specific configuration settings for a DocumentDB event source.</td></tr>
<tr><td><CopyableCode code="tumbling_window_in_seconds" /></td><td><code>integer</code></td><td>(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.</td></tr>
<tr><td><CopyableCode code="bisect_batch_on_function_error" /></td><td><code>boolean</code></td><td>(Kinesis and DynamoDB Streams only) If the function returns an error, split the batch in two and retry. The default value is false.</td></tr>
<tr><td><CopyableCode code="maximum_record_age_in_seconds" /></td><td><code>integer</code></td><td>(Kinesis and DynamoDB Streams only) Discard records older than the specified age. The default value is -1, which sets the maximum age to infinite. When the value is set to infinite, Lambda never discards old records.<br />The minimum valid value for maximum record age is 60s. Although values less than 60 and greater than -1 fall within the parameter's absolute range, they are not allowed</td></tr>
<tr><td><CopyableCode code="starting_position_timestamp" /></td><td><code>number</code></td><td>With <code>StartingPosition</code> set to <code>AT_TIMESTAMP</code>, the time from which to start reading, in Unix time seconds. <code>StartingPositionTimestamp</code> cannot be in the future.</td></tr>
<tr><td><CopyableCode code="queues" /></td><td><code>array</code></td><td>(Amazon MQ) The name of the Amazon MQ broker destination queue to consume.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="function_response_types" /></td><td><code>array</code></td><td>(Streams and SQS) A list of current response type enums applied to the event source mapping.<br />Valid Values: <code>ReportBatchItemFailures</code></td></tr>
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
Lists all <code>event_source_mappings</code> in a region.
```sql
SELECT
region,
id
FROM aws.lambda.event_source_mappings_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>event_source_mappings_list_only</code> resource, see <a href="/providers/aws/lambda/event_source_mappings/#permissions"><code>event_source_mappings</code></a>



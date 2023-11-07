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
Retrieves a list of <code>event_source_mappings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_source_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.lambda.event_source_mappings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>Event Source Mapping Identifier UUID.</td></tr>
<tr><td><code>BatchSize</code></td><td><code>integer</code></td><td>The maximum number of items to retrieve in a single batch.</td></tr>
<tr><td><code>BisectBatchOnFunctionError</code></td><td><code>boolean</code></td><td>(Streams) If the function returns an error, split the batch in two and retry.</td></tr>
<tr><td><code>DestinationConfig</code></td><td><code>undefined</code></td><td>(Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.</td></tr>
<tr><td><code>Enabled</code></td><td><code>boolean</code></td><td>Disables the event source mapping to pause polling and invocation.</td></tr>
<tr><td><code>EventSourceArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the event source.</td></tr>
<tr><td><code>FilterCriteria</code></td><td><code>undefined</code></td><td>The filter criteria to control event filtering.</td></tr>
<tr><td><code>FunctionName</code></td><td><code>string</code></td><td>The name of the Lambda function.</td></tr>
<tr><td><code>MaximumBatchingWindowInSeconds</code></td><td><code>integer</code></td><td>(Streams) The maximum amount of time to gather records before invoking the function, in seconds.</td></tr>
<tr><td><code>MaximumRecordAgeInSeconds</code></td><td><code>integer</code></td><td>(Streams) The maximum age of a record that Lambda sends to a function for processing.</td></tr>
<tr><td><code>MaximumRetryAttempts</code></td><td><code>integer</code></td><td>(Streams) The maximum number of times to retry when the function returns an error.</td></tr>
<tr><td><code>ParallelizationFactor</code></td><td><code>integer</code></td><td>(Streams) The number of batches to process from each shard concurrently.</td></tr>
<tr><td><code>StartingPosition</code></td><td><code>string</code></td><td>The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Streams sources.</td></tr>
<tr><td><code>StartingPositionTimestamp</code></td><td><code>number</code></td><td>With StartingPosition set to AT_TIMESTAMP, the time from which to start reading, in Unix time seconds.</td></tr>
<tr><td><code>Topics</code></td><td><code>array</code></td><td>(Kafka) A list of Kafka topics.</td></tr>
<tr><td><code>Queues</code></td><td><code>array</code></td><td>(ActiveMQ) A list of ActiveMQ queues.</td></tr>
<tr><td><code>SourceAccessConfigurations</code></td><td><code>array</code></td><td>A list of SourceAccessConfiguration.</td></tr>
<tr><td><code>TumblingWindowInSeconds</code></td><td><code>integer</code></td><td>(Streams) Tumbling window (non-overlapping time window) duration to perform aggregations.</td></tr>
<tr><td><code>FunctionResponseTypes</code></td><td><code>array</code></td><td>(Streams) A list of response types supported by the function.</td></tr>
<tr><td><code>SelfManagedEventSource</code></td><td><code>undefined</code></td><td>Self-managed event source endpoints.</td></tr>
<tr><td><code>AmazonManagedKafkaEventSourceConfig</code></td><td><code>undefined</code></td><td>Specific configuration settings for an MSK event source.</td></tr>
<tr><td><code>SelfManagedKafkaEventSourceConfig</code></td><td><code>undefined</code></td><td>Specific configuration settings for a Self-Managed Apache Kafka event source.</td></tr>
<tr><td><code>ScalingConfig</code></td><td><code>undefined</code></td><td>The scaling configuration for the event source.</td></tr>
<tr><td><code>DocumentDBEventSourceConfig</code></td><td><code>undefined</code></td><td>Document db event source config.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.lambda.event_source_mappings
WHERE region = 'us-east-1'
</pre>

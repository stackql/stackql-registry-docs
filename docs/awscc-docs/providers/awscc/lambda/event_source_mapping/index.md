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
Gets an individual <code>event_source_mapping</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_source_mapping</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>event_source_mapping</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lambda.event_source_mapping</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Event Source Mapping Identifier UUID.</td></tr>
<tr><td><code>batch_size</code></td><td><code>integer</code></td><td>The maximum number of items to retrieve in a single batch.</td></tr>
<tr><td><code>bisect_batch_on_function_error</code></td><td><code>boolean</code></td><td>(Streams) If the function returns an error, split the batch in two and retry.</td></tr>
<tr><td><code>destination_config</code></td><td><code>object</code></td><td>(Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.</td></tr>
<tr><td><code>enabled</code></td><td><code>boolean</code></td><td>Disables the event source mapping to pause polling and invocation.</td></tr>
<tr><td><code>event_source_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the event source.</td></tr>
<tr><td><code>filter_criteria</code></td><td><code>object</code></td><td>The filter criteria to control event filtering.</td></tr>
<tr><td><code>function_name</code></td><td><code>string</code></td><td>The name of the Lambda function.</td></tr>
<tr><td><code>maximum_batching_window_in_seconds</code></td><td><code>integer</code></td><td>(Streams) The maximum amount of time to gather records before invoking the function, in seconds.</td></tr>
<tr><td><code>maximum_record_age_in_seconds</code></td><td><code>integer</code></td><td>(Streams) The maximum age of a record that Lambda sends to a function for processing.</td></tr>
<tr><td><code>maximum_retry_attempts</code></td><td><code>integer</code></td><td>(Streams) The maximum number of times to retry when the function returns an error.</td></tr>
<tr><td><code>parallelization_factor</code></td><td><code>integer</code></td><td>(Streams) The number of batches to process from each shard concurrently.</td></tr>
<tr><td><code>starting_position</code></td><td><code>string</code></td><td>The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Streams sources.</td></tr>
<tr><td><code>starting_position_timestamp</code></td><td><code>number</code></td><td>With StartingPosition set to AT_TIMESTAMP, the time from which to start reading, in Unix time seconds.</td></tr>
<tr><td><code>topics</code></td><td><code>array</code></td><td>(Kafka) A list of Kafka topics.</td></tr>
<tr><td><code>queues</code></td><td><code>array</code></td><td>(ActiveMQ) A list of ActiveMQ queues.</td></tr>
<tr><td><code>source_access_configurations</code></td><td><code>array</code></td><td>A list of SourceAccessConfiguration.</td></tr>
<tr><td><code>tumbling_window_in_seconds</code></td><td><code>integer</code></td><td>(Streams) Tumbling window (non-overlapping time window) duration to perform aggregations.</td></tr>
<tr><td><code>function_response_types</code></td><td><code>array</code></td><td>(Streams) A list of response types supported by the function.</td></tr>
<tr><td><code>self_managed_event_source</code></td><td><code>object</code></td><td>Self-managed event source endpoints.</td></tr>
<tr><td><code>amazon_managed_kafka_event_source_config</code></td><td><code>object</code></td><td>Specific configuration settings for an MSK event source.</td></tr>
<tr><td><code>self_managed_kafka_event_source_config</code></td><td><code>object</code></td><td>Specific configuration settings for a Self-Managed Apache Kafka event source.</td></tr>
<tr><td><code>scaling_config</code></td><td><code>object</code></td><td>The scaling configuration for the event source.</td></tr>
<tr><td><code>document_db_event_source_config</code></td><td><code>object</code></td><td>Document db event source config.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.lambda.event_source_mapping
WHERE region = 'us-east-1'
AND data__Identifier = '{Id}';
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


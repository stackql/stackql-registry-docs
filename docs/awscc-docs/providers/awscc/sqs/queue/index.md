---
title: queue
hide_title: false
hide_table_of_contents: false
keywords:
  - queue
  - sqs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>queue</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queue</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>queue</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sqs.queue</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>queue_url</code></td><td><code>string</code></td><td>URL of the source queue.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the queue.</td></tr>
<tr><td><code>content_based_deduplication</code></td><td><code>boolean</code></td><td>For first-in-first-out (FIFO) queues, specifies whether to enable content-based deduplication. During the deduplication interval, Amazon SQS treats messages that are sent with identical content as duplicates and delivers only one copy of the message.</td></tr>
<tr><td><code>deduplication_scope</code></td><td><code>string</code></td><td>Specifies whether message deduplication occurs at the message group or queue level. Valid values are messageGroup and queue.</td></tr>
<tr><td><code>delay_seconds</code></td><td><code>integer</code></td><td>The time in seconds for which the delivery of all messages in the queue is delayed. You can specify an integer value of 0 to 900 (15 minutes). The default value is 0.</td></tr>
<tr><td><code>fifo_queue</code></td><td><code>boolean</code></td><td>If set to true, creates a FIFO queue. If you don't specify this property, Amazon SQS creates a standard queue.</td></tr>
<tr><td><code>fifo_throughput_limit</code></td><td><code>string</code></td><td>Specifies whether the FIFO queue throughput quota applies to the entire queue or per message group. Valid values are perQueue and perMessageGroupId. The perMessageGroupId value is allowed only when the value for DeduplicationScope is messageGroup.</td></tr>
<tr><td><code>kms_data_key_reuse_period_seconds</code></td><td><code>integer</code></td><td>The length of time in seconds for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. The value must be an integer between 60 (1 minute) and 86,400 (24 hours). The default is 300 (5 minutes).</td></tr>
<tr><td><code>kms_master_key_id</code></td><td><code>string</code></td><td>The ID of an AWS managed customer master key (CMK) for Amazon SQS or a custom CMK. To use the AWS managed CMK for Amazon SQS, specify the (default) alias alias&#x2F;aws&#x2F;sqs.</td></tr>
<tr><td><code>sqs_managed_sse_enabled</code></td><td><code>boolean</code></td><td>Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (e.g. SSE-KMS or SSE-SQS ).</td></tr>
<tr><td><code>maximum_message_size</code></td><td><code>integer</code></td><td>The limit of how many bytes that a message can contain before Amazon SQS rejects it. You can specify an integer value from 1,024 bytes (1 KiB) to 262,144 bytes (256 KiB). The default value is 262,144 (256 KiB).</td></tr>
<tr><td><code>message_retention_period</code></td><td><code>integer</code></td><td>The number of seconds that Amazon SQS retains a message. You can specify an integer value from 60 seconds (1 minute) to 1,209,600 seconds (14 days). The default value is 345,600 seconds (4 days).</td></tr>
<tr><td><code>queue_name</code></td><td><code>string</code></td><td>A name for the queue. To create a FIFO queue, the name of your FIFO queue must end with the .fifo suffix.</td></tr>
<tr><td><code>receive_message_wait_time_seconds</code></td><td><code>integer</code></td><td>Specifies the duration, in seconds, that the ReceiveMessage action call waits until a message is in the queue in order to include it in the response, rather than returning an empty response if a message isn't yet available. You can specify an integer from 1 to 20. Short polling is used as the default or when you specify 0 for this property.</td></tr>
<tr><td><code>redrive_allow_policy</code></td><td><code>object</code></td><td>The string that includes the parameters for the permissions for the dead-letter queue redrive permission and which source queues can specify dead-letter queues as a JSON object.</td></tr>
<tr><td><code>redrive_policy</code></td><td><code>object</code></td><td>A string that includes the parameters for the dead-letter queue functionality (redrive policy) of the source queue.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags that you attach to this queue.</td></tr>
<tr><td><code>visibility_timeout</code></td><td><code>integer</code></td><td>The length of time during which a message will be unavailable after a message is delivered from the queue. This blocks other components from receiving the same message and gives the initial component time to process and delete the message from the queue. Values must be from 0 to 43,200 seconds (12 hours). If you don't specify a value, AWS CloudFormation uses the default value of 30 seconds.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
queue_url,
arn,
content_based_deduplication,
deduplication_scope,
delay_seconds,
fifo_queue,
fifo_throughput_limit,
kms_data_key_reuse_period_seconds,
kms_master_key_id,
sqs_managed_sse_enabled,
maximum_message_size,
message_retention_period,
queue_name,
receive_message_wait_time_seconds,
redrive_allow_policy,
redrive_policy,
tags,
visibility_timeout
FROM awscc.sqs.queue
WHERE region = 'us-east-1'
AND data__Identifier = '{QueueUrl}';
```

## Permissions

To operate on the <code>queue</code> resource, the following permissions are required:

### Read
```json
sqs:GetQueueAttributes,
sqs:ListQueueTags
```

### Update
```json
sqs:SetQueueAttributes,
sqs:GetQueueAttributes,
sqs:ListQueueTags,
sqs:TagQueue,
sqs:UntagQueue
```

### Delete
```json
sqs:DeleteQueue,
sqs:GetQueueAttributes
```


---
title: queues
hide_title: false
hide_table_of_contents: false
keywords:
  - queues
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
Retrieves a list of <code>queues</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sqs.queues</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>QueueUrl</code></td><td><code>string</code></td><td>URL of the source queue.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the queue.</td></tr><tr><td><code>ContentBasedDeduplication</code></td><td><code>boolean</code></td><td>For first-in-first-out (FIFO) queues, specifies whether to enable content-based deduplication. During the deduplication interval, Amazon SQS treats messages that are sent with identical content as duplicates and delivers only one copy of the message.</td></tr><tr><td><code>DeduplicationScope</code></td><td><code>string</code></td><td>Specifies whether message deduplication occurs at the message group or queue level. Valid values are messageGroup and queue.</td></tr><tr><td><code>DelaySeconds</code></td><td><code>integer</code></td><td>The time in seconds for which the delivery of all messages in the queue is delayed. You can specify an integer value of 0 to 900 (15 minutes). The default value is 0.</td></tr><tr><td><code>FifoQueue</code></td><td><code>boolean</code></td><td>If set to true, creates a FIFO queue. If you don't specify this property, Amazon SQS creates a standard queue.</td></tr><tr><td><code>FifoThroughputLimit</code></td><td><code>string</code></td><td>Specifies whether the FIFO queue throughput quota applies to the entire queue or per message group. Valid values are perQueue and perMessageGroupId. The perMessageGroupId value is allowed only when the value for DeduplicationScope is messageGroup.</td></tr><tr><td><code>KmsDataKeyReusePeriodSeconds</code></td><td><code>integer</code></td><td>The length of time in seconds for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. The value must be an integer between 60 (1 minute) and 86,400 (24 hours). The default is 300 (5 minutes).</td></tr><tr><td><code>KmsMasterKeyId</code></td><td><code>string</code></td><td>The ID of an AWS managed customer master key (CMK) for Amazon SQS or a custom CMK. To use the AWS managed CMK for Amazon SQS, specify the (default) alias alias/aws/sqs.</td></tr><tr><td><code>SqsManagedSseEnabled</code></td><td><code>boolean</code></td><td>Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (e.g. SSE-KMS or SSE-SQS ).</td></tr><tr><td><code>MaximumMessageSize</code></td><td><code>integer</code></td><td>The limit of how many bytes that a message can contain before Amazon SQS rejects it. You can specify an integer value from 1,024 bytes (1 KiB) to 262,144 bytes (256 KiB). The default value is 262,144 (256 KiB).</td></tr><tr><td><code>MessageRetentionPeriod</code></td><td><code>integer</code></td><td>The number of seconds that Amazon SQS retains a message. You can specify an integer value from 60 seconds (1 minute) to 1,209,600 seconds (14 days). The default value is 345,600 seconds (4 days).</td></tr><tr><td><code>QueueName</code></td><td><code>string</code></td><td>A name for the queue. To create a FIFO queue, the name of your FIFO queue must end with the .fifo suffix.</td></tr><tr><td><code>ReceiveMessageWaitTimeSeconds</code></td><td><code>integer</code></td><td>Specifies the duration, in seconds, that the ReceiveMessage action call waits until a message is in the queue in order to include it in the response, rather than returning an empty response if a message isn't yet available. You can specify an integer from 1 to 20. Short polling is used as the default or when you specify 0 for this property.</td></tr><tr><td><code>RedriveAllowPolicy</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RedrivePolicy</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags that you attach to this queue.</td></tr><tr><td><code>VisibilityTimeout</code></td><td><code>integer</code></td><td>The length of time during which a message will be unavailable after a message is delivered from the queue. This blocks other components from receiving the same message and gives the initial component time to process and delete the message from the queue. Values must be from 0 to 43,200 seconds (12 hours). If you don't specify a value, AWS CloudFormation uses the default value of 30 seconds.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.sqs.queues
WHERE region = 'us-east-1'
</pre>

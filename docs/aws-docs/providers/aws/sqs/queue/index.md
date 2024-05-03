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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>queue</code> resource, use <code>queues</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queue</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::SQS::Queue`` resource creates an SQS standard or FIFO queue.&lt;br&#x2F;&gt; Keep the following caveats in mind:&lt;br&#x2F;&gt;  +  If you don't specify the ``FifoQueue`` property, SQS creates a standard queue.&lt;br&#x2F;&gt;  You can't change the queue type after you create it and you can't convert an existing standard queue into a FIFO queue. You must either create a new FIFO queue for your application or delete your existing standard queue and recreate it as a FIFO queue. For more information, see &#91;Moving from a standard queue to a FIFO queue&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;FIFO-queues-moving.html) in the *Developer Guide*. &lt;br&#x2F;&gt;   +  If you don't provide a value for a property, the queue is created with the default value for the property.&lt;br&#x2F;&gt;  +  If you delete a queue, you must wait at least 60 seconds before creating a queue with the same name.&lt;br&#x2F;&gt;  +  To successfully create a new queue, you must provide a queue name that adheres to the &#91;limits related to queues&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;limits-queues.html) and is unique within the scope of your queues.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; For more information about creating FIFO (first-in-first-out) queues, see &#91;Creating an queue ()&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;screate-queue-cloudformation.html) in the *Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sqs.queue" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="queue_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="content_based_deduplication" /></td><td><code>boolean</code></td><td>For first-in-first-out (FIFO) queues, specifies whether to enable content-based deduplication. During the deduplication interval, SQS treats messages that are sent with identical content as duplicates and delivers only one copy of the message. For more information, see the ``ContentBasedDeduplication`` attribute for the ``CreateQueue`` action in the *API Reference*.</td></tr>
<tr><td><CopyableCode code="deduplication_scope" /></td><td><code>string</code></td><td>For high throughput for FIFO queues, specifies whether message deduplication occurs at the message group or queue level. Valid values are ``messageGroup`` and ``queue``.&lt;br&#x2F;&gt; To enable high throughput for a FIFO queue, set this attribute to ``messageGroup`` *and* set the ``FifoThroughputLimit`` attribute to ``perMessageGroupId``. If you set these attributes to anything other than these values, normal throughput is in effect and deduplication occurs as specified. For more information, see &#91;High throughput for FIFO queues&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;high-throughput-fifo.html) and &#91;Quotas related to messages&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;quotas-messages.html) in the *Developer Guide*.</td></tr>
<tr><td><CopyableCode code="delay_seconds" /></td><td><code>integer</code></td><td>The time in seconds for which the delivery of all messages in the queue is delayed. You can specify an integer value of ``0`` to ``900`` (15 minutes). The default value is ``0``.</td></tr>
<tr><td><CopyableCode code="fifo_queue" /></td><td><code>boolean</code></td><td>If set to true, creates a FIFO queue. If you don't specify this property, SQS creates a standard queue. For more information, see &#91;FIFO queues&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;FIFO-queues.html) in the *Developer Guide*.</td></tr>
<tr><td><CopyableCode code="fifo_throughput_limit" /></td><td><code>string</code></td><td>For high throughput for FIFO queues, specifies whether the FIFO queue throughput quota applies to the entire queue or per message group. Valid values are ``perQueue`` and ``perMessageGroupId``.&lt;br&#x2F;&gt; To enable high throughput for a FIFO queue, set this attribute to ``perMessageGroupId`` *and* set the ``DeduplicationScope`` attribute to ``messageGroup``. If you set these attributes to anything other than these values, normal throughput is in effect and deduplication occurs as specified. For more information, see &#91;High throughput for FIFO queues&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;high-throughput-fifo.html) and &#91;Quotas related to messages&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;quotas-messages.html) in the *Developer Guide*.</td></tr>
<tr><td><CopyableCode code="kms_data_key_reuse_period_seconds" /></td><td><code>integer</code></td><td>The length of time in seconds for which SQS can reuse a data key to encrypt or decrypt messages before calling KMS again. The value must be an integer between 60 (1 minute) and 86,400 (24 hours). The default is 300 (5 minutes).&lt;br&#x2F;&gt;  A shorter time period provides better security, but results in more calls to KMS, which might incur charges after Free Tier. For more information, see &#91;Encryption at rest&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;sqs-server-side-encryption.html#sqs-how-does-the-data-key-reuse-period-work) in the *Developer Guide*.</td></tr>
<tr><td><CopyableCode code="kms_master_key_id" /></td><td><code>string</code></td><td>The ID of an AWS Key Management Service (KMS) for SQS, or a custom KMS. To use the AWS managed KMS for SQS, specify a (default) alias ARN, alias name (e.g. ``alias&#x2F;aws&#x2F;sqs``), key ARN, or key ID. For more information, see the following:&lt;br&#x2F;&gt;  +   &#91;Encryption at rest&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;sqs-server-side-encryption.html) in the *Developer Guide* &lt;br&#x2F;&gt;  +   &#91;CreateQueue&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;APIReference&#x2F;API_CreateQueue.html) in the *API Reference* &lt;br&#x2F;&gt;  +   &#91;Request Parameters&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;kms&#x2F;latest&#x2F;APIReference&#x2F;API_DescribeKey.html#API_DescribeKey_RequestParameters) in the *Key Management Service API Reference* &lt;br&#x2F;&gt;  +   The Key Management Service (KMS) section of the &#91;Best Practices&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;https:&#x2F;&#x2F;d0.awsstatic.com&#x2F;whitepapers&#x2F;aws-kms-best-practices.pdf) whitepaper</td></tr>
<tr><td><CopyableCode code="sqs_managed_sse_enabled" /></td><td><code>boolean</code></td><td>Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (for example, &#91;SSE-KMS&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;sqs-configure-sse-existing-queue.html) or &#91;SSE-SQS&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;sqs-configure-sqs-sse-queue.html)). When ``SqsManagedSseEnabled`` is not defined, ``SSE-SQS`` encryption is enabled by default.</td></tr>
<tr><td><CopyableCode code="maximum_message_size" /></td><td><code>integer</code></td><td>The limit of how many bytes that a message can contain before SQS rejects it. You can specify an integer value from ``1,024`` bytes (1 KiB) to ``262,144`` bytes (256 KiB). The default value is ``262,144`` (256 KiB).</td></tr>
<tr><td><CopyableCode code="message_retention_period" /></td><td><code>integer</code></td><td>The number of seconds that SQS retains a message. You can specify an integer value from ``60`` seconds (1 minute) to ``1,209,600`` seconds (14 days). The default value is ``345,600`` seconds (4 days).</td></tr>
<tr><td><CopyableCode code="queue_name" /></td><td><code>string</code></td><td>A name for the queue. To create a FIFO queue, the name of your FIFO queue must end with the ``.fifo`` suffix. For more information, see &#91;FIFO queues&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;FIFO-queues.html) in the *Developer Guide*.&lt;br&#x2F;&gt; If you don't specify a name, CFN generates a unique physical ID and uses that ID for the queue name. For more information, see &#91;Name type&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html) in the *User Guide*. &lt;br&#x2F;&gt;  If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="receive_message_wait_time_seconds" /></td><td><code>integer</code></td><td>Specifies the duration, in seconds, that the ReceiveMessage action call waits until a message is in the queue in order to include it in the response, rather than returning an empty response if a message isn't yet available. You can specify an integer from 1 to 20. Short polling is used as the default or when you specify 0 for this property. For more information, see &#91;Consuming messages using long polling&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;sqs-short-and-long-polling.html#sqs-long-polling) in the *Developer Guide*.</td></tr>
<tr><td><CopyableCode code="redrive_allow_policy" /></td><td><code>object</code></td><td>The string that includes the parameters for the permissions for the dead-letter queue redrive permission and which source queues can specify dead-letter queues as a JSON object. The parameters are as follows:&lt;br&#x2F;&gt;  +  ``redrivePermission``: The permission type that defines which source queues can specify the current queue as the dead-letter queue. Valid values are:&lt;br&#x2F;&gt;  +  ``allowAll``: (Default) Any source queues in this AWS account in the same Region can specify this queue as the dead-letter queue.&lt;br&#x2F;&gt;  +  ``denyAll``: No source queues can specify this queue as the dead-letter queue.&lt;br&#x2F;&gt;  +  ``byQueue``: Only queues specified by the ``sourceQueueArns`` parameter can specify this queue as the dead-letter queue.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt;  +  ``sourceQueueArns``: The Amazon Resource Names (ARN)s of the source queues that can specify this queue as the dead-letter queue and redrive messages. You can specify this parameter only when the ``redrivePermission`` parameter is set to ``byQueue``. You can specify up to 10 source queue ARNs. To allow more than 10 source queues to specify dead-letter queues, set the ``redrivePermission`` parameter to ``allowAll``.</td></tr>
<tr><td><CopyableCode code="redrive_policy" /></td><td><code>object</code></td><td>The string that includes the parameters for the dead-letter queue functionality of the source queue as a JSON object. The parameters are as follows:&lt;br&#x2F;&gt;  +  ``deadLetterTargetArn``: The Amazon Resource Name (ARN) of the dead-letter queue to which SQS moves messages after the value of ``maxReceiveCount`` is exceeded.&lt;br&#x2F;&gt;  +  ``maxReceiveCount``: The number of times a message is delivered to the source queue before being moved to the dead-letter queue. When the ``ReceiveCount`` for a message exceeds the ``maxReceiveCount`` for a queue, SQS moves the message to the dead-letter-queue.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt;  The dead-letter queue of a FIFO queue must also be a FIFO queue. Similarly, the dead-letter queue of a standard queue must also be a standard queue.&lt;br&#x2F;&gt;   *JSON* &lt;br&#x2F;&gt;  ``&#123; "deadLetterTargetArn" : String, "maxReceiveCount" : Integer &#125;`` &lt;br&#x2F;&gt;  *YAML* &lt;br&#x2F;&gt;  ``deadLetterTargetArn : String`` &lt;br&#x2F;&gt;  ``maxReceiveCount : Integer``</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags that you attach to this queue. For more information, see &#91;Resource tag&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-resource-tags.html) in the *User Guide*.</td></tr>
<tr><td><CopyableCode code="visibility_timeout" /></td><td><code>integer</code></td><td>The length of time during which a message will be unavailable after a message is delivered from the queue. This blocks other components from receiving the same message and gives the initial component time to process and delete the message from the queue.&lt;br&#x2F;&gt; Values must be from 0 to 43,200 seconds (12 hours). If you don't specify a value, AWS CloudFormation uses the default value of 30 seconds.&lt;br&#x2F;&gt; For more information about SQS queue visibility timeouts, see &#91;Visibility timeout&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;sqs-visibility-timeout.html) in the *Developer Guide*.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.sqs.queue
WHERE data__Identifier = '<QueueUrl>';
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


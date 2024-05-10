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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>queues</code> in a region or to create or delete a <code>queues</code> resource, use <code>queue</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::SQS::Queue`` resource creates an SQS standard or FIFO queue.&lt;br&#x2F;&gt; Keep the following caveats in mind:&lt;br&#x2F;&gt;  +  If you don't specify the ``FifoQueue`` property, SQS creates a standard queue.&lt;br&#x2F;&gt;  You can't change the queue type after you create it and you can't convert an existing standard queue into a FIFO queue. You must either create a new FIFO queue for your application or delete your existing standard queue and recreate it as a FIFO queue. For more information, see &#91;Moving from a standard queue to a FIFO queue&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;FIFO-queues-moving.html) in the *Developer Guide*. &lt;br&#x2F;&gt;   +  If you don't provide a value for a property, the queue is created with the default value for the property.&lt;br&#x2F;&gt;  +  If you delete a queue, you must wait at least 60 seconds before creating a queue with the same name.&lt;br&#x2F;&gt;  +  To successfully create a new queue, you must provide a queue name that adheres to the &#91;limits related to queues&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;limits-queues.html) and is unique within the scope of your queues.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; For more information about creating FIFO (first-in-first-out) queues, see &#91;Creating an queue ()&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;screate-queue-cloudformation.html) in the *Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sqs.queues" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="queue_url" /></td><td><code>string</code></td><td></td></tr>
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
queue_url
FROM aws.sqs.queues
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>queue</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- queue.iql (required properties only)
INSERT INTO aws.sqs.queues (
 ContentBasedDeduplication,
 DeduplicationScope,
 DelaySeconds,
 FifoQueue,
 FifoThroughputLimit,
 KmsDataKeyReusePeriodSeconds,
 KmsMasterKeyId,
 SqsManagedSseEnabled,
 MaximumMessageSize,
 MessageRetentionPeriod,
 QueueName,
 ReceiveMessageWaitTimeSeconds,
 RedriveAllowPolicy,
 RedrivePolicy,
 Tags,
 VisibilityTimeout,
 region
)
SELECT 
'{{ ContentBasedDeduplication }}',
 '{{ DeduplicationScope }}',
 '{{ DelaySeconds }}',
 '{{ FifoQueue }}',
 '{{ FifoThroughputLimit }}',
 '{{ KmsDataKeyReusePeriodSeconds }}',
 '{{ KmsMasterKeyId }}',
 '{{ SqsManagedSseEnabled }}',
 '{{ MaximumMessageSize }}',
 '{{ MessageRetentionPeriod }}',
 '{{ QueueName }}',
 '{{ ReceiveMessageWaitTimeSeconds }}',
 '{{ RedriveAllowPolicy }}',
 '{{ RedrivePolicy }}',
 '{{ Tags }}',
 '{{ VisibilityTimeout }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- queue.iql (all properties)
INSERT INTO aws.sqs.queues (
 ContentBasedDeduplication,
 DeduplicationScope,
 DelaySeconds,
 FifoQueue,
 FifoThroughputLimit,
 KmsDataKeyReusePeriodSeconds,
 KmsMasterKeyId,
 SqsManagedSseEnabled,
 MaximumMessageSize,
 MessageRetentionPeriod,
 QueueName,
 ReceiveMessageWaitTimeSeconds,
 RedriveAllowPolicy,
 RedrivePolicy,
 Tags,
 VisibilityTimeout,
 region
)
SELECT 
 '{{ ContentBasedDeduplication }}',
 '{{ DeduplicationScope }}',
 '{{ DelaySeconds }}',
 '{{ FifoQueue }}',
 '{{ FifoThroughputLimit }}',
 '{{ KmsDataKeyReusePeriodSeconds }}',
 '{{ KmsMasterKeyId }}',
 '{{ SqsManagedSseEnabled }}',
 '{{ MaximumMessageSize }}',
 '{{ MessageRetentionPeriod }}',
 '{{ QueueName }}',
 '{{ ReceiveMessageWaitTimeSeconds }}',
 '{{ RedriveAllowPolicy }}',
 '{{ RedrivePolicy }}',
 '{{ Tags }}',
 '{{ VisibilityTimeout }}',
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
  - name: queue
    props:
      - name: ContentBasedDeduplication
        value: '{{ ContentBasedDeduplication }}'
      - name: DeduplicationScope
        value: '{{ DeduplicationScope }}'
      - name: DelaySeconds
        value: '{{ DelaySeconds }}'
      - name: FifoQueue
        value: '{{ FifoQueue }}'
      - name: FifoThroughputLimit
        value: '{{ FifoThroughputLimit }}'
      - name: KmsDataKeyReusePeriodSeconds
        value: '{{ KmsDataKeyReusePeriodSeconds }}'
      - name: KmsMasterKeyId
        value: '{{ KmsMasterKeyId }}'
      - name: SqsManagedSseEnabled
        value: '{{ SqsManagedSseEnabled }}'
      - name: MaximumMessageSize
        value: '{{ MaximumMessageSize }}'
      - name: MessageRetentionPeriod
        value: '{{ MessageRetentionPeriod }}'
      - name: QueueName
        value: '{{ QueueName }}'
      - name: ReceiveMessageWaitTimeSeconds
        value: '{{ ReceiveMessageWaitTimeSeconds }}'
      - name: RedriveAllowPolicy
        value: {}
      - name: RedrivePolicy
        value: {}
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: VisibilityTimeout
        value: '{{ VisibilityTimeout }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.sqs.queues
WHERE data__Identifier = '<QueueUrl>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>queues</code> resource, the following permissions are required:

### Create
```json
sqs:CreateQueue,
sqs:GetQueueUrl,
sqs:GetQueueAttributes,
sqs:ListQueueTags,
sqs:TagQueue
```

### Delete
```json
sqs:DeleteQueue,
sqs:GetQueueAttributes
```

### List
```json
sqs:ListQueues
```


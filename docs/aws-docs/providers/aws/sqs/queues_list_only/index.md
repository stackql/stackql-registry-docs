---
title: queues_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - queues_list_only
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

Lists <code>queues</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/queues/"><code>queues</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queues_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::SQS::Queue</code> resource creates an SQS standard or FIFO queue.<br />Keep the following caveats in mind:<br />+ If you don't specify the <code>FifoQueue</code> property, SQS creates a standard queue.<br />You can't change the queue type after you create it and you can't convert an existing standard queue into a FIFO queue. You must either create a new FIFO queue for your application or delete your existing standard queue and recreate it as a FIFO queue. For more information, see &#91;Moving from a standard queue to a FIFO queue&#93;(https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-moving.html) in the *Developer Guide*. <br />+ If you don't provide a value for a property, the queue is created with the default value for the property.<br />+ If you delete a queue, you must wait at least 60 seconds before creating a queue with the same name.<br />+ To successfully create a new queue, you must provide a queue name that adheres to the &#91;limits related to queues&#93;(https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/limits-queues.html) and is unique within the scope of your queues.<br /><br />For more information about creating FIFO (first-in-first-out) queues, see &#91;Creating an queue ()&#93;(https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/create-queue-cloudformation.html) in the *Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sqs.queues_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="queue_url" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>queues</code> in a region.
```sql
SELECT
region,
queue_url
FROM aws.sqs.queues_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>queues_list_only</code> resource, see <a href="/providers/aws/sqs/queues/#permissions"><code>queues</code></a>


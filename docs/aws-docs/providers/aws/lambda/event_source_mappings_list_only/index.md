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
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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


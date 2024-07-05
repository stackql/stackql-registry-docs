---
title: queues_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - queues_list_only
  - connect
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
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::Queue</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.queues_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the queue.</td></tr>
<tr><td><CopyableCode code="hours_of_operation_arn" /></td><td><code>string</code></td><td>The identifier for the hours of operation.</td></tr>
<tr><td><CopyableCode code="max_contacts" /></td><td><code>integer</code></td><td>The maximum number of contacts that can be in the queue before it is considered full.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the queue.</td></tr>
<tr><td><CopyableCode code="outbound_caller_config" /></td><td><code>object</code></td><td>The outbound caller ID name, number, and outbound whisper flow.</td></tr>
<tr><td><CopyableCode code="queue_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the queue.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the queue.</td></tr>
<tr><td><CopyableCode code="quick_connect_arns" /></td><td><code>array</code></td><td>The quick connects available to agents who are working the queue.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of queue.</td></tr>
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
queue_arn
FROM aws.connect.queues_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>queues_list_only</code> resource, see <a href="/providers/aws/connect/queues/#permissions"><code>queues</code></a>



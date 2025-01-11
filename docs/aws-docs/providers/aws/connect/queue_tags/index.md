---
title: queue_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - queue_tags
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

Expands all tag keys and values for <code>queues</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queue_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::Queue</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.queue_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the queue.</td></tr>
<tr><td><CopyableCode code="hours_of_operation_arn" /></td><td><code>string</code></td><td>The identifier for the hours of operation.</td></tr>
<tr><td><CopyableCode code="max_contacts" /></td><td><code>integer</code></td><td>The maximum number of contacts that can be in the queue before it is considered full.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the queue.</td></tr>
<tr><td><CopyableCode code="outbound_caller_config" /></td><td><code>object</code></td><td>The outbound caller ID name, number, and outbound whisper flow.</td></tr>
<tr><td><CopyableCode code="outbound_email_config" /></td><td><code>object</code></td><td>The outbound email address ID.</td></tr>
<tr><td><CopyableCode code="queue_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the queue.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the queue.</td></tr>
<tr><td><CopyableCode code="quick_connect_arns" /></td><td><code>array</code></td><td>The quick connects available to agents who are working the queue.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of queue.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>queues</code> in a region.
```sql
SELECT
region,
instance_arn,
description,
hours_of_operation_arn,
max_contacts,
name,
outbound_caller_config,
outbound_email_config,
queue_arn,
status,
quick_connect_arns,
type,
tag_key,
tag_value
FROM aws.connect.queue_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>queue_tags</code> resource, see <a href="/providers/aws/connect/queues/#permissions"><code>queues</code></a>


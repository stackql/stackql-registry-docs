---
title: queue_inline_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - queue_inline_policy
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


Gets or updates an individual <code>queue_inline_policy</code> resource, use <code>queue_inline_policies</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queue_inline_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for SQS QueueInlinePolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sqs.queue_inline_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="policy_document" /></td><td><code>object</code></td><td>A policy document that contains permissions to add to the specified SQS queue</td></tr>
<tr><td><CopyableCode code="queue" /></td><td><code>string</code></td><td>The URL of the SQS queue.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
policy_document,
queue
FROM aws.sqs.queue_inline_policy
WHERE region = 'us-east-1' AND data__Identifier = '<Queue>';
```


## Permissions

To operate on the <code>queue_inline_policy</code> resource, the following permissions are required:

### Read
```json
sqs:GetQueueAttributes,
sqs:GetQueueUrl
```

### Update
```json
sqs:SetQueueAttributes,
sqs:GetQueueAttributes,
sqs:GetQueueUrl
```


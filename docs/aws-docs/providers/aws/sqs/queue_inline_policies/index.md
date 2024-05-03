---
title: queue_inline_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - queue_inline_policies
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

Used to retrieve a list of <code>queue_inline_policies</code> in a region or create a <code>queue_inline_policies</code> resource, use <code>queue_inline_policy</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queue_inline_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for SQS QueueInlinePolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sqs.queue_inline_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
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
queue
FROM aws.sqs.queue_inline_policies
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>queue_inline_policies</code> resource, the following permissions are required:

### Create
```json
sqs:SetQueueAttributes,
sqs:GetQueueAttributes,
sqs:GetQueueUrl
```


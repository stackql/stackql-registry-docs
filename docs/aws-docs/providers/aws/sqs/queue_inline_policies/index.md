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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>queue_inline_policy</code> resource or lists <code>queue_inline_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queue_inline_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for SQS QueueInlinePolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sqs.queue_inline_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="policy_document" /></td><td><code>object</code></td><td>A policy document that contains permissions to add to the specified SQS queue</td></tr>
<tr><td><CopyableCode code="queue" /></td><td><code>string</code></td><td>The URL of the SQS queue.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queueinlinepolicy.html"><code>AWS::SQS::QueueInlinePolicy</code></a>.

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
    <td><CopyableCode code="PolicyDocument, Queue, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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

## `SELECT` examples

Gets all properties from an individual <code>queue_inline_policy</code>.
```sql
SELECT
region,
policy_document,
queue
FROM aws.sqs.queue_inline_policies
WHERE region = 'us-east-1' AND data__Identifier = '<Queue>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>queue_inline_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
INSERT INTO aws.sqs.queue_inline_policies (
 PolicyDocument,
 Queue,
 region
)
SELECT 
'{{ PolicyDocument }}',
 '{{ Queue }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sqs.queue_inline_policies (
 PolicyDocument,
 Queue,
 region
)
SELECT 
 '{{ PolicyDocument }}',
 '{{ Queue }}',
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
  - name: queue_inline_policy
    props:
      - name: PolicyDocument
        value: {}
      - name: Queue
        value: '{{ Queue }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sqs.queue_inline_policies
WHERE data__Identifier = '<Queue>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>queue_inline_policies</code> resource, the following permissions are required:

### Create
```json
sqs:SetQueueAttributes,
sqs:GetQueueAttributes,
sqs:GetQueueUrl
```

### Read
```json
sqs:GetQueueAttributes,
sqs:GetQueueUrl
```

### Delete
```json
sqs:SetQueueAttributes,
sqs:GetQueueAttributes
```

### Update
```json
sqs:SetQueueAttributes,
sqs:GetQueueAttributes,
sqs:GetQueueUrl
```

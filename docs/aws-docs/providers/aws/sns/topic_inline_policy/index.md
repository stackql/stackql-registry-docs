---
title: topic_inline_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - topic_inline_policy
  - sns
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

Gets or operates on an individual <code>topic_inline_policy</code> resource, use <code>topic_inline_policies</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic_inline_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for AWS::SNS::TopicInlinePolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sns.topic_inline_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="policy_document" /></td><td><code>object</code></td><td>A policy document that contains permissions to add to the specified SNS topics.</td></tr>
<tr><td><CopyableCode code="topic_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the topic to which you want to add the policy.</td></tr>
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
policy_document,
topic_arn
FROM aws.sns.topic_inline_policy
WHERE data__Identifier = '<TopicArn>';
```

## Permissions

To operate on the <code>topic_inline_policy</code> resource, the following permissions are required:

### Read
```json
sns:GetTopicAttributes
```

### Delete
```json
sns:SetTopicAttributes,
sns:GetTopicAttributes
```

### Update
```json
sns:SetTopicAttributes,
sns:GetTopicAttributes
```

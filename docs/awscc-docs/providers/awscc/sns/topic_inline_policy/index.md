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
Gets an individual <code>topic_inline_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic_inline_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>topic_inline_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sns.topic_inline_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>policy_document</code></td><td><code>object</code></td><td>A policy document that contains permissions to add to the specified SNS topics.</td></tr>
<tr><td><code>topic_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the topic to which you want to add the policy.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
policy_document,
topic_arn
FROM awscc.sns.topic_inline_policy
WHERE region = 'us-east-1'
AND data__Identifier = '{TopicArn}';
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


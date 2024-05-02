---
title: topic_inline_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - topic_inline_policies
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
Retrieves a list of <code>topic_inline_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic_inline_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for AWS::SNS::TopicInlinePolicy</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sns.topic_inline_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>topic_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the topic to which you want to add the policy.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
topic_arn
FROM aws.sns.topic_inline_policies
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>topic_inline_policies</code> resource, the following permissions are required:

### Create
```json
sns:SetTopicAttributes,
sns:GetTopicAttributes
```


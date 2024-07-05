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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>topic_inline_policy</code> resource or lists <code>topic_inline_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic_inline_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for AWS::SNS::TopicInlinePolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sns.topic_inline_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="policy_document" /></td><td><code>object</code></td><td>A policy document that contains permissions to add to the specified SNS topics.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="PolicyDocument, TopicArn, region" /></td>
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

Gets all properties from an individual <code>topic_inline_policy</code>.
```sql
SELECT
region,
policy_document,
topic_arn
FROM aws.sns.topic_inline_policies
WHERE region = 'us-east-1' AND data__Identifier = '<TopicArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>topic_inline_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sns.topic_inline_policies (
 PolicyDocument,
 TopicArn,
 region
)
SELECT 
'{{ PolicyDocument }}',
 '{{ TopicArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sns.topic_inline_policies (
 PolicyDocument,
 TopicArn,
 region
)
SELECT 
 '{{ PolicyDocument }}',
 '{{ TopicArn }}',
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
  - name: topic_inline_policy
    props:
      - name: PolicyDocument
        value: {}
      - name: TopicArn
        value: '{{ TopicArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sns.topic_inline_policies
WHERE data__Identifier = '<TopicArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>topic_inline_policies</code> resource, the following permissions are required:

### Create
```json
sns:SetTopicAttributes,
sns:GetTopicAttributes
```

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


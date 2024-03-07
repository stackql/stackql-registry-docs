---
title: topic_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - topic_policy
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
Gets an individual <code>topic_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>topic_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sns.topic_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The provider-assigned unique ID for this managed resource.</td></tr>
<tr><td><code>policy_document</code></td><td><code>object</code></td><td>A policy document that contains permissions to add to the specified SNS topics.</td></tr>
<tr><td><code>topics</code></td><td><code>array</code></td><td>The Amazon Resource Names (ARN) of the topics to which you want to add the policy. You can use the &#91;Ref&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;intrinsic-function-reference-ref.html)` function to specify an &#91;AWS::SNS::Topic&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-sns-topic.html) resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>topic_policy</code> resource, the following permissions are required:

### Update
```json
sns:SetTopicAttributes
```

### Delete
```json
sns:SetTopicAttributes
```


## Example
```sql
SELECT
region,
id,
policy_document,
topics
FROM awscc.sns.topic_policy
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```

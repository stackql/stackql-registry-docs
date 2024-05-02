---
title: topic
hide_title: false
hide_table_of_contents: false
keywords:
  - topic
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
Gets an individual <code>topic</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::SNS::Topic`` resource creates a topic to which notifications can be published.&lt;br&#x2F;&gt;  One account can create a maximum of 100,000 standard topics and 1,000 FIFO topics. For more information, see &#91;endpoints and quotas&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;general&#x2F;latest&#x2F;gr&#x2F;sns.html) in the *General Reference*.&lt;br&#x2F;&gt;   The structure of ``AUTHPARAMS`` depends on the .signature of the API request. For more information, see &#91;Examples of the complete Signature Version 4 signing process&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;general&#x2F;latest&#x2F;gr&#x2F;sigv4-signed-request-examples.html) in the *General Reference*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sns.topic</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td>The display name to use for an SNS topic with SMS subscriptions. The display name must be maximum 100 characters long, including hyphens (-), underscores (_), spaces, and tabs.</td></tr>
<tr><td><code>kms_master_key_id</code></td><td><code>string</code></td><td>The ID of an AWS managed customer master key (CMK) for SNS or a custom CMK. For more information, see &#91;Key terms&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;sns&#x2F;latest&#x2F;dg&#x2F;sns-server-side-encryption.html#sse-key-terms). For more examples, see ``KeyId`` in the *API Reference*.&lt;br&#x2F;&gt; This property applies only to &#91;server-side-encryption&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;sns&#x2F;latest&#x2F;dg&#x2F;sns-server-side-encryption.html).</td></tr>
<tr><td><code>data_protection_policy</code></td><td><code>object</code></td><td>The body of the policy document you want to use for this topic.&lt;br&#x2F;&gt; You can only add one policy per topic.&lt;br&#x2F;&gt; The policy must be in JSON string format.&lt;br&#x2F;&gt; Length Constraints: Maximum length of 30,720.</td></tr>
<tr><td><code>subscription</code></td><td><code>array</code></td><td>The SNS subscriptions (endpoints) for this topic.&lt;br&#x2F;&gt;  If you specify the ``Subscription`` property in the ``AWS::SNS::Topic`` resource and it creates an associated subscription resource, the associated subscription is not deleted when the ``AWS::SNS::Topic`` resource is deleted.</td></tr>
<tr><td><code>fifo_topic</code></td><td><code>boolean</code></td><td>Set to true to create a FIFO topic.</td></tr>
<tr><td><code>content_based_deduplication</code></td><td><code>boolean</code></td><td>Enables content-based deduplication for FIFO topics.&lt;br&#x2F;&gt;  +  By default, ``ContentBasedDeduplication`` is set to ``false``. If you create a FIFO topic and this attribute is ``false``, you must specify a value for the ``MessageDeduplicationId`` parameter for the &#91;Publish&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;sns&#x2F;latest&#x2F;api&#x2F;API_Publish.html) action. &lt;br&#x2F;&gt;  +  When you set ``ContentBasedDeduplication`` to ``true``, SNS uses a SHA-256 hash to generate the ``MessageDeduplicationId`` using the body of the message (but not the attributes of the message).&lt;br&#x2F;&gt; (Optional) To override the generated value, you can specify a value for the the ``MessageDeduplicationId`` parameter for the ``Publish`` action.</td></tr>
<tr><td><code>archive_policy</code></td><td><code>object</code></td><td>The archive policy determines the number of days SNS retains messages. You can set a retention period from 1 to 365 days.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The list of tags to add to a new topic.&lt;br&#x2F;&gt;  To be able to tag a topic on creation, you must have the ``sns:CreateTopic`` and ``sns:TagResource`` permissions.</td></tr>
<tr><td><code>topic_name</code></td><td><code>string</code></td><td>The name of the topic you want to create. Topic names must include only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long. FIFO topic names must end with ``.fifo``.&lt;br&#x2F;&gt; If you don't specify a name, CFN generates a unique physical ID and uses that ID for the topic name. For more information, see &#91;Name type&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html).&lt;br&#x2F;&gt;  If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><code>topic_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>signature_version</code></td><td><code>string</code></td><td>The signature version corresponds to the hashing algorithm used while creating the signature of the notifications, subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS. By default, ``SignatureVersion`` is set to ``1``.</td></tr>
<tr><td><code>tracing_config</code></td><td><code>string</code></td><td>Tracing mode of an SNS topic. By default ``TracingConfig`` is set to ``PassThrough``, and the topic passes through the tracing header it receives from an SNS publisher to its subscriptions. If set to ``Active``, SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true.</td></tr>
<tr><td><code>delivery_status_logging</code></td><td><code>array</code></td><td></td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
display_name,
kms_master_key_id,
data_protection_policy,
subscription,
fifo_topic,
content_based_deduplication,
archive_policy,
tags,
topic_name,
topic_arn,
signature_version,
tracing_config,
delivery_status_logging
FROM aws.sns.topic
WHERE data__Identifier = '<TopicArn>';
```

## Permissions

To operate on the <code>topic</code> resource, the following permissions are required:

### Read
```json
sns:GetTopicAttributes,
sns:ListTagsForResource,
sns:ListSubscriptionsByTopic,
sns:GetDataProtectionPolicy
```

### Update
```json
sns:SetTopicAttributes,
sns:TagResource,
sns:UntagResource,
sns:Subscribe,
sns:Unsubscribe,
sns:GetTopicAttributes,
sns:ListTagsForResource,
sns:ListSubscriptionsByTopic,
sns:GetDataProtectionPolicy,
sns:PutDataProtectionPolicy,
iam:GetRole,
iam:PassRole
```

### Delete
```json
sns:GetTopicAttributes,
sns:DeleteTopic
```


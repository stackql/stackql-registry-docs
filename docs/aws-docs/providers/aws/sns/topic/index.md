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
<tr><td><b>Description</b></td><td>topic</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sns.topic</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td>The display name to use for an Amazon SNS topic with SMS subscriptions.</td></tr>
<tr><td><code>kms_master_key_id</code></td><td><code>string</code></td><td>The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see Key Terms. For more examples, see KeyId in the AWS Key Management Service API Reference.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;This property applies only to &#91;server-side-encryption&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;sns&#x2F;latest&#x2F;dg&#x2F;sns-server-side-encryption.html).</td></tr>
<tr><td><code>data_protection_policy</code></td><td><code>object</code></td><td>The body of the policy document you want to use for this topic.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;You can only add one policy per topic.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;The policy must be in JSON string format.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Length Constraints: Maximum length of 30720</td></tr>
<tr><td><code>subscription</code></td><td><code>array</code></td><td>The SNS subscriptions (endpoints) for this topic.</td></tr>
<tr><td><code>fifo_topic</code></td><td><code>boolean</code></td><td>Set to true to create a FIFO topic.</td></tr>
<tr><td><code>content_based_deduplication</code></td><td><code>boolean</code></td><td>Enables content-based deduplication for FIFO topics. By default, ContentBasedDeduplication is set to false. If you create a FIFO topic and this attribute is false, you must specify a value for the MessageDeduplicationId parameter for the Publish action.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;When you set ContentBasedDeduplication to true, Amazon SNS uses a SHA-256 hash to generate the MessageDeduplicationId using the body of the message (but not the attributes of the message).&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;(Optional) To override the generated value, you can specify a value for the the MessageDeduplicationId parameter for the Publish action.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>topic_name</code></td><td><code>string</code></td><td>The name of the topic you want to create. Topic names must include only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long. FIFO topic names must end with .fifo.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the topic name. For more information, see Name Type.</td></tr>
<tr><td><code>topic_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>signature_version</code></td><td><code>string</code></td><td>Version of the Amazon SNS signature used. If the SignatureVersion is 1, Signature is a Base64-encoded SHA1withRSA signature of the Message, MessageId, Type, Timestamp, and TopicArn values. If the SignatureVersion is 2, Signature is a Base64-encoded SHA256withRSA signature of the Message, MessageId, Type, Timestamp, and TopicArn values.</td></tr>
<tr><td><code>tracing_config</code></td><td><code>string</code></td><td>Tracing mode of an Amazon SNS topic. By default TracingConfig is set to PassThrough, and the topic passes through the tracing header it receives from an SNS publisher to its subscriptions. If set to Active, SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true. Only supported on standard topics.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
display_name,
kms_master_key_id,
data_protection_policy,
subscription,
fifo_topic,
content_based_deduplication,
tags,
topic_name,
topic_arn,
signature_version,
tracing_config
FROM aws.sns.topic
WHERE region = 'us-east-1'
AND data__Identifier = '<TopicArn>'
```

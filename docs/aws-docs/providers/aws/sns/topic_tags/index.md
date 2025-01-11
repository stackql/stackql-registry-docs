---
title: topic_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - topic_tags
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

Expands all tag keys and values for <code>topics</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::SNS::Topic</code> resource creates a topic to which notifications can be published.<br />One account can create a maximum of 100,000 standard topics and 1,000 FIFO topics. For more information, see &#91;endpoints and quotas&#93;(https://docs.aws.amazon.com/general/latest/gr/sns.html) in the *General Reference*.<br />The structure of <code>AUTHPARAMS</code> depends on the .signature of the API request. For more information, see &#91;Examples of the complete Signature Version 4 signing process&#93;(https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the *General Reference*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sns.topic_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td>The display name to use for an SNS topic with SMS subscriptions. The display name must be maximum 100 characters long, including hyphens (-), underscores (_), spaces, and tabs.</td></tr>
<tr><td><CopyableCode code="kms_master_key_id" /></td><td><code>string</code></td><td>The ID of an AWS managed customer master key (CMK) for SNS or a custom CMK. For more information, see &#91;Key terms&#93;(https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms). For more examples, see <code>KeyId</code> in the *API Reference*.<br />This property applies only to &#91;server-side-encryption&#93;(https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html).</td></tr>
<tr><td><CopyableCode code="data_protection_policy" /></td><td><code>object</code></td><td>The body of the policy document you want to use for this topic.<br />You can only add one policy per topic.<br />The policy must be in JSON string format.<br />Length Constraints: Maximum length of 30,720.</td></tr>
<tr><td><CopyableCode code="subscription" /></td><td><code>array</code></td><td>The SNS subscriptions (endpoints) for this topic.<br />If you specify the <code>Subscription</code> property in the <code>AWS::SNS::Topic</code> resource and it creates an associated subscription resource, the associated subscription is not deleted when the <code>AWS::SNS::Topic</code> resource is deleted.</td></tr>
<tr><td><CopyableCode code="fifo_topic" /></td><td><code>boolean</code></td><td>Set to true to create a FIFO topic.</td></tr>
<tr><td><CopyableCode code="content_based_deduplication" /></td><td><code>boolean</code></td><td>Enables content-based deduplication for FIFO topics.<br />+ By default, <code>ContentBasedDeduplication</code> is set to <code>false</code>. If you create a FIFO topic and this attribute is <code>false</code>, you must specify a value for the <code>MessageDeduplicationId</code> parameter for the &#91;Publish&#93;(https://docs.aws.amazon.com/sns/latest/api/API_Publish.html) action. <br />+ When you set <code>ContentBasedDeduplication</code> to <code>true</code>, SNS uses a SHA-256 hash to generate the <code>MessageDeduplicationId</code> using the body of the message (but not the attributes of the message).<br />(Optional) To override the generated value, you can specify a value for the the <code>MessageDeduplicationId</code> parameter for the <code>Publish</code> action.</td></tr>
<tr><td><CopyableCode code="archive_policy" /></td><td><code>object</code></td><td>The archive policy determines the number of days SNS retains messages. You can set a retention period from 1 to 365 days.</td></tr>
<tr><td><CopyableCode code="topic_name" /></td><td><code>string</code></td><td>The name of the topic you want to create. Topic names must include only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long. FIFO topic names must end with <code>.fifo</code>.<br />If you don't specify a name, CFN generates a unique physical ID and uses that ID for the topic name. For more information, see &#91;Name type&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).<br />If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="topic_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="signature_version" /></td><td><code>string</code></td><td>The signature version corresponds to the hashing algorithm used while creating the signature of the notifications, subscription confirmations, or unsubscribe confirmation messages sent by Amazon SNS. By default, <code>SignatureVersion</code> is set to <code>1</code>.</td></tr>
<tr><td><CopyableCode code="tracing_config" /></td><td><code>string</code></td><td>Tracing mode of an SNS topic. By default <code>TracingConfig</code> is set to <code>PassThrough</code>, and the topic passes through the tracing header it receives from an SNS publisher to its subscriptions. If set to <code>Active</code>, SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true.</td></tr>
<tr><td><CopyableCode code="delivery_status_logging" /></td><td><code>array</code></td><td>The <code>DeliveryStatusLogging</code> configuration enables you to log the delivery status of messages sent from your Amazon SNS topic to subscribed endpoints with the following supported delivery protocols:<br />+ HTTP <br />+ Amazon Kinesis Data Firehose<br />+ AWS Lambda<br />+ Platform application endpoint<br />+ Amazon Simple Queue Service<br /><br />Once configured, log entries are sent to Amazon CloudWatch Logs.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>topics</code> in a region.
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
topic_name,
topic_arn,
signature_version,
tracing_config,
delivery_status_logging,
tag_key,
tag_value
FROM aws.sns.topic_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>topic_tags</code> resource, see <a href="/providers/aws/sns/topics/#permissions"><code>topics</code></a>


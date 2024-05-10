---
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
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


Used to retrieve a list of <code>topics</code> in a region or to create or delete a <code>topics</code> resource, use <code>topic</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::SNS::Topic`` resource creates a topic to which notifications can be published.&lt;br&#x2F;&gt;  One account can create a maximum of 100,000 standard topics and 1,000 FIFO topics. For more information, see &#91;endpoints and quotas&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;general&#x2F;latest&#x2F;gr&#x2F;sns.html) in the *General Reference*.&lt;br&#x2F;&gt;   The structure of ``AUTHPARAMS`` depends on the .signature of the API request. For more information, see &#91;Examples of the complete Signature Version 4 signing process&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;general&#x2F;latest&#x2F;gr&#x2F;sigv4-signed-request-examples.html) in the *General Reference*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sns.topics" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="topic_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
topic_arn
FROM aws.sns.topics
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>topic</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- topic.iql (required properties only)
INSERT INTO aws.sns.topics (
 DisplayName,
 KmsMasterKeyId,
 DataProtectionPolicy,
 Subscription,
 FifoTopic,
 ContentBasedDeduplication,
 ArchivePolicy,
 Tags,
 TopicName,
 SignatureVersion,
 TracingConfig,
 DeliveryStatusLogging,
 region
)
SELECT 
'{{ DisplayName }}',
 '{{ KmsMasterKeyId }}',
 '{{ DataProtectionPolicy }}',
 '{{ Subscription }}',
 '{{ FifoTopic }}',
 '{{ ContentBasedDeduplication }}',
 '{{ ArchivePolicy }}',
 '{{ Tags }}',
 '{{ TopicName }}',
 '{{ SignatureVersion }}',
 '{{ TracingConfig }}',
 '{{ DeliveryStatusLogging }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- topic.iql (all properties)
INSERT INTO aws.sns.topics (
 DisplayName,
 KmsMasterKeyId,
 DataProtectionPolicy,
 Subscription,
 FifoTopic,
 ContentBasedDeduplication,
 ArchivePolicy,
 Tags,
 TopicName,
 SignatureVersion,
 TracingConfig,
 DeliveryStatusLogging,
 region
)
SELECT 
 '{{ DisplayName }}',
 '{{ KmsMasterKeyId }}',
 '{{ DataProtectionPolicy }}',
 '{{ Subscription }}',
 '{{ FifoTopic }}',
 '{{ ContentBasedDeduplication }}',
 '{{ ArchivePolicy }}',
 '{{ Tags }}',
 '{{ TopicName }}',
 '{{ SignatureVersion }}',
 '{{ TracingConfig }}',
 '{{ DeliveryStatusLogging }}',
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
  - name: topic
    props:
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: KmsMasterKeyId
        value: '{{ KmsMasterKeyId }}'
      - name: DataProtectionPolicy
        value: {}
      - name: Subscription
        value:
          - Endpoint: '{{ Endpoint }}'
            Protocol: '{{ Protocol }}'
      - name: FifoTopic
        value: '{{ FifoTopic }}'
      - name: ContentBasedDeduplication
        value: '{{ ContentBasedDeduplication }}'
      - name: ArchivePolicy
        value: {}
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TopicName
        value: '{{ TopicName }}'
      - name: SignatureVersion
        value: '{{ SignatureVersion }}'
      - name: TracingConfig
        value: '{{ TracingConfig }}'
      - name: DeliveryStatusLogging
        value:
          - Protocol: '{{ Protocol }}'
            SuccessFeedbackRoleArn: '{{ SuccessFeedbackRoleArn }}'
            SuccessFeedbackSampleRate: '{{ SuccessFeedbackSampleRate }}'
            FailureFeedbackRoleArn: '{{ FailureFeedbackRoleArn }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.sns.topics
WHERE data__Identifier = '<TopicArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>topics</code> resource, the following permissions are required:

### Create
```json
sns:CreateTopic,
sns:TagResource,
sns:Subscribe,
sns:GetTopicAttributes,
sns:PutDataProtectionPolicy,
iam:GetRole,
iam:PassRole
```

### Delete
```json
sns:GetTopicAttributes,
sns:DeleteTopic
```

### List
```json
sns:ListTopics
```


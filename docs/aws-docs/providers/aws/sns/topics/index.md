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

Used to retrieve a list of <code>topics</code> in a region or create a <code>topics</code> resource, use <code>topic</code> to operate on an individual resource.

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
WHERE region = 'us-east-1'
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

### List
```json
sns:ListTopics
```


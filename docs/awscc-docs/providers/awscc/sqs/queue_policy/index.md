---
title: queue_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - queue_policy
  - sqs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>queue_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queue_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>queue_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sqs.queue_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy_document</code></td><td><code>object</code></td><td>A policy document that contains the permissions for the specified SQS queues. For more information about SQS policies, see &#91;Using custom policies with the access policy language&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSSimpleQueueService&#x2F;latest&#x2F;SQSDeveloperGuide&#x2F;sqs-creating-custom-policies.html) in the *Developer Guide*.</td></tr>
<tr><td><code>queues</code></td><td><code>array</code></td><td>The URLs of the queues to which you want to add the policy. You can use the ``Ref`` function to specify an ``AWS::SQS::Queue`` resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>queue_policy</code> resource, the following permissions are required:

### Update
```json
sqs:SetQueueAttributes
```

### Delete
```json
sqs:SetQueueAttributes
```


## Example
```sql
SELECT
region,
id,
policy_document,
queues
FROM awscc.sqs.queue_policy
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```

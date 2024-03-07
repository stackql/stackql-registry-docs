---
title: queue
hide_title: false
hide_table_of_contents: false
keywords:
  - queue
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>queue</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queue</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>queue</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.queue</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the queue.</td></tr>
<tr><td><code>hours_of_operation_arn</code></td><td><code>string</code></td><td>The identifier for the hours of operation.</td></tr>
<tr><td><code>max_contacts</code></td><td><code>integer</code></td><td>The maximum number of contacts that can be in the queue before it is considered full.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the queue.</td></tr>
<tr><td><code>outbound_caller_config</code></td><td><code>object</code></td><td>The outbound caller ID name, number, and outbound whisper flow.</td></tr>
<tr><td><code>queue_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the queue.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the queue.</td></tr>
<tr><td><code>quick_connect_arns</code></td><td><code>array</code></td><td>The quick connects available to agents who are working the queue.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of queue.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>queue</code> resource, the following permissions are required:

### Read
```json
connect:DescribeQueue,
connect:ListQueueQuickConnects
```

### Delete
```json
connect:DeleteQueue,
connect:UntagResource
```

### Update
```json
connect:UpdateQueueHoursOfOperation,
connect:UpdateQueueMaxContacts,
connect:UpdateQueueName,
connect:UpdateQueueOutboundCallerConfig,
connect:UpdateQueueStatus,
connect:AssociateQueueQuickConnects,
connect:DisassociateQueueQuickConnects,
connect:TagResource,
connect:UntagResource
```


## Example
```sql
SELECT
region,
instance_arn,
description,
hours_of_operation_arn,
max_contacts,
name,
outbound_caller_config,
queue_arn,
status,
quick_connect_arns,
tags,
type
FROM awscc.connect.queue
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;QueueArn&gt;'
```

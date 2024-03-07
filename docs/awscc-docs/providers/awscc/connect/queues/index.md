---
title: queues
hide_title: false
hide_table_of_contents: false
keywords:
  - queues
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
Retrieves a list of <code>queues</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>queues</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.queues</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>queue_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the queue.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>queues</code> resource, the following permissions are required:

### Create
<pre>
connect:CreateQueue,
connect:TagResource</pre>

### List
<pre>
connect:ListQueues,
connect:ListQueueQuickConnects</pre>


## Example
```sql
SELECT
region,
queue_arn
FROM awscc.connect.queues
WHERE region = 'us-east-1'
```

---
title: job_queue
hide_title: false
hide_table_of_contents: false
keywords:
  - job_queue
  - batch
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>job_queue</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_queue</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.batch.job_queue</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>JobQueueName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>JobQueueArn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ComputeEnvironmentOrder</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Priority</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>State</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SchedulingPolicyArn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.batch.job_queue
WHERE region = 'us-east-1' AND data__Identifier = '{JobQueueArn}'
```

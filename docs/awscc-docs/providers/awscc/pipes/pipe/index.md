---
title: pipe
hide_title: false
hide_table_of_contents: false
keywords:
  - pipe
  - pipes
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>pipe</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipe</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>pipe</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.pipes.pipe</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>current_state</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>desired_state</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enrichment</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enrichment_parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>last_modified_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>log_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>state_reason</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>target</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>target_parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>pipe</code> resource, the following permissions are required:

### Read
<pre>
pipes:DescribePipe</pre>

### Update
<pre>
pipes:UpdatePipe,
pipes:TagResource,
pipes:UntagResource,
pipes:DescribePipe,
iam:PassRole,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
iam:CreateServiceLinkedRole,
logs:CreateLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries,
s3:PutBucketPolicy,
s3:GetBucketPolicy,
firehose:TagDeliveryStream</pre>

### Delete
<pre>
pipes:DeletePipe,
pipes:DescribePipe,
logs:CreateLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries</pre>


## Example
```sql
SELECT
region,
arn,
creation_time,
current_state,
description,
desired_state,
enrichment,
enrichment_parameters,
last_modified_time,
log_configuration,
name,
role_arn,
source,
source_parameters,
state_reason,
tags,
target,
target_parameters
FROM awscc.pipes.pipe
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Name&gt;'
```

---
title: pipes
hide_title: false
hide_table_of_contents: false
keywords:
  - pipes
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
Retrieves a list of <code>pipes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>pipes</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.pipes.pipes</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>pipes</code> resource, the following permissions are required:

### Create
<pre>
pipes:CreatePipe,
pipes:DescribePipe,
pipes:TagResource,
iam:PassRole,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
iam:CreateServiceLinkedRole,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries,
s3:PutBucketPolicy,
s3:GetBucketPolicy,
firehose:TagDeliveryStream</pre>

### List
<pre>
pipes:ListPipes</pre>


## Example
```sql
SELECT
region,
name
FROM awscc.pipes.pipes
WHERE region = 'us-east-1'
```

---
title: resiliency_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - resiliency_policies
  - resiliencehub
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>resiliency_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resiliency_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resiliency_policies</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.resiliencehub.resiliency_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>policy_arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the Resiliency Policy.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>resiliency_policies</code> resource, the following permissions are required:

### Create
<pre>
resiliencehub:CreateResiliencyPolicy,
resiliencehub:DescribeResiliencyPolicy,
resiliencehub:TagResource</pre>

### List
<pre>
resiliencehub:ListResiliencyPolicies</pre>


## Example
```sql
SELECT
region,
policy_arn
FROM awscc.resiliencehub.resiliency_policies
WHERE region = 'us-east-1'
```

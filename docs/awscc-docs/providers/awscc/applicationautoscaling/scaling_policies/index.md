---
title: scaling_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - scaling_policies
  - applicationautoscaling
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>scaling_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>scaling_policies</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.applicationautoscaling.scaling_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>ARN is a read only property for the resource.</td></tr>
<tr><td><code>scalable_dimension</code></td><td><code>string</code></td><td>The scalable dimension. This string consists of the service namespace, resource type, and scaling property.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>scaling_policies</code> resource, the following permissions are required:

### Create
<pre>
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:PutScalingPolicy</pre>

### List
<pre>
application-autoscaling:DescribeScalingPolicies</pre>


## Example
```sql
SELECT
region,
arn,
scalable_dimension
FROM awscc.applicationautoscaling.scaling_policies
WHERE region = 'us-east-1'
```

---
title: scalable_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - scalable_targets
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
Retrieves a list of <code>scalable_targets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scalable_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>scalable_targets</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.applicationautoscaling.scalable_targets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td>The identifier of the resource associated with the scalable target</td></tr>
<tr><td><code>scalable_dimension</code></td><td><code>string</code></td><td>The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property</td></tr>
<tr><td><code>service_namespace</code></td><td><code>string</code></td><td>The namespace of the AWS service that provides the resource, or a custom-resource</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>scalable_targets</code> resource, the following permissions are required:

### Create
<pre>
application-autoscaling:DescribeScalableTargets,
application-autoscaling:RegisterScalableTarget,
application-autoscaling:DescribeScheduledActions,
application-autoscaling:PutScheduledAction,
iam:PassRole,
iam:CreateServiceLinkedRole,
cloudwatch:PutMetricAlarm,
cloudwatch:DeleteAlarms,
cloudwatch:DescribeAlarms,
lambda:GetProvisionedConcurrencyConfig,
lambda:PutProvisionedConcurrencyConfig,
lambda:DeleteProvisionedConcurrencyConfig</pre>

### List
<pre>
application-autoscaling:DescribeScalableTargets</pre>


## Example
```sql
SELECT
region,
resource_id,
scalable_dimension,
service_namespace
FROM awscc.applicationautoscaling.scalable_targets
WHERE region = 'us-east-1'
```

---
title: scaling_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - scaling_policy
  - autoscaling
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>scaling_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>scaling_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.autoscaling.scaling_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>metric_aggregation_type</code></td><td><code>string</code></td><td>The aggregation type for the CloudWatch metrics. The valid values are Minimum, Maximum, and Average. If the aggregation type is null, the value is treated as Average. Valid only if the policy type is StepScaling.</td></tr>
<tr><td><code>policy_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy_type</code></td><td><code>string</code></td><td>One of the following policy types: TargetTrackingScaling, StepScaling, SimpleScaling (default), PredictiveScaling</td></tr>
<tr><td><code>predictive_scaling_configuration</code></td><td><code>object</code></td><td>A predictive scaling policy. Includes support for predefined metrics only.</td></tr>
<tr><td><code>scaling_adjustment</code></td><td><code>integer</code></td><td>The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity. For exact capacity, you must specify a positive value. Required if the policy type is SimpleScaling. (Not used with any other policy type.)</td></tr>
<tr><td><code>cooldown</code></td><td><code>string</code></td><td>The duration of the policy's cooldown period, in seconds. When a cooldown period is specified here, it overrides the default cooldown period defined for the Auto Scaling group.</td></tr>
<tr><td><code>step_adjustments</code></td><td><code>array</code></td><td>A set of adjustments that enable you to scale based on the size of the alarm breach. Required if the policy type is StepScaling. (Not used with any other policy type.)</td></tr>
<tr><td><code>auto_scaling_group_name</code></td><td><code>string</code></td><td>The name of the Auto Scaling group.</td></tr>
<tr><td><code>min_adjustment_magnitude</code></td><td><code>integer</code></td><td>The minimum value to scale by when the adjustment type is PercentChangeInCapacity. For example, suppose that you create a step scaling policy to scale out an Auto Scaling group by 25 percent and you specify a MinAdjustmentMagnitude of 2. If the group has 4 instances and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a MinAdjustmentMagnitude of 2, Amazon EC2 Auto Scaling scales out the group by 2 instances.</td></tr>
<tr><td><code>target_tracking_configuration</code></td><td><code>object</code></td><td>A target tracking scaling policy. Includes support for predefined or customized metrics.</td></tr>
<tr><td><code>estimated_instance_warmup</code></td><td><code>integer</code></td><td>The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. If not provided, the default is to use the value from the default cooldown period for the Auto Scaling group. Valid only if the policy type is TargetTrackingScaling or StepScaling.</td></tr>
<tr><td><code>adjustment_type</code></td><td><code>string</code></td><td>Specifies how the scaling adjustment is interpreted. The valid values are ChangeInCapacity, ExactCapacity, and PercentChangeInCapacity.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the AutoScaling scaling policy</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
metric_aggregation_type,
policy_name,
policy_type,
predictive_scaling_configuration,
scaling_adjustment,
cooldown,
step_adjustments,
auto_scaling_group_name,
min_adjustment_magnitude,
target_tracking_configuration,
estimated_instance_warmup,
adjustment_type,
arn
FROM awscc.autoscaling.scaling_policy
WHERE region = 'us-east-1'
AND data__Identifier = '{Arn}';
```

## Permissions

To operate on the <code>scaling_policy</code> resource, the following permissions are required:

### Read
```json
autoscaling:DescribePolicies
```

### Update
```json
autoscaling:DescribePolicies,
autoscaling:PutScalingPolicy,
cloudwatch:GetMetricData
```

### Delete
```json
autoscaling:DeletePolicy,
autoscaling:DescribePolicies
```


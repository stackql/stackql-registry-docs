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
null
<tr><td><b>Id</b></td><td><code>aws.autoscaling.scaling_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>MetricAggregationType</code></td><td><code>string</code></td><td>The aggregation type for the CloudWatch metrics. The valid values are Minimum, Maximum, and Average. If the aggregation type is null, the value is treated as Average. Valid only if the policy type is StepScaling.</td></tr>
<tr><td><code>PolicyName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PolicyType</code></td><td><code>string</code></td><td>One of the following policy types: TargetTrackingScaling, StepScaling, SimpleScaling (default), PredictiveScaling</td></tr>
<tr><td><code>PredictiveScalingConfiguration</code></td><td><code>undefined</code></td><td>A predictive scaling policy. Includes support for predefined metrics only.</td></tr>
<tr><td><code>ScalingAdjustment</code></td><td><code>integer</code></td><td>The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity. For exact capacity, you must specify a positive value. Required if the policy type is SimpleScaling. (Not used with any other policy type.)</td></tr>
<tr><td><code>Cooldown</code></td><td><code>string</code></td><td>The duration of the policy's cooldown period, in seconds. When a cooldown period is specified here, it overrides the default cooldown period defined for the Auto Scaling group.</td></tr>
<tr><td><code>StepAdjustments</code></td><td><code>array</code></td><td>A set of adjustments that enable you to scale based on the size of the alarm breach. Required if the policy type is StepScaling. (Not used with any other policy type.)</td></tr>
<tr><td><code>AutoScalingGroupName</code></td><td><code>string</code></td><td>The name of the Auto Scaling group.</td></tr>
<tr><td><code>MinAdjustmentMagnitude</code></td><td><code>integer</code></td><td>The minimum value to scale by when the adjustment type is PercentChangeInCapacity. For example, suppose that you create a step scaling policy to scale out an Auto Scaling group by 25 percent and you specify a MinAdjustmentMagnitude of 2. If the group has 4 instances and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a MinAdjustmentMagnitude of 2, Amazon EC2 Auto Scaling scales out the group by 2 instances.</td></tr>
<tr><td><code>TargetTrackingConfiguration</code></td><td><code>undefined</code></td><td>A target tracking scaling policy. Includes support for predefined or customized metrics.</td></tr>
<tr><td><code>EstimatedInstanceWarmup</code></td><td><code>integer</code></td><td>The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. If not provided, the default is to use the value from the default cooldown period for the Auto Scaling group. Valid only if the policy type is TargetTrackingScaling or StepScaling.</td></tr>
<tr><td><code>AdjustmentType</code></td><td><code>string</code></td><td>Specifies how the scaling adjustment is interpreted. The valid values are ChangeInCapacity, ExactCapacity, and PercentChangeInCapacity.</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The ARN of the AutoScaling scaling policy</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.autoscaling.scaling_policy
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Arn&gt;'
</pre>

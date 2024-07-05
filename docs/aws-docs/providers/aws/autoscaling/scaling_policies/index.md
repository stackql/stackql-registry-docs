---
title: scaling_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - scaling_policies
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>scaling_policy</code> resource or lists <code>scaling_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AutoScaling::ScalingPolicy resource specifies an Amazon EC2 Auto Scaling scaling policy so that the Auto Scaling group can scale the number of instances available for your application.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.autoscaling.scaling_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="metric_aggregation_type" /></td><td><code>string</code></td><td>The aggregation type for the CloudWatch metrics. The valid values are Minimum, Maximum, and Average. If the aggregation type is null, the value is treated as Average. Valid only if the policy type is StepScaling.</td></tr>
<tr><td><CopyableCode code="policy_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_type" /></td><td><code>string</code></td><td>One of the following policy types: TargetTrackingScaling, StepScaling, SimpleScaling (default), PredictiveScaling</td></tr>
<tr><td><CopyableCode code="predictive_scaling_configuration" /></td><td><code>object</code></td><td>A predictive scaling policy. Includes support for predefined metrics only.</td></tr>
<tr><td><CopyableCode code="scaling_adjustment" /></td><td><code>integer</code></td><td>The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity. For exact capacity, you must specify a positive value. Required if the policy type is SimpleScaling. (Not used with any other policy type.)</td></tr>
<tr><td><CopyableCode code="cooldown" /></td><td><code>string</code></td><td>The duration of the policy's cooldown period, in seconds. When a cooldown period is specified here, it overrides the default cooldown period defined for the Auto Scaling group.</td></tr>
<tr><td><CopyableCode code="step_adjustments" /></td><td><code>array</code></td><td>A set of adjustments that enable you to scale based on the size of the alarm breach. Required if the policy type is StepScaling. (Not used with any other policy type.)</td></tr>
<tr><td><CopyableCode code="auto_scaling_group_name" /></td><td><code>string</code></td><td>The name of the Auto Scaling group.</td></tr>
<tr><td><CopyableCode code="min_adjustment_magnitude" /></td><td><code>integer</code></td><td>The minimum value to scale by when the adjustment type is PercentChangeInCapacity. For example, suppose that you create a step scaling policy to scale out an Auto Scaling group by 25 percent and you specify a MinAdjustmentMagnitude of 2. If the group has 4 instances and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a MinAdjustmentMagnitude of 2, Amazon EC2 Auto Scaling scales out the group by 2 instances.</td></tr>
<tr><td><CopyableCode code="target_tracking_configuration" /></td><td><code>object</code></td><td>A target tracking scaling policy. Includes support for predefined or customized metrics.</td></tr>
<tr><td><CopyableCode code="estimated_instance_warmup" /></td><td><code>integer</code></td><td>The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. If not provided, the default is to use the value from the default cooldown period for the Auto Scaling group. Valid only if the policy type is TargetTrackingScaling or StepScaling.</td></tr>
<tr><td><CopyableCode code="adjustment_type" /></td><td><code>string</code></td><td>Specifies how the scaling adjustment is interpreted. The valid values are ChangeInCapacity, ExactCapacity, and PercentChangeInCapacity.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the AutoScaling scaling policy</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="AutoScalingGroupName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>scaling_policies</code> in a region.
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
FROM aws.autoscaling.scaling_policies
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>scaling_policy</code>.
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
FROM aws.autoscaling.scaling_policies
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scaling_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.autoscaling.scaling_policies (
 AutoScalingGroupName,
 region
)
SELECT 
'{{ AutoScalingGroupName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.autoscaling.scaling_policies (
 MetricAggregationType,
 PolicyType,
 PredictiveScalingConfiguration,
 ScalingAdjustment,
 Cooldown,
 StepAdjustments,
 AutoScalingGroupName,
 MinAdjustmentMagnitude,
 TargetTrackingConfiguration,
 EstimatedInstanceWarmup,
 AdjustmentType,
 region
)
SELECT 
 '{{ MetricAggregationType }}',
 '{{ PolicyType }}',
 '{{ PredictiveScalingConfiguration }}',
 '{{ ScalingAdjustment }}',
 '{{ Cooldown }}',
 '{{ StepAdjustments }}',
 '{{ AutoScalingGroupName }}',
 '{{ MinAdjustmentMagnitude }}',
 '{{ TargetTrackingConfiguration }}',
 '{{ EstimatedInstanceWarmup }}',
 '{{ AdjustmentType }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: scaling_policy
    props:
      - name: MetricAggregationType
        value: '{{ MetricAggregationType }}'
      - name: PolicyType
        value: '{{ PolicyType }}'
      - name: PredictiveScalingConfiguration
        value:
          MetricSpecifications:
            - CustomizedCapacityMetricSpecification:
                MetricDataQueries:
                  - Label: '{{ Label }}'
                    MetricStat:
                      Metric:
                        MetricName: '{{ MetricName }}'
                        Dimensions:
                          - Value: '{{ Value }}'
                            Name: '{{ Name }}'
                        Namespace: '{{ Namespace }}'
                      Stat: '{{ Stat }}'
                      Unit: '{{ Unit }}'
                    Id: '{{ Id }}'
                    ReturnData: '{{ ReturnData }}'
                    Expression: '{{ Expression }}'
              CustomizedLoadMetricSpecification:
                MetricDataQueries:
                  - null
              CustomizedScalingMetricSpecification:
                MetricDataQueries:
                  - null
              PredefinedLoadMetricSpecification:
                ResourceLabel: '{{ ResourceLabel }}'
                PredefinedMetricType: '{{ PredefinedMetricType }}'
              TargetValue: null
              PredefinedScalingMetricSpecification:
                ResourceLabel: '{{ ResourceLabel }}'
                PredefinedMetricType: '{{ PredefinedMetricType }}'
              PredefinedMetricPairSpecification:
                ResourceLabel: '{{ ResourceLabel }}'
                PredefinedMetricType: '{{ PredefinedMetricType }}'
          MaxCapacityBreachBehavior: '{{ MaxCapacityBreachBehavior }}'
          MaxCapacityBuffer: '{{ MaxCapacityBuffer }}'
          SchedulingBufferTime: '{{ SchedulingBufferTime }}'
          Mode: '{{ Mode }}'
      - name: ScalingAdjustment
        value: '{{ ScalingAdjustment }}'
      - name: Cooldown
        value: '{{ Cooldown }}'
      - name: StepAdjustments
        value:
          - MetricIntervalUpperBound: null
            MetricIntervalLowerBound: null
            ScalingAdjustment: '{{ ScalingAdjustment }}'
      - name: AutoScalingGroupName
        value: '{{ AutoScalingGroupName }}'
      - name: MinAdjustmentMagnitude
        value: '{{ MinAdjustmentMagnitude }}'
      - name: TargetTrackingConfiguration
        value:
          CustomizedMetricSpecification:
            MetricName: '{{ MetricName }}'
            Dimensions:
              - null
            Statistic: '{{ Statistic }}'
            Unit: '{{ Unit }}'
            Namespace: '{{ Namespace }}'
          TargetValue: null
          DisableScaleIn: '{{ DisableScaleIn }}'
          PredefinedMetricSpecification:
            ResourceLabel: '{{ ResourceLabel }}'
            PredefinedMetricType: '{{ PredefinedMetricType }}'
      - name: EstimatedInstanceWarmup
        value: '{{ EstimatedInstanceWarmup }}'
      - name: AdjustmentType
        value: '{{ AdjustmentType }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.autoscaling.scaling_policies
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>scaling_policies</code> resource, the following permissions are required:

### Create
```json
autoscaling:DescribePolicies,
autoscaling:PutScalingPolicy,
cloudwatch:GetMetricData
```

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

### List
```json
autoscaling:DescribePolicies
```


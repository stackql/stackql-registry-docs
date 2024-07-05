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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>scaling_policy</code> resource or lists <code>scaling_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ApplicationAutoScaling::ScalingPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.applicationautoscaling.scaling_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="policy_name" /></td><td><code>string</code></td><td>The name of the scaling policy.<br />Updates to the name of a target tracking scaling policy are not supported, unless you also update the metric used for scaling. To change only a target tracking scaling policy's name, first delete the policy by removing the existing AWS::ApplicationAutoScaling::ScalingPolicy resource from the template and updating the stack. Then, recreate the resource with the same settings and a different name.</td></tr>
<tr><td><CopyableCode code="policy_type" /></td><td><code>string</code></td><td>The scaling policy type.<br />The following policy types are supported:<br />TargetTrackingScaling Not supported for Amazon EMR<br />StepScaling Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier.</td></tr>
<tr><td><CopyableCode code="scalable_dimension" /></td><td><code>string</code></td><td>The scalable dimension. This string consists of the service namespace, resource type, and scaling property.</td></tr>
<tr><td><CopyableCode code="scaling_target_id" /></td><td><code>string</code></td><td>The CloudFormation-generated ID of an Application Auto Scaling scalable target. For more information about the ID, see the Return Value section of the AWS::ApplicationAutoScaling::ScalableTarget resource.</td></tr>
<tr><td><CopyableCode code="service_namespace" /></td><td><code>string</code></td><td>The namespace of the AWS service that provides the resource, or a custom-resource.</td></tr>
<tr><td><CopyableCode code="step_scaling_policy_configuration" /></td><td><code>object</code></td><td>A step scaling policy.</td></tr>
<tr><td><CopyableCode code="target_tracking_scaling_policy_configuration" /></td><td><code>object</code></td><td>A target tracking scaling policy.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN is a read only property for the resource.</td></tr>
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
    <td><CopyableCode code="PolicyName, PolicyType, region" /></td>
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
policy_name,
policy_type,
resource_id,
scalable_dimension,
scaling_target_id,
service_namespace,
step_scaling_policy_configuration,
target_tracking_scaling_policy_configuration,
arn
FROM aws.applicationautoscaling.scaling_policies
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>scaling_policy</code>.
```sql
SELECT
region,
policy_name,
policy_type,
resource_id,
scalable_dimension,
scaling_target_id,
service_namespace,
step_scaling_policy_configuration,
target_tracking_scaling_policy_configuration,
arn
FROM aws.applicationautoscaling.scaling_policies
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>|<ScalableDimension>';
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
INSERT INTO aws.applicationautoscaling.scaling_policies (
 PolicyName,
 PolicyType,
 region
)
SELECT 
'{{ PolicyName }}',
 '{{ PolicyType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.applicationautoscaling.scaling_policies (
 PolicyName,
 PolicyType,
 ResourceId,
 ScalableDimension,
 ScalingTargetId,
 ServiceNamespace,
 StepScalingPolicyConfiguration,
 TargetTrackingScalingPolicyConfiguration,
 region
)
SELECT 
 '{{ PolicyName }}',
 '{{ PolicyType }}',
 '{{ ResourceId }}',
 '{{ ScalableDimension }}',
 '{{ ScalingTargetId }}',
 '{{ ServiceNamespace }}',
 '{{ StepScalingPolicyConfiguration }}',
 '{{ TargetTrackingScalingPolicyConfiguration }}',
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
      - name: PolicyName
        value: '{{ PolicyName }}'
      - name: PolicyType
        value: '{{ PolicyType }}'
      - name: ResourceId
        value: '{{ ResourceId }}'
      - name: ScalableDimension
        value: '{{ ScalableDimension }}'
      - name: ScalingTargetId
        value: '{{ ScalingTargetId }}'
      - name: ServiceNamespace
        value: '{{ ServiceNamespace }}'
      - name: StepScalingPolicyConfiguration
        value:
          AdjustmentType: '{{ AdjustmentType }}'
          Cooldown: '{{ Cooldown }}'
          MetricAggregationType: '{{ MetricAggregationType }}'
          MinAdjustmentMagnitude: '{{ MinAdjustmentMagnitude }}'
          StepAdjustments:
            - MetricIntervalLowerBound: null
              MetricIntervalUpperBound: null
              ScalingAdjustment: '{{ ScalingAdjustment }}'
      - name: TargetTrackingScalingPolicyConfiguration
        value:
          CustomizedMetricSpecification:
            Dimensions:
              - Name: '{{ Name }}'
                Value: '{{ Value }}'
            MetricName: '{{ MetricName }}'
            Namespace: '{{ Namespace }}'
            Statistic: '{{ Statistic }}'
            Unit: '{{ Unit }}'
            Metrics:
              - Expression: '{{ Expression }}'
                Id: '{{ Id }}'
                Label: '{{ Label }}'
                ReturnData: '{{ ReturnData }}'
                MetricStat:
                  Metric:
                    Dimensions:
                      - Name: '{{ Name }}'
                        Value: '{{ Value }}'
                    MetricName: '{{ MetricName }}'
                    Namespace: '{{ Namespace }}'
                  Stat: '{{ Stat }}'
                  Unit: '{{ Unit }}'
          DisableScaleIn: '{{ DisableScaleIn }}'
          PredefinedMetricSpecification:
            PredefinedMetricType: '{{ PredefinedMetricType }}'
            ResourceLabel: '{{ ResourceLabel }}'
          ScaleInCooldown: '{{ ScaleInCooldown }}'
          ScaleOutCooldown: '{{ ScaleOutCooldown }}'
          TargetValue: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.applicationautoscaling.scaling_policies
WHERE data__Identifier = '<Arn|ScalableDimension>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>scaling_policies</code> resource, the following permissions are required:

### Create
```json
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:PutScalingPolicy
```

### Read
```json
application-autoscaling:DescribeScalingPolicies
```

### Update
```json
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:PutScalingPolicy
```

### Delete
```json
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:DeleteScalingPolicy
```

### List
```json
application-autoscaling:DescribeScalingPolicies
```


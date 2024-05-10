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


Used to retrieve a list of <code>scaling_policies</code> in a region or to create or delete a <code>scaling_policies</code> resource, use <code>scaling_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AutoScaling::ScalingPolicy resource specifies an Amazon EC2 Auto Scaling scaling policy so that the Auto Scaling group can scale the number of instances available for your application.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.autoscaling.scaling_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.autoscaling.scaling_policies
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "AutoScalingGroupName": "{{ AutoScalingGroupName }}"
}
>>>
--required properties only
INSERT INTO aws.autoscaling.scaling_policies (
 AutoScalingGroupName,
 region
)
SELECT 
{{ AutoScalingGroupName }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "MetricAggregationType": "{{ MetricAggregationType }}",
 "PolicyType": "{{ PolicyType }}",
 "PredictiveScalingConfiguration": {
  "MetricSpecifications": [
   {
    "CustomizedCapacityMetricSpecification": {
     "MetricDataQueries": [
      {
       "Label": "{{ Label }}",
       "MetricStat": {
        "Metric": {
         "MetricName": "{{ MetricName }}",
         "Dimensions": [
          {
           "Value": "{{ Value }}",
           "Name": "{{ Name }}"
          }
         ],
         "Namespace": "{{ Namespace }}"
        },
        "Stat": "{{ Stat }}",
        "Unit": "{{ Unit }}"
       },
       "Id": "{{ Id }}",
       "ReturnData": "{{ ReturnData }}",
       "Expression": "{{ Expression }}"
      }
     ]
    },
    "CustomizedLoadMetricSpecification": {
     "MetricDataQueries": [
      null
     ]
    },
    "CustomizedScalingMetricSpecification": {
     "MetricDataQueries": [
      null
     ]
    },
    "PredefinedLoadMetricSpecification": {
     "ResourceLabel": "{{ ResourceLabel }}",
     "PredefinedMetricType": "{{ PredefinedMetricType }}"
    },
    "TargetValue": null,
    "PredefinedScalingMetricSpecification": {
     "ResourceLabel": "{{ ResourceLabel }}",
     "PredefinedMetricType": "{{ PredefinedMetricType }}"
    },
    "PredefinedMetricPairSpecification": {
     "ResourceLabel": "{{ ResourceLabel }}",
     "PredefinedMetricType": "{{ PredefinedMetricType }}"
    }
   }
  ],
  "MaxCapacityBreachBehavior": "{{ MaxCapacityBreachBehavior }}",
  "MaxCapacityBuffer": "{{ MaxCapacityBuffer }}",
  "SchedulingBufferTime": "{{ SchedulingBufferTime }}",
  "Mode": "{{ Mode }}"
 },
 "ScalingAdjustment": "{{ ScalingAdjustment }}",
 "Cooldown": "{{ Cooldown }}",
 "StepAdjustments": [
  {
   "MetricIntervalUpperBound": null,
   "MetricIntervalLowerBound": null,
   "ScalingAdjustment": "{{ ScalingAdjustment }}"
  }
 ],
 "AutoScalingGroupName": "{{ AutoScalingGroupName }}",
 "MinAdjustmentMagnitude": "{{ MinAdjustmentMagnitude }}",
 "TargetTrackingConfiguration": {
  "CustomizedMetricSpecification": {
   "MetricName": "{{ MetricName }}",
   "Dimensions": [
    null
   ],
   "Statistic": "{{ Statistic }}",
   "Unit": "{{ Unit }}",
   "Namespace": "{{ Namespace }}"
  },
  "TargetValue": null,
  "DisableScaleIn": "{{ DisableScaleIn }}",
  "PredefinedMetricSpecification": {
   "ResourceLabel": "{{ ResourceLabel }}",
   "PredefinedMetricType": "{{ PredefinedMetricType }}"
  }
 },
 "EstimatedInstanceWarmup": "{{ EstimatedInstanceWarmup }}",
 "AdjustmentType": "{{ AdjustmentType }}"
}
>>>
--all properties
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
 {{ MetricAggregationType }},
 {{ PolicyType }},
 {{ PredictiveScalingConfiguration }},
 {{ ScalingAdjustment }},
 {{ Cooldown }},
 {{ StepAdjustments }},
 {{ AutoScalingGroupName }},
 {{ MinAdjustmentMagnitude }},
 {{ TargetTrackingConfiguration }},
 {{ EstimatedInstanceWarmup }},
 {{ AdjustmentType }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
autoscaling:DeletePolicy,
autoscaling:DescribePolicies
```

### List
```json
autoscaling:DescribePolicies
```


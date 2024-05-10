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


Used to retrieve a list of <code>scaling_policies</code> in a region or to create or delete a <code>scaling_policies</code> resource, use <code>scaling_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ApplicationAutoScaling::ScalingPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.applicationautoscaling.scaling_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN is a read only property for the resource.</td></tr>
<tr><td><CopyableCode code="scalable_dimension" /></td><td><code>string</code></td><td>The scalable dimension. This string consists of the service namespace, resource type, and scaling property.</td></tr>
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
arn,
scalable_dimension
FROM aws.applicationautoscaling.scaling_policies
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
 "PolicyName": "{{ PolicyName }}",
 "PolicyType": "{{ PolicyType }}"
}
>>>
--required properties only
INSERT INTO aws.applicationautoscaling.scaling_policies (
 PolicyName,
 PolicyType,
 region
)
SELECT 
{{ PolicyName }},
 {{ PolicyType }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "PolicyName": "{{ PolicyName }}",
 "PolicyType": "{{ PolicyType }}",
 "ResourceId": "{{ ResourceId }}",
 "ScalableDimension": "{{ ScalableDimension }}",
 "ScalingTargetId": "{{ ScalingTargetId }}",
 "ServiceNamespace": "{{ ServiceNamespace }}",
 "StepScalingPolicyConfiguration": {
  "AdjustmentType": "{{ AdjustmentType }}",
  "Cooldown": "{{ Cooldown }}",
  "MetricAggregationType": "{{ MetricAggregationType }}",
  "MinAdjustmentMagnitude": "{{ MinAdjustmentMagnitude }}",
  "StepAdjustments": [
   {
    "MetricIntervalLowerBound": null,
    "MetricIntervalUpperBound": null,
    "ScalingAdjustment": "{{ ScalingAdjustment }}"
   }
  ]
 },
 "TargetTrackingScalingPolicyConfiguration": {
  "CustomizedMetricSpecification": {
   "Dimensions": [
    {
     "Name": "{{ Name }}",
     "Value": "{{ Value }}"
    }
   ],
   "MetricName": "{{ MetricName }}",
   "Namespace": "{{ Namespace }}",
   "Statistic": "{{ Statistic }}",
   "Unit": "{{ Unit }}",
   "Metrics": [
    {
     "Expression": "{{ Expression }}",
     "Id": "{{ Id }}",
     "Label": "{{ Label }}",
     "ReturnData": "{{ ReturnData }}",
     "MetricStat": {
      "Metric": {
       "Dimensions": [
        {
         "Name": "{{ Name }}",
         "Value": "{{ Value }}"
        }
       ],
       "MetricName": "{{ MetricName }}",
       "Namespace": "{{ Namespace }}"
      },
      "Stat": "{{ Stat }}",
      "Unit": "{{ Unit }}"
     }
    }
   ]
  },
  "DisableScaleIn": "{{ DisableScaleIn }}",
  "PredefinedMetricSpecification": {
   "PredefinedMetricType": "{{ PredefinedMetricType }}",
   "ResourceLabel": "{{ ResourceLabel }}"
  },
  "ScaleInCooldown": "{{ ScaleInCooldown }}",
  "ScaleOutCooldown": "{{ ScaleOutCooldown }}",
  "TargetValue": null
 }
}
>>>
--all properties
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
 {{ PolicyName }},
 {{ PolicyType }},
 {{ ResourceId }},
 {{ ScalableDimension }},
 {{ ScalingTargetId }},
 {{ ServiceNamespace }},
 {{ StepScalingPolicyConfiguration }},
 {{ TargetTrackingScalingPolicyConfiguration }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:DeleteScalingPolicy
```

### List
```json
application-autoscaling:DescribeScalingPolicies
```


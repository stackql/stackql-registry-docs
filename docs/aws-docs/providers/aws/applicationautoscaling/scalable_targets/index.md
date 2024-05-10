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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>scalable_targets</code> in a region or to create or delete a <code>scalable_targets</code> resource, use <code>scalable_target</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scalable_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ApplicationAutoScaling::ScalableTarget</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.applicationautoscaling.scalable_targets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>The identifier of the resource associated with the scalable target</td></tr>
<tr><td><CopyableCode code="scalable_dimension" /></td><td><code>string</code></td><td>The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property</td></tr>
<tr><td><CopyableCode code="service_namespace" /></td><td><code>string</code></td><td>The namespace of the AWS service that provides the resource, or a custom-resource</td></tr>
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
resource_id,
scalable_dimension,
service_namespace
FROM aws.applicationautoscaling.scalable_targets
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
 "MaxCapacity": "{{ MaxCapacity }}",
 "MinCapacity": "{{ MinCapacity }}",
 "ResourceId": "{{ ResourceId }}",
 "ScalableDimension": "{{ ScalableDimension }}",
 "ServiceNamespace": "{{ ServiceNamespace }}"
}
>>>
--required properties only
INSERT INTO aws.applicationautoscaling.scalable_targets (
 MaxCapacity,
 MinCapacity,
 ResourceId,
 ScalableDimension,
 ServiceNamespace,
 region
)
SELECT 
{{ .MaxCapacity }},
 {{ .MinCapacity }},
 {{ .ResourceId }},
 {{ .ScalableDimension }},
 {{ .ServiceNamespace }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "MaxCapacity": "{{ MaxCapacity }}",
 "MinCapacity": "{{ MinCapacity }}",
 "ResourceId": "{{ ResourceId }}",
 "RoleARN": "{{ RoleARN }}",
 "ScalableDimension": "{{ ScalableDimension }}",
 "ScheduledActions": [
  {
   "Timezone": "{{ Timezone }}",
   "ScheduledActionName": "{{ ScheduledActionName }}",
   "EndTime": "{{ EndTime }}",
   "Schedule": "{{ Schedule }}",
   "StartTime": "{{ StartTime }}",
   "ScalableTargetAction": {
    "MinCapacity": "{{ MinCapacity }}",
    "MaxCapacity": "{{ MaxCapacity }}"
   }
  }
 ],
 "ServiceNamespace": "{{ ServiceNamespace }}",
 "SuspendedState": {
  "ScheduledScalingSuspended": "{{ ScheduledScalingSuspended }}",
  "DynamicScalingOutSuspended": "{{ DynamicScalingOutSuspended }}",
  "DynamicScalingInSuspended": "{{ DynamicScalingInSuspended }}"
 }
}
>>>
--all properties
INSERT INTO aws.applicationautoscaling.scalable_targets (
 MaxCapacity,
 MinCapacity,
 ResourceId,
 RoleARN,
 ScalableDimension,
 ScheduledActions,
 ServiceNamespace,
 SuspendedState,
 region
)
SELECT 
 {{ .MaxCapacity }},
 {{ .MinCapacity }},
 {{ .ResourceId }},
 {{ .RoleARN }},
 {{ .ScalableDimension }},
 {{ .ScheduledActions }},
 {{ .ServiceNamespace }},
 {{ .SuspendedState }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.applicationautoscaling.scalable_targets
WHERE data__Identifier = '<ResourceId|ScalableDimension|ServiceNamespace>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>scalable_targets</code> resource, the following permissions are required:

### Create
```json
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
lambda:DeleteProvisionedConcurrencyConfig
```

### List
```json
application-autoscaling:DescribeScalableTargets
```

### Delete
```json
application-autoscaling:DeregisterScalableTarget
```


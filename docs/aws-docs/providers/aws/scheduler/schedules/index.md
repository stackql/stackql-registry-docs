---
title: schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - schedules
  - scheduler
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


Used to retrieve a list of <code>schedules</code> in a region or to create or delete a <code>schedules</code> resource, use <code>schedule</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Scheduler::Schedule Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.scheduler.schedules" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
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
name
FROM aws.scheduler.schedules
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
 "FlexibleTimeWindow": {
  "Mode": "{{ Mode }}",
  "MaximumWindowInMinutes": null
 },
 "ScheduleExpression": "{{ ScheduleExpression }}",
 "Target": {
  "Arn": "{{ Arn }}",
  "RoleArn": "{{ RoleArn }}",
  "DeadLetterConfig": {
   "Arn": "{{ Arn }}"
  },
  "RetryPolicy": {
   "MaximumEventAgeInSeconds": null,
   "MaximumRetryAttempts": null
  },
  "Input": "{{ Input }}",
  "EcsParameters": {
   "TaskDefinitionArn": "{{ TaskDefinitionArn }}",
   "TaskCount": null,
   "LaunchType": "{{ LaunchType }}",
   "NetworkConfiguration": {
    "AwsvpcConfiguration": {
     "Subnets": [
      "{{ Subnets[0] }}"
     ],
     "SecurityGroups": [
      "{{ SecurityGroups[0] }}"
     ],
     "AssignPublicIp": "{{ AssignPublicIp }}"
    }
   },
   "PlatformVersion": "{{ PlatformVersion }}",
   "Group": "{{ Group }}",
   "CapacityProviderStrategy": [
    {
     "CapacityProvider": "{{ CapacityProvider }}",
     "Weight": null,
     "Base": null
    }
   ],
   "EnableECSManagedTags": "{{ EnableECSManagedTags }}",
   "EnableExecuteCommand": "{{ EnableExecuteCommand }}",
   "PlacementConstraints": [
    {
     "Type": "{{ Type }}",
     "Expression": "{{ Expression }}"
    }
   ],
   "PlacementStrategy": [
    {
     "Type": "{{ Type }}",
     "Field": "{{ Field }}"
    }
   ],
   "PropagateTags": "{{ PropagateTags }}",
   "ReferenceId": "{{ ReferenceId }}",
   "Tags": [
    {}
   ]
  },
  "EventBridgeParameters": {
   "DetailType": "{{ DetailType }}",
   "Source": "{{ Source }}"
  },
  "KinesisParameters": {
   "PartitionKey": "{{ PartitionKey }}"
  },
  "SageMakerPipelineParameters": {
   "PipelineParameterList": [
    {
     "Name": "{{ Name }}",
     "Value": "{{ Value }}"
    }
   ]
  },
  "SqsParameters": {
   "MessageGroupId": "{{ MessageGroupId }}"
  }
 }
}
>>>
--required properties only
INSERT INTO aws.scheduler.schedules (
 FlexibleTimeWindow,
 ScheduleExpression,
 Target,
 region
)
SELECT 
{{ .FlexibleTimeWindow }},
 {{ .ScheduleExpression }},
 {{ .Target }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "EndDate": "{{ EndDate }}",
 "FlexibleTimeWindow": {
  "Mode": "{{ Mode }}",
  "MaximumWindowInMinutes": null
 },
 "GroupName": "{{ GroupName }}",
 "KmsKeyArn": "{{ KmsKeyArn }}",
 "Name": "{{ Name }}",
 "ScheduleExpression": "{{ ScheduleExpression }}",
 "ScheduleExpressionTimezone": "{{ ScheduleExpressionTimezone }}",
 "StartDate": "{{ StartDate }}",
 "State": "{{ State }}",
 "Target": {
  "Arn": "{{ Arn }}",
  "RoleArn": "{{ RoleArn }}",
  "DeadLetterConfig": {
   "Arn": "{{ Arn }}"
  },
  "RetryPolicy": {
   "MaximumEventAgeInSeconds": null,
   "MaximumRetryAttempts": null
  },
  "Input": "{{ Input }}",
  "EcsParameters": {
   "TaskDefinitionArn": "{{ TaskDefinitionArn }}",
   "TaskCount": null,
   "LaunchType": "{{ LaunchType }}",
   "NetworkConfiguration": {
    "AwsvpcConfiguration": {
     "Subnets": [
      "{{ Subnets[0] }}"
     ],
     "SecurityGroups": [
      "{{ SecurityGroups[0] }}"
     ],
     "AssignPublicIp": "{{ AssignPublicIp }}"
    }
   },
   "PlatformVersion": "{{ PlatformVersion }}",
   "Group": "{{ Group }}",
   "CapacityProviderStrategy": [
    {
     "CapacityProvider": "{{ CapacityProvider }}",
     "Weight": null,
     "Base": null
    }
   ],
   "EnableECSManagedTags": "{{ EnableECSManagedTags }}",
   "EnableExecuteCommand": "{{ EnableExecuteCommand }}",
   "PlacementConstraints": [
    {
     "Type": "{{ Type }}",
     "Expression": "{{ Expression }}"
    }
   ],
   "PlacementStrategy": [
    {
     "Type": "{{ Type }}",
     "Field": "{{ Field }}"
    }
   ],
   "PropagateTags": "{{ PropagateTags }}",
   "ReferenceId": "{{ ReferenceId }}",
   "Tags": [
    {}
   ]
  },
  "EventBridgeParameters": {
   "DetailType": "{{ DetailType }}",
   "Source": "{{ Source }}"
  },
  "KinesisParameters": {
   "PartitionKey": "{{ PartitionKey }}"
  },
  "SageMakerPipelineParameters": {
   "PipelineParameterList": [
    {
     "Name": "{{ Name }}",
     "Value": "{{ Value }}"
    }
   ]
  },
  "SqsParameters": {
   "MessageGroupId": "{{ MessageGroupId }}"
  }
 }
}
>>>
--all properties
INSERT INTO aws.scheduler.schedules (
 Description,
 EndDate,
 FlexibleTimeWindow,
 GroupName,
 KmsKeyArn,
 Name,
 ScheduleExpression,
 ScheduleExpressionTimezone,
 StartDate,
 State,
 Target,
 region
)
SELECT 
 {{ .Description }},
 {{ .EndDate }},
 {{ .FlexibleTimeWindow }},
 {{ .GroupName }},
 {{ .KmsKeyArn }},
 {{ .Name }},
 {{ .ScheduleExpression }},
 {{ .ScheduleExpressionTimezone }},
 {{ .StartDate }},
 {{ .State }},
 {{ .Target }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.scheduler.schedules
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>schedules</code> resource, the following permissions are required:

### Create
```json
scheduler:CreateSchedule,
scheduler:GetSchedule,
iam:PassRole
```

### Delete
```json
scheduler:DeleteSchedule,
scheduler:GetSchedule
```

### List
```json
scheduler:ListSchedules
```


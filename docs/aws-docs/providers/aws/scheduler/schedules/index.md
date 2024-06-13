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

Creates, updates, deletes or gets a <code>schedule</code> resource or lists <code>schedules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Scheduler::Schedule Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.scheduler.schedules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the schedule.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the schedule.</td></tr>
<tr><td><CopyableCode code="end_date" /></td><td><code>string</code></td><td>The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the EndDate you specify.</td></tr>
<tr><td><CopyableCode code="flexible_time_window" /></td><td><code>object</code></td><td>Flexible time window allows configuration of a window within which a schedule can be invoked</td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td>The name of the schedule group to associate with this schedule. If you omit this, the default schedule group is used.</td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td>The ARN for a KMS Key that will be used to encrypt customer data.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="schedule_expression" /></td><td><code>string</code></td><td>The scheduling expression.</td></tr>
<tr><td><CopyableCode code="schedule_expression_timezone" /></td><td><code>string</code></td><td>The timezone in which the scheduling expression is evaluated.</td></tr>
<tr><td><CopyableCode code="start_date" /></td><td><code>string</code></td><td>The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the StartDate you specify.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>Specifies whether the schedule is enabled or disabled.</td></tr>
<tr><td><CopyableCode code="target" /></td><td><code>object</code></td><td>The schedule target.</td></tr>
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
    <td><CopyableCode code="FlexibleTimeWindow, ScheduleExpression, Target, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>schedules</code> in a region.
```sql
SELECT
region,
name
FROM aws.scheduler.schedules
WHERE region = 'us-east-1';
```
Gets all properties from a <code>schedule</code>.
```sql
SELECT
region,
arn,
description,
end_date,
flexible_time_window,
group_name,
kms_key_arn,
name,
schedule_expression,
schedule_expression_timezone,
start_date,
state,
target
FROM aws.scheduler.schedules
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>schedule</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.scheduler.schedules (
 FlexibleTimeWindow,
 ScheduleExpression,
 Target,
 region
)
SELECT 
'{{ FlexibleTimeWindow }}',
 '{{ ScheduleExpression }}',
 '{{ Target }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ Description }}',
 '{{ EndDate }}',
 '{{ FlexibleTimeWindow }}',
 '{{ GroupName }}',
 '{{ KmsKeyArn }}',
 '{{ Name }}',
 '{{ ScheduleExpression }}',
 '{{ ScheduleExpressionTimezone }}',
 '{{ StartDate }}',
 '{{ State }}',
 '{{ Target }}',
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
  - name: schedule
    props:
      - name: Description
        value: '{{ Description }}'
      - name: EndDate
        value: '{{ EndDate }}'
      - name: FlexibleTimeWindow
        value:
          Mode: '{{ Mode }}'
          MaximumWindowInMinutes: null
      - name: GroupName
        value: '{{ GroupName }}'
      - name: KmsKeyArn
        value: '{{ KmsKeyArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: ScheduleExpression
        value: '{{ ScheduleExpression }}'
      - name: ScheduleExpressionTimezone
        value: '{{ ScheduleExpressionTimezone }}'
      - name: StartDate
        value: '{{ StartDate }}'
      - name: State
        value: '{{ State }}'
      - name: Target
        value:
          Arn: '{{ Arn }}'
          RoleArn: '{{ RoleArn }}'
          DeadLetterConfig:
            Arn: '{{ Arn }}'
          RetryPolicy:
            MaximumEventAgeInSeconds: null
            MaximumRetryAttempts: null
          Input: '{{ Input }}'
          EcsParameters:
            TaskDefinitionArn: '{{ TaskDefinitionArn }}'
            TaskCount: null
            LaunchType: '{{ LaunchType }}'
            NetworkConfiguration:
              AwsvpcConfiguration:
                Subnets:
                  - '{{ Subnets[0] }}'
                SecurityGroups:
                  - '{{ SecurityGroups[0] }}'
                AssignPublicIp: '{{ AssignPublicIp }}'
            PlatformVersion: '{{ PlatformVersion }}'
            Group: '{{ Group }}'
            CapacityProviderStrategy:
              - CapacityProvider: '{{ CapacityProvider }}'
                Weight: null
                Base: null
            EnableECSManagedTags: '{{ EnableECSManagedTags }}'
            EnableExecuteCommand: '{{ EnableExecuteCommand }}'
            PlacementConstraints:
              - Type: '{{ Type }}'
                Expression: '{{ Expression }}'
            PlacementStrategy:
              - Type: '{{ Type }}'
                Field: '{{ Field }}'
            PropagateTags: '{{ PropagateTags }}'
            ReferenceId: '{{ ReferenceId }}'
            Tags:
              - {}
          EventBridgeParameters:
            DetailType: '{{ DetailType }}'
            Source: '{{ Source }}'
          KinesisParameters:
            PartitionKey: '{{ PartitionKey }}'
          SageMakerPipelineParameters:
            PipelineParameterList:
              - Name: '{{ Name }}'
                Value: '{{ Value }}'
          SqsParameters:
            MessageGroupId: '{{ MessageGroupId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
scheduler:GetSchedule
```

### Update
```json
scheduler:UpdateSchedule,
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


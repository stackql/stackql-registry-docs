---
title: restore_testing_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_testing_plans
  - backup
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

Creates, updates, deletes or gets a <code>restore_testing_plan</code> resource or lists <code>restore_testing_plans</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restore_testing_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Backup::RestoreTestingPlan Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backup.restore_testing_plans" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="recovery_point_selection" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="restore_testing_plan_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="restore_testing_plan_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="schedule_expression" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="schedule_expression_timezone" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="start_window_hours" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="RecoveryPointSelection, ScheduleExpression, RestoreTestingPlanName, region" /></td>
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
Gets all <code>restore_testing_plans</code> in a region.
```sql
SELECT
region,
recovery_point_selection,
restore_testing_plan_arn,
restore_testing_plan_name,
schedule_expression,
schedule_expression_timezone,
start_window_hours,
tags
FROM aws.backup.restore_testing_plans
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>restore_testing_plan</code>.
```sql
SELECT
region,
recovery_point_selection,
restore_testing_plan_arn,
restore_testing_plan_name,
schedule_expression,
schedule_expression_timezone,
start_window_hours,
tags
FROM aws.backup.restore_testing_plans
WHERE region = 'us-east-1' AND data__Identifier = '<RestoreTestingPlanName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>restore_testing_plan</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.backup.restore_testing_plans (
 RecoveryPointSelection,
 RestoreTestingPlanName,
 ScheduleExpression,
 region
)
SELECT 
'{{ RecoveryPointSelection }}',
 '{{ RestoreTestingPlanName }}',
 '{{ ScheduleExpression }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.backup.restore_testing_plans (
 RecoveryPointSelection,
 RestoreTestingPlanName,
 ScheduleExpression,
 ScheduleExpressionTimezone,
 StartWindowHours,
 Tags,
 region
)
SELECT 
 '{{ RecoveryPointSelection }}',
 '{{ RestoreTestingPlanName }}',
 '{{ ScheduleExpression }}',
 '{{ ScheduleExpressionTimezone }}',
 '{{ StartWindowHours }}',
 '{{ Tags }}',
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
  - name: restore_testing_plan
    props:
      - name: RecoveryPointSelection
        value:
          Algorithm: '{{ Algorithm }}'
          SelectionWindowDays: '{{ SelectionWindowDays }}'
          RecoveryPointTypes:
            - '{{ RecoveryPointTypes[0] }}'
          IncludeVaults:
            - '{{ IncludeVaults[0] }}'
          ExcludeVaults:
            - '{{ ExcludeVaults[0] }}'
      - name: RestoreTestingPlanName
        value: '{{ RestoreTestingPlanName }}'
      - name: ScheduleExpression
        value: '{{ ScheduleExpression }}'
      - name: ScheduleExpressionTimezone
        value: '{{ ScheduleExpressionTimezone }}'
      - name: StartWindowHours
        value: '{{ StartWindowHours }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.backup.restore_testing_plans
WHERE data__Identifier = '<RestoreTestingPlanName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>restore_testing_plans</code> resource, the following permissions are required:

### Create
```json
backup:CreateRestoreTestingPlan,
backup:TagResource,
backup:GetRestoreTestingPlan,
backup:ListTags
```

### Read
```json
backup:GetRestoreTestingPlan,
backup:ListTags
```

### Update
```json
backup:UpdateRestoreTestingPlan,
backup:TagResource,
backup:UntagResource,
backup:GetRestoreTestingPlan,
backup:ListTags
```

### Delete
```json
backup:DeleteRestoreTestingPlan,
backup:GetRestoreTestingPlan
```

### List
```json
backup:ListRestoreTestingPlans
```


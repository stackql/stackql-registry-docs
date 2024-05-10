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


Used to retrieve a list of <code>restore_testing_plans</code> in a region or to create or delete a <code>restore_testing_plans</code> resource, use <code>restore_testing_plan</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restore_testing_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Backup::RestoreTestingPlan Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backup.restore_testing_plans" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="restore_testing_plan_name" /></td><td><code>string</code></td><td></td></tr>
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
restore_testing_plan_name
FROM aws.backup.restore_testing_plans
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- restore_testing_plan.iql (required properties only)
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
-- restore_testing_plan.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
backup:DeleteRestoreTestingPlan,
backup:GetRestoreTestingPlan
```

### List
```json
backup:ListRestoreTestingPlans
```


---
title: refresh_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - refresh_schedules
  - quicksight
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

Creates, updates, deletes or gets a <code>refresh_schedule</code> resource or lists <code>refresh_schedules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>refresh_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::RefreshSchedule Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.refresh_schedules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) of the data source.</p></td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_set_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="schedule" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code=", region" /></td>
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
List all <code>refresh_schedules</code> in a region.
```sql
SELECT
region,
aws_account_id,
data_set_id,
schedule/schedule_id
FROM aws.quicksight.refresh_schedules
WHERE region = 'us-east-1';
```
Gets all properties from a <code>refresh_schedule</code>.
```sql
SELECT
region,
arn,
aws_account_id,
data_set_id,
schedule
FROM aws.quicksight.refresh_schedules
WHERE region = 'us-east-1' AND data__Identifier = '<AwsAccountId>|<DataSetId>|<Schedule/ScheduleId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>refresh_schedule</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.quicksight.refresh_schedules (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.quicksight.refresh_schedules (
 AwsAccountId,
 DataSetId,
 Schedule,
 region
)
SELECT 
 '{{ AwsAccountId }}',
 '{{ DataSetId }}',
 '{{ Schedule }}',
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
  - name: refresh_schedule
    props:
      - name: AwsAccountId
        value: '{{ AwsAccountId }}'
      - name: DataSetId
        value: '{{ DataSetId }}'
      - name: Schedule
        value:
          ScheduleId: '{{ ScheduleId }}'
          ScheduleFrequency:
            Interval: '{{ Interval }}'
            RefreshOnDay:
              DayOfWeek: '{{ DayOfWeek }}'
              DayOfMonth: '{{ DayOfMonth }}'
            TimeZone: '{{ TimeZone }}'
            TimeOfTheDay: '{{ TimeOfTheDay }}'
          StartAfterDateTime: '{{ StartAfterDateTime }}'
          RefreshType: '{{ RefreshType }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.quicksight.refresh_schedules
WHERE data__Identifier = '<AwsAccountId|DataSetId|Schedule/ScheduleId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>refresh_schedules</code> resource, the following permissions are required:

### Create
```json
quicksight:CreateRefreshSchedule,
quicksight:DescribeRefreshSchedule
```

### Update
```json
quicksight:UpdateRefreshSchedule,
quicksight:DescribeRefreshSchedule
```

### Delete
```json
quicksight:DeleteRefreshSchedule,
quicksight:DescribeRefreshSchedule
```

### List
```json
quicksight:ListRefreshSchedules
```

### Read
```json
quicksight:DescribeRefreshSchedule
```


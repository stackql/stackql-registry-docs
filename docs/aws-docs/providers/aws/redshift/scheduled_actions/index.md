---
title: scheduled_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_actions
  - redshift
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

Creates, updates, deletes or gets a <code>scheduled_action</code> resource or lists <code>scheduled_actions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The `AWS::Redshift::ScheduledAction` resource creates an Amazon Redshift Scheduled Action.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.scheduled_actions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="scheduled_action_description" /></td><td><code>string</code></td><td>The description of the scheduled action.</td></tr>
<tr><td><CopyableCode code="scheduled_action_name" /></td><td><code>string</code></td><td>The name of the scheduled action. The name must be unique within an account.</td></tr>
<tr><td><CopyableCode code="end_time" /></td><td><code>string</code></td><td>The end time in UTC of the scheduled action. After this time, the scheduled action does not trigger.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the scheduled action.</td></tr>
<tr><td><CopyableCode code="schedule" /></td><td><code>string</code></td><td>The schedule in `at( )` or `cron( )` format.</td></tr>
<tr><td><CopyableCode code="iam_role" /></td><td><code>string</code></td><td>The IAM role to assume to run the target action.</td></tr>
<tr><td><CopyableCode code="start_time" /></td><td><code>string</code></td><td>The start time in UTC of the scheduled action. Before this time, the scheduled action does not trigger.</td></tr>
<tr><td><CopyableCode code="enable" /></td><td><code>boolean</code></td><td>If true, the schedule is enabled. If false, the scheduled action does not trigger.</td></tr>
<tr><td><CopyableCode code="target_action" /></td><td><code>object</code></td><td>A JSON format string of the Amazon Redshift API operation with input parameters.</td></tr>
<tr><td><CopyableCode code="next_invocations" /></td><td><code>array</code></td><td>List of times when the scheduled action will run.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-scheduledaction.html"><code>AWS::Redshift::ScheduledAction</code></a>.

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
    <td><CopyableCode code="ScheduledActionName, region" /></td>
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
Gets all <code>scheduled_actions</code> in a region.
```sql
SELECT
region,
scheduled_action_description,
scheduled_action_name,
end_time,
state,
schedule,
iam_role,
start_time,
enable,
target_action,
next_invocations
FROM aws.redshift.scheduled_actions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>scheduled_action</code>.
```sql
SELECT
region,
scheduled_action_description,
scheduled_action_name,
end_time,
state,
schedule,
iam_role,
start_time,
enable,
target_action,
next_invocations
FROM aws.redshift.scheduled_actions
WHERE region = 'us-east-1' AND data__Identifier = '<ScheduledActionName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scheduled_action</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.redshift.scheduled_actions (
 ScheduledActionName,
 region
)
SELECT 
'{{ ScheduledActionName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.redshift.scheduled_actions (
 ScheduledActionDescription,
 ScheduledActionName,
 EndTime,
 Schedule,
 IamRole,
 StartTime,
 Enable,
 TargetAction,
 region
)
SELECT 
 '{{ ScheduledActionDescription }}',
 '{{ ScheduledActionName }}',
 '{{ EndTime }}',
 '{{ Schedule }}',
 '{{ IamRole }}',
 '{{ StartTime }}',
 '{{ Enable }}',
 '{{ TargetAction }}',
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
  - name: scheduled_action
    props:
      - name: ScheduledActionDescription
        value: '{{ ScheduledActionDescription }}'
      - name: ScheduledActionName
        value: '{{ ScheduledActionName }}'
      - name: EndTime
        value: '{{ EndTime }}'
      - name: Schedule
        value: '{{ Schedule }}'
      - name: IamRole
        value: '{{ IamRole }}'
      - name: StartTime
        value: null
      - name: Enable
        value: '{{ Enable }}'
      - name: TargetAction
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.redshift.scheduled_actions
WHERE data__Identifier = '<ScheduledActionName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>scheduled_actions</code> resource, the following permissions are required:

### Read
```json
redshift:DescribeScheduledActions,
redshift:DescribeTags
```

### Create
```json
redshift:CreateScheduledAction,
redshift:DescribeScheduledActions,
redshift:DescribeTags,
redshift:PauseCluster,
redshift:ResumeCluster,
redshift:ResizeCluster,
iam:PassRole
```

### Update
```json
redshift:DescribeScheduledActions,
redshift:ModifyScheduledAction,
redshift:PauseCluster,
redshift:ResumeCluster,
redshift:ResizeCluster,
redshift:DescribeTags,
iam:PassRole
```

### List
```json
redshift:DescribeTags,
redshift:DescribeScheduledActions
```

### Delete
```json
redshift:DescribeTags,
redshift:DescribeScheduledActions,
redshift:DeleteScheduledAction
```

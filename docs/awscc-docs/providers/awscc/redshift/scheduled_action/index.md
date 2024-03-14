---
title: scheduled_action
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_action
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
Gets an individual <code>scheduled_action</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_action</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>scheduled_action</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.redshift.scheduled_action</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>scheduled_action_name</code></td><td><code>string</code></td><td>The name of the scheduled action. The name must be unique within an account.</td></tr>
<tr><td><code>target_action</code></td><td><code>object</code></td><td>A JSON format string of the Amazon Redshift API operation with input parameters.</td></tr>
<tr><td><code>schedule</code></td><td><code>string</code></td><td>The schedule in `at( )` or `cron( )` format.</td></tr>
<tr><td><code>iam_role</code></td><td><code>string</code></td><td>The IAM role to assume to run the target action.</td></tr>
<tr><td><code>scheduled_action_description</code></td><td><code>string</code></td><td>The description of the scheduled action.</td></tr>
<tr><td><code>start_time</code></td><td><code>string</code></td><td>The start time in UTC of the scheduled action. Before this time, the scheduled action does not trigger.</td></tr>
<tr><td><code>end_time</code></td><td><code>string</code></td><td>The end time in UTC of the scheduled action. After this time, the scheduled action does not trigger.</td></tr>
<tr><td><code>enable</code></td><td><code>boolean</code></td><td>If true, the schedule is enabled. If false, the scheduled action does not trigger.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of the scheduled action.</td></tr>
<tr><td><code>next_invocations</code></td><td><code>array</code></td><td>List of times when the scheduled action will run.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
scheduled_action_name,
target_action,
schedule,
iam_role,
scheduled_action_description,
start_time,
end_time,
enable,
state,
next_invocations
FROM awscc.redshift.scheduled_action
WHERE data__Identifier = '<ScheduledActionName>';
```

## Permissions

To operate on the <code>scheduled_action</code> resource, the following permissions are required:

### Read
```json
redshift:DescribeScheduledActions,
redshift:DescribeTags
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

### Delete
```json
redshift:DescribeTags,
redshift:DescribeScheduledActions,
redshift:DeleteScheduledAction
```


---
title: restore_testing_plan
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_testing_plan
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
Gets an individual <code>restore_testing_plan</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restore_testing_plan</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>restore_testing_plan</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.backup.restore_testing_plan</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>recovery_point_selection</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>restore_testing_plan_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>restore_testing_plan_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schedule_expression</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schedule_expression_timezone</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>start_window_hours</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.backup.restore_testing_plan
WHERE data__Identifier = '<RestoreTestingPlanName>';
```

## Permissions

To operate on the <code>restore_testing_plan</code> resource, the following permissions are required:

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


---
title: restore_testing_selection
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_testing_selection
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
Gets an individual <code>restore_testing_selection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restore_testing_selection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>restore_testing_selection</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.backup.restore_testing_selection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>iam_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>protected_resource_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>protected_resource_conditions</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>protected_resource_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>restore_metadata_overrides</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>restore_testing_plan_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>restore_testing_selection_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>validation_window_hours</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>restore_testing_selection</code> resource, the following permissions are required:

### Read
<pre>
backup:GetRestoreTestingSelection</pre>

### Update
<pre>
backup:UpdateRestoreTestingSelection,
backup:GetRestoreTestingSelection,
iam:PassRole</pre>

### Delete
<pre>
backup:DeleteRestoreTestingSelection,
backup:GetRestoreTestingSelection</pre>


## Example
```sql
SELECT
region,
iam_role_arn,
protected_resource_arns,
protected_resource_conditions,
protected_resource_type,
restore_metadata_overrides,
restore_testing_plan_name,
restore_testing_selection_name,
validation_window_hours
FROM awscc.backup.restore_testing_selection
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;RestoreTestingPlanName&gt;'
AND data__Identifier = '&lt;RestoreTestingSelectionName&gt;'
```

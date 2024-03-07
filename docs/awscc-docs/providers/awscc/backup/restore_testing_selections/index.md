---
title: restore_testing_selections
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_testing_selections
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
Retrieves a list of <code>restore_testing_selections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restore_testing_selections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>restore_testing_selections</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.backup.restore_testing_selections</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>restore_testing_plan_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>restore_testing_selection_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
restore_testing_plan_name,
restore_testing_selection_name
FROM awscc.backup.restore_testing_selections
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>restore_testing_selections</code> resource, the following permissions are required:

### Create
```json
backup:CreateRestoreTestingSelection,
backup:GetRestoreTestingSelection,
iam:PassRole
```

### List
```json
backup:ListRestoreTestingSelections
```


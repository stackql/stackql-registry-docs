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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>restore_testing_selection</code> resource, use <code>restore_testing_selections</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restore_testing_selection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Backup::RestoreTestingSelection</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backup.restore_testing_selection" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="iam_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="protected_resource_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="protected_resource_conditions" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="protected_resource_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="restore_metadata_overrides" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="restore_testing_plan_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="restore_testing_selection_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="validation_window_hours" /></td><td><code>integer</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.backup.restore_testing_selection
WHERE region = 'us-east-1' AND data__Identifier = '<RestoreTestingPlanName>|<RestoreTestingSelectionName>';
```


## Permissions

To operate on the <code>restore_testing_selection</code> resource, the following permissions are required:

### Read
```json
backup:GetRestoreTestingSelection
```

### Update
```json
backup:UpdateRestoreTestingSelection,
backup:GetRestoreTestingSelection,
iam:PassRole
```


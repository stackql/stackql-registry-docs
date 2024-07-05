---
title: restore_testing_selections_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_testing_selections_list_only
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

Lists <code>restore_testing_selections</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/restore_testing_selections/"><code>restore_testing_selections</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restore_testing_selections_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Backup::RestoreTestingSelection</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backup.restore_testing_selections_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="iam_role_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>restore_testing_selections</code> in a region.
```sql
SELECT
region,
restore_testing_plan_name,
restore_testing_selection_name
FROM aws.backup.restore_testing_selections_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>restore_testing_selections_list_only</code> resource, see <a href="/providers/aws/backup/restore_testing_selections/#permissions"><code>restore_testing_selections</code></a>



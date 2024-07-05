---
title: restore_testing_plans_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_testing_plans_list_only
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

Lists <code>restore_testing_plans</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/restore_testing_plans/"><code>restore_testing_plans</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restore_testing_plans_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Backup::RestoreTestingPlan Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backup.restore_testing_plans_list_only" /></td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>restore_testing_plans</code> in a region.
```sql
SELECT
region,
restore_testing_plan_name
FROM aws.backup.restore_testing_plans_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>restore_testing_plans_list_only</code> resource, see <a href="/providers/aws/backup/restore_testing_plans/#permissions"><code>restore_testing_plans</code></a>



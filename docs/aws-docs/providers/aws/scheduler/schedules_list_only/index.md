---
title: schedules_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - schedules_list_only
  - scheduler
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

Lists <code>schedules</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/schedules/"><code>schedules</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schedules_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Scheduler::Schedule Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.scheduler.schedules_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the schedule.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the schedule.</td></tr>
<tr><td><CopyableCode code="end_date" /></td><td><code>string</code></td><td>The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the EndDate you specify.</td></tr>
<tr><td><CopyableCode code="flexible_time_window" /></td><td><code>object</code></td><td>Flexible time window allows configuration of a window within which a schedule can be invoked</td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td>The name of the schedule group to associate with this schedule. If you omit this, the default schedule group is used.</td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td>The ARN for a KMS Key that will be used to encrypt customer data.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="schedule_expression" /></td><td><code>string</code></td><td>The scheduling expression.</td></tr>
<tr><td><CopyableCode code="schedule_expression_timezone" /></td><td><code>string</code></td><td>The timezone in which the scheduling expression is evaluated.</td></tr>
<tr><td><CopyableCode code="start_date" /></td><td><code>string</code></td><td>The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the StartDate you specify.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>Specifies whether the schedule is enabled or disabled.</td></tr>
<tr><td><CopyableCode code="target" /></td><td><code>object</code></td><td>The schedule target.</td></tr>
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
Lists all <code>schedules</code> in a region.
```sql
SELECT
region,
name
FROM aws.scheduler.schedules_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>schedules_list_only</code> resource, see <a href="/providers/aws/scheduler/schedules/#permissions"><code>schedules</code></a>



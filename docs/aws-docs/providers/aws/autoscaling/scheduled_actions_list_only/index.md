---
title: scheduled_actions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_actions_list_only
  - autoscaling
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

Lists <code>scheduled_actions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/scheduled_actions/"><code>scheduled_actions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_actions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AutoScaling::ScheduledAction resource specifies an Amazon EC2 Auto Scaling scheduled action so that the Auto Scaling group can change the number of instances available for your application in response to predictable load changes.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.autoscaling.scheduled_actions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="scheduled_action_name" /></td><td><code>string</code></td><td>Auto-generated unique identifier</td></tr>
<tr><td><CopyableCode code="min_size" /></td><td><code>integer</code></td><td>The minimum size of the Auto Scaling group.</td></tr>
<tr><td><CopyableCode code="recurrence" /></td><td><code>string</code></td><td>The recurring schedule for the action, in Unix cron syntax format. When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.</td></tr>
<tr><td><CopyableCode code="time_zone" /></td><td><code>string</code></td><td>The time zone for the cron expression.</td></tr>
<tr><td><CopyableCode code="end_time" /></td><td><code>string</code></td><td>The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.</td></tr>
<tr><td><CopyableCode code="auto_scaling_group_name" /></td><td><code>string</code></td><td>The name of the Auto Scaling group.</td></tr>
<tr><td><CopyableCode code="start_time" /></td><td><code>string</code></td><td>The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.</td></tr>
<tr><td><CopyableCode code="desired_capacity" /></td><td><code>integer</code></td><td>The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.</td></tr>
<tr><td><CopyableCode code="max_size" /></td><td><code>integer</code></td><td>The minimum size of the Auto Scaling group.</td></tr>
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
Lists all <code>scheduled_actions</code> in a region.
```sql
SELECT
region,
scheduled_action_name,
auto_scaling_group_name
FROM aws.autoscaling.scheduled_actions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>scheduled_actions_list_only</code> resource, see <a href="/providers/aws/autoscaling/scheduled_actions/#permissions"><code>scheduled_actions</code></a>



---
title: scheduled_action
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_action
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
Gets an individual <code>scheduled_action</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_action</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.autoscaling.scheduled_action</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ScheduledActionName</code></td><td><code>string</code></td><td>Auto-generated unique identifier</td></tr><tr><td><code>MinSize</code></td><td><code>integer</code></td><td>The minimum size of the Auto Scaling group.</td></tr><tr><td><code>Recurrence</code></td><td><code>string</code></td><td>The recurring schedule for the action, in Unix cron syntax format. When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.</td></tr><tr><td><code>TimeZone</code></td><td><code>string</code></td><td>The time zone for the cron expression.</td></tr><tr><td><code>EndTime</code></td><td><code>string</code></td><td>The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.</td></tr><tr><td><code>AutoScalingGroupName</code></td><td><code>string</code></td><td>The name of the Auto Scaling group.</td></tr><tr><td><code>StartTime</code></td><td><code>string</code></td><td>The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.</td></tr><tr><td><code>DesiredCapacity</code></td><td><code>integer</code></td><td>The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.</td></tr><tr><td><code>MaxSize</code></td><td><code>integer</code></td><td>The minimum size of the Auto Scaling group.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.autoscaling.scheduled_action
WHERE region = 'us-east-1' AND data__Identifier = '<ScheduledActionName>' AND data__Identifier = '<AutoScalingGroupName>'
</pre>

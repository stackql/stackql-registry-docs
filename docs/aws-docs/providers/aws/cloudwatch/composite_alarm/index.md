---
title: composite_alarm
hide_title: false
hide_table_of_contents: false
keywords:
  - composite_alarm
  - cloudwatch
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>composite_alarm</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>composite_alarm</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.cloudwatch.composite_alarm</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the alarm</td></tr><tr><td><code>AlarmName</code></td><td><code>string</code></td><td>The name of the Composite Alarm</td></tr><tr><td><code>AlarmRule</code></td><td><code>string</code></td><td>Expression which aggregates the state of other Alarms (Metric or Composite Alarms)</td></tr><tr><td><code>AlarmDescription</code></td><td><code>string</code></td><td>The description of the alarm</td></tr><tr><td><code>ActionsEnabled</code></td><td><code>boolean</code></td><td>Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.</td></tr><tr><td><code>OKActions</code></td><td><code>array</code></td><td>The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).</td></tr><tr><td><code>AlarmActions</code></td><td><code>array</code></td><td>The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN).</td></tr><tr><td><code>InsufficientDataActions</code></td><td><code>array</code></td><td>The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).</td></tr><tr><td><code>ActionsSuppressor</code></td><td><code>string</code></td><td>Actions will be suppressed if the suppressor alarm is in the ALARM state. ActionsSuppressor can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm. </td></tr><tr><td><code>ActionsSuppressorWaitPeriod</code></td><td><code>integer</code></td><td>Actions will be suppressed if ExtensionPeriod is active. The length of time that actions are suppressed is in seconds.</td></tr><tr><td><code>ActionsSuppressorExtensionPeriod</code></td><td><code>integer</code></td><td>Actions will be suppressed if WaitPeriod is active. The length of time that actions are suppressed is in seconds.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.cloudwatch.composite_alarm
WHERE region = 'us-east-1' AND data__Identifier = '<AlarmName>'
</pre>

---
title: scheduled_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_actions
  - redshift
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>scheduled_actions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.redshift.scheduled_actions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ScheduledActionName</code></td><td><code>string</code></td><td>The name of the scheduled action. The name must be unique within an account.</td></tr>
<tr><td><code>TargetAction</code></td><td><code>undefined</code></td><td>A JSON format string of the Amazon Redshift API operation with input parameters.</td></tr>
<tr><td><code>Schedule</code></td><td><code>string</code></td><td>The schedule in `at( )` or `cron( )` format.</td></tr>
<tr><td><code>IamRole</code></td><td><code>string</code></td><td>The IAM role to assume to run the target action.</td></tr>
<tr><td><code>ScheduledActionDescription</code></td><td><code>string</code></td><td>The description of the scheduled action.</td></tr>
<tr><td><code>StartTime</code></td><td><code>undefined</code></td><td>The start time in UTC of the scheduled action. Before this time, the scheduled action does not trigger.</td></tr>
<tr><td><code>EndTime</code></td><td><code>undefined</code></td><td>The end time in UTC of the scheduled action. After this time, the scheduled action does not trigger.</td></tr>
<tr><td><code>Enable</code></td><td><code>boolean</code></td><td>If true, the schedule is enabled. If false, the scheduled action does not trigger.</td></tr>
<tr><td><code>State</code></td><td><code>string</code></td><td>The state of the scheduled action.</td></tr>
<tr><td><code>NextInvocations</code></td><td><code>array</code></td><td>List of times when the scheduled action will run.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.redshift.scheduled_actions
WHERE region = 'us-east-1'
</pre>

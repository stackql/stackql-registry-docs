---
title: schedule
hide_title: false
hide_table_of_contents: false
keywords:
  - schedule
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
Gets an individual <code>schedule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schedule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.scheduler.schedule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the schedule.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the schedule.</td></tr><tr><td><code>EndDate</code></td><td><code>string</code></td><td>The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the EndDate you specify.</td></tr><tr><td><code>FlexibleTimeWindow</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>GroupName</code></td><td><code>string</code></td><td>The name of the schedule group to associate with this schedule. If you omit this, the default schedule group is used.</td></tr><tr><td><code>KmsKeyArn</code></td><td><code>string</code></td><td>The ARN for a KMS Key that will be used to encrypt customer data.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ScheduleExpression</code></td><td><code>string</code></td><td>The scheduling expression.</td></tr><tr><td><code>ScheduleExpressionTimezone</code></td><td><code>string</code></td><td>The timezone in which the scheduling expression is evaluated.</td></tr><tr><td><code>StartDate</code></td><td><code>string</code></td><td>The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the StartDate you specify.</td></tr><tr><td><code>State</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Target</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.scheduler.schedule
WHERE region = 'us-east-1' AND data__Identifier = '<Name>'
</pre>

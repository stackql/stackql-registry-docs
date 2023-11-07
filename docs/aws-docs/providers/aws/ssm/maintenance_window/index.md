---
title: maintenance_window
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenance_window
  - ssm
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>maintenance_window</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>maintenance_window</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>maintenance_window</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ssm.maintenance_window</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>StartDate</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AllowUnassociatedTargets</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>Cutoff</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Schedule</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Duration</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>ScheduleOffset</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EndDate</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ScheduleTimezone</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ssm.maintenance_window
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Id&gt;'
</pre>

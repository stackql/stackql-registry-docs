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
<tr><td><code>start_date</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>allow_unassociated_targets</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>cutoff</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>schedule</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>duration</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>schedule_offset</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>end_date</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schedule_timezone</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
start_date,
description,
allow_unassociated_targets,
cutoff,
schedule,
duration,
schedule_offset,
id,
end_date,
tags,
name,
schedule_timezone
FROM aws.ssm.maintenance_window
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```

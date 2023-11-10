---
title: maintenance_window_task
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenance_window_task
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
Gets an individual <code>maintenance_window_task</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>maintenance_window_task</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>maintenance_window_task</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ssm.maintenance_window_task</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>max_errors</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>priority</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>max_concurrency</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>targets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>task_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>task_invocation_parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>window_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>task_parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>task_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cutoff_behavior</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>logging_info</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
max_errors,
description,
service_role_arn,
priority,
max_concurrency,
targets,
name,
task_arn,
task_invocation_parameters,
window_id,
task_parameters,
task_type,
cutoff_behavior,
id,
logging_info
FROM aws.ssm.maintenance_window_task
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```

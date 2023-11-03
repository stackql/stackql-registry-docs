---
title: maintenance_window_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenance_window_tasks
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
Retrieves a list of <code>maintenance_window_tasks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>maintenance_window_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.ssm.maintenance_window_tasks</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>MaxErrors</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ServiceRoleArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Priority</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>MaxConcurrency</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Targets</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TaskArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TaskInvocationParameters</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>WindowId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TaskParameters</code></td><td><code>object</code></td><td></td></tr><tr><td><code>TaskType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CutoffBehavior</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>LoggingInfo</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ssm.maintenance_window_tasks
WHERE region = 'us-east-1'
</pre>

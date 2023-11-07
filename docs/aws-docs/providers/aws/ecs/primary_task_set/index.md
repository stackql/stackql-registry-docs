---
title: primary_task_set
hide_title: false
hide_table_of_contents: false
keywords:
  - primary_task_set
  - ecs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>primary_task_set</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>primary_task_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.ecs.primary_task_set</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Cluster</code></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.</td></tr>
<tr><td><code>TaskSetId</code></td><td><code>string</code></td><td>The ID or full Amazon Resource Name (ARN) of the task set.</td></tr>
<tr><td><code>Service</code></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the service to create the task set in.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ecs.primary_task_set
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Cluster&gt;' AND data__Identifier = '&lt;Service&gt;'
</pre>

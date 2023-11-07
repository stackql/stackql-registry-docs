---
title: scalable_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - scalable_targets
  - applicationautoscaling
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>scalable_targets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scalable_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>scalable_targets</td></tr>
<tr><td><b>Id</b></td><td><code>aws.applicationautoscaling.scalable_targets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ScheduledActions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ResourceId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ServiceNamespace</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ScalableDimension</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SuspendedState</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MinCapacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>RoleARN</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MaxCapacity</code></td><td><code>integer</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.applicationautoscaling.scalable_targets<br/>WHERE region = 'us-east-1'
</pre>

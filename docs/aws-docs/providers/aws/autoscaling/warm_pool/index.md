---
title: warm_pool
hide_title: false
hide_table_of_contents: false
keywords:
  - warm_pool
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
Gets an individual <code>warm_pool</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>warm_pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>warm_pool</td></tr>
<tr><td><b>Id</b></td><td><code>aws.autoscaling.warm_pool</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AutoScalingGroupName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MaxGroupPreparedCapacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>MinSize</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>PoolState</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>InstanceReusePolicy</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.autoscaling.warm_pool<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;AutoScalingGroupName&gt;'
</pre>

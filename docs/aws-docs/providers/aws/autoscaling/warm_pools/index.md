---
title: warm_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - warm_pools
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
Retrieves a list of <code>warm_pools</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>warm_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.autoscaling.warm_pools</code></td></tr>
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
SELECT * 
FROM aws.autoscaling.warm_pools
WHERE region = 'us-east-1'
</pre>

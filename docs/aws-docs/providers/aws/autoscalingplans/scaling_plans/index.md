---
title: scaling_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - scaling_plans
  - autoscalingplans
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>scaling_plans</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.autoscalingplans.scaling_plans</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ScalingPlanName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ScalingPlanVersion</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ApplicationSource</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ScalingInstructions</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.autoscalingplans.scaling_plans
WHERE region = 'us-east-1'
```

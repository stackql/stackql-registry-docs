---
title: scaling_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - scaling_policy
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
Gets an individual <code>scaling_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>scaling_policy</td></tr>
<tr><td><b>Id</b></td><td><code>aws.applicationautoscaling.scaling_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>policy_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>scalable_dimension</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>scaling_target_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_namespace</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>step_scaling_policy_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>target_tracking_scaling_policy_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
policy_name,
policy_type,
resource_id,
scalable_dimension,
scaling_target_id,
service_namespace,
step_scaling_policy_configuration,
target_tracking_scaling_policy_configuration
FROM aws.applicationautoscaling.scaling_policy
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```

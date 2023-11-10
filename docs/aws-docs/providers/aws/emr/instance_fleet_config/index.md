---
title: instance_fleet_config
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_fleet_config
  - emr
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>instance_fleet_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_fleet_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>instance_fleet_config</td></tr>
<tr><td><b>Id</b></td><td><code>aws.emr.instance_fleet_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_fleet_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>target_on_demand_capacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>cluster_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>target_spot_capacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>launch_specifications</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instance_type_configs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
instance_fleet_type,
target_on_demand_capacity,
cluster_id,
target_spot_capacity,
launch_specifications,
id,
instance_type_configs,
name
FROM aws.emr.instance_fleet_config
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```

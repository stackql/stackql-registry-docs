---
title: ec2fleet
hide_title: false
hide_table_of_contents: false
keywords:
  - ec2fleet
  - ec2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>ec2fleet</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ec2fleet</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>ec2fleet</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.ec2fleet</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>target_capacity_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>on_demand_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>excess_capacity_termination_policy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tag_specifications</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>spot_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>valid_from</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>replace_unhealthy_instances</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>launch_template_configs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>fleet_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>terminate_instances_with_expiration</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>valid_until</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>context</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
target_capacity_specification,
on_demand_options,
type,
excess_capacity_termination_policy,
tag_specifications,
spot_options,
valid_from,
replace_unhealthy_instances,
launch_template_configs,
fleet_id,
terminate_instances_with_expiration,
valid_until,
context
FROM awscc.ec2.ec2fleet
WHERE data__Identifier = '<FleetId>';
```

## Permissions

To operate on the <code>ec2fleet</code> resource, the following permissions are required:

### Delete
```json
ec2:DescribeFleets,
ec2:DeleteFleets
```

### Read
```json
ec2:DescribeFleets
```

### Update
```json
ec2:ModifyFleet,
ec2:DescribeFleets
```


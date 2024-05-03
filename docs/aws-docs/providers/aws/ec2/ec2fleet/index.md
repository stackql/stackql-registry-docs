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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>ec2fleet</code> resource, use <code>ec2fleets</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ec2fleet</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::EC2Fleet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ec2fleet" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="target_capacity_specification" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="on_demand_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="excess_capacity_termination_policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_specifications" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="spot_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="valid_from" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="replace_unhealthy_instances" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="launch_template_configs" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="fleet_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="terminate_instances_with_expiration" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="valid_until" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="context" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.ec2.ec2fleet
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


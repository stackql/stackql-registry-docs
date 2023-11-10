---
title: instance_group_config
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_group_config
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
Gets an individual <code>instance_group_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_group_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>instance_group_config</td></tr>
<tr><td><b>Id</b></td><td><code>aws.emr.instance_group_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>job_flow_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>auto_scaling_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>bid_price</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instance_count</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>ebs_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>instance_role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>custom_ami_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>configurations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>instance_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>market</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
job_flow_id,
auto_scaling_policy,
bid_price,
instance_count,
ebs_configuration,
instance_role,
custom_ami_id,
id,
configurations,
instance_type,
market,
name
FROM aws.emr.instance_group_config
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```

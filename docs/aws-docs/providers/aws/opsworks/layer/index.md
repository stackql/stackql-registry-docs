---
title: layer
hide_title: false
hide_table_of_contents: false
keywords:
  - layer
  - opsworks
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>layer</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>layer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>layer</td></tr>
<tr><td><b>Id</b></td><td><code>aws.opsworks.layer</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>auto_assign_elastic_ips</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>auto_assign_public_ips</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>custom_instance_profile_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>custom_json</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>custom_recipes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>custom_security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>enable_auto_healing</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>install_updates_on_boot</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>lifecycle_event_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>load_based_auto_scaling</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>packages</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>shortname</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stack_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>use_ebs_optimized_instances</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>volume_configurations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
attributes,
auto_assign_elastic_ips,
auto_assign_public_ips,
custom_instance_profile_arn,
custom_json,
custom_recipes,
custom_security_group_ids,
enable_auto_healing,
install_updates_on_boot,
lifecycle_event_configuration,
load_based_auto_scaling,
name,
packages,
shortname,
stack_id,
tags,
type,
use_ebs_optimized_instances,
volume_configurations
FROM aws.opsworks.layer
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```

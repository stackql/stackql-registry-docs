---
title: deployment_group
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_group
  - codedeploy
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>deployment_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>deployment_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codedeploy.deployment_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>on_premises_tag_set</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>application_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>deployment_style</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>service_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>blue_green_deployment_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>auto_scaling_groups</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ec2_tag_set</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>outdated_instances_strategy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>trigger_configurations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>deployment</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>deployment_config_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>alarm_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>ec2_tag_filters</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>e_cs_services</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>auto_rollback_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>load_balancer_info</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>deployment_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>on_premises_instance_tag_filters</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
on_premises_tag_set,
application_name,
deployment_style,
service_role_arn,
blue_green_deployment_configuration,
auto_scaling_groups,
ec2_tag_set,
outdated_instances_strategy,
trigger_configurations,
deployment,
deployment_config_name,
alarm_configuration,
ec2_tag_filters,
e_cs_services,
auto_rollback_configuration,
load_balancer_info,
id,
deployment_group_name,
tags,
on_premises_instance_tag_filters
FROM aws.codedeploy.deployment_group
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```

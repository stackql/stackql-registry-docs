---
title: auto_scaling_group
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_scaling_group
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
Gets an individual <code>auto_scaling_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auto_scaling_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>auto_scaling_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.autoscaling.auto_scaling_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>lifecycle_hook_specification_list</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>load_balancer_names</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>launch_configuration_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_linked_role_ar_n</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>target_group_ar_ns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>cooldown</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>notification_configurations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>desired_capacity</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>health_check_grace_period</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>default_instance_warmup</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>new_instances_protected_from_scale_in</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>launch_template</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>mixed_instances_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>v_pc_zone_identifier</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>context</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>capacity_rebalance</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>instance_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>availability_zones</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>notification_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>metrics_collection</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>instance_maintenance_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>max_size</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>min_size</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>termination_policies</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>auto_scaling_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>desired_capacity_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>placement_group</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>health_check_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>max_instance_lifetime</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>auto_scaling_group</code> resource, the following permissions are required:

### Read
<pre>
autoscaling:*,
managed-fleets:GetAutoScalingGroup</pre>

### Update
<pre>
autoscaling:*,
cloudwatch:PutMetricAlarm,
ec2:Describe*,
ec2:GetInstanceTypesFromInstanceRequirements,
ec2:RunInstances,
elasticloadbalancing:DescribeLoadBalancers,
elasticloadbalancing:DescribeTargetGroups,
iam:CreateServiceLinkedRole,
iam:PassRole,
managed-fleets:GetAutoScalingGroup,
managed-fleets:RegisterAutoScalingGroup,
managed-fleets:DeregisterAutoScalingGroup,
managed-fleets:UpdateAutoScalingGroup,
ssm:GetParameters</pre>

### Delete
<pre>
autoscaling:*,
managed-fleets:GetAutoScalingGroup,
managed-fleets:DeleteAutoScalingGroup</pre>


## Example
```sql
SELECT
region,
lifecycle_hook_specification_list,
load_balancer_names,
launch_configuration_name,
service_linked_role_ar_n,
target_group_ar_ns,
cooldown,
notification_configurations,
desired_capacity,
health_check_grace_period,
default_instance_warmup,
new_instances_protected_from_scale_in,
launch_template,
mixed_instances_policy,
v_pc_zone_identifier,
tags,
context,
capacity_rebalance,
instance_id,
availability_zones,
notification_configuration,
metrics_collection,
instance_maintenance_policy,
max_size,
min_size,
termination_policies,
auto_scaling_group_name,
desired_capacity_type,
placement_group,
health_check_type,
max_instance_lifetime
FROM awscc.autoscaling.auto_scaling_group
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AutoScalingGroupName&gt;'
```

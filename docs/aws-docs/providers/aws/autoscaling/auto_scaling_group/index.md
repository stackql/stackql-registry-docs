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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>auto_scaling_group</code> resource, use <code>auto_scaling_groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auto_scaling_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::AutoScaling::AutoScalingGroup`` resource defines an Amazon EC2 Auto Scaling group, which is a collection of Amazon EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management. &lt;br&#x2F;&gt; For more information about Amazon EC2 Auto Scaling, see the &#91;Amazon EC2 Auto Scaling User Guide&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;what-is-amazon-ec2-auto-scaling.html). &lt;br&#x2F;&gt;  Amazon EC2 Auto Scaling configures instances launched as part of an Auto Scaling group using either a &#91;launch template&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-ec2-launchtemplate.html) or a launch configuration. We strongly recommend that you do not use launch configurations. They do not provide full functionality for Amazon EC2 Auto Scaling or Amazon EC2. For more information, see &#91;Launch configurations&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;launch-configurations.html) and &#91;Migrate CloudFormation stacks from launch configurations to launch templates&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;migrate-launch-configurations-with-cloudformation.html) in the *Amazon EC2 Auto Scaling User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.autoscaling.auto_scaling_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="lifecycle_hook_specification_list" /></td><td><code>array</code></td><td>One or more lifecycle hooks to add to the Auto Scaling group before instances are launched.</td></tr>
<tr><td><CopyableCode code="load_balancer_names" /></td><td><code>array</code></td><td>A list of Classic Load Balancers associated with this Auto Scaling group. For Application Load Balancers, Network Load Balancers, and Gateway Load Balancers, specify the ``TargetGroupARNs`` property instead.</td></tr>
<tr><td><CopyableCode code="launch_configuration_name" /></td><td><code>string</code></td><td>The name of the launch configuration to use to launch instances.&lt;br&#x2F;&gt; Required only if you don't specify ``LaunchTemplate``, ``MixedInstancesPolicy``, or ``InstanceId``.</td></tr>
<tr><td><CopyableCode code="service_linked_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS service on your behalf. By default, Amazon EC2 Auto Scaling uses a service-linked role named ``AWSServiceRoleForAutoScaling``, which it creates if it does not exist. For more information, see &#91;Service-linked roles&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;autoscaling-service-linked-role.html) in the *Amazon EC2 Auto Scaling User Guide*.</td></tr>
<tr><td><CopyableCode code="target_group_arns" /></td><td><code>array</code></td><td>The Amazon Resource Names (ARN) of the Elastic Load Balancing target groups to associate with the Auto Scaling group. Instances are registered as targets with the target groups. The target groups receive incoming traffic and route requests to one or more registered targets. For more information, see &#91;Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;autoscaling-load-balancer.html) in the *Amazon EC2 Auto Scaling User Guide*.</td></tr>
<tr><td><CopyableCode code="cooldown" /></td><td><code>string</code></td><td>*Only needed if you use simple scaling policies.* &lt;br&#x2F;&gt; The amount of time, in seconds, between one scaling activity ending and another one starting due to simple scaling policies. For more information, see &#91;Scaling cooldowns for Amazon EC2 Auto Scaling&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;Cooldown.html) in the *Amazon EC2 Auto Scaling User Guide*.&lt;br&#x2F;&gt; Default: ``300`` seconds</td></tr>
<tr><td><CopyableCode code="notification_configurations" /></td><td><code>array</code></td><td>Configures an Auto Scaling group to send notifications when specified events take place.</td></tr>
<tr><td><CopyableCode code="desired_capacity" /></td><td><code>string</code></td><td>The desired capacity is the initial capacity of the Auto Scaling group at the time of its creation and the capacity it attempts to maintain. It can scale beyond this capacity if you configure automatic scaling.&lt;br&#x2F;&gt; The number must be greater than or equal to the minimum size of the group and less than or equal to the maximum size of the group. If you do not specify a desired capacity when creating the stack, the default is the minimum size of the group.&lt;br&#x2F;&gt; CloudFormation marks the Auto Scaling group as successful (by setting its status to CREATE_COMPLETE) when the desired capacity is reached. However, if a maximum Spot price is set in the launch template or launch configuration that you specified, then desired capacity is not used as a criteria for success. Whether your request is fulfilled depends on Spot Instance capacity and your maximum price.</td></tr>
<tr><td><CopyableCode code="health_check_grace_period" /></td><td><code>integer</code></td><td>The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service and marking it unhealthy due to a failed health check. This is useful if your instances do not immediately pass their health checks after they enter the ``InService`` state. For more information, see &#91;Set the health check grace period for an Auto Scaling group&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;health-check-grace-period.html) in the *Amazon EC2 Auto Scaling User Guide*.&lt;br&#x2F;&gt; Default: ``0`` seconds</td></tr>
<tr><td><CopyableCode code="default_instance_warmup" /></td><td><code>integer</code></td><td>The amount of time, in seconds, until a new instance is considered to have finished initializing and resource consumption to become stable after it enters the ``InService`` state. &lt;br&#x2F;&gt; During an instance refresh, Amazon EC2 Auto Scaling waits for the warm-up period after it replaces an instance before it moves on to replacing the next instance. Amazon EC2 Auto Scaling also waits for the warm-up period before aggregating the metrics for new instances with existing instances in the Amazon CloudWatch metrics that are used for scaling, resulting in more reliable usage data. For more information, see &#91;Set the default instance warmup for an Auto Scaling group&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;ec2-auto-scaling-default-instance-warmup.html) in the *Amazon EC2 Auto Scaling User Guide*.&lt;br&#x2F;&gt;  To manage various warm-up settings at the group level, we recommend that you set the default instance warmup, *even if it is set to 0 seconds*. To remove a value that you previously set, include the property but specify ``-1`` for the value. However, we strongly recommend keeping the default instance warmup enabled by specifying a value of ``0`` or other nominal value.&lt;br&#x2F;&gt;  Default: None</td></tr>
<tr><td><CopyableCode code="new_instances_protected_from_scale_in" /></td><td><code>boolean</code></td><td>Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in. For more information about preventing instances from terminating on scale in, see &#91;Using instance scale-in protection&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;ec2-auto-scaling-instance-protection.html) in the *Amazon EC2 Auto Scaling User Guide*.</td></tr>
<tr><td><CopyableCode code="launch_template" /></td><td><code>object</code></td><td>Information used to specify the launch template and version to use to launch instances. You can alternatively associate a launch template to the Auto Scaling group by specifying a ``MixedInstancesPolicy``. For more information about creating launch templates, see &#91;Create a launch template for an Auto Scaling group&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;create-launch-template.html) in the *Amazon EC2 Auto Scaling User Guide*.&lt;br&#x2F;&gt; If you omit this property, you must specify ``MixedInstancesPolicy``, ``LaunchConfigurationName``, or ``InstanceId``.</td></tr>
<tr><td><CopyableCode code="mixed_instances_policy" /></td><td><code>object</code></td><td>An embedded object that specifies a mixed instances policy.&lt;br&#x2F;&gt; The policy includes properties that not only define the distribution of On-Demand Instances and Spot Instances, the maximum price to pay for Spot Instances (optional), and how the Auto Scaling group allocates instance types to fulfill On-Demand and Spot capacities, but also the properties that specify the instance configuration information—the launch template and instance types. The policy can also include a weight for each instance type and different launch templates for individual instance types.&lt;br&#x2F;&gt; For more information, see &#91;Auto Scaling groups with multiple instance types and purchase options&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;ec2-auto-scaling-mixed-instances-groups.html) in the *Amazon EC2 Auto Scaling User Guide*.</td></tr>
<tr><td><CopyableCode code="vpc_zone_identifier" /></td><td><code>array</code></td><td>A list of subnet IDs for a virtual private cloud (VPC) where instances in the Auto Scaling group can be created.&lt;br&#x2F;&gt; If this resource specifies public subnets and is also in a VPC that is defined in the same stack template, you must use the &#91;DependsOn attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-attribute-dependson.html) to declare a dependency on the &#91;VPC-gateway attachment&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-ec2-vpc-gateway-attachment.html).&lt;br&#x2F;&gt;  When you update ``VPCZoneIdentifier``, this retains the same Auto Scaling group and replaces old instances with new ones, according to the specified subnets. You can optionally specify how CloudFormation handles these updates by using an &#91;UpdatePolicy attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-attribute-updatepolicy.html).&lt;br&#x2F;&gt;  Required to launch instances into a nondefault VPC. If you specify ``VPCZoneIdentifier`` with ``AvailabilityZones``, the subnets that you specify for this property must reside in those Availability Zones.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags. You can tag your Auto Scaling group and propagate the tags to the Amazon EC2 instances it launches. Tags are not propagated to Amazon EBS volumes. To add tags to Amazon EBS volumes, specify the tags in a launch template but use caution. If the launch template specifies an instance tag with a key that is also specified for the Auto Scaling group, Amazon EC2 Auto Scaling overrides the value of that instance tag with the value specified by the Auto Scaling group. For more information, see &#91;Tag Auto Scaling groups and instances&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;ec2-auto-scaling-tagging.html) in the *Amazon EC2 Auto Scaling User Guide*.</td></tr>
<tr><td><CopyableCode code="context" /></td><td><code>string</code></td><td>Reserved.</td></tr>
<tr><td><CopyableCode code="capacity_rebalance" /></td><td><code>boolean</code></td><td>Indicates whether Capacity Rebalancing is enabled. Otherwise, Capacity Rebalancing is disabled. When you turn on Capacity Rebalancing, Amazon EC2 Auto Scaling attempts to launch a Spot Instance whenever Amazon EC2 notifies that a Spot Instance is at an elevated risk of interruption. After launching a new instance, it then terminates an old instance. For more information, see &#91;Use Capacity Rebalancing to handle Amazon EC2 Spot Interruptions&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;ec2-auto-scaling-capacity-rebalancing.html) in the in the *Amazon EC2 Auto Scaling User Guide*.</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>The ID of the instance used to base the launch configuration on. For more information, see &#91;Create an Auto Scaling group using an EC2 instance&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;create-asg-from-instance.html) in the *Amazon EC2 Auto Scaling User Guide*.&lt;br&#x2F;&gt; If you specify ``LaunchTemplate``, ``MixedInstancesPolicy``, or ``LaunchConfigurationName``, don't specify ``InstanceId``.</td></tr>
<tr><td><CopyableCode code="availability_zones" /></td><td><code>array</code></td><td>A list of Availability Zones where instances in the Auto Scaling group can be created. Used for launching into the default VPC subnet in each Availability Zone when not using the ``VPCZoneIdentifier`` property, or for attaching a network interface when an existing network interface ID is specified in a launch template.</td></tr>
<tr><td><CopyableCode code="notification_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="metrics_collection" /></td><td><code>array</code></td><td>Enables the monitoring of group metrics of an Auto Scaling group. By default, these metrics are disabled.</td></tr>
<tr><td><CopyableCode code="instance_maintenance_policy" /></td><td><code>object</code></td><td>An instance maintenance policy. For more information, see &#91;Set instance maintenance policy&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;ec2-auto-scaling-instance-maintenance-policy.html) in the *Amazon EC2 Auto Scaling User Guide*.</td></tr>
<tr><td><CopyableCode code="max_size" /></td><td><code>string</code></td><td>The maximum size of the group.&lt;br&#x2F;&gt;  With a mixed instances policy that uses instance weighting, Amazon EC2 Auto Scaling may need to go above ``MaxSize`` to meet your capacity requirements. In this event, Amazon EC2 Auto Scaling will never go above ``MaxSize`` by more than your largest instance weight (weights that define how many units each instance contributes to the desired capacity of the group).</td></tr>
<tr><td><CopyableCode code="min_size" /></td><td><code>string</code></td><td>The minimum size of the group.</td></tr>
<tr><td><CopyableCode code="termination_policies" /></td><td><code>array</code></td><td>A policy or a list of policies that are used to select the instance to terminate. These policies are executed in the order that you list them. For more information, see &#91;Work with Amazon EC2 Auto Scaling termination policies&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;ec2-auto-scaling-termination-policies.html) in the *Amazon EC2 Auto Scaling User Guide*.&lt;br&#x2F;&gt; Valid values: ``Default`` | ``AllocationStrategy`` | ``ClosestToNextInstanceHour`` | ``NewestInstance`` | ``OldestInstance`` | ``OldestLaunchConfiguration`` | ``OldestLaunchTemplate`` | ``arn:aws:lambda:region:account-id:function:my-function:my-alias``</td></tr>
<tr><td><CopyableCode code="auto_scaling_group_name" /></td><td><code>string</code></td><td>The name of the Auto Scaling group. This name must be unique per Region per account.&lt;br&#x2F;&gt; The name can contain any ASCII character 33 to 126 including most punctuation characters, digits, and upper and lowercased letters.&lt;br&#x2F;&gt;  You cannot use a colon (:) in the name.</td></tr>
<tr><td><CopyableCode code="desired_capacity_type" /></td><td><code>string</code></td><td>The unit of measurement for the value specified for desired capacity. Amazon EC2 Auto Scaling supports ``DesiredCapacityType`` for attribute-based instance type selection only. For more information, see &#91;Creating an Auto Scaling group using attribute-based instance type selection&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;create-asg-instance-type-requirements.html) in the *Amazon EC2 Auto Scaling User Guide*.&lt;br&#x2F;&gt; By default, Amazon EC2 Auto Scaling specifies ``units``, which translates into number of instances.&lt;br&#x2F;&gt; Valid values: ``units`` | ``vcpu`` | ``memory-mib``</td></tr>
<tr><td><CopyableCode code="placement_group" /></td><td><code>string</code></td><td>The name of the placement group into which to launch your instances. For more information, see &#91;Placement groups&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;placement-groups.html) in the *Amazon EC2 User Guide for Linux Instances*.&lt;br&#x2F;&gt;  A *cluster* placement group is a logical grouping of instances within a single Availability Zone. You cannot specify multiple Availability Zones and a cluster placement group.</td></tr>
<tr><td><CopyableCode code="health_check_type" /></td><td><code>string</code></td><td>A comma-separated value string of one or more health check types.&lt;br&#x2F;&gt; The valid values are ``EC2``, ``ELB``, and ``VPC_LATTICE``. ``EC2`` is the default health check and cannot be disabled. For more information, see &#91;Health checks for Auto Scaling instances&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;healthcheck.html) in the *Amazon EC2 Auto Scaling User Guide*.&lt;br&#x2F;&gt; Only specify ``EC2`` if you must clear a value that was previously set.</td></tr>
<tr><td><CopyableCode code="max_instance_lifetime" /></td><td><code>integer</code></td><td>The maximum amount of time, in seconds, that an instance can be in service. The default is null. If specified, the value must be either 0 or a number equal to or greater than 86,400 seconds (1 day). For more information, see &#91;Replacing Auto Scaling instances based on maximum instance lifetime&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;asg-max-instance-lifetime.html) in the *Amazon EC2 Auto Scaling User Guide*.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
lifecycle_hook_specification_list,
load_balancer_names,
launch_configuration_name,
service_linked_role_arn,
target_group_arns,
cooldown,
notification_configurations,
desired_capacity,
health_check_grace_period,
default_instance_warmup,
new_instances_protected_from_scale_in,
launch_template,
mixed_instances_policy,
vpc_zone_identifier,
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
FROM aws.autoscaling.auto_scaling_group
WHERE region = 'us-east-1' AND data__Identifier = '<AutoScalingGroupName>';
```


## Permissions

To operate on the <code>auto_scaling_group</code> resource, the following permissions are required:

### Read
```json
autoscaling:Describe*,
managed-fleets:Get*
```

### Update
```json
autoscaling:UpdateAutoScalingGroup,
autoscaling:CreateOrUpdateTags,
autoscaling:DeleteTags,
autoscaling:Describe*,
autoscaling:EnableMetricsCollection,
autoscaling:DisableMetricsCollection,
autoscaling:PutNotificationConfiguration,
autoscaling:DeleteNotificationConfiguration,
autoscaling:DetachLoadBalancerTargetGroups,
autoscaling:AttachLoadBalancerTargetGroups,
autoscaling:AttachLoadBalancers,
autoscaling:DetachLoadBalancers,
autoscaling:AttachTrafficSources,
autoscaling:DetachTrafficSources,
autoscaling:DeleteLifecycleHook,
autoscaling:PutLifecycleHook,
cloudwatch:PutMetricAlarm,
ec2:Describe*,
ec2:Get*,
ec2:RunInstances,
elasticloadbalancing:Describe*,
iam:CreateServiceLinkedRole,
iam:PassRole,
managed-fleets:Get*,
managed-fleets:RegisterAutoScalingGroup,
managed-fleets:DeregisterAutoScalingGroup,
managed-fleets:UpdateAutoScalingGroup,
ssm:Get*
```


---
title: game_server_group
hide_title: false
hide_table_of_contents: false
keywords:
  - game_server_group
  - gamelift
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>game_server_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>game_server_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>game_server_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.gamelift.game_server_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>auto_scaling_group_arn</code></td><td><code>string</code></td><td>A generated unique ID for the EC2 Auto Scaling group that is associated with this game server group.</td></tr>
<tr><td><code>auto_scaling_policy</code></td><td><code>object</code></td><td>Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting</td></tr>
<tr><td><code>balancing_strategy</code></td><td><code>string</code></td><td>The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.</td></tr>
<tr><td><code>delete_option</code></td><td><code>string</code></td><td>The type of delete to perform.</td></tr>
<tr><td><code>game_server_group_arn</code></td><td><code>string</code></td><td>A generated unique ID for the game server group.</td></tr>
<tr><td><code>game_server_group_name</code></td><td><code>string</code></td><td>An identifier for the new game server group.</td></tr>
<tr><td><code>game_server_protection_policy</code></td><td><code>string</code></td><td>A flag that indicates whether instances in the game server group are protected from early termination.</td></tr>
<tr><td><code>instance_definitions</code></td><td><code>array</code></td><td>A set of EC2 instance types to use when creating instances in the group.</td></tr>
<tr><td><code>launch_template</code></td><td><code>object</code></td><td>The EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group.</td></tr>
<tr><td><code>max_size</code></td><td><code>number</code></td><td>The maximum number of instances allowed in the EC2 Auto Scaling group.</td></tr>
<tr><td><code>min_size</code></td><td><code>number</code></td><td>The minimum number of instances allowed in the EC2 Auto Scaling group.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of labels to assign to the new game server group resource.</td></tr>
<tr><td><code>vpc_subnets</code></td><td><code>array</code></td><td>A list of virtual private cloud (VPC) subnets to use with instances in the game server group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>game_server_group</code> resource, the following permissions are required:

### Read
<pre>
gamelift:DescribeGameServerGroup</pre>

### Update
<pre>
gamelift:UpdateGameServerGroup,
iam:assumeRole,
iam:PassRole,
autoscaling:DescribeAutoScalingGroups,
autoscaling:UpdateAutoScalingGroup,
autoscaling:SetInstanceProtection</pre>

### Delete
<pre>
gamelift:DeleteGameServerGroup,
gamelift:DescribeGameServerGroup,
iam:assumeRole,
iam:PassRole,
iam:CreateServiceLinkedRole,
ec2:DescribeAvailabilityZones,
ec2:DescribeSubnets,
ec2:DescribeLaunchTemplateVersions,
autoscaling:CreateAutoScalingGroup,
autoscaling:DescribeLifecycleHooks,
autoscaling:DescribeNotificationConfigurations,
autoscaling:DescribeAutoScalingGroups,
autoscaling:ExitStandby,
autoscaling:PutLifecycleHook,
autoscaling:PutScalingPolicy,
autoscaling:ResumeProcesses,
autoscaling:SetInstanceProtection,
autoscaling:UpdateAutoScalingGroup,
autoscaling:DeleteAutoScalingGroup,
events:PutRule,
events:PutTargets</pre>


## Example
```sql
SELECT
region,
auto_scaling_group_arn,
auto_scaling_policy,
balancing_strategy,
delete_option,
game_server_group_arn,
game_server_group_name,
game_server_protection_policy,
instance_definitions,
launch_template,
max_size,
min_size,
role_arn,
tags,
vpc_subnets
FROM awscc.gamelift.game_server_group
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;GameServerGroupArn&gt;'
```

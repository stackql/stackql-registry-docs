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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>game_server_group</code> resource, use <code>game_server_groups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>game_server_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::GameServerGroup resource creates an Amazon GameLift (GameLift) GameServerGroup.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.game_server_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="auto_scaling_group_arn" /></td><td><code>string</code></td><td>A generated unique ID for the EC2 Auto Scaling group that is associated with this game server group.</td></tr>
<tr><td><CopyableCode code="auto_scaling_policy" /></td><td><code>object</code></td><td>Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.</td></tr>
<tr><td><CopyableCode code="balancing_strategy" /></td><td><code>string</code></td><td>The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.</td></tr>
<tr><td><CopyableCode code="delete_option" /></td><td><code>string</code></td><td>The type of delete to perform.</td></tr>
<tr><td><CopyableCode code="game_server_group_arn" /></td><td><code>string</code></td><td>A generated unique ID for the game server group.</td></tr>
<tr><td><CopyableCode code="game_server_group_name" /></td><td><code>string</code></td><td>An identifier for the new game server group.</td></tr>
<tr><td><CopyableCode code="game_server_protection_policy" /></td><td><code>string</code></td><td>A flag that indicates whether instances in the game server group are protected from early termination.</td></tr>
<tr><td><CopyableCode code="instance_definitions" /></td><td><code>array</code></td><td>A set of EC2 instance types to use when creating instances in the group.</td></tr>
<tr><td><CopyableCode code="launch_template" /></td><td><code>object</code></td><td>The EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.</td></tr>
<tr><td><CopyableCode code="max_size" /></td><td><code>number</code></td><td>The maximum number of instances allowed in the EC2 Auto Scaling group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.</td></tr>
<tr><td><CopyableCode code="min_size" /></td><td><code>number</code></td><td>The minimum number of instances allowed in the EC2 Auto Scaling group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of labels to assign to the new game server group resource. Updating game server group tags with CloudFormation will not take effect. Please update this property using AWS GameLift APIs instead.</td></tr>
<tr><td><CopyableCode code="vpc_subnets" /></td><td><code>array</code></td><td>A list of virtual private cloud (VPC) subnets to use with instances in the game server group. Updating this game server group property will not take effect for the created EC2 Auto Scaling group, please update the EC2 Auto Scaling group directly after creating the resource.</td></tr>
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
FROM aws.gamelift.game_server_group
WHERE data__Identifier = '<GameServerGroupArn>';
```

## Permissions

To operate on the <code>game_server_group</code> resource, the following permissions are required:

### Read
```json
gamelift:DescribeGameServerGroup
```

### Update
```json
gamelift:UpdateGameServerGroup,
iam:assumeRole,
iam:PassRole,
autoscaling:DescribeAutoScalingGroups,
autoscaling:UpdateAutoScalingGroup,
autoscaling:SetInstanceProtection
```

### Delete
```json
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
events:PutTargets
```


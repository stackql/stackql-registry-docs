---
title: game_server_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - game_server_groups
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
Retrieves a list of <code>game_server_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>game_server_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::GameServerGroup resource creates an Amazon GameLift (GameLift) GameServerGroup.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.gamelift.game_server_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>game_server_group_arn</code></td><td><code>undefined</code></td><td>A generated unique ID for the game server group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
game_server_group_arn
FROM aws.gamelift.game_server_groups
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>game_server_groups</code> resource, the following permissions are required:

### Create
```json
gamelift:CreateGameServerGroup,
gamelift:TagResource,
gamelift:DescribeGameServerGroup,
iam:assumeRole,
iam:PassRole,
iam:CreateServiceLinkedRole,
ec2:DescribeAvailabilityZones,
ec2:DescribeSubnets,
ec2:RunInstances,
ec2:CreateTags,
ec2:DescribeLaunchTemplateVersions,
autoscaling:CreateAutoScalingGroup,
autoscaling:DescribeLifecycleHooks,
autoscaling:DescribeNotificationConfigurations,
autoscaling:CreateAutoScalingGroup,
autoscaling:CreateOrUpdateTags,
autoscaling:DescribeAutoScalingGroups,
autoscaling:ExitStandby,
autoscaling:PutLifecycleHook,
autoscaling:PutScalingPolicy,
autoscaling:ResumeProcesses,
autoscaling:SetInstanceProtection,
autoscaling:UpdateAutoScalingGroup,
events:PutRule,
events:PutTargets
```

### List
```json
gamelift:ListGameServerGroups
```


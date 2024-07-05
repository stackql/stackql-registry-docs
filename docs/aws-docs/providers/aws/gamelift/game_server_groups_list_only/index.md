---
title: game_server_groups_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - game_server_groups_list_only
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>game_server_groups</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/game_server_groups/"><code>game_server_groups</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>game_server_groups_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::GameServerGroup resource creates an Amazon GameLift (GameLift) GameServerGroup.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.game_server_groups_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="auto_scaling_group_arn" /></td><td><code>string</code></td><td>A generated unique ID for the EC2 Auto Scaling group that is associated with this game server group.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>game_server_groups</code> in a region.
```sql
SELECT
region,
game_server_group_arn
FROM aws.gamelift.game_server_groups_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>game_server_groups_list_only</code> resource, see <a href="/providers/aws/gamelift/game_server_groups/#permissions"><code>game_server_groups</code></a>



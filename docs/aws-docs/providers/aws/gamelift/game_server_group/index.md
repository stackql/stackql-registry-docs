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
<tr><td><b>Id</b></td><td><code>aws.gamelift.game_server_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AutoScalingGroupArn</code></td><td><code>undefined</code></td><td>A generated unique ID for the EC2 Auto Scaling group that is associated with this game server group.</td></tr><tr><td><code>AutoScalingPolicy</code></td><td><code>undefined</code></td><td>Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting</td></tr><tr><td><code>BalancingStrategy</code></td><td><code>undefined</code></td><td>The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.</td></tr><tr><td><code>DeleteOption</code></td><td><code>undefined</code></td><td>The type of delete to perform.</td></tr><tr><td><code>GameServerGroupArn</code></td><td><code>undefined</code></td><td>A generated unique ID for the game server group.</td></tr><tr><td><code>GameServerGroupName</code></td><td><code>undefined</code></td><td>An identifier for the new game server group.</td></tr><tr><td><code>GameServerProtectionPolicy</code></td><td><code>undefined</code></td><td>A flag that indicates whether instances in the game server group are protected from early termination.</td></tr><tr><td><code>InstanceDefinitions</code></td><td><code>undefined</code></td><td>A set of EC2 instance types to use when creating instances in the group.</td></tr><tr><td><code>LaunchTemplate</code></td><td><code>undefined</code></td><td>The EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group.</td></tr><tr><td><code>MaxSize</code></td><td><code>undefined</code></td><td>The maximum number of instances allowed in the EC2 Auto Scaling group.</td></tr><tr><td><code>MinSize</code></td><td><code>undefined</code></td><td>The minimum number of instances allowed in the EC2 Auto Scaling group.</td></tr><tr><td><code>RoleArn</code></td><td><code>undefined</code></td><td>The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.</td></tr><tr><td><code>Tags</code></td><td><code>undefined</code></td><td>A list of labels to assign to the new game server group resource.</td></tr><tr><td><code>VpcSubnets</code></td><td><code>undefined</code></td><td>A list of virtual private cloud (VPC) subnets to use with instances in the game server group.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.gamelift.game_server_group
WHERE region = 'us-east-1' AND data__Identifier = '{GameServerGroupArn}'
</pre>

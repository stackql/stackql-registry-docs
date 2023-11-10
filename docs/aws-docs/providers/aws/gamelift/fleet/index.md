---
title: fleet
hide_title: false
hide_table_of_contents: false
keywords:
  - fleet
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
Gets an individual <code>fleet</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleet</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>fleet</td></tr>
<tr><td><b>Id</b></td><td><code>aws.gamelift.fleet</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>anywhere_configuration</code></td><td><code>undefined</code></td><td>Configuration for Anywhere fleet.</td></tr>
<tr><td><code>certificate_configuration</code></td><td><code>object</code></td><td>Indicates whether to generate a TLS&#x2F;SSL certificate for the new fleet. TLS certificates are used for encrypting traffic between game clients and game servers running on GameLift. If this parameter is not set, certificate generation is disabled. This fleet setting cannot be changed once the fleet is created.</td></tr>
<tr><td><code>compute_type</code></td><td><code>string</code></td><td>ComputeType to differentiate EC2 hardware managed by GameLift and Anywhere hardware managed by the customer.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A human-readable description of a fleet.</td></tr>
<tr><td><code>desired_ec2_instances</code></td><td><code>integer</code></td><td>&#91;DEPRECATED&#93; The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.</td></tr>
<tr><td><code>e_c2_inbound_permissions</code></td><td><code>array</code></td><td>A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift server.</td></tr>
<tr><td><code>e_c2_instance_type</code></td><td><code>string</code></td><td>The name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions.</td></tr>
<tr><td><code>fleet_type</code></td><td><code>string</code></td><td>Indicates whether to use On-Demand instances or Spot instances for this fleet. If empty, the default is ON_DEMAND. Both categories of instances use identical hardware and configurations based on the instance type selected for this fleet.</td></tr>
<tr><td><code>instance_role_ar_n</code></td><td><code>string</code></td><td>A unique identifier for an AWS IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN from the IAM dashboard in the AWS Management Console.</td></tr>
<tr><td><code>locations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>log_paths</code></td><td><code>array</code></td><td>This parameter is no longer used. When hosting a custom game build, specify where Amazon GameLift should store log files using the Amazon GameLift server API call ProcessReady()</td></tr>
<tr><td><code>max_size</code></td><td><code>integer</code></td><td>&#91;DEPRECATED&#93; The maximum value that is allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "1". Once the fleet is active, you can change this value.</td></tr>
<tr><td><code>metric_groups</code></td><td><code>array</code></td><td>The name of an Amazon CloudWatch metric group. A metric group aggregates the metrics for all fleets in the group. Specify a string containing the metric group name. You can use an existing name or use a new name to create a new metric group. Currently, this parameter can have only one string.</td></tr>
<tr><td><code>min_size</code></td><td><code>integer</code></td><td>&#91;DEPRECATED&#93; The minimum value allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "0". After the fleet is active, you can change this value.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A descriptive label that is associated with a fleet. Fleet names do not need to be unique.</td></tr>
<tr><td><code>new_game_session_protection_policy</code></td><td><code>string</code></td><td>A game session protection policy to apply to all game sessions hosted on instances in this fleet. When protected, active game sessions cannot be terminated during a scale-down event. If this parameter is not set, instances in this fleet default to no protection. You can change a fleet's protection policy to affect future game sessions on the fleet. You can also set protection for individual game sessions.</td></tr>
<tr><td><code>peer_vpc_aws_account_id</code></td><td><code>string</code></td><td>A unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift fleet with. You can find your account ID in the AWS Management Console under account settings.</td></tr>
<tr><td><code>peer_vpc_id</code></td><td><code>string</code></td><td>A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the VPC Dashboard in the AWS Management Console.</td></tr>
<tr><td><code>resource_creation_limit_policy</code></td><td><code>object</code></td><td>A policy that limits the number of game sessions an individual player can create over a span of time for this fleet.</td></tr>
<tr><td><code>fleet_id</code></td><td><code>string</code></td><td>Unique fleet ID</td></tr>
<tr><td><code>build_id</code></td><td><code>string</code></td><td>A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.</td></tr>
<tr><td><code>script_id</code></td><td><code>string</code></td><td>A unique identifier for a Realtime script to be deployed on a new Realtime Servers fleet. The script must have been successfully uploaded to Amazon GameLift. This fleet setting cannot be changed once the fleet is created.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Note: It is not currently possible to use the !Ref command to reference a script created with a CloudFormation template for the fleet property ScriptId. Instead, use Fn::GetAtt Script.Arn or Fn::GetAtt Script.Id to retrieve either of these properties as input for ScriptId. Alternatively, enter a ScriptId string manually.</td></tr>
<tr><td><code>runtime_configuration</code></td><td><code>object</code></td><td>Instructions for launching server processes on each instance in the fleet. Server processes run either a custom game build executable or a Realtime script. The runtime configuration defines the server executables or launch script file, launch parameters, and the number of processes to run concurrently on each instance. When creating a fleet, the runtime configuration must have at least one server process configuration; otherwise the request fails with an invalid request exception.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;This parameter is required unless the parameters ServerLaunchPath and ServerLaunchParameters are defined. Runtime configuration has replaced these parameters, but fleets that use them will continue to work.</td></tr>
<tr><td><code>server_launch_parameters</code></td><td><code>string</code></td><td>This parameter is no longer used but is retained for backward compatibility. Instead, specify server launch parameters in the RuntimeConfiguration parameter. A request must specify either a runtime configuration or values for both ServerLaunchParameters and ServerLaunchPath.</td></tr>
<tr><td><code>server_launch_path</code></td><td><code>string</code></td><td>This parameter is no longer used. Instead, specify a server launch path using the RuntimeConfiguration parameter. Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
anywhere_configuration,
certificate_configuration,
compute_type,
description,
desired_ec2_instances,
e_c2_inbound_permissions,
e_c2_instance_type,
fleet_type,
instance_role_ar_n,
locations,
log_paths,
max_size,
metric_groups,
min_size,
name,
new_game_session_protection_policy,
peer_vpc_aws_account_id,
peer_vpc_id,
resource_creation_limit_policy,
fleet_id,
build_id,
script_id,
runtime_configuration,
server_launch_parameters,
server_launch_path
FROM aws.gamelift.fleet
WHERE region = 'us-east-1'
AND data__Identifier = '<FleetId>'
```

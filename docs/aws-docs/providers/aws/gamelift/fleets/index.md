---
title: fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - fleets
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

Creates, updates, deletes or gets a <code>fleet</code> resource or lists <code>fleets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::Fleet resource creates an Amazon GameLift (GameLift) fleet to host game servers. A fleet is a set of EC2 or Anywhere instances, each of which can host multiple game sessions.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.fleets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="scaling_policies" /></td><td><code>array</code></td><td>A list of rules that control how a fleet is scaled.</td></tr>
<tr><td><CopyableCode code="anywhere_configuration" /></td><td><code>undefined</code></td><td>Configuration for Anywhere fleet.</td></tr>
<tr><td><CopyableCode code="apply_capacity" /></td><td><code>string</code></td><td>Determines whether to apply fleet or location capacities on fleet creation.</td></tr>
<tr><td><CopyableCode code="certificate_configuration" /></td><td><code>object</code></td><td>Indicates whether to generate a TLS/SSL certificate for the new fleet. TLS certificates are used for encrypting traffic between game clients and game servers running on GameLift. If this parameter is not set, certificate generation is disabled. This fleet setting cannot be changed once the fleet is created.</td></tr>
<tr><td><CopyableCode code="compute_type" /></td><td><code>string</code></td><td>ComputeType to differentiate EC2 hardware managed by GameLift and Anywhere hardware managed by the customer.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A human-readable description of a fleet.</td></tr>
<tr><td><CopyableCode code="desired_ec2_instances" /></td><td><code>integer</code></td><td>&#91;DEPRECATED&#93; The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.</td></tr>
<tr><td><CopyableCode code="e_c2_inbound_permissions" /></td><td><code>array</code></td><td>A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an Amazon GameLift server.</td></tr>
<tr><td><CopyableCode code="e_c2_instance_type" /></td><td><code>string</code></td><td>The name of an EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Amazon GameLift supports the following EC2 instance types. See Amazon EC2 Instance Types for detailed descriptions.</td></tr>
<tr><td><CopyableCode code="fleet_type" /></td><td><code>string</code></td><td>Indicates whether to use On-Demand instances or Spot instances for this fleet. If empty, the default is ON_DEMAND. Both categories of instances use identical hardware and configurations based on the instance type selected for this fleet.</td></tr>
<tr><td><CopyableCode code="instance_role_arn" /></td><td><code>string</code></td><td>A unique identifier for an AWS IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN from the IAM dashboard in the AWS Management Console.</td></tr>
<tr><td><CopyableCode code="instance_role_credentials_provider" /></td><td><code>string</code></td><td>Credentials provider implementation that loads credentials from the Amazon EC2 Instance Metadata Service.</td></tr>
<tr><td><CopyableCode code="locations" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="log_paths" /></td><td><code>array</code></td><td>This parameter is no longer used. When hosting a custom game build, specify where Amazon GameLift should store log files using the Amazon GameLift server API call ProcessReady()</td></tr>
<tr><td><CopyableCode code="max_size" /></td><td><code>integer</code></td><td>&#91;DEPRECATED&#93; The maximum value that is allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "1". Once the fleet is active, you can change this value.</td></tr>
<tr><td><CopyableCode code="metric_groups" /></td><td><code>array</code></td><td>The name of an Amazon CloudWatch metric group. A metric group aggregates the metrics for all fleets in the group. Specify a string containing the metric group name. You can use an existing name or use a new name to create a new metric group. Currently, this parameter can have only one string.</td></tr>
<tr><td><CopyableCode code="min_size" /></td><td><code>integer</code></td><td>&#91;DEPRECATED&#93; The minimum value allowed for the fleet's instance count. When creating a new fleet, GameLift automatically sets this value to "0". After the fleet is active, you can change this value.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A descriptive label that is associated with a fleet. Fleet names do not need to be unique.</td></tr>
<tr><td><CopyableCode code="new_game_session_protection_policy" /></td><td><code>string</code></td><td>A game session protection policy to apply to all game sessions hosted on instances in this fleet. When protected, active game sessions cannot be terminated during a scale-down event. If this parameter is not set, instances in this fleet default to no protection. You can change a fleet's protection policy to affect future game sessions on the fleet. You can also set protection for individual game sessions.</td></tr>
<tr><td><CopyableCode code="peer_vpc_aws_account_id" /></td><td><code>string</code></td><td>A unique identifier for the AWS account with the VPC that you want to peer your Amazon GameLift fleet with. You can find your account ID in the AWS Management Console under account settings.</td></tr>
<tr><td><CopyableCode code="peer_vpc_id" /></td><td><code>string</code></td><td>A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the VPC Dashboard in the AWS Management Console.</td></tr>
<tr><td><CopyableCode code="resource_creation_limit_policy" /></td><td><code>object</code></td><td>A policy that limits the number of game sessions an individual player can create over a span of time for this fleet.</td></tr>
<tr><td><CopyableCode code="fleet_id" /></td><td><code>string</code></td><td>Unique fleet ID</td></tr>
<tr><td><CopyableCode code="build_id" /></td><td><code>string</code></td><td>A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.</td></tr>
<tr><td><CopyableCode code="script_id" /></td><td><code>string</code></td><td>A unique identifier for a Realtime script to be deployed on a new Realtime Servers fleet. The script must have been successfully uploaded to Amazon GameLift. This fleet setting cannot be changed once the fleet is created.<br />Note: It is not currently possible to use the !Ref command to reference a script created with a CloudFormation template for the fleet property ScriptId. Instead, use Fn::GetAtt Script.Arn or Fn::GetAtt Script.Id to retrieve either of these properties as input for ScriptId. Alternatively, enter a ScriptId string manually.</td></tr>
<tr><td><CopyableCode code="runtime_configuration" /></td><td><code>object</code></td><td>Instructions for launching server processes on each instance in the fleet. Server processes run either a custom game build executable or a Realtime script. The runtime configuration defines the server executables or launch script file, launch parameters, and the number of processes to run concurrently on each instance. When creating a fleet, the runtime configuration must have at least one server process configuration; otherwise the request fails with an invalid request exception.<br />This parameter is required unless the parameters ServerLaunchPath and ServerLaunchParameters are defined. Runtime configuration has replaced these parameters, but fleets that use them will continue to work.</td></tr>
<tr><td><CopyableCode code="server_launch_parameters" /></td><td><code>string</code></td><td>This parameter is no longer used but is retained for backward compatibility. Instead, specify server launch parameters in the RuntimeConfiguration parameter. A request must specify either a runtime configuration or values for both ServerLaunchParameters and ServerLaunchPath.</td></tr>
<tr><td><CopyableCode code="server_launch_path" /></td><td><code>string</code></td><td>This parameter is no longer used. Instead, specify a server launch path using the RuntimeConfiguration parameter. Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html"><code>AWS::GameLift::Fleet</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="Name, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>fleets</code> in a region.
```sql
SELECT
region,
scaling_policies,
anywhere_configuration,
apply_capacity,
certificate_configuration,
compute_type,
description,
desired_ec2_instances,
e_c2_inbound_permissions,
e_c2_instance_type,
fleet_type,
instance_role_arn,
instance_role_credentials_provider,
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
FROM aws.gamelift.fleets
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>fleet</code>.
```sql
SELECT
region,
scaling_policies,
anywhere_configuration,
apply_capacity,
certificate_configuration,
compute_type,
description,
desired_ec2_instances,
e_c2_inbound_permissions,
e_c2_instance_type,
fleet_type,
instance_role_arn,
instance_role_credentials_provider,
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
FROM aws.gamelift.fleets
WHERE region = 'us-east-1' AND data__Identifier = '<FleetId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>fleet</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.gamelift.fleets (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.gamelift.fleets (
 ScalingPolicies,
 AnywhereConfiguration,
 ApplyCapacity,
 CertificateConfiguration,
 ComputeType,
 Description,
 DesiredEC2Instances,
 EC2InboundPermissions,
 EC2InstanceType,
 FleetType,
 InstanceRoleARN,
 InstanceRoleCredentialsProvider,
 Locations,
 LogPaths,
 MaxSize,
 MetricGroups,
 MinSize,
 Name,
 NewGameSessionProtectionPolicy,
 PeerVpcAwsAccountId,
 PeerVpcId,
 ResourceCreationLimitPolicy,
 BuildId,
 ScriptId,
 RuntimeConfiguration,
 ServerLaunchParameters,
 ServerLaunchPath,
 region
)
SELECT 
 '{{ ScalingPolicies }}',
 '{{ AnywhereConfiguration }}',
 '{{ ApplyCapacity }}',
 '{{ CertificateConfiguration }}',
 '{{ ComputeType }}',
 '{{ Description }}',
 '{{ DesiredEC2Instances }}',
 '{{ EC2InboundPermissions }}',
 '{{ EC2InstanceType }}',
 '{{ FleetType }}',
 '{{ InstanceRoleARN }}',
 '{{ InstanceRoleCredentialsProvider }}',
 '{{ Locations }}',
 '{{ LogPaths }}',
 '{{ MaxSize }}',
 '{{ MetricGroups }}',
 '{{ MinSize }}',
 '{{ Name }}',
 '{{ NewGameSessionProtectionPolicy }}',
 '{{ PeerVpcAwsAccountId }}',
 '{{ PeerVpcId }}',
 '{{ ResourceCreationLimitPolicy }}',
 '{{ BuildId }}',
 '{{ ScriptId }}',
 '{{ RuntimeConfiguration }}',
 '{{ ServerLaunchParameters }}',
 '{{ ServerLaunchPath }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: fleet
    props:
      - name: ScalingPolicies
        value:
          - ComparisonOperator: '{{ ComparisonOperator }}'
            EvaluationPeriods: '{{ EvaluationPeriods }}'
            Location:
              LocationName: '{{ LocationName }}'
              Tags:
                - Key: '{{ Key }}'
                  Value: '{{ Value }}'
            MetricName: '{{ MetricName }}'
            Name: '{{ Name }}'
            PolicyType: '{{ PolicyType }}'
            ScalingAdjustment: '{{ ScalingAdjustment }}'
            ScalingAdjustmentType: '{{ ScalingAdjustmentType }}'
            Status: '{{ Status }}'
            TargetConfiguration:
              TargetValue: null
            Threshold: null
            UpdateStatus: '{{ UpdateStatus }}'
      - name: AnywhereConfiguration
        value: null
      - name: ApplyCapacity
        value: '{{ ApplyCapacity }}'
      - name: CertificateConfiguration
        value:
          CertificateType: '{{ CertificateType }}'
      - name: ComputeType
        value: '{{ ComputeType }}'
      - name: Description
        value: '{{ Description }}'
      - name: DesiredEC2Instances
        value: '{{ DesiredEC2Instances }}'
      - name: EC2InboundPermissions
        value:
          - FromPort: '{{ FromPort }}'
            IpRange: '{{ IpRange }}'
            Protocol: '{{ Protocol }}'
            ToPort: '{{ ToPort }}'
      - name: EC2InstanceType
        value: '{{ EC2InstanceType }}'
      - name: FleetType
        value: '{{ FleetType }}'
      - name: InstanceRoleARN
        value: '{{ InstanceRoleARN }}'
      - name: InstanceRoleCredentialsProvider
        value: '{{ InstanceRoleCredentialsProvider }}'
      - name: Locations
        value:
          - Location: null
            LocationCapacity:
              DesiredEC2Instances: '{{ DesiredEC2Instances }}'
              MinSize: '{{ MinSize }}'
              MaxSize: '{{ MaxSize }}'
      - name: LogPaths
        value:
          - '{{ LogPaths[0] }}'
      - name: MaxSize
        value: '{{ MaxSize }}'
      - name: MetricGroups
        value:
          - '{{ MetricGroups[0] }}'
      - name: MinSize
        value: '{{ MinSize }}'
      - name: Name
        value: '{{ Name }}'
      - name: NewGameSessionProtectionPolicy
        value: '{{ NewGameSessionProtectionPolicy }}'
      - name: PeerVpcAwsAccountId
        value: '{{ PeerVpcAwsAccountId }}'
      - name: PeerVpcId
        value: '{{ PeerVpcId }}'
      - name: ResourceCreationLimitPolicy
        value:
          NewGameSessionsPerCreator: '{{ NewGameSessionsPerCreator }}'
          PolicyPeriodInMinutes: '{{ PolicyPeriodInMinutes }}'
      - name: BuildId
        value: '{{ BuildId }}'
      - name: ScriptId
        value: '{{ ScriptId }}'
      - name: RuntimeConfiguration
        value:
          GameSessionActivationTimeoutSeconds: '{{ GameSessionActivationTimeoutSeconds }}'
          MaxConcurrentGameSessionActivations: '{{ MaxConcurrentGameSessionActivations }}'
          ServerProcesses:
            - ConcurrentExecutions: '{{ ConcurrentExecutions }}'
              LaunchPath: '{{ LaunchPath }}'
              Parameters: '{{ Parameters }}'
      - name: ServerLaunchParameters
        value: '{{ ServerLaunchParameters }}'
      - name: ServerLaunchPath
        value: '{{ ServerLaunchPath }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.gamelift.fleets
WHERE data__Identifier = '<FleetId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>fleets</code> resource, the following permissions are required:

### Create
```json
gamelift:CreateFleet,
gamelift:DescribeFleetAttributes,
gamelift:DescribeFleetLocationAttributes,
gamelift:UpdateFleetCapacity,
gamelift:DescribeFleetLocationCapacity,
gamelift:PutScalingPolicy,
gamelift:DescribeScalingPolicies
```

### Read
```json
gamelift:DescribeFleetAttributes,
gamelift:DescribeFleetLocationAttributes,
gamelift:DescribeFleetCapacity,
gamelift:DescribeFleetPortSettings,
gamelift:DescribeFleetUtilization,
gamelift:DescribeRuntimeConfiguration,
gamelift:DescribeEC2InstanceLimits,
gamelift:DescribeFleetEvents,
gamelift:DescribeScalingPolicies
```

### Update
```json
gamelift:UpdateFleetAttributes,
gamelift:CreateFleetLocations,
gamelift:DeleteFleetLocations,
gamelift:UpdateFleetCapacity,
gamelift:UpdateFleetPortSettings,
gamelift:UpdateRuntimeConfiguration,
gamelift:DescribeFleetLocationCapacity,
gamelift:DescribeFleetPortSettings,
gamelift:DescribeFleetLocationAttributes,
gamelift:PutScalingPolicy,
gamelift:DescribeScalingPolicies,
gamelift:DeleteScalingPolicy
```

### Delete
```json
gamelift:DeleteFleet,
gamelift:DescribeFleetLocationCapacity,
gamelift:DescribeScalingPolicies,
gamelift:DeleteScalingPolicy
```

### List
```json
gamelift:ListFleets
```

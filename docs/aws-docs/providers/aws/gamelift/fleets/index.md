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


Used to retrieve a list of <code>fleets</code> in a region or to create or delete a <code>fleets</code> resource, use <code>fleet</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::Fleet resource creates an Amazon GameLift (GameLift) fleet to host game servers. A fleet is a set of EC2 or Anywhere instances, each of which can host multiple game sessions.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.fleets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="fleet_id" /></td><td><code>string</code></td><td>Unique fleet ID</td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
fleet_id
FROM aws.gamelift.fleets
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
 Description,
 PeerVpcId,
 ApplyCapacity,
 EC2InboundPermissions,
 ComputeType,
 Name,
 AnywhereConfiguration,
 InstanceRoleARN,
 CertificateConfiguration,
 InstanceRoleCredentialsProvider,
 DesiredEC2Instances,
 ServerLaunchParameters,
 FleetType,
 Locations,
 NewGameSessionProtectionPolicy,
 ScriptId,
 MaxSize,
 RuntimeConfiguration,
 LogPaths,
 ServerLaunchPath,
 MinSize,
 PeerVpcAwsAccountId,
 MetricGroups,
 BuildId,
 ResourceCreationLimitPolicy,
 EC2InstanceType,
 region
)
SELECT 
 '{{ ScalingPolicies }}',
 '{{ Description }}',
 '{{ PeerVpcId }}',
 '{{ ApplyCapacity }}',
 '{{ EC2InboundPermissions }}',
 '{{ ComputeType }}',
 '{{ Name }}',
 '{{ AnywhereConfiguration }}',
 '{{ InstanceRoleARN }}',
 '{{ CertificateConfiguration }}',
 '{{ InstanceRoleCredentialsProvider }}',
 '{{ DesiredEC2Instances }}',
 '{{ ServerLaunchParameters }}',
 '{{ FleetType }}',
 '{{ Locations }}',
 '{{ NewGameSessionProtectionPolicy }}',
 '{{ ScriptId }}',
 '{{ MaxSize }}',
 '{{ RuntimeConfiguration }}',
 '{{ LogPaths }}',
 '{{ ServerLaunchPath }}',
 '{{ MinSize }}',
 '{{ PeerVpcAwsAccountId }}',
 '{{ MetricGroups }}',
 '{{ BuildId }}',
 '{{ ResourceCreationLimitPolicy }}',
 '{{ EC2InstanceType }}',
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
          - Status: '{{ Status }}'
            MetricName: '{{ MetricName }}'
            PolicyType: '{{ PolicyType }}'
            ComparisonOperator: '{{ ComparisonOperator }}'
            TargetConfiguration:
              TargetValue: null
            UpdateStatus: '{{ UpdateStatus }}'
            ScalingAdjustment: '{{ ScalingAdjustment }}'
            EvaluationPeriods: '{{ EvaluationPeriods }}'
            Location:
              LocationName: '{{ LocationName }}'
              Tags:
                - Key: '{{ Key }}'
                  Value: '{{ Value }}'
            Name: '{{ Name }}'
            ScalingAdjustmentType: '{{ ScalingAdjustmentType }}'
            Threshold: null
      - name: Description
        value: '{{ Description }}'
      - name: PeerVpcId
        value: '{{ PeerVpcId }}'
      - name: ApplyCapacity
        value: '{{ ApplyCapacity }}'
      - name: EC2InboundPermissions
        value:
          - IpRange: '{{ IpRange }}'
            FromPort: '{{ FromPort }}'
            ToPort: '{{ ToPort }}'
            Protocol: '{{ Protocol }}'
      - name: ComputeType
        value: '{{ ComputeType }}'
      - name: Name
        value: '{{ Name }}'
      - name: AnywhereConfiguration
        value: null
      - name: InstanceRoleARN
        value: '{{ InstanceRoleARN }}'
      - name: CertificateConfiguration
        value:
          CertificateType: '{{ CertificateType }}'
      - name: InstanceRoleCredentialsProvider
        value: '{{ InstanceRoleCredentialsProvider }}'
      - name: DesiredEC2Instances
        value: '{{ DesiredEC2Instances }}'
      - name: ServerLaunchParameters
        value: '{{ ServerLaunchParameters }}'
      - name: FleetType
        value: '{{ FleetType }}'
      - name: Locations
        value:
          - LocationCapacity:
              MinSize: '{{ MinSize }}'
              DesiredEC2Instances: '{{ DesiredEC2Instances }}'
              MaxSize: '{{ MaxSize }}'
            Location: null
      - name: NewGameSessionProtectionPolicy
        value: '{{ NewGameSessionProtectionPolicy }}'
      - name: ScriptId
        value: '{{ ScriptId }}'
      - name: MaxSize
        value: '{{ MaxSize }}'
      - name: RuntimeConfiguration
        value:
          ServerProcesses:
            - ConcurrentExecutions: '{{ ConcurrentExecutions }}'
              Parameters: '{{ Parameters }}'
              LaunchPath: '{{ LaunchPath }}'
          MaxConcurrentGameSessionActivations: '{{ MaxConcurrentGameSessionActivations }}'
          GameSessionActivationTimeoutSeconds: '{{ GameSessionActivationTimeoutSeconds }}'
      - name: LogPaths
        value:
          - '{{ LogPaths[0] }}'
      - name: ServerLaunchPath
        value: '{{ ServerLaunchPath }}'
      - name: MinSize
        value: '{{ MinSize }}'
      - name: PeerVpcAwsAccountId
        value: '{{ PeerVpcAwsAccountId }}'
      - name: MetricGroups
        value:
          - '{{ MetricGroups[0] }}'
      - name: BuildId
        value: '{{ BuildId }}'
      - name: ResourceCreationLimitPolicy
        value:
          PolicyPeriodInMinutes: '{{ PolicyPeriodInMinutes }}'
          NewGameSessionsPerCreator: '{{ NewGameSessionsPerCreator }}'
      - name: EC2InstanceType
        value: '{{ EC2InstanceType }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

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

### List
```json
gamelift:ListFleets
```

### Delete
```json
gamelift:DeleteFleet,
gamelift:DescribeFleetLocationCapacity,
gamelift:DescribeScalingPolicies,
gamelift:DeleteScalingPolicy
```


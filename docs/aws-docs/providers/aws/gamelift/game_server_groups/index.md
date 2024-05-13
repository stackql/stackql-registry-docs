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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>game_server_groups</code> in a region or to create or delete a <code>game_server_groups</code> resource, use <code>game_server_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>game_server_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::GameServerGroup resource creates an Amazon GameLift (GameLift) GameServerGroup.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.game_server_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="game_server_group_arn" /></td><td><code>undefined</code></td><td>A generated unique ID for the game server group.</td></tr>
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
    <td><CopyableCode code="GameServerGroupName, InstanceDefinitions, RoleArn, region" /></td>
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
game_server_group_arn
FROM aws.gamelift.game_server_groups
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>game_server_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.gamelift.game_server_groups (
 GameServerGroupName,
 InstanceDefinitions,
 RoleArn,
 region
)
SELECT 
'{{ GameServerGroupName }}',
 '{{ InstanceDefinitions }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.gamelift.game_server_groups (
 AutoScalingPolicy,
 BalancingStrategy,
 DeleteOption,
 GameServerGroupName,
 GameServerProtectionPolicy,
 InstanceDefinitions,
 LaunchTemplate,
 MaxSize,
 MinSize,
 RoleArn,
 Tags,
 VpcSubnets,
 region
)
SELECT 
 '{{ AutoScalingPolicy }}',
 '{{ BalancingStrategy }}',
 '{{ DeleteOption }}',
 '{{ GameServerGroupName }}',
 '{{ GameServerProtectionPolicy }}',
 '{{ InstanceDefinitions }}',
 '{{ LaunchTemplate }}',
 '{{ MaxSize }}',
 '{{ MinSize }}',
 '{{ RoleArn }}',
 '{{ Tags }}',
 '{{ VpcSubnets }}',
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
  - name: game_server_group
    props:
      - name: AutoScalingPolicy
        value:
          EstimatedInstanceWarmup: null
          TargetTrackingConfiguration:
            TargetValue: null
      - name: BalancingStrategy
        value: '{{ BalancingStrategy }}'
      - name: DeleteOption
        value: '{{ DeleteOption }}'
      - name: GameServerGroupName
        value: '{{ GameServerGroupName }}'
      - name: GameServerProtectionPolicy
        value: '{{ GameServerProtectionPolicy }}'
      - name: InstanceDefinitions
        value:
          - InstanceType: '{{ InstanceType }}'
            WeightedCapacity: '{{ WeightedCapacity }}'
      - name: LaunchTemplate
        value:
          LaunchTemplateId: '{{ LaunchTemplateId }}'
          LaunchTemplateName: '{{ LaunchTemplateName }}'
          Version: '{{ Version }}'
      - name: MaxSize
        value: null
      - name: MinSize
        value: null
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: VpcSubnets
        value:
          - '{{ VpcSubnets[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.gamelift.game_server_groups
WHERE data__Identifier = '<GameServerGroupArn>'
AND region = 'us-east-1';
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

### List
```json
gamelift:ListGameServerGroups
```


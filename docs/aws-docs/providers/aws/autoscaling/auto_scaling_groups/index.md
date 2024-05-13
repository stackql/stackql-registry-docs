---
title: auto_scaling_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_scaling_groups
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


Used to retrieve a list of <code>auto_scaling_groups</code> in a region or to create or delete a <code>auto_scaling_groups</code> resource, use <code>auto_scaling_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auto_scaling_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::AutoScaling::AutoScalingGroup</code> resource defines an Amazon EC2 Auto Scaling group, which is a collection of Amazon EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management. &lt;br&#x2F;&gt; For more information about Amazon EC2 Auto Scaling, see the &#91;Amazon EC2 Auto Scaling User Guide&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;what-is-amazon-ec2-auto-scaling.html). &lt;br&#x2F;&gt;  Amazon EC2 Auto Scaling configures instances launched as part of an Auto Scaling group using either a &#91;launch template&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-ec2-launchtemplate.html) or a launch configuration. We strongly recommend that you do not use launch configurations. They do not provide full functionality for Amazon EC2 Auto Scaling or Amazon EC2. For more information, see &#91;Launch configurations&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;launch-configurations.html) and &#91;Migrate CloudFormation stacks from launch configurations to launch templates&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;migrate-launch-configurations-with-cloudformation.html) in the *Amazon EC2 Auto Scaling User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.autoscaling.auto_scaling_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="auto_scaling_group_name" /></td><td><code>string</code></td><td>The name of the Auto Scaling group. This name must be unique per Region per account.&lt;br&#x2F;&gt; The name can contain any ASCII character 33 to 126 including most punctuation characters, digits, and upper and lowercased letters.&lt;br&#x2F;&gt;  You cannot use a colon (:) in the name.</td></tr>
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
    <td><CopyableCode code="MinSize, MaxSize, region" /></td>
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
auto_scaling_group_name
FROM aws.autoscaling.auto_scaling_groups
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>auto_scaling_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.autoscaling.auto_scaling_groups (
 MaxSize,
 MinSize,
 region
)
SELECT 
'{{ MaxSize }}',
 '{{ MinSize }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.autoscaling.auto_scaling_groups (
 LifecycleHookSpecificationList,
 LoadBalancerNames,
 LaunchConfigurationName,
 ServiceLinkedRoleARN,
 TargetGroupARNs,
 Cooldown,
 NotificationConfigurations,
 DesiredCapacity,
 HealthCheckGracePeriod,
 DefaultInstanceWarmup,
 NewInstancesProtectedFromScaleIn,
 LaunchTemplate,
 MixedInstancesPolicy,
 VPCZoneIdentifier,
 Tags,
 Context,
 CapacityRebalance,
 InstanceId,
 AvailabilityZones,
 NotificationConfiguration,
 MetricsCollection,
 InstanceMaintenancePolicy,
 MaxSize,
 MinSize,
 TerminationPolicies,
 AutoScalingGroupName,
 DesiredCapacityType,
 PlacementGroup,
 HealthCheckType,
 MaxInstanceLifetime,
 region
)
SELECT 
 '{{ LifecycleHookSpecificationList }}',
 '{{ LoadBalancerNames }}',
 '{{ LaunchConfigurationName }}',
 '{{ ServiceLinkedRoleARN }}',
 '{{ TargetGroupARNs }}',
 '{{ Cooldown }}',
 '{{ NotificationConfigurations }}',
 '{{ DesiredCapacity }}',
 '{{ HealthCheckGracePeriod }}',
 '{{ DefaultInstanceWarmup }}',
 '{{ NewInstancesProtectedFromScaleIn }}',
 '{{ LaunchTemplate }}',
 '{{ MixedInstancesPolicy }}',
 '{{ VPCZoneIdentifier }}',
 '{{ Tags }}',
 '{{ Context }}',
 '{{ CapacityRebalance }}',
 '{{ InstanceId }}',
 '{{ AvailabilityZones }}',
 '{{ NotificationConfiguration }}',
 '{{ MetricsCollection }}',
 '{{ InstanceMaintenancePolicy }}',
 '{{ MaxSize }}',
 '{{ MinSize }}',
 '{{ TerminationPolicies }}',
 '{{ AutoScalingGroupName }}',
 '{{ DesiredCapacityType }}',
 '{{ PlacementGroup }}',
 '{{ HealthCheckType }}',
 '{{ MaxInstanceLifetime }}',
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
  - name: auto_scaling_group
    props:
      - name: LifecycleHookSpecificationList
        value:
          - LifecycleHookName: '{{ LifecycleHookName }}'
            LifecycleTransition: '{{ LifecycleTransition }}'
            HeartbeatTimeout: '{{ HeartbeatTimeout }}'
            NotificationMetadata: '{{ NotificationMetadata }}'
            DefaultResult: '{{ DefaultResult }}'
            NotificationTargetARN: '{{ NotificationTargetARN }}'
            RoleARN: '{{ RoleARN }}'
      - name: LoadBalancerNames
        value:
          - '{{ LoadBalancerNames[0] }}'
      - name: LaunchConfigurationName
        value: '{{ LaunchConfigurationName }}'
      - name: ServiceLinkedRoleARN
        value: '{{ ServiceLinkedRoleARN }}'
      - name: TargetGroupARNs
        value:
          - '{{ TargetGroupARNs[0] }}'
      - name: Cooldown
        value: '{{ Cooldown }}'
      - name: NotificationConfigurations
        value:
          - TopicARN:
              - '{{ TopicARN[0] }}'
            NotificationTypes:
              - '{{ NotificationTypes[0] }}'
      - name: DesiredCapacity
        value: '{{ DesiredCapacity }}'
      - name: HealthCheckGracePeriod
        value: '{{ HealthCheckGracePeriod }}'
      - name: DefaultInstanceWarmup
        value: '{{ DefaultInstanceWarmup }}'
      - name: NewInstancesProtectedFromScaleIn
        value: '{{ NewInstancesProtectedFromScaleIn }}'
      - name: LaunchTemplate
        value:
          LaunchTemplateName: '{{ LaunchTemplateName }}'
          Version: '{{ Version }}'
          LaunchTemplateId: '{{ LaunchTemplateId }}'
      - name: MixedInstancesPolicy
        value:
          InstancesDistribution:
            OnDemandAllocationStrategy: '{{ OnDemandAllocationStrategy }}'
            OnDemandBaseCapacity: '{{ OnDemandBaseCapacity }}'
            OnDemandPercentageAboveBaseCapacity: '{{ OnDemandPercentageAboveBaseCapacity }}'
            SpotInstancePools: '{{ SpotInstancePools }}'
            SpotAllocationStrategy: '{{ SpotAllocationStrategy }}'
            SpotMaxPrice: '{{ SpotMaxPrice }}'
          LaunchTemplate:
            LaunchTemplateSpecification: null
            Overrides:
              - LaunchTemplateSpecification: null
                WeightedCapacity: '{{ WeightedCapacity }}'
                InstanceRequirements:
                  LocalStorageTypes:
                    - '{{ LocalStorageTypes[0] }}'
                  InstanceGenerations:
                    - '{{ InstanceGenerations[0] }}'
                  NetworkInterfaceCount:
                    Min: '{{ Min }}'
                    Max: '{{ Max }}'
                  AcceleratorTypes:
                    - '{{ AcceleratorTypes[0] }}'
                  MemoryGiBPerVCpu:
                    Min: null
                    Max: null
                  AcceleratorManufacturers:
                    - '{{ AcceleratorManufacturers[0] }}'
                  ExcludedInstanceTypes:
                    - '{{ ExcludedInstanceTypes[0] }}'
                  VCpuCount:
                    Min: '{{ Min }}'
                    Max: '{{ Max }}'
                  AllowedInstanceTypes:
                    - '{{ AllowedInstanceTypes[0] }}'
                  LocalStorage: '{{ LocalStorage }}'
                  CpuManufacturers:
                    - '{{ CpuManufacturers[0] }}'
                  AcceleratorCount:
                    Min: '{{ Min }}'
                    Max: '{{ Max }}'
                  NetworkBandwidthGbps:
                    Min: null
                    Max: null
                  BareMetal: '{{ BareMetal }}'
                  RequireHibernateSupport: '{{ RequireHibernateSupport }}'
                  MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: '{{ MaxSpotPriceAsPercentageOfOptimalOnDemandPrice }}'
                  BaselineEbsBandwidthMbps:
                    Min: '{{ Min }}'
                    Max: '{{ Max }}'
                  SpotMaxPricePercentageOverLowestPrice: '{{ SpotMaxPricePercentageOverLowestPrice }}'
                  AcceleratorNames:
                    - '{{ AcceleratorNames[0] }}'
                  AcceleratorTotalMemoryMiB:
                    Min: '{{ Min }}'
                    Max: '{{ Max }}'
                  OnDemandMaxPricePercentageOverLowestPrice: '{{ OnDemandMaxPricePercentageOverLowestPrice }}'
                  BurstablePerformance: '{{ BurstablePerformance }}'
                  MemoryMiB:
                    Min: '{{ Min }}'
                    Max: '{{ Max }}'
                  TotalLocalStorageGB:
                    Min: null
                    Max: null
                InstanceType: '{{ InstanceType }}'
      - name: VPCZoneIdentifier
        value:
          - '{{ VPCZoneIdentifier[0] }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
            PropagateAtLaunch: '{{ PropagateAtLaunch }}'
      - name: Context
        value: '{{ Context }}'
      - name: CapacityRebalance
        value: '{{ CapacityRebalance }}'
      - name: InstanceId
        value: '{{ InstanceId }}'
      - name: AvailabilityZones
        value:
          - '{{ AvailabilityZones[0] }}'
      - name: NotificationConfiguration
        value: null
      - name: MetricsCollection
        value:
          - Metrics:
              - '{{ Metrics[0] }}'
            Granularity: '{{ Granularity }}'
      - name: InstanceMaintenancePolicy
        value:
          MaxHealthyPercentage: '{{ MaxHealthyPercentage }}'
          MinHealthyPercentage: '{{ MinHealthyPercentage }}'
      - name: MaxSize
        value: '{{ MaxSize }}'
      - name: MinSize
        value: '{{ MinSize }}'
      - name: TerminationPolicies
        value:
          - '{{ TerminationPolicies[0] }}'
      - name: AutoScalingGroupName
        value: '{{ AutoScalingGroupName }}'
      - name: DesiredCapacityType
        value: '{{ DesiredCapacityType }}'
      - name: PlacementGroup
        value: '{{ PlacementGroup }}'
      - name: HealthCheckType
        value: '{{ HealthCheckType }}'
      - name: MaxInstanceLifetime
        value: '{{ MaxInstanceLifetime }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.autoscaling.auto_scaling_groups
WHERE data__Identifier = '<AutoScalingGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>auto_scaling_groups</code> resource, the following permissions are required:

### Create
```json
autoscaling:CreateAutoScalingGroup,
autoscaling:UpdateAutoScalingGroup,
autoscaling:CreateOrUpdateTags,
autoscaling:Describe*,
autoscaling:EnableMetricsCollection,
autoscaling:PutNotificationConfiguration,
cloudwatch:PutMetricAlarm,
ec2:Describe*,
ec2:Get*,
ec2:RunInstances,
elasticloadbalancing:Describe*,
iam:CreateServiceLinkedRole,
iam:PassRole,
managed-fleets:Get*,
managed-fleets:CreateAutoScalingGroup,
managed-fleets:UpdateAutoScalingGroup,
ssm:Get*
```

### List
```json
autoscaling:Describe*
```

### Delete
```json
autoscaling:DeleteAutoScalingGroup,
autoscaling:UpdateAutoScalingGroup,
autoscaling:Describe*,
managed-fleets:Get*,
managed-fleets:DeleteAutoScalingGroup
```


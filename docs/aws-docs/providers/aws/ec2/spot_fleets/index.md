---
title: spot_fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - spot_fleets
  - ec2
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

Creates, updates, deletes or gets a <code>spot_fleet</code> resource or lists <code>spot_fleets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>spot_fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::SpotFleet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.spot_fleets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="spot_fleet_request_config_data" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-spotfleet.html"><code>AWS::EC2::SpotFleet</code></a>.

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
    <td><CopyableCode code="SpotFleetRequestConfigData, region" /></td>
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
Gets all <code>spot_fleets</code> in a region.
```sql
SELECT
region,
id,
spot_fleet_request_config_data
FROM aws.ec2.spot_fleets
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>spot_fleet</code>.
```sql
SELECT
region,
id,
spot_fleet_request_config_data
FROM aws.ec2.spot_fleets
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>spot_fleet</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.spot_fleets (
 SpotFleetRequestConfigData,
 region
)
SELECT 
'{{ SpotFleetRequestConfigData }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.spot_fleets (
 SpotFleetRequestConfigData,
 region
)
SELECT 
 '{{ SpotFleetRequestConfigData }}',
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
  - name: spot_fleet
    props:
      - name: SpotFleetRequestConfigData
        value:
          AllocationStrategy: '{{ AllocationStrategy }}'
          Context: '{{ Context }}'
          ExcessCapacityTerminationPolicy: '{{ ExcessCapacityTerminationPolicy }}'
          IamFleetRole: '{{ IamFleetRole }}'
          InstanceInterruptionBehavior: '{{ InstanceInterruptionBehavior }}'
          InstancePoolsToUseCount: '{{ InstancePoolsToUseCount }}'
          LaunchSpecifications:
            - BlockDeviceMappings:
                - DeviceName: '{{ DeviceName }}'
                  Ebs:
                    DeleteOnTermination: '{{ DeleteOnTermination }}'
                    Encrypted: '{{ Encrypted }}'
                    Iops: '{{ Iops }}'
                    SnapshotId: '{{ SnapshotId }}'
                    VolumeSize: '{{ VolumeSize }}'
                    VolumeType: '{{ VolumeType }}'
                  NoDevice: '{{ NoDevice }}'
                  VirtualName: '{{ VirtualName }}'
              EbsOptimized: '{{ EbsOptimized }}'
              IamInstanceProfile:
                Arn: '{{ Arn }}'
              ImageId: '{{ ImageId }}'
              InstanceType: '{{ InstanceType }}'
              KernelId: '{{ KernelId }}'
              KeyName: '{{ KeyName }}'
              Monitoring:
                Enabled: '{{ Enabled }}'
              NetworkInterfaces:
                - AssociatePublicIpAddress: '{{ AssociatePublicIpAddress }}'
                  DeleteOnTermination: '{{ DeleteOnTermination }}'
                  Description: '{{ Description }}'
                  DeviceIndex: '{{ DeviceIndex }}'
                  Groups:
                    - '{{ Groups[0] }}'
                  Ipv6AddressCount: '{{ Ipv6AddressCount }}'
                  Ipv6Addresses:
                    - Ipv6Address: '{{ Ipv6Address }}'
                  NetworkInterfaceId: '{{ NetworkInterfaceId }}'
                  PrivateIpAddresses:
                    - Primary: '{{ Primary }}'
                      PrivateIpAddress: '{{ PrivateIpAddress }}'
                  SecondaryPrivateIpAddressCount: '{{ SecondaryPrivateIpAddressCount }}'
                  SubnetId: '{{ SubnetId }}'
              Placement:
                AvailabilityZone: '{{ AvailabilityZone }}'
                GroupName: '{{ GroupName }}'
                Tenancy: '{{ Tenancy }}'
              RamdiskId: '{{ RamdiskId }}'
              SecurityGroups:
                - GroupId: '{{ GroupId }}'
              SpotPrice: '{{ SpotPrice }}'
              SubnetId: '{{ SubnetId }}'
              TagSpecifications:
                - ResourceType: '{{ ResourceType }}'
                  Tags:
                    - Key: '{{ Key }}'
                      Value: '{{ Value }}'
              UserData: '{{ UserData }}'
              WeightedCapacity: null
              InstanceRequirements:
                VCpuCount:
                  Min: '{{ Min }}'
                  Max: '{{ Max }}'
                MemoryMiB:
                  Min: '{{ Min }}'
                  Max: '{{ Max }}'
                CpuManufacturers:
                  - '{{ CpuManufacturers[0] }}'
                MemoryGiBPerVCpu:
                  Min: null
                  Max: null
                AllowedInstanceTypes:
                  - '{{ AllowedInstanceTypes[0] }}'
                ExcludedInstanceTypes:
                  - '{{ ExcludedInstanceTypes[0] }}'
                InstanceGenerations:
                  - '{{ InstanceGenerations[0] }}'
                SpotMaxPricePercentageOverLowestPrice: '{{ SpotMaxPricePercentageOverLowestPrice }}'
                OnDemandMaxPricePercentageOverLowestPrice: '{{ OnDemandMaxPricePercentageOverLowestPrice }}'
                MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: '{{ MaxSpotPriceAsPercentageOfOptimalOnDemandPrice }}'
                BareMetal: '{{ BareMetal }}'
                BurstablePerformance: '{{ BurstablePerformance }}'
                RequireHibernateSupport: '{{ RequireHibernateSupport }}'
                NetworkBandwidthGbps:
                  Min: null
                  Max: null
                NetworkInterfaceCount:
                  Min: '{{ Min }}'
                  Max: '{{ Max }}'
                LocalStorage: '{{ LocalStorage }}'
                LocalStorageTypes:
                  - '{{ LocalStorageTypes[0] }}'
                TotalLocalStorageGB:
                  Min: null
                  Max: null
                BaselineEbsBandwidthMbps:
                  Min: '{{ Min }}'
                  Max: '{{ Max }}'
                AcceleratorTypes:
                  - '{{ AcceleratorTypes[0] }}'
                AcceleratorCount:
                  Min: '{{ Min }}'
                  Max: '{{ Max }}'
                AcceleratorManufacturers:
                  - '{{ AcceleratorManufacturers[0] }}'
                AcceleratorNames:
                  - '{{ AcceleratorNames[0] }}'
                AcceleratorTotalMemoryMiB:
                  Min: '{{ Min }}'
                  Max: '{{ Max }}'
                BaselinePerformanceFactors:
                  Cpu:
                    References:
                      - InstanceFamily: '{{ InstanceFamily }}'
          LaunchTemplateConfigs:
            - LaunchTemplateSpecification:
                LaunchTemplateId: '{{ LaunchTemplateId }}'
                LaunchTemplateName: '{{ LaunchTemplateName }}'
                Version: '{{ Version }}'
              Overrides:
                - AvailabilityZone: '{{ AvailabilityZone }}'
                  InstanceType: '{{ InstanceType }}'
                  SpotPrice: '{{ SpotPrice }}'
                  SubnetId: '{{ SubnetId }}'
                  WeightedCapacity: null
                  InstanceRequirements: null
                  Priority: null
          LoadBalancersConfig:
            ClassicLoadBalancersConfig:
              ClassicLoadBalancers:
                - Name: '{{ Name }}'
            TargetGroupsConfig:
              TargetGroups:
                - Arn: '{{ Arn }}'
          OnDemandAllocationStrategy: '{{ OnDemandAllocationStrategy }}'
          OnDemandMaxTotalPrice: '{{ OnDemandMaxTotalPrice }}'
          OnDemandTargetCapacity: '{{ OnDemandTargetCapacity }}'
          ReplaceUnhealthyInstances: '{{ ReplaceUnhealthyInstances }}'
          SpotMaintenanceStrategies:
            CapacityRebalance:
              ReplacementStrategy: '{{ ReplacementStrategy }}'
              TerminationDelay: '{{ TerminationDelay }}'
          SpotMaxTotalPrice: '{{ SpotMaxTotalPrice }}'
          SpotPrice: '{{ SpotPrice }}'
          TargetCapacity: '{{ TargetCapacity }}'
          TerminateInstancesWithExpiration: '{{ TerminateInstancesWithExpiration }}'
          Type: '{{ Type }}'
          ValidFrom: '{{ ValidFrom }}'
          ValidUntil: '{{ ValidUntil }}'
          TagSpecifications:
            - null
          TargetCapacityUnitType: '{{ TargetCapacityUnitType }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.spot_fleets
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>spot_fleets</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
ec2:CreateTags,
ec2:RequestSpotFleet,
ec2:DescribeSpotFleetRequests,
ec2:RunInstances
```

### Delete
```json
ec2:DescribeSpotFleetRequests,
ec2:CancelSpotFleetRequests
```

### List
```json
ec2:DescribeSpotFleetRequests
```

### Read
```json
ec2:DescribeSpotFleetRequests
```

### Update
```json
ec2:ModifySpotFleetRequest,
ec2:DescribeSpotFleetRequests
```

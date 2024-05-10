---
title: ec2fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - ec2fleets
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


Used to retrieve a list of <code>ec2fleets</code> in a region or to create or delete a <code>ec2fleets</code> resource, use <code>ec2fleet</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ec2fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::EC2Fleet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ec2fleets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="fleet_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
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
FROM aws.ec2.ec2fleets
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>ec2fleet</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- ec2fleet.iql (required properties only)
INSERT INTO aws.ec2.ec2fleets (
 TargetCapacitySpecification,
 LaunchTemplateConfigs,
 region
)
SELECT 
'{{ TargetCapacitySpecification }}',
 '{{ LaunchTemplateConfigs }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- ec2fleet.iql (all properties)
INSERT INTO aws.ec2.ec2fleets (
 TargetCapacitySpecification,
 OnDemandOptions,
 Type,
 ExcessCapacityTerminationPolicy,
 TagSpecifications,
 SpotOptions,
 ValidFrom,
 ReplaceUnhealthyInstances,
 LaunchTemplateConfigs,
 TerminateInstancesWithExpiration,
 ValidUntil,
 Context,
 region
)
SELECT 
 '{{ TargetCapacitySpecification }}',
 '{{ OnDemandOptions }}',
 '{{ Type }}',
 '{{ ExcessCapacityTerminationPolicy }}',
 '{{ TagSpecifications }}',
 '{{ SpotOptions }}',
 '{{ ValidFrom }}',
 '{{ ReplaceUnhealthyInstances }}',
 '{{ LaunchTemplateConfigs }}',
 '{{ TerminateInstancesWithExpiration }}',
 '{{ ValidUntil }}',
 '{{ Context }}',
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
  - name: ec2fleet
    props:
      - name: TargetCapacitySpecification
        value:
          DefaultTargetCapacityType: '{{ DefaultTargetCapacityType }}'
          TargetCapacityUnitType: '{{ TargetCapacityUnitType }}'
          TotalTargetCapacity: '{{ TotalTargetCapacity }}'
          OnDemandTargetCapacity: '{{ OnDemandTargetCapacity }}'
          SpotTargetCapacity: '{{ SpotTargetCapacity }}'
      - name: OnDemandOptions
        value:
          SingleAvailabilityZone: '{{ SingleAvailabilityZone }}'
          AllocationStrategy: '{{ AllocationStrategy }}'
          SingleInstanceType: '{{ SingleInstanceType }}'
          MinTargetCapacity: '{{ MinTargetCapacity }}'
          MaxTotalPrice: '{{ MaxTotalPrice }}'
          CapacityReservationOptions:
            UsageStrategy: '{{ UsageStrategy }}'
      - name: Type
        value: '{{ Type }}'
      - name: ExcessCapacityTerminationPolicy
        value: '{{ ExcessCapacityTerminationPolicy }}'
      - name: TagSpecifications
        value:
          - ResourceType: '{{ ResourceType }}'
            Tags:
              - Key: '{{ Key }}'
                Value: '{{ Value }}'
      - name: SpotOptions
        value:
          MaintenanceStrategies:
            CapacityRebalance:
              ReplacementStrategy: '{{ ReplacementStrategy }}'
              TerminationDelay: '{{ TerminationDelay }}'
          SingleAvailabilityZone: '{{ SingleAvailabilityZone }}'
          AllocationStrategy: '{{ AllocationStrategy }}'
          SingleInstanceType: '{{ SingleInstanceType }}'
          MinTargetCapacity: '{{ MinTargetCapacity }}'
          MaxTotalPrice: '{{ MaxTotalPrice }}'
          InstanceInterruptionBehavior: '{{ InstanceInterruptionBehavior }}'
          InstancePoolsToUseCount: '{{ InstancePoolsToUseCount }}'
      - name: ValidFrom
        value: '{{ ValidFrom }}'
      - name: ReplaceUnhealthyInstances
        value: '{{ ReplaceUnhealthyInstances }}'
      - name: LaunchTemplateConfigs
        value:
          - LaunchTemplateSpecification:
              LaunchTemplateName: '{{ LaunchTemplateName }}'
              LaunchTemplateId: '{{ LaunchTemplateId }}'
              Version: '{{ Version }}'
            Overrides:
              - WeightedCapacity: null
                Placement:
                  GroupName: '{{ GroupName }}'
                  Tenancy: '{{ Tenancy }}'
                  SpreadDomain: '{{ SpreadDomain }}'
                  PartitionNumber: '{{ PartitionNumber }}'
                  AvailabilityZone: '{{ AvailabilityZone }}'
                  Affinity: '{{ Affinity }}'
                  HostId: '{{ HostId }}'
                  HostResourceGroupArn: '{{ HostResourceGroupArn }}'
                  GroupId: '{{ GroupId }}'
                Priority: null
                AvailabilityZone: '{{ AvailabilityZone }}'
                SubnetId: '{{ SubnetId }}'
                InstanceType: '{{ InstanceType }}'
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
                MaxPrice: '{{ MaxPrice }}'
      - name: TerminateInstancesWithExpiration
        value: '{{ TerminateInstancesWithExpiration }}'
      - name: ValidUntil
        value: '{{ ValidUntil }}'
      - name: Context
        value: '{{ Context }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.ec2fleets
WHERE data__Identifier = '<FleetId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>ec2fleets</code> resource, the following permissions are required:

### Create
```json
ec2:CreateFleet,
ec2:DescribeFleets
```

### Delete
```json
ec2:DescribeFleets,
ec2:DeleteFleets
```

### List
```json
ec2:DescribeFleets
```


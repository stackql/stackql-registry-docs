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

Creates, updates, deletes or gets an <code>ec2fleet</code> resource or lists <code>ec2fleets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ec2fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::EC2Fleet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ec2fleets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="target_capacity_specification" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="on_demand_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="excess_capacity_termination_policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_specifications" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="spot_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="valid_from" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="replace_unhealthy_instances" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="launch_template_configs" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="fleet_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="terminate_instances_with_expiration" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="valid_until" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="context" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="TargetCapacitySpecification, LaunchTemplateConfigs, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>ec2fleets</code> in a region.
```sql
SELECT
region,
fleet_id
FROM aws.ec2.ec2fleets
WHERE region = 'us-east-1';
```
Gets all properties from an <code>ec2fleet</code>.
```sql
SELECT
region,
target_capacity_specification,
on_demand_options,
type,
excess_capacity_termination_policy,
tag_specifications,
spot_options,
valid_from,
replace_unhealthy_instances,
launch_template_configs,
fleet_id,
terminate_instances_with_expiration,
valid_until,
context
FROM aws.ec2.ec2fleets
WHERE region = 'us-east-1' AND data__Identifier = '<FleetId>';
```


## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
ec2:DescribeFleets
```

### Update
```json
ec2:ModifyFleet,
ec2:DescribeFleets
```


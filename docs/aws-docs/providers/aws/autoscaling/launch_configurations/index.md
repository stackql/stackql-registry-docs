---
title: launch_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - launch_configurations
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


Used to retrieve a list of <code>launch_configurations</code> in a region or to create or delete a <code>launch_configurations</code> resource, use <code>launch_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AutoScaling::LaunchConfiguration resource specifies the launch configuration that can be used by an Auto Scaling group to configure Amazon EC2 instances.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.autoscaling.launch_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="launch_configuration_name" /></td><td><code>string</code></td><td>The name of the launch configuration. This name must be unique per Region per account.</td></tr>
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
    <td><CopyableCode code="ImageId, InstanceType, region" /></td>
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
launch_configuration_name
FROM aws.autoscaling.launch_configurations
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>launch_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.autoscaling.launch_configurations (
 ImageId,
 InstanceType,
 region
)
SELECT 
'{{ ImageId }}',
 '{{ InstanceType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.autoscaling.launch_configurations (
 AssociatePublicIpAddress,
 BlockDeviceMappings,
 ClassicLinkVPCId,
 ClassicLinkVPCSecurityGroups,
 EbsOptimized,
 IamInstanceProfile,
 ImageId,
 InstanceId,
 InstanceMonitoring,
 InstanceType,
 KernelId,
 KeyName,
 LaunchConfigurationName,
 MetadataOptions,
 PlacementTenancy,
 RamDiskId,
 SecurityGroups,
 SpotPrice,
 UserData,
 region
)
SELECT 
 '{{ AssociatePublicIpAddress }}',
 '{{ BlockDeviceMappings }}',
 '{{ ClassicLinkVPCId }}',
 '{{ ClassicLinkVPCSecurityGroups }}',
 '{{ EbsOptimized }}',
 '{{ IamInstanceProfile }}',
 '{{ ImageId }}',
 '{{ InstanceId }}',
 '{{ InstanceMonitoring }}',
 '{{ InstanceType }}',
 '{{ KernelId }}',
 '{{ KeyName }}',
 '{{ LaunchConfigurationName }}',
 '{{ MetadataOptions }}',
 '{{ PlacementTenancy }}',
 '{{ RamDiskId }}',
 '{{ SecurityGroups }}',
 '{{ SpotPrice }}',
 '{{ UserData }}',
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
  - name: launch_configuration
    props:
      - name: AssociatePublicIpAddress
        value: '{{ AssociatePublicIpAddress }}'
      - name: BlockDeviceMappings
        value:
          - NoDevice: '{{ NoDevice }}'
            VirtualName: '{{ VirtualName }}'
            Ebs:
              SnapshotId: '{{ SnapshotId }}'
              VolumeType: '{{ VolumeType }}'
              Encrypted: '{{ Encrypted }}'
              Iops: '{{ Iops }}'
              VolumeSize: '{{ VolumeSize }}'
              DeleteOnTermination: '{{ DeleteOnTermination }}'
              Throughput: '{{ Throughput }}'
            DeviceName: '{{ DeviceName }}'
      - name: ClassicLinkVPCId
        value: '{{ ClassicLinkVPCId }}'
      - name: ClassicLinkVPCSecurityGroups
        value:
          - '{{ ClassicLinkVPCSecurityGroups[0] }}'
      - name: EbsOptimized
        value: '{{ EbsOptimized }}'
      - name: IamInstanceProfile
        value: '{{ IamInstanceProfile }}'
      - name: ImageId
        value: '{{ ImageId }}'
      - name: InstanceId
        value: '{{ InstanceId }}'
      - name: InstanceMonitoring
        value: '{{ InstanceMonitoring }}'
      - name: InstanceType
        value: '{{ InstanceType }}'
      - name: KernelId
        value: '{{ KernelId }}'
      - name: KeyName
        value: '{{ KeyName }}'
      - name: LaunchConfigurationName
        value: '{{ LaunchConfigurationName }}'
      - name: MetadataOptions
        value:
          HttpPutResponseHopLimit: '{{ HttpPutResponseHopLimit }}'
          HttpTokens: '{{ HttpTokens }}'
          HttpEndpoint: '{{ HttpEndpoint }}'
      - name: PlacementTenancy
        value: '{{ PlacementTenancy }}'
      - name: RamDiskId
        value: '{{ RamDiskId }}'
      - name: SecurityGroups
        value:
          - '{{ SecurityGroups[0] }}'
      - name: SpotPrice
        value: '{{ SpotPrice }}'
      - name: UserData
        value: '{{ UserData }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.autoscaling.launch_configurations
WHERE data__Identifier = '<LaunchConfigurationName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>launch_configurations</code> resource, the following permissions are required:

### Create
```json
autoscaling:CreateLaunchConfiguration,
autoscaling:DescribeLaunchConfigurations,
iam:PassRole
```

### Delete
```json
autoscaling:DeleteLaunchConfiguration,
autoscaling:DescribeLaunchConfigurations
```

### List
```json
autoscaling:DescribeLaunchConfigurations
```


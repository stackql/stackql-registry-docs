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

Creates, updates, deletes or gets a <code>launch_configuration</code> resource or lists <code>launch_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AutoScaling::LaunchConfiguration resource specifies the launch configuration that can be used by an Auto Scaling group to configure Amazon EC2 instances.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.autoscaling.launch_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="placement_tenancy" /></td><td><code>string</code></td><td>The tenancy of the instance, either default or dedicated.</td></tr>
<tr><td><CopyableCode code="security_groups" /></td><td><code>array</code></td><td>A list that contains the security groups to assign to the instances in the Auto Scaling group.</td></tr>
<tr><td><CopyableCode code="launch_configuration_name" /></td><td><code>string</code></td><td>The name of the launch configuration. This name must be unique per Region per account.</td></tr>
<tr><td><CopyableCode code="metadata_options" /></td><td><code>object</code></td><td>The metadata options for the instances.</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>The ID of the Amazon EC2 instance you want to use to create the launch configuration.</td></tr>
<tr><td><CopyableCode code="user_data" /></td><td><code>string</code></td><td>The Base64-encoded user data to make available to the launched EC2 instances.</td></tr>
<tr><td><CopyableCode code="classic_link_vpc_security_groups" /></td><td><code>array</code></td><td>The IDs of one or more security groups for the VPC that you specified in the ClassicLinkVPCId property.</td></tr>
<tr><td><CopyableCode code="block_device_mappings" /></td><td><code>array</code></td><td>Specifies how block devices are exposed to the instance. You can specify virtual devices and EBS volumes.</td></tr>
<tr><td><CopyableCode code="iam_instance_profile" /></td><td><code>string</code></td><td>Provides the name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance. The instance profile contains the IAM role.</td></tr>
<tr><td><CopyableCode code="kernel_id" /></td><td><code>string</code></td><td>Provides the ID of the kernel associated with the EC2 AMI.</td></tr>
<tr><td><CopyableCode code="associate_public_ip_address" /></td><td><code>boolean</code></td><td>For Auto Scaling groups that are running in a virtual private cloud (VPC), specifies whether to assign a public IP address to the group's instances.</td></tr>
<tr><td><CopyableCode code="classic_link_vpc_id" /></td><td><code>string</code></td><td>The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to.</td></tr>
<tr><td><CopyableCode code="ebs_optimized" /></td><td><code>boolean</code></td><td>Specifies whether the launch configuration is optimized for EBS I/O (true) or not (false).</td></tr>
<tr><td><CopyableCode code="key_name" /></td><td><code>string</code></td><td>Provides the name of the EC2 key pair.</td></tr>
<tr><td><CopyableCode code="spot_price" /></td><td><code>string</code></td><td>The maximum hourly price you are willing to pay for any Spot Instances launched to fulfill the request.</td></tr>
<tr><td><CopyableCode code="image_id" /></td><td><code>string</code></td><td>Provides the unique ID of the Amazon Machine Image (AMI) that was assigned during registration.</td></tr>
<tr><td><CopyableCode code="instance_type" /></td><td><code>string</code></td><td>Specifies the instance type of the EC2 instance.</td></tr>
<tr><td><CopyableCode code="ram_disk_id" /></td><td><code>string</code></td><td>The ID of the RAM disk to select.</td></tr>
<tr><td><CopyableCode code="instance_monitoring" /></td><td><code>boolean</code></td><td>Controls whether instances in this group are launched with detailed (true) or basic (false) monitoring.</td></tr>
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
Gets all <code>launch_configurations</code> in a region.
```sql
SELECT
region,
placement_tenancy,
security_groups,
launch_configuration_name,
metadata_options,
instance_id,
user_data,
classic_link_vpc_security_groups,
block_device_mappings,
iam_instance_profile,
kernel_id,
associate_public_ip_address,
classic_link_vpc_id,
ebs_optimized,
key_name,
spot_price,
image_id,
instance_type,
ram_disk_id,
instance_monitoring
FROM aws.autoscaling.launch_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>launch_configuration</code>.
```sql
SELECT
region,
placement_tenancy,
security_groups,
launch_configuration_name,
metadata_options,
instance_id,
user_data,
classic_link_vpc_security_groups,
block_device_mappings,
iam_instance_profile,
kernel_id,
associate_public_ip_address,
classic_link_vpc_id,
ebs_optimized,
key_name,
spot_price,
image_id,
instance_type,
ram_disk_id,
instance_monitoring
FROM aws.autoscaling.launch_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<LaunchConfigurationName>';
```

## `INSERT` example

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
 PlacementTenancy,
 SecurityGroups,
 LaunchConfigurationName,
 MetadataOptions,
 InstanceId,
 UserData,
 ClassicLinkVPCSecurityGroups,
 BlockDeviceMappings,
 IamInstanceProfile,
 KernelId,
 AssociatePublicIpAddress,
 ClassicLinkVPCId,
 EbsOptimized,
 KeyName,
 SpotPrice,
 ImageId,
 InstanceType,
 RamDiskId,
 InstanceMonitoring,
 region
)
SELECT 
 '{{ PlacementTenancy }}',
 '{{ SecurityGroups }}',
 '{{ LaunchConfigurationName }}',
 '{{ MetadataOptions }}',
 '{{ InstanceId }}',
 '{{ UserData }}',
 '{{ ClassicLinkVPCSecurityGroups }}',
 '{{ BlockDeviceMappings }}',
 '{{ IamInstanceProfile }}',
 '{{ KernelId }}',
 '{{ AssociatePublicIpAddress }}',
 '{{ ClassicLinkVPCId }}',
 '{{ EbsOptimized }}',
 '{{ KeyName }}',
 '{{ SpotPrice }}',
 '{{ ImageId }}',
 '{{ InstanceType }}',
 '{{ RamDiskId }}',
 '{{ InstanceMonitoring }}',
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
      - name: PlacementTenancy
        value: '{{ PlacementTenancy }}'
      - name: SecurityGroups
        value:
          - '{{ SecurityGroups[0] }}'
      - name: LaunchConfigurationName
        value: '{{ LaunchConfigurationName }}'
      - name: MetadataOptions
        value:
          HttpPutResponseHopLimit: '{{ HttpPutResponseHopLimit }}'
          HttpTokens: '{{ HttpTokens }}'
          HttpEndpoint: '{{ HttpEndpoint }}'
      - name: InstanceId
        value: '{{ InstanceId }}'
      - name: UserData
        value: '{{ UserData }}'
      - name: ClassicLinkVPCSecurityGroups
        value:
          - '{{ ClassicLinkVPCSecurityGroups[0] }}'
      - name: BlockDeviceMappings
        value:
          - Ebs:
              SnapshotId: '{{ SnapshotId }}'
              VolumeType: '{{ VolumeType }}'
              Encrypted: '{{ Encrypted }}'
              Throughput: '{{ Throughput }}'
              Iops: '{{ Iops }}'
              VolumeSize: '{{ VolumeSize }}'
              DeleteOnTermination: '{{ DeleteOnTermination }}'
            NoDevice: '{{ NoDevice }}'
            VirtualName: '{{ VirtualName }}'
            DeviceName: '{{ DeviceName }}'
      - name: IamInstanceProfile
        value: '{{ IamInstanceProfile }}'
      - name: KernelId
        value: '{{ KernelId }}'
      - name: AssociatePublicIpAddress
        value: '{{ AssociatePublicIpAddress }}'
      - name: ClassicLinkVPCId
        value: '{{ ClassicLinkVPCId }}'
      - name: EbsOptimized
        value: '{{ EbsOptimized }}'
      - name: KeyName
        value: '{{ KeyName }}'
      - name: SpotPrice
        value: '{{ SpotPrice }}'
      - name: ImageId
        value: '{{ ImageId }}'
      - name: InstanceType
        value: '{{ InstanceType }}'
      - name: RamDiskId
        value: '{{ RamDiskId }}'
      - name: InstanceMonitoring
        value: '{{ InstanceMonitoring }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.autoscaling.launch_configurations
WHERE data__Identifier = '<LaunchConfigurationName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>launch_configurations</code> resource, the following permissions are required:

### Read
```json
autoscaling:DescribeLaunchConfigurations
```

### Create
```json
autoscaling:CreateLaunchConfiguration,
autoscaling:DescribeLaunchConfigurations,
iam:PassRole
```

### List
```json
autoscaling:DescribeLaunchConfigurations
```

### Delete
```json
autoscaling:DeleteLaunchConfiguration,
autoscaling:DescribeLaunchConfigurations
```


---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
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


Used to retrieve a list of <code>instances</code> in a region or to create or delete a <code>instances</code> resource, use <code>instance</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::Instance</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.instances" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>The EC2 Instance ID.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
instance_id
FROM aws.ec2.instances
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>instance</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.instances (
 Tenancy,
 SecurityGroups,
 PrivateIpAddress,
 UserData,
 BlockDeviceMappings,
 IamInstanceProfile,
 Ipv6Addresses,
 KernelId,
 SubnetId,
 EbsOptimized,
 PropagateTagsToVolumeOnCreation,
 ElasticGpuSpecifications,
 ElasticInferenceAccelerators,
 Volumes,
 Ipv6AddressCount,
 LaunchTemplate,
 EnclaveOptions,
 NetworkInterfaces,
 ImageId,
 InstanceType,
 Monitoring,
 Tags,
 AdditionalInfo,
 HibernationOptions,
 LicenseSpecifications,
 InstanceInitiatedShutdownBehavior,
 CpuOptions,
 AvailabilityZone,
 PrivateDnsNameOptions,
 HostId,
 HostResourceGroupArn,
 SecurityGroupIds,
 DisableApiTermination,
 KeyName,
 RamdiskId,
 SourceDestCheck,
 PlacementGroupName,
 SsmAssociations,
 Affinity,
 CreditSpecification,
 region
)
SELECT 
'{{ Tenancy }}',
 '{{ SecurityGroups }}',
 '{{ PrivateIpAddress }}',
 '{{ UserData }}',
 '{{ BlockDeviceMappings }}',
 '{{ IamInstanceProfile }}',
 '{{ Ipv6Addresses }}',
 '{{ KernelId }}',
 '{{ SubnetId }}',
 '{{ EbsOptimized }}',
 '{{ PropagateTagsToVolumeOnCreation }}',
 '{{ ElasticGpuSpecifications }}',
 '{{ ElasticInferenceAccelerators }}',
 '{{ Volumes }}',
 '{{ Ipv6AddressCount }}',
 '{{ LaunchTemplate }}',
 '{{ EnclaveOptions }}',
 '{{ NetworkInterfaces }}',
 '{{ ImageId }}',
 '{{ InstanceType }}',
 '{{ Monitoring }}',
 '{{ Tags }}',
 '{{ AdditionalInfo }}',
 '{{ HibernationOptions }}',
 '{{ LicenseSpecifications }}',
 '{{ InstanceInitiatedShutdownBehavior }}',
 '{{ CpuOptions }}',
 '{{ AvailabilityZone }}',
 '{{ PrivateDnsNameOptions }}',
 '{{ HostId }}',
 '{{ HostResourceGroupArn }}',
 '{{ SecurityGroupIds }}',
 '{{ DisableApiTermination }}',
 '{{ KeyName }}',
 '{{ RamdiskId }}',
 '{{ SourceDestCheck }}',
 '{{ PlacementGroupName }}',
 '{{ SsmAssociations }}',
 '{{ Affinity }}',
 '{{ CreditSpecification }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.instances (
 Tenancy,
 SecurityGroups,
 PrivateIpAddress,
 UserData,
 BlockDeviceMappings,
 IamInstanceProfile,
 Ipv6Addresses,
 KernelId,
 SubnetId,
 EbsOptimized,
 PropagateTagsToVolumeOnCreation,
 ElasticGpuSpecifications,
 ElasticInferenceAccelerators,
 Volumes,
 Ipv6AddressCount,
 LaunchTemplate,
 EnclaveOptions,
 NetworkInterfaces,
 ImageId,
 InstanceType,
 Monitoring,
 Tags,
 AdditionalInfo,
 HibernationOptions,
 LicenseSpecifications,
 InstanceInitiatedShutdownBehavior,
 CpuOptions,
 AvailabilityZone,
 PrivateDnsNameOptions,
 HostId,
 HostResourceGroupArn,
 SecurityGroupIds,
 DisableApiTermination,
 KeyName,
 RamdiskId,
 SourceDestCheck,
 PlacementGroupName,
 SsmAssociations,
 Affinity,
 CreditSpecification,
 region
)
SELECT 
 '{{ Tenancy }}',
 '{{ SecurityGroups }}',
 '{{ PrivateIpAddress }}',
 '{{ UserData }}',
 '{{ BlockDeviceMappings }}',
 '{{ IamInstanceProfile }}',
 '{{ Ipv6Addresses }}',
 '{{ KernelId }}',
 '{{ SubnetId }}',
 '{{ EbsOptimized }}',
 '{{ PropagateTagsToVolumeOnCreation }}',
 '{{ ElasticGpuSpecifications }}',
 '{{ ElasticInferenceAccelerators }}',
 '{{ Volumes }}',
 '{{ Ipv6AddressCount }}',
 '{{ LaunchTemplate }}',
 '{{ EnclaveOptions }}',
 '{{ NetworkInterfaces }}',
 '{{ ImageId }}',
 '{{ InstanceType }}',
 '{{ Monitoring }}',
 '{{ Tags }}',
 '{{ AdditionalInfo }}',
 '{{ HibernationOptions }}',
 '{{ LicenseSpecifications }}',
 '{{ InstanceInitiatedShutdownBehavior }}',
 '{{ CpuOptions }}',
 '{{ AvailabilityZone }}',
 '{{ PrivateDnsNameOptions }}',
 '{{ HostId }}',
 '{{ HostResourceGroupArn }}',
 '{{ SecurityGroupIds }}',
 '{{ DisableApiTermination }}',
 '{{ KeyName }}',
 '{{ RamdiskId }}',
 '{{ SourceDestCheck }}',
 '{{ PlacementGroupName }}',
 '{{ SsmAssociations }}',
 '{{ Affinity }}',
 '{{ CreditSpecification }}',
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
  - name: instance
    props:
      - name: Tenancy
        value: '{{ Tenancy }}'
      - name: SecurityGroups
        value:
          - '{{ SecurityGroups[0] }}'
      - name: PrivateIpAddress
        value: '{{ PrivateIpAddress }}'
      - name: UserData
        value: '{{ UserData }}'
      - name: BlockDeviceMappings
        value:
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
      - name: IamInstanceProfile
        value: '{{ IamInstanceProfile }}'
      - name: Ipv6Addresses
        value:
          - Ipv6Address: '{{ Ipv6Address }}'
      - name: KernelId
        value: '{{ KernelId }}'
      - name: SubnetId
        value: '{{ SubnetId }}'
      - name: EbsOptimized
        value: '{{ EbsOptimized }}'
      - name: PropagateTagsToVolumeOnCreation
        value: '{{ PropagateTagsToVolumeOnCreation }}'
      - name: ElasticGpuSpecifications
        value:
          - Type: '{{ Type }}'
      - name: ElasticInferenceAccelerators
        value:
          - Type: '{{ Type }}'
            Count: '{{ Count }}'
      - name: Volumes
        value:
          - MultiAttachEnabled: '{{ MultiAttachEnabled }}'
            KmsKeyId: '{{ KmsKeyId }}'
            Encrypted: '{{ Encrypted }}'
            Size: '{{ Size }}'
            AutoEnableIO: '{{ AutoEnableIO }}'
            OutpostArn: '{{ OutpostArn }}'
            AvailabilityZone: '{{ AvailabilityZone }}'
            Throughput: '{{ Throughput }}'
            Iops: '{{ Iops }}'
            SnapshotId: '{{ SnapshotId }}'
            VolumeType: '{{ VolumeType }}'
            Tags:
              - Key: '{{ Key }}'
                Value: '{{ Value }}'
      - name: Ipv6AddressCount
        value: '{{ Ipv6AddressCount }}'
      - name: LaunchTemplate
        value:
          LaunchTemplateName: '{{ LaunchTemplateName }}'
          Version: '{{ Version }}'
          LaunchTemplateId: '{{ LaunchTemplateId }}'
      - name: EnclaveOptions
        value:
          Enabled: '{{ Enabled }}'
      - name: NetworkInterfaces
        value:
          - Description: '{{ Description }}'
            PrivateIpAddress: '{{ PrivateIpAddress }}'
            PrivateIpAddresses:
              - Primary: '{{ Primary }}'
                PrivateIpAddress: '{{ PrivateIpAddress }}'
            SecondaryPrivateIpAddressCount: '{{ SecondaryPrivateIpAddressCount }}'
            Ipv4Prefixes:
              - Ipv4Prefix: '{{ Ipv4Prefix }}'
            Ipv4PrefixCount: '{{ Ipv4PrefixCount }}'
            GroupSet:
              - '{{ GroupSet[0] }}'
            Ipv6Addresses:
              - null
            Ipv6Prefixes:
              - Ipv6Prefix: '{{ Ipv6Prefix }}'
            Ipv6PrefixCount: '{{ Ipv6PrefixCount }}'
            SubnetId: '{{ SubnetId }}'
            SourceDestCheck: '{{ SourceDestCheck }}'
            InterfaceType: '{{ InterfaceType }}'
            Ipv6AddressCount: '{{ Ipv6AddressCount }}'
            EnablePrimaryIpv6: '{{ EnablePrimaryIpv6 }}'
            ConnectionTrackingSpecification:
              TcpEstablishedTimeout: '{{ TcpEstablishedTimeout }}'
              UdpStreamTimeout: '{{ UdpStreamTimeout }}'
              UdpTimeout: '{{ UdpTimeout }}'
            Tags:
              - null
      - name: ImageId
        value: '{{ ImageId }}'
      - name: InstanceType
        value: '{{ InstanceType }}'
      - name: Monitoring
        value: '{{ Monitoring }}'
      - name: Tags
        value:
          - null
      - name: AdditionalInfo
        value: '{{ AdditionalInfo }}'
      - name: HibernationOptions
        value:
          Configured: '{{ Configured }}'
      - name: LicenseSpecifications
        value:
          - LicenseConfigurationArn: '{{ LicenseConfigurationArn }}'
      - name: InstanceInitiatedShutdownBehavior
        value: '{{ InstanceInitiatedShutdownBehavior }}'
      - name: CpuOptions
        value:
          ThreadsPerCore: '{{ ThreadsPerCore }}'
          CoreCount: '{{ CoreCount }}'
      - name: AvailabilityZone
        value: '{{ AvailabilityZone }}'
      - name: PrivateDnsNameOptions
        value:
          EnableResourceNameDnsARecord: '{{ EnableResourceNameDnsARecord }}'
          HostnameType: '{{ HostnameType }}'
          EnableResourceNameDnsAAAARecord: '{{ EnableResourceNameDnsAAAARecord }}'
      - name: HostId
        value: '{{ HostId }}'
      - name: HostResourceGroupArn
        value: '{{ HostResourceGroupArn }}'
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: DisableApiTermination
        value: '{{ DisableApiTermination }}'
      - name: KeyName
        value: '{{ KeyName }}'
      - name: RamdiskId
        value: '{{ RamdiskId }}'
      - name: SourceDestCheck
        value: '{{ SourceDestCheck }}'
      - name: PlacementGroupName
        value: '{{ PlacementGroupName }}'
      - name: SsmAssociations
        value:
          - AssociationParameters:
              - Value:
                  - '{{ Value[0] }}'
                Key: '{{ Key }}'
            DocumentName: '{{ DocumentName }}'
      - name: Affinity
        value: '{{ Affinity }}'
      - name: CreditSpecification
        value:
          CPUCredits: '{{ CPUCredits }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.ec2.instances
WHERE data__Identifier = '<InstanceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>instances</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
ec2:ModifyPrivateDnsNameOptions,
ec2:DescribeElasticGpus,
ec2:DescribeNetworkInterfaces,
ec2:DescribeVolumes,
ec2:RunInstances,
ec2:AssociateIamInstanceProfile,
ec2:DescribeIamInstanceProfileAssociations,
ec2:DescribeInstances,
ec2:DescribeSubnets,
ec2:DescribeKeyPairs,
ec2:DescribeSecurityGroups,
ec2:DescribeVpcs,
ec2:DescribeInstanceAttribute,
ec2:DescribeInstanceCreditSpecifications,
ec2:DescribeLaunchTemplates,
ec2:DescribeLaunchTemplateVersions,
ec2:DetachVolume,
ec2:DisassociateIamInstanceProfile,
ec2:ModifyInstanceAttribute,
ec2:ModifyInstanceCreditSpecification,
ec2:ModifyInstancePlacement,
ec2:MonitorInstances,
ec2:AttachVolume,
ec2:CreateTags,
ec2:ReplaceIamInstanceProfileAssociation,
ec2:StartInstances,
elastic-inference:DescribeAccelerators,
ssm:CreateAssociation,
ssm:DescribeAssociation,
ssm:ListAssociations
```

### List
```json
ec2:DescribeInstances
```

### Delete
```json
ec2:DescribeInstances,
ec2:TerminateInstances,
ec2:DescribeElasticGpus,
ec2:DescribeNetworkInterfaces,
ec2:DescribeVolumes,
ec2:DescribeInstances,
ec2:DescribeInstanceAttribute,
ec2:DescribeInstanceCreditSpecifications,
ec2:DescribeLaunchTemplates,
elastic-inference:DescribeAccelerators,
ssm:DescribeAssociation,
ssm:ListAssociations
```


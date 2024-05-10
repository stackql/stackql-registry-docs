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
instance_id
FROM aws.ec2.instances
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Tenancy": "{{ Tenancy }}",
 "SecurityGroups": [
  "{{ SecurityGroups[0] }}"
 ],
 "PrivateIpAddress": "{{ PrivateIpAddress }}",
 "UserData": "{{ UserData }}",
 "BlockDeviceMappings": [
  {
   "DeviceName": "{{ DeviceName }}",
   "Ebs": {
    "DeleteOnTermination": "{{ DeleteOnTermination }}",
    "Encrypted": "{{ Encrypted }}",
    "Iops": "{{ Iops }}",
    "SnapshotId": "{{ SnapshotId }}",
    "VolumeSize": "{{ VolumeSize }}",
    "VolumeType": "{{ VolumeType }}"
   },
   "NoDevice": "{{ NoDevice }}",
   "VirtualName": "{{ VirtualName }}"
  }
 ],
 "IamInstanceProfile": "{{ IamInstanceProfile }}",
 "Ipv6Addresses": [
  {
   "Ipv6Address": "{{ Ipv6Address }}"
  }
 ],
 "KernelId": "{{ KernelId }}",
 "SubnetId": "{{ SubnetId }}",
 "EbsOptimized": "{{ EbsOptimized }}",
 "PropagateTagsToVolumeOnCreation": "{{ PropagateTagsToVolumeOnCreation }}",
 "ElasticGpuSpecifications": [
  {
   "Type": "{{ Type }}"
  }
 ],
 "ElasticInferenceAccelerators": [
  {
   "Type": "{{ Type }}",
   "Count": "{{ Count }}"
  }
 ],
 "Volumes": [
  {
   "AvailabilityZone": "{{ AvailabilityZone }}"
  }
 ],
 "Ipv6AddressCount": "{{ Ipv6AddressCount }}",
 "LaunchTemplate": {
  "LaunchTemplateName": "{{ LaunchTemplateName }}",
  "Version": "{{ Version }}",
  "LaunchTemplateId": "{{ LaunchTemplateId }}"
 },
 "EnclaveOptions": {
  "Enabled": "{{ Enabled }}"
 },
 "NetworkInterfaces": [
  {
   "SubnetId": "{{ SubnetId }}"
  }
 ],
 "ImageId": "{{ ImageId }}",
 "InstanceType": "{{ InstanceType }}",
 "Monitoring": "{{ Monitoring }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "AdditionalInfo": "{{ AdditionalInfo }}",
 "HibernationOptions": {
  "Configured": "{{ Configured }}"
 },
 "LicenseSpecifications": [
  {
   "LicenseConfigurationArn": "{{ LicenseConfigurationArn }}"
  }
 ],
 "InstanceInitiatedShutdownBehavior": "{{ InstanceInitiatedShutdownBehavior }}",
 "CpuOptions": {
  "ThreadsPerCore": "{{ ThreadsPerCore }}",
  "CoreCount": "{{ CoreCount }}"
 },
 "AvailabilityZone": "{{ AvailabilityZone }}",
 "PrivateDnsNameOptions": {
  "EnableResourceNameDnsARecord": "{{ EnableResourceNameDnsARecord }}",
  "HostnameType": "{{ HostnameType }}",
  "EnableResourceNameDnsAAAARecord": "{{ EnableResourceNameDnsAAAARecord }}"
 },
 "HostId": "{{ HostId }}",
 "HostResourceGroupArn": "{{ HostResourceGroupArn }}",
 "SecurityGroupIds": [
  "{{ SecurityGroupIds[0] }}"
 ],
 "DisableApiTermination": "{{ DisableApiTermination }}",
 "KeyName": "{{ KeyName }}",
 "RamdiskId": "{{ RamdiskId }}",
 "SourceDestCheck": "{{ SourceDestCheck }}",
 "PlacementGroupName": "{{ PlacementGroupName }}",
 "SsmAssociations": [
  {
   "AssociationParameters": [
    {
     "Value": [
      "{{ Value[0] }}"
     ],
     "Key": "{{ Key }}"
    }
   ],
   "DocumentName": "{{ DocumentName }}"
  }
 ],
 "Affinity": "{{ Affinity }}",
 "CreditSpecification": {
  "CPUCredits": "{{ CPUCredits }}"
 }
}
>>>
--required properties only
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
{{ .Tenancy }},
 {{ .SecurityGroups }},
 {{ .PrivateIpAddress }},
 {{ .UserData }},
 {{ .BlockDeviceMappings }},
 {{ .IamInstanceProfile }},
 {{ .Ipv6Addresses }},
 {{ .KernelId }},
 {{ .SubnetId }},
 {{ .EbsOptimized }},
 {{ .PropagateTagsToVolumeOnCreation }},
 {{ .ElasticGpuSpecifications }},
 {{ .ElasticInferenceAccelerators }},
 {{ .Volumes }},
 {{ .Ipv6AddressCount }},
 {{ .LaunchTemplate }},
 {{ .EnclaveOptions }},
 {{ .NetworkInterfaces }},
 {{ .ImageId }},
 {{ .InstanceType }},
 {{ .Monitoring }},
 {{ .Tags }},
 {{ .AdditionalInfo }},
 {{ .HibernationOptions }},
 {{ .LicenseSpecifications }},
 {{ .InstanceInitiatedShutdownBehavior }},
 {{ .CpuOptions }},
 {{ .AvailabilityZone }},
 {{ .PrivateDnsNameOptions }},
 {{ .HostId }},
 {{ .HostResourceGroupArn }},
 {{ .SecurityGroupIds }},
 {{ .DisableApiTermination }},
 {{ .KeyName }},
 {{ .RamdiskId }},
 {{ .SourceDestCheck }},
 {{ .PlacementGroupName }},
 {{ .SsmAssociations }},
 {{ .Affinity }},
 {{ .CreditSpecification }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Tenancy": "{{ Tenancy }}",
 "SecurityGroups": [
  "{{ SecurityGroups[0] }}"
 ],
 "PrivateIpAddress": "{{ PrivateIpAddress }}",
 "UserData": "{{ UserData }}",
 "BlockDeviceMappings": [
  {
   "DeviceName": "{{ DeviceName }}",
   "Ebs": {
    "DeleteOnTermination": "{{ DeleteOnTermination }}",
    "Encrypted": "{{ Encrypted }}",
    "Iops": "{{ Iops }}",
    "SnapshotId": "{{ SnapshotId }}",
    "VolumeSize": "{{ VolumeSize }}",
    "VolumeType": "{{ VolumeType }}"
   },
   "NoDevice": "{{ NoDevice }}",
   "VirtualName": "{{ VirtualName }}"
  }
 ],
 "IamInstanceProfile": "{{ IamInstanceProfile }}",
 "Ipv6Addresses": [
  {
   "Ipv6Address": "{{ Ipv6Address }}"
  }
 ],
 "KernelId": "{{ KernelId }}",
 "SubnetId": "{{ SubnetId }}",
 "EbsOptimized": "{{ EbsOptimized }}",
 "PropagateTagsToVolumeOnCreation": "{{ PropagateTagsToVolumeOnCreation }}",
 "ElasticGpuSpecifications": [
  {
   "Type": "{{ Type }}"
  }
 ],
 "ElasticInferenceAccelerators": [
  {
   "Type": "{{ Type }}",
   "Count": "{{ Count }}"
  }
 ],
 "Volumes": [
  {
   "MultiAttachEnabled": "{{ MultiAttachEnabled }}",
   "KmsKeyId": "{{ KmsKeyId }}",
   "Encrypted": "{{ Encrypted }}",
   "Size": "{{ Size }}",
   "AutoEnableIO": "{{ AutoEnableIO }}",
   "OutpostArn": "{{ OutpostArn }}",
   "AvailabilityZone": "{{ AvailabilityZone }}",
   "Throughput": "{{ Throughput }}",
   "Iops": "{{ Iops }}",
   "SnapshotId": "{{ SnapshotId }}",
   "VolumeType": "{{ VolumeType }}",
   "Tags": [
    {
     "Key": "{{ Key }}",
     "Value": "{{ Value }}"
    }
   ]
  }
 ],
 "Ipv6AddressCount": "{{ Ipv6AddressCount }}",
 "LaunchTemplate": {
  "LaunchTemplateName": "{{ LaunchTemplateName }}",
  "Version": "{{ Version }}",
  "LaunchTemplateId": "{{ LaunchTemplateId }}"
 },
 "EnclaveOptions": {
  "Enabled": "{{ Enabled }}"
 },
 "NetworkInterfaces": [
  {
   "Description": "{{ Description }}",
   "PrivateIpAddress": "{{ PrivateIpAddress }}",
   "PrivateIpAddresses": [
    {
     "Primary": "{{ Primary }}",
     "PrivateIpAddress": "{{ PrivateIpAddress }}"
    }
   ],
   "SecondaryPrivateIpAddressCount": "{{ SecondaryPrivateIpAddressCount }}",
   "Ipv4Prefixes": [
    {
     "Ipv4Prefix": "{{ Ipv4Prefix }}"
    }
   ],
   "Ipv4PrefixCount": "{{ Ipv4PrefixCount }}",
   "GroupSet": [
    "{{ GroupSet[0] }}"
   ],
   "Ipv6Addresses": [
    null
   ],
   "Ipv6Prefixes": [
    {
     "Ipv6Prefix": "{{ Ipv6Prefix }}"
    }
   ],
   "Ipv6PrefixCount": "{{ Ipv6PrefixCount }}",
   "SubnetId": "{{ SubnetId }}",
   "SourceDestCheck": "{{ SourceDestCheck }}",
   "InterfaceType": "{{ InterfaceType }}",
   "Ipv6AddressCount": "{{ Ipv6AddressCount }}",
   "EnablePrimaryIpv6": "{{ EnablePrimaryIpv6 }}",
   "ConnectionTrackingSpecification": {
    "TcpEstablishedTimeout": "{{ TcpEstablishedTimeout }}",
    "UdpStreamTimeout": "{{ UdpStreamTimeout }}",
    "UdpTimeout": "{{ UdpTimeout }}"
   },
   "Tags": [
    null
   ]
  }
 ],
 "ImageId": "{{ ImageId }}",
 "InstanceType": "{{ InstanceType }}",
 "Monitoring": "{{ Monitoring }}",
 "Tags": [
  null
 ],
 "AdditionalInfo": "{{ AdditionalInfo }}",
 "HibernationOptions": {
  "Configured": "{{ Configured }}"
 },
 "LicenseSpecifications": [
  {
   "LicenseConfigurationArn": "{{ LicenseConfigurationArn }}"
  }
 ],
 "InstanceInitiatedShutdownBehavior": "{{ InstanceInitiatedShutdownBehavior }}",
 "CpuOptions": {
  "ThreadsPerCore": "{{ ThreadsPerCore }}",
  "CoreCount": "{{ CoreCount }}"
 },
 "AvailabilityZone": "{{ AvailabilityZone }}",
 "PrivateDnsNameOptions": {
  "EnableResourceNameDnsARecord": "{{ EnableResourceNameDnsARecord }}",
  "HostnameType": "{{ HostnameType }}",
  "EnableResourceNameDnsAAAARecord": "{{ EnableResourceNameDnsAAAARecord }}"
 },
 "HostId": "{{ HostId }}",
 "HostResourceGroupArn": "{{ HostResourceGroupArn }}",
 "SecurityGroupIds": [
  "{{ SecurityGroupIds[0] }}"
 ],
 "DisableApiTermination": "{{ DisableApiTermination }}",
 "KeyName": "{{ KeyName }}",
 "RamdiskId": "{{ RamdiskId }}",
 "SourceDestCheck": "{{ SourceDestCheck }}",
 "PlacementGroupName": "{{ PlacementGroupName }}",
 "SsmAssociations": [
  {
   "AssociationParameters": [
    {
     "Value": [
      "{{ Value[0] }}"
     ],
     "Key": "{{ Key }}"
    }
   ],
   "DocumentName": "{{ DocumentName }}"
  }
 ],
 "Affinity": "{{ Affinity }}",
 "CreditSpecification": {
  "CPUCredits": "{{ CPUCredits }}"
 }
}
>>>
--all properties
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
 {{ .Tenancy }},
 {{ .SecurityGroups }},
 {{ .PrivateIpAddress }},
 {{ .UserData }},
 {{ .BlockDeviceMappings }},
 {{ .IamInstanceProfile }},
 {{ .Ipv6Addresses }},
 {{ .KernelId }},
 {{ .SubnetId }},
 {{ .EbsOptimized }},
 {{ .PropagateTagsToVolumeOnCreation }},
 {{ .ElasticGpuSpecifications }},
 {{ .ElasticInferenceAccelerators }},
 {{ .Volumes }},
 {{ .Ipv6AddressCount }},
 {{ .LaunchTemplate }},
 {{ .EnclaveOptions }},
 {{ .NetworkInterfaces }},
 {{ .ImageId }},
 {{ .InstanceType }},
 {{ .Monitoring }},
 {{ .Tags }},
 {{ .AdditionalInfo }},
 {{ .HibernationOptions }},
 {{ .LicenseSpecifications }},
 {{ .InstanceInitiatedShutdownBehavior }},
 {{ .CpuOptions }},
 {{ .AvailabilityZone }},
 {{ .PrivateDnsNameOptions }},
 {{ .HostId }},
 {{ .HostResourceGroupArn }},
 {{ .SecurityGroupIds }},
 {{ .DisableApiTermination }},
 {{ .KeyName }},
 {{ .RamdiskId }},
 {{ .SourceDestCheck }},
 {{ .PlacementGroupName }},
 {{ .SsmAssociations }},
 {{ .Affinity }},
 {{ .CreditSpecification }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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


---
title: launch_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - launch_templates
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


Used to retrieve a list of <code>launch_templates</code> in a region or to create or delete a <code>launch_templates</code> resource, use <code>launch_template</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies the properties for creating a launch template.&lt;br&#x2F;&gt; The minimum required properties for specifying a launch template are as follows:&lt;br&#x2F;&gt;  +  You must specify at least one property for the launch template data.&lt;br&#x2F;&gt;  +  You do not need to specify a name for the launch template. If you do not specify a name, CFN creates the name for you.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; A launch template can contain some or all of the configuration information to launch an instance. When you launch an instance using a launch template, instance properties that are not specified in the launch template use default values, except the ``ImageId`` property, which has no default value. If you do not specify an AMI ID for the launch template ``ImageId`` property, you must specify an AMI ID for the instance ``ImageId`` property.&lt;br&#x2F;&gt; For more information, see &#91;Launch an instance from a launch template&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;ec2-launch-templates.html) in the *Amazon EC2 User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.launch_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="launch_template_id" /></td><td><code>string</code></td><td></td></tr>
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
launch_template_id
FROM aws.ec2.launch_templates
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
 "LaunchTemplateData": {
  "SecurityGroups": [
   "{{ SecurityGroups[0] }}"
  ],
  "TagSpecifications": [
   {
    "ResourceType": "{{ ResourceType }}",
    "Tags": [
     {
      "Key": "{{ Key }}",
      "Value": "{{ Value }}"
     }
    ]
   }
  ],
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
  "MaintenanceOptions": {
   "AutoRecovery": "{{ AutoRecovery }}"
  },
  "IamInstanceProfile": {
   "Arn": "{{ Arn }}",
   "Name": "{{ Name }}"
  },
  "KernelId": "{{ KernelId }}",
  "EbsOptimized": "{{ EbsOptimized }}",
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
  "Placement": {
   "GroupName": "{{ GroupName }}",
   "Tenancy": "{{ Tenancy }}",
   "SpreadDomain": "{{ SpreadDomain }}",
   "PartitionNumber": "{{ PartitionNumber }}",
   "AvailabilityZone": "{{ AvailabilityZone }}",
   "Affinity": "{{ Affinity }}",
   "HostId": "{{ HostId }}",
   "HostResourceGroupArn": "{{ HostResourceGroupArn }}",
   "GroupId": "{{ GroupId }}"
  },
  "NetworkInterfaces": [
   {
    "SubnetId": "{{ SubnetId }}"
   }
  ],
  "EnclaveOptions": {
   "Enabled": "{{ Enabled }}"
  },
  "ImageId": "{{ ImageId }}",
  "InstanceType": "{{ InstanceType }}",
  "Monitoring": {
   "Enabled": "{{ Enabled }}"
  },
  "HibernationOptions": {
   "Configured": "{{ Configured }}"
  },
  "MetadataOptions": {
   "HttpPutResponseHopLimit": "{{ HttpPutResponseHopLimit }}",
   "HttpTokens": "{{ HttpTokens }}",
   "HttpProtocolIpv6": "{{ HttpProtocolIpv6 }}",
   "InstanceMetadataTags": "{{ InstanceMetadataTags }}",
   "HttpEndpoint": "{{ HttpEndpoint }}"
  },
  "LicenseSpecifications": [
   {
    "LicenseConfigurationArn": "{{ LicenseConfigurationArn }}"
   }
  ],
  "InstanceInitiatedShutdownBehavior": "{{ InstanceInitiatedShutdownBehavior }}",
  "DisableApiStop": "{{ DisableApiStop }}",
  "CpuOptions": {
   "ThreadsPerCore": "{{ ThreadsPerCore }}",
   "AmdSevSnp": "{{ AmdSevSnp }}",
   "CoreCount": "{{ CoreCount }}"
  },
  "PrivateDnsNameOptions": {
   "EnableResourceNameDnsARecord": "{{ EnableResourceNameDnsARecord }}",
   "HostnameType": "{{ HostnameType }}",
   "EnableResourceNameDnsAAAARecord": "{{ EnableResourceNameDnsAAAARecord }}"
  },
  "SecurityGroupIds": [
   "{{ SecurityGroupIds[0] }}"
  ],
  "KeyName": "{{ KeyName }}",
  "DisableApiTermination": "{{ DisableApiTermination }}",
  "InstanceMarketOptions": {
   "SpotOptions": {
    "SpotInstanceType": "{{ SpotInstanceType }}",
    "InstanceInterruptionBehavior": "{{ InstanceInterruptionBehavior }}",
    "MaxPrice": "{{ MaxPrice }}",
    "BlockDurationMinutes": "{{ BlockDurationMinutes }}",
    "ValidUntil": "{{ ValidUntil }}"
   },
   "MarketType": "{{ MarketType }}"
  },
  "InstanceRequirements": {
   "LocalStorageTypes": [
    "{{ LocalStorageTypes[0] }}"
   ],
   "InstanceGenerations": [
    "{{ InstanceGenerations[0] }}"
   ],
   "NetworkInterfaceCount": {
    "Min": "{{ Min }}",
    "Max": "{{ Max }}"
   },
   "MemoryGiBPerVCpu": {
    "Min": null,
    "Max": null
   },
   "AcceleratorTypes": [
    "{{ AcceleratorTypes[0] }}"
   ],
   "VCpuCount": {
    "Min": "{{ Min }}",
    "Max": "{{ Max }}"
   },
   "ExcludedInstanceTypes": [
    "{{ ExcludedInstanceTypes[0] }}"
   ],
   "AcceleratorManufacturers": [
    "{{ AcceleratorManufacturers[0] }}"
   ],
   "AllowedInstanceTypes": [
    "{{ AllowedInstanceTypes[0] }}"
   ],
   "LocalStorage": "{{ LocalStorage }}",
   "CpuManufacturers": [
    "{{ CpuManufacturers[0] }}"
   ],
   "AcceleratorCount": {
    "Min": "{{ Min }}",
    "Max": "{{ Max }}"
   },
   "NetworkBandwidthGbps": {
    "Min": null,
    "Max": null
   },
   "BareMetal": "{{ BareMetal }}",
   "RequireHibernateSupport": "{{ RequireHibernateSupport }}",
   "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice": "{{ MaxSpotPriceAsPercentageOfOptimalOnDemandPrice }}",
   "SpotMaxPricePercentageOverLowestPrice": "{{ SpotMaxPricePercentageOverLowestPrice }}",
   "BaselineEbsBandwidthMbps": {
    "Min": "{{ Min }}",
    "Max": "{{ Max }}"
   },
   "OnDemandMaxPricePercentageOverLowestPrice": "{{ OnDemandMaxPricePercentageOverLowestPrice }}",
   "AcceleratorNames": [
    "{{ AcceleratorNames[0] }}"
   ],
   "AcceleratorTotalMemoryMiB": {
    "Min": "{{ Min }}",
    "Max": "{{ Max }}"
   },
   "BurstablePerformance": "{{ BurstablePerformance }}",
   "MemoryMiB": {
    "Min": "{{ Min }}",
    "Max": "{{ Max }}"
   },
   "TotalLocalStorageGB": {
    "Min": null,
    "Max": null
   }
  },
  "RamDiskId": "{{ RamDiskId }}",
  "CapacityReservationSpecification": {
   "CapacityReservationPreference": "{{ CapacityReservationPreference }}",
   "CapacityReservationTarget": {
    "CapacityReservationResourceGroupArn": "{{ CapacityReservationResourceGroupArn }}",
    "CapacityReservationId": "{{ CapacityReservationId }}"
   }
  },
  "CreditSpecification": {
   "CpuCredits": "{{ CpuCredits }}"
  }
 }
}
>>>
--required properties only
INSERT INTO aws.ec2.launch_templates (
 LaunchTemplateData,
 region
)
SELECT 
{{ LaunchTemplateData }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "LaunchTemplateName": "{{ LaunchTemplateName }}",
 "LaunchTemplateData": {
  "SecurityGroups": [
   "{{ SecurityGroups[0] }}"
  ],
  "TagSpecifications": [
   {
    "ResourceType": "{{ ResourceType }}",
    "Tags": [
     {
      "Key": "{{ Key }}",
      "Value": "{{ Value }}"
     }
    ]
   }
  ],
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
  "MaintenanceOptions": {
   "AutoRecovery": "{{ AutoRecovery }}"
  },
  "IamInstanceProfile": {
   "Arn": "{{ Arn }}",
   "Name": "{{ Name }}"
  },
  "KernelId": "{{ KernelId }}",
  "EbsOptimized": "{{ EbsOptimized }}",
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
  "Placement": {
   "GroupName": "{{ GroupName }}",
   "Tenancy": "{{ Tenancy }}",
   "SpreadDomain": "{{ SpreadDomain }}",
   "PartitionNumber": "{{ PartitionNumber }}",
   "AvailabilityZone": "{{ AvailabilityZone }}",
   "Affinity": "{{ Affinity }}",
   "HostId": "{{ HostId }}",
   "HostResourceGroupArn": "{{ HostResourceGroupArn }}",
   "GroupId": "{{ GroupId }}"
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
     {
      "Ipv6Address": "{{ Ipv6Address }}"
     }
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
  "EnclaveOptions": {
   "Enabled": "{{ Enabled }}"
  },
  "ImageId": "{{ ImageId }}",
  "InstanceType": "{{ InstanceType }}",
  "Monitoring": {
   "Enabled": "{{ Enabled }}"
  },
  "HibernationOptions": {
   "Configured": "{{ Configured }}"
  },
  "MetadataOptions": {
   "HttpPutResponseHopLimit": "{{ HttpPutResponseHopLimit }}",
   "HttpTokens": "{{ HttpTokens }}",
   "HttpProtocolIpv6": "{{ HttpProtocolIpv6 }}",
   "InstanceMetadataTags": "{{ InstanceMetadataTags }}",
   "HttpEndpoint": "{{ HttpEndpoint }}"
  },
  "LicenseSpecifications": [
   {
    "LicenseConfigurationArn": "{{ LicenseConfigurationArn }}"
   }
  ],
  "InstanceInitiatedShutdownBehavior": "{{ InstanceInitiatedShutdownBehavior }}",
  "DisableApiStop": "{{ DisableApiStop }}",
  "CpuOptions": {
   "ThreadsPerCore": "{{ ThreadsPerCore }}",
   "AmdSevSnp": "{{ AmdSevSnp }}",
   "CoreCount": "{{ CoreCount }}"
  },
  "PrivateDnsNameOptions": {
   "EnableResourceNameDnsARecord": "{{ EnableResourceNameDnsARecord }}",
   "HostnameType": "{{ HostnameType }}",
   "EnableResourceNameDnsAAAARecord": "{{ EnableResourceNameDnsAAAARecord }}"
  },
  "SecurityGroupIds": [
   "{{ SecurityGroupIds[0] }}"
  ],
  "KeyName": "{{ KeyName }}",
  "DisableApiTermination": "{{ DisableApiTermination }}",
  "InstanceMarketOptions": {
   "SpotOptions": {
    "SpotInstanceType": "{{ SpotInstanceType }}",
    "InstanceInterruptionBehavior": "{{ InstanceInterruptionBehavior }}",
    "MaxPrice": "{{ MaxPrice }}",
    "BlockDurationMinutes": "{{ BlockDurationMinutes }}",
    "ValidUntil": "{{ ValidUntil }}"
   },
   "MarketType": "{{ MarketType }}"
  },
  "InstanceRequirements": {
   "LocalStorageTypes": [
    "{{ LocalStorageTypes[0] }}"
   ],
   "InstanceGenerations": [
    "{{ InstanceGenerations[0] }}"
   ],
   "NetworkInterfaceCount": {
    "Min": "{{ Min }}",
    "Max": "{{ Max }}"
   },
   "MemoryGiBPerVCpu": {
    "Min": null,
    "Max": null
   },
   "AcceleratorTypes": [
    "{{ AcceleratorTypes[0] }}"
   ],
   "VCpuCount": {
    "Min": "{{ Min }}",
    "Max": "{{ Max }}"
   },
   "ExcludedInstanceTypes": [
    "{{ ExcludedInstanceTypes[0] }}"
   ],
   "AcceleratorManufacturers": [
    "{{ AcceleratorManufacturers[0] }}"
   ],
   "AllowedInstanceTypes": [
    "{{ AllowedInstanceTypes[0] }}"
   ],
   "LocalStorage": "{{ LocalStorage }}",
   "CpuManufacturers": [
    "{{ CpuManufacturers[0] }}"
   ],
   "AcceleratorCount": {
    "Min": "{{ Min }}",
    "Max": "{{ Max }}"
   },
   "NetworkBandwidthGbps": {
    "Min": null,
    "Max": null
   },
   "BareMetal": "{{ BareMetal }}",
   "RequireHibernateSupport": "{{ RequireHibernateSupport }}",
   "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice": "{{ MaxSpotPriceAsPercentageOfOptimalOnDemandPrice }}",
   "SpotMaxPricePercentageOverLowestPrice": "{{ SpotMaxPricePercentageOverLowestPrice }}",
   "BaselineEbsBandwidthMbps": {
    "Min": "{{ Min }}",
    "Max": "{{ Max }}"
   },
   "OnDemandMaxPricePercentageOverLowestPrice": "{{ OnDemandMaxPricePercentageOverLowestPrice }}",
   "AcceleratorNames": [
    "{{ AcceleratorNames[0] }}"
   ],
   "AcceleratorTotalMemoryMiB": {
    "Min": "{{ Min }}",
    "Max": "{{ Max }}"
   },
   "BurstablePerformance": "{{ BurstablePerformance }}",
   "MemoryMiB": {
    "Min": "{{ Min }}",
    "Max": "{{ Max }}"
   },
   "TotalLocalStorageGB": {
    "Min": null,
    "Max": null
   }
  },
  "RamDiskId": "{{ RamDiskId }}",
  "CapacityReservationSpecification": {
   "CapacityReservationPreference": "{{ CapacityReservationPreference }}",
   "CapacityReservationTarget": {
    "CapacityReservationResourceGroupArn": "{{ CapacityReservationResourceGroupArn }}",
    "CapacityReservationId": "{{ CapacityReservationId }}"
   }
  },
  "CreditSpecification": {
   "CpuCredits": "{{ CpuCredits }}"
  }
 },
 "VersionDescription": "{{ VersionDescription }}",
 "TagSpecifications": [
  {
   "ResourceType": "{{ ResourceType }}",
   "Tags": [
    null
   ]
  }
 ]
}
>>>
--all properties
INSERT INTO aws.ec2.launch_templates (
 LaunchTemplateName,
 LaunchTemplateData,
 VersionDescription,
 TagSpecifications,
 region
)
SELECT 
 {{ LaunchTemplateName }},
 {{ LaunchTemplateData }},
 {{ VersionDescription }},
 {{ TagSpecifications }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.launch_templates
WHERE data__Identifier = '<LaunchTemplateId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>launch_templates</code> resource, the following permissions are required:

### Create
```json
ec2:CreateLaunchTemplate,
ec2:CreateTags
```

### List
```json
ec2:DescribeLaunchTemplates
```

### Delete
```json
ec2:DeleteLaunchTemplate,
ec2:DeleteTags,
ec2:DescribeLaunchTemplates
```


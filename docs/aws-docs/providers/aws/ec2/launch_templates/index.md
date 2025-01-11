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

Creates, updates, deletes or gets a <code>launch_template</code> resource or lists <code>launch_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies the properties for creating a launch template.<br />The minimum required properties for specifying a launch template are as follows:<br />+ You must specify at least one property for the launch template data.<br />+ You can optionally specify a name for the launch template. If you do not specify a name, CFN creates a name for you.<br /><br />A launch template can contain some or all of the configuration information to launch an instance. When you launch an instance using a launch template, instance properties that are not specified in the launch template use default values, except the <code>ImageId</code> property, which has no default value. If you do not specify an AMI ID for the launch template <code>ImageId</code> property, you must specify an AMI ID for the instance <code>ImageId</code> property.<br />For more information, see &#91;Launch an instance from a launch template&#93;(https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon EC2 User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.launch_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="launch_template_name" /></td><td><code>string</code></td><td>A name for the launch template.</td></tr>
<tr><td><CopyableCode code="launch_template_data" /></td><td><code>object</code></td><td>The information for the launch template.</td></tr>
<tr><td><CopyableCode code="version_description" /></td><td><code>string</code></td><td>A description for the first version of the launch template.</td></tr>
<tr><td><CopyableCode code="tag_specifications" /></td><td><code>array</code></td><td>The tags to apply to the launch template on creation. To tag the launch template, the resource type must be <code>launch-template</code>.<br />To specify the tags for resources that are created during instance launch, use &#91;TagSpecifications&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-tagspecifications).</td></tr>
<tr><td><CopyableCode code="latest_version_number" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="launch_template_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_version_number" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html"><code>AWS::EC2::LaunchTemplate</code></a>.

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
    <td><CopyableCode code="LaunchTemplateData, region" /></td>
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
Gets all <code>launch_templates</code> in a region.
```sql
SELECT
region,
launch_template_name,
launch_template_data,
version_description,
tag_specifications,
latest_version_number,
launch_template_id,
default_version_number
FROM aws.ec2.launch_templates
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>launch_template</code>.
```sql
SELECT
region,
launch_template_name,
launch_template_data,
version_description,
tag_specifications,
latest_version_number,
launch_template_id,
default_version_number
FROM aws.ec2.launch_templates
WHERE region = 'us-east-1' AND data__Identifier = '<LaunchTemplateId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>launch_template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.launch_templates (
 LaunchTemplateData,
 region
)
SELECT 
'{{ LaunchTemplateData }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.launch_templates (
 LaunchTemplateName,
 LaunchTemplateData,
 VersionDescription,
 TagSpecifications,
 region
)
SELECT 
 '{{ LaunchTemplateName }}',
 '{{ LaunchTemplateData }}',
 '{{ VersionDescription }}',
 '{{ TagSpecifications }}',
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
  - name: launch_template
    props:
      - name: LaunchTemplateName
        value: '{{ LaunchTemplateName }}'
      - name: LaunchTemplateData
        value:
          SecurityGroups:
            - '{{ SecurityGroups[0] }}'
          TagSpecifications:
            - ResourceType: '{{ ResourceType }}'
              Tags:
                - Key: '{{ Key }}'
                  Value: '{{ Value }}'
          NetworkPerformanceOptions: null
          UserData: '{{ UserData }}'
          BlockDeviceMappings:
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
          MaintenanceOptions:
            AutoRecovery: '{{ AutoRecovery }}'
          IamInstanceProfile:
            Arn: '{{ Arn }}'
            Name: '{{ Name }}'
          KernelId: '{{ KernelId }}'
          EbsOptimized: '{{ EbsOptimized }}'
          ElasticGpuSpecifications:
            - Type: '{{ Type }}'
          ElasticInferenceAccelerators:
            - Type: '{{ Type }}'
              Count: '{{ Count }}'
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
          NetworkInterfaces:
            - Description: '{{ Description }}'
              PrivateIpAddress: '{{ PrivateIpAddress }}'
              PrivateIpAddresses:
                - Primary: '{{ Primary }}'
                  PrivateIpAddress: '{{ PrivateIpAddress }}'
              SecondaryPrivateIpAddressCount: '{{ SecondaryPrivateIpAddressCount }}'
              Ipv6PrefixCount: '{{ Ipv6PrefixCount }}'
              Ipv4Prefixes:
                - Ipv4Prefix: '{{ Ipv4Prefix }}'
              Ipv4PrefixCount: '{{ Ipv4PrefixCount }}'
              EnablePrimaryIpv6: '{{ EnablePrimaryIpv6 }}'
              GroupSet:
                - '{{ GroupSet[0] }}'
              Ipv6Addresses:
                - Ipv6Address: '{{ Ipv6Address }}'
              Ipv6Prefixes:
                - Ipv6Prefix: '{{ Ipv6Prefix }}'
              SubnetId: '{{ SubnetId }}'
              SourceDestCheck: '{{ SourceDestCheck }}'
              InterfaceType: '{{ InterfaceType }}'
              Ipv6AddressCount: '{{ Ipv6AddressCount }}'
              Tags:
                - null
              ConnectionTrackingSpecification:
                UdpTimeout: '{{ UdpTimeout }}'
                TcpEstablishedTimeout: '{{ TcpEstablishedTimeout }}'
                UdpStreamTimeout: '{{ UdpStreamTimeout }}'
          EnclaveOptions:
            Enabled: '{{ Enabled }}'
          ImageId: '{{ ImageId }}'
          InstanceType: '{{ InstanceType }}'
          Monitoring:
            Enabled: '{{ Enabled }}'
          HibernationOptions:
            Configured: '{{ Configured }}'
          MetadataOptions:
            HttpPutResponseHopLimit: '{{ HttpPutResponseHopLimit }}'
            HttpTokens: '{{ HttpTokens }}'
            HttpProtocolIpv6: '{{ HttpProtocolIpv6 }}'
            InstanceMetadataTags: '{{ InstanceMetadataTags }}'
            HttpEndpoint: '{{ HttpEndpoint }}'
          LicenseSpecifications:
            - LicenseConfigurationArn: '{{ LicenseConfigurationArn }}'
          InstanceInitiatedShutdownBehavior: '{{ InstanceInitiatedShutdownBehavior }}'
          DisableApiStop: '{{ DisableApiStop }}'
          CpuOptions:
            ThreadsPerCore: '{{ ThreadsPerCore }}'
            AmdSevSnp: '{{ AmdSevSnp }}'
            CoreCount: '{{ CoreCount }}'
          PrivateDnsNameOptions:
            EnableResourceNameDnsARecord: '{{ EnableResourceNameDnsARecord }}'
            HostnameType: '{{ HostnameType }}'
            EnableResourceNameDnsAAAARecord: '{{ EnableResourceNameDnsAAAARecord }}'
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
          KeyName: '{{ KeyName }}'
          DisableApiTermination: '{{ DisableApiTermination }}'
          InstanceMarketOptions:
            SpotOptions:
              SpotInstanceType: '{{ SpotInstanceType }}'
              InstanceInterruptionBehavior: '{{ InstanceInterruptionBehavior }}'
              MaxPrice: '{{ MaxPrice }}'
              BlockDurationMinutes: '{{ BlockDurationMinutes }}'
              ValidUntil: '{{ ValidUntil }}'
            MarketType: '{{ MarketType }}'
          InstanceRequirements:
            InstanceGenerations:
              - '{{ InstanceGenerations[0] }}'
            MemoryGiBPerVCpu:
              Min: null
              Max: null
            AcceleratorTypes:
              - '{{ AcceleratorTypes[0] }}'
            VCpuCount:
              Min: '{{ Min }}'
              Max: '{{ Max }}'
            AcceleratorManufacturers:
              - '{{ AcceleratorManufacturers[0] }}'
            LocalStorage: '{{ LocalStorage }}'
            CpuManufacturers:
              - '{{ CpuManufacturers[0] }}'
            BareMetal: '{{ BareMetal }}'
            RequireHibernateSupport: '{{ RequireHibernateSupport }}'
            MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: '{{ MaxSpotPriceAsPercentageOfOptimalOnDemandPrice }}'
            OnDemandMaxPricePercentageOverLowestPrice: '{{ OnDemandMaxPricePercentageOverLowestPrice }}'
            MemoryMiB:
              Min: '{{ Min }}'
              Max: '{{ Max }}'
            LocalStorageTypes:
              - '{{ LocalStorageTypes[0] }}'
            NetworkInterfaceCount:
              Min: '{{ Min }}'
              Max: '{{ Max }}'
            ExcludedInstanceTypes:
              - '{{ ExcludedInstanceTypes[0] }}'
            AllowedInstanceTypes:
              - '{{ AllowedInstanceTypes[0] }}'
            AcceleratorCount:
              Min: '{{ Min }}'
              Max: '{{ Max }}'
            NetworkBandwidthGbps:
              Min: null
              Max: null
            BaselinePerformanceFactors:
              Cpu:
                References:
                  - InstanceFamily: '{{ InstanceFamily }}'
            SpotMaxPricePercentageOverLowestPrice: '{{ SpotMaxPricePercentageOverLowestPrice }}'
            BaselineEbsBandwidthMbps:
              Min: '{{ Min }}'
              Max: '{{ Max }}'
            AcceleratorNames:
              - '{{ AcceleratorNames[0] }}'
            AcceleratorTotalMemoryMiB:
              Min: '{{ Min }}'
              Max: '{{ Max }}'
            BurstablePerformance: '{{ BurstablePerformance }}'
            TotalLocalStorageGB:
              Min: null
              Max: null
          RamDiskId: '{{ RamDiskId }}'
          CapacityReservationSpecification:
            CapacityReservationPreference: '{{ CapacityReservationPreference }}'
            CapacityReservationTarget:
              CapacityReservationResourceGroupArn: '{{ CapacityReservationResourceGroupArn }}'
              CapacityReservationId: '{{ CapacityReservationId }}'
          CreditSpecification:
            CpuCredits: '{{ CpuCredits }}'
      - name: VersionDescription
        value: '{{ VersionDescription }}'
      - name: TagSpecifications
        value:
          - ResourceType: '{{ ResourceType }}'
            Tags:
              - null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.launch_templates
WHERE data__Identifier = '<LaunchTemplateId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>launch_templates</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeLaunchTemplates
```

### Create
```json
ec2:CreateLaunchTemplate,
ec2:CreateTags
```

### Update
```json
ec2:CreateLaunchTemplateVersion
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

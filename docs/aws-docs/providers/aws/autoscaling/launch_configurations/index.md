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
launch_configuration_name
FROM aws.autoscaling.launch_configurations
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
 "ImageId": "{{ ImageId }}",
 "InstanceType": "{{ InstanceType }}"
}
>>>
--required properties only
INSERT INTO aws.autoscaling.launch_configurations (
 ImageId,
 InstanceType,
 region
)
SELECT 
{{ ImageId }},
 {{ InstanceType }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AssociatePublicIpAddress": "{{ AssociatePublicIpAddress }}",
 "BlockDeviceMappings": [
  {
   "NoDevice": "{{ NoDevice }}",
   "VirtualName": "{{ VirtualName }}",
   "Ebs": {
    "SnapshotId": "{{ SnapshotId }}",
    "VolumeType": "{{ VolumeType }}",
    "Encrypted": "{{ Encrypted }}",
    "Iops": "{{ Iops }}",
    "VolumeSize": "{{ VolumeSize }}",
    "DeleteOnTermination": "{{ DeleteOnTermination }}",
    "Throughput": "{{ Throughput }}"
   },
   "DeviceName": "{{ DeviceName }}"
  }
 ],
 "ClassicLinkVPCId": "{{ ClassicLinkVPCId }}",
 "ClassicLinkVPCSecurityGroups": [
  "{{ ClassicLinkVPCSecurityGroups[0] }}"
 ],
 "EbsOptimized": "{{ EbsOptimized }}",
 "IamInstanceProfile": "{{ IamInstanceProfile }}",
 "ImageId": "{{ ImageId }}",
 "InstanceId": "{{ InstanceId }}",
 "InstanceMonitoring": "{{ InstanceMonitoring }}",
 "InstanceType": "{{ InstanceType }}",
 "KernelId": "{{ KernelId }}",
 "KeyName": "{{ KeyName }}",
 "LaunchConfigurationName": "{{ LaunchConfigurationName }}",
 "MetadataOptions": {
  "HttpPutResponseHopLimit": "{{ HttpPutResponseHopLimit }}",
  "HttpTokens": "{{ HttpTokens }}",
  "HttpEndpoint": "{{ HttpEndpoint }}"
 },
 "PlacementTenancy": "{{ PlacementTenancy }}",
 "RamDiskId": "{{ RamDiskId }}",
 "SecurityGroups": [
  "{{ SecurityGroups[0] }}"
 ],
 "SpotPrice": "{{ SpotPrice }}",
 "UserData": "{{ UserData }}"
}
>>>
--all properties
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
 {{ AssociatePublicIpAddress }},
 {{ BlockDeviceMappings }},
 {{ ClassicLinkVPCId }},
 {{ ClassicLinkVPCSecurityGroups }},
 {{ EbsOptimized }},
 {{ IamInstanceProfile }},
 {{ ImageId }},
 {{ InstanceId }},
 {{ InstanceMonitoring }},
 {{ InstanceType }},
 {{ KernelId }},
 {{ KeyName }},
 {{ LaunchConfigurationName }},
 {{ MetadataOptions }},
 {{ PlacementTenancy }},
 {{ RamDiskId }},
 {{ SecurityGroups }},
 {{ SpotPrice }},
 {{ UserData }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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


---
title: launch_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - launch_profiles
  - nimblestudio
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


Used to retrieve a list of <code>launch_profiles</code> in a region or to create or delete a <code>launch_profiles</code> resource, use <code>launch_profile</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a launch profile which delegates access to a collection of studio components to studio users</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.launch_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="launch_profile_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td>&lt;p&gt;The studio ID. &lt;&#x2F;p&gt;</td></tr>
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
launch_profile_id,
studio_id
FROM aws.nimblestudio.launch_profiles
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
 "Ec2SubnetIds": [
  "{{ Ec2SubnetIds[0] }}"
 ],
 "LaunchProfileProtocolVersions": [
  "{{ LaunchProfileProtocolVersions[0] }}"
 ],
 "Name": "{{ Name }}",
 "StreamConfiguration": {
  "ClipboardMode": "{{ ClipboardMode }}",
  "Ec2InstanceTypes": [
   "{{ Ec2InstanceTypes[0] }}"
  ],
  "MaxSessionLengthInMinutes": null,
  "StreamingImageIds": [
   "{{ StreamingImageIds[0] }}"
  ],
  "MaxStoppedSessionLengthInMinutes": null,
  "SessionStorage": {
   "Root": {
    "Linux": "{{ Linux }}",
    "Windows": "{{ Windows }}"
   },
   "Mode": [
    "{{ Mode[0] }}"
   ]
  },
  "SessionBackup": {
   "Mode": "{{ Mode }}",
   "MaxBackupsToRetain": null
  },
  "SessionPersistenceMode": "{{ SessionPersistenceMode }}",
  "VolumeConfiguration": {
   "Size": null,
   "Throughput": null,
   "Iops": null
  },
  "AutomaticTerminationMode": "{{ AutomaticTerminationMode }}"
 },
 "StudioComponentIds": [
  "{{ StudioComponentIds[0] }}"
 ],
 "StudioId": "{{ StudioId }}"
}
>>>
--required properties only
INSERT INTO aws.nimblestudio.launch_profiles (
 Ec2SubnetIds,
 LaunchProfileProtocolVersions,
 Name,
 StreamConfiguration,
 StudioComponentIds,
 StudioId,
 region
)
SELECT 
{{ .Ec2SubnetIds }},
 {{ .LaunchProfileProtocolVersions }},
 {{ .Name }},
 {{ .StreamConfiguration }},
 {{ .StudioComponentIds }},
 {{ .StudioId }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "Ec2SubnetIds": [
  "{{ Ec2SubnetIds[0] }}"
 ],
 "LaunchProfileProtocolVersions": [
  "{{ LaunchProfileProtocolVersions[0] }}"
 ],
 "Name": "{{ Name }}",
 "StreamConfiguration": {
  "ClipboardMode": "{{ ClipboardMode }}",
  "Ec2InstanceTypes": [
   "{{ Ec2InstanceTypes[0] }}"
  ],
  "MaxSessionLengthInMinutes": null,
  "StreamingImageIds": [
   "{{ StreamingImageIds[0] }}"
  ],
  "MaxStoppedSessionLengthInMinutes": null,
  "SessionStorage": {
   "Root": {
    "Linux": "{{ Linux }}",
    "Windows": "{{ Windows }}"
   },
   "Mode": [
    "{{ Mode[0] }}"
   ]
  },
  "SessionBackup": {
   "Mode": "{{ Mode }}",
   "MaxBackupsToRetain": null
  },
  "SessionPersistenceMode": "{{ SessionPersistenceMode }}",
  "VolumeConfiguration": {
   "Size": null,
   "Throughput": null,
   "Iops": null
  },
  "AutomaticTerminationMode": "{{ AutomaticTerminationMode }}"
 },
 "StudioComponentIds": [
  "{{ StudioComponentIds[0] }}"
 ],
 "StudioId": "{{ StudioId }}",
 "Tags": {}
}
>>>
--all properties
INSERT INTO aws.nimblestudio.launch_profiles (
 Description,
 Ec2SubnetIds,
 LaunchProfileProtocolVersions,
 Name,
 StreamConfiguration,
 StudioComponentIds,
 StudioId,
 Tags,
 region
)
SELECT 
 {{ .Description }},
 {{ .Ec2SubnetIds }},
 {{ .LaunchProfileProtocolVersions }},
 {{ .Name }},
 {{ .StreamConfiguration }},
 {{ .StudioComponentIds }},
 {{ .StudioId }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.nimblestudio.launch_profiles
WHERE data__Identifier = '<LaunchProfileId|StudioId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>launch_profiles</code> resource, the following permissions are required:

### Create
```json
nimble:CreateLaunchProfile,
nimble:GetLaunchProfile,
nimble:TagResource,
ec2:CreateNetworkInterface,
ec2:CreateNetworkInterfacePermission,
ec2:RunInstances,
ec2:DescribeSubnets
```

### Delete
```json
nimble:DeleteLaunchProfile,
nimble:GetLaunchProfile,
nimble:UntagResource
```

### List
```json
nimble:ListLaunchProfiles
```


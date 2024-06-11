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

Creates, updates, deletes or gets a <code>launch_profile</code> resource or lists <code>launch_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a launch profile which delegates access to a collection of studio components to studio users</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.launch_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td><p>The description.</p></td></tr>
<tr><td><CopyableCode code="ec2_subnet_ids" /></td><td><code>array</code></td><td><p>Specifies the IDs of the EC2 subnets where streaming sessions will be accessible from.<br/>            These subnets must support the specified instance types. </p></td></tr>
<tr><td><CopyableCode code="launch_profile_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="launch_profile_protocol_versions" /></td><td><code>array</code></td><td><p>The version number of the protocol that is used by the launch profile. The only valid<br/>            version is "2021-03-31".</p></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td><p>The name for the launch profile.</p></td></tr>
<tr><td><CopyableCode code="stream_configuration" /></td><td><code><p>A configuration for a streaming session.</p></code></td><td></td></tr>
<tr><td><CopyableCode code="studio_component_ids" /></td><td><code>array</code></td><td><p>Unique identifiers for a collection of studio components that can be used with this<br/>            launch profile.</p></td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td><p>The studio ID. </p></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="StudioId, Name, StudioComponentIds, Ec2SubnetIds, StreamConfiguration, LaunchProfileProtocolVersions, region" /></td>
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
List all <code>launch_profiles</code> in a region.
```sql
SELECT
region,
launch_profile_id,
studio_id
FROM aws.nimblestudio.launch_profiles
WHERE region = 'us-east-1';
```
Gets all properties from a <code>launch_profile</code>.
```sql
SELECT
region,
description,
ec2_subnet_ids,
launch_profile_id,
launch_profile_protocol_versions,
name,
stream_configuration,
studio_component_ids,
studio_id,
tags
FROM aws.nimblestudio.launch_profiles
WHERE region = 'us-east-1' AND data__Identifier = '<LaunchProfileId>|<StudioId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>launch_profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
'{{ Ec2SubnetIds }}',
 '{{ LaunchProfileProtocolVersions }}',
 '{{ Name }}',
 '{{ StreamConfiguration }}',
 '{{ StudioComponentIds }}',
 '{{ StudioId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ Description }}',
 '{{ Ec2SubnetIds }}',
 '{{ LaunchProfileProtocolVersions }}',
 '{{ Name }}',
 '{{ StreamConfiguration }}',
 '{{ StudioComponentIds }}',
 '{{ StudioId }}',
 '{{ Tags }}',
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
  - name: launch_profile
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Ec2SubnetIds
        value:
          - '{{ Ec2SubnetIds[0] }}'
      - name: LaunchProfileProtocolVersions
        value:
          - '{{ LaunchProfileProtocolVersions[0] }}'
      - name: Name
        value: '{{ Name }}'
      - name: StreamConfiguration
        value:
          ClipboardMode: '{{ ClipboardMode }}'
          Ec2InstanceTypes:
            - '{{ Ec2InstanceTypes[0] }}'
          MaxSessionLengthInMinutes: null
          StreamingImageIds:
            - '{{ StreamingImageIds[0] }}'
          MaxStoppedSessionLengthInMinutes: null
          SessionStorage:
            Root:
              Linux: '{{ Linux }}'
              Windows: '{{ Windows }}'
            Mode:
              - '{{ Mode[0] }}'
          SessionBackup:
            Mode: '{{ Mode }}'
            MaxBackupsToRetain: null
          SessionPersistenceMode: '{{ SessionPersistenceMode }}'
          VolumeConfiguration:
            Size: null
            Throughput: null
            Iops: null
          AutomaticTerminationMode: '{{ AutomaticTerminationMode }}'
      - name: StudioComponentIds
        value:
          - '{{ StudioComponentIds[0] }}'
      - name: StudioId
        value: '{{ StudioId }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
nimble:GetLaunchProfile
```

### Update
```json
nimble:UpdateLaunchProfile,
nimble:GetLaunchProfile,
ec2:CreateNetworkInterface,
ec2:CreateNetworkInterfacePermission,
ec2:DescribeSubnets,
ec2:RunInstances
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


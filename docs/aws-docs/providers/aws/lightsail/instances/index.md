---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - lightsail
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

Creates, updates, deletes or gets an <code>instance</code> resource or lists <code>instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Instance</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.instances" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="support_code" /></td><td><code>string</code></td><td>Support code to help identify any issues</td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>Resource type of Lightsail instance.</td></tr>
<tr><td><CopyableCode code="is_static_ip" /></td><td><code>boolean</code></td><td>Is the IP Address of the Instance is the static IP</td></tr>
<tr><td><CopyableCode code="private_ip_address" /></td><td><code>string</code></td><td>Private IP Address of the Instance</td></tr>
<tr><td><CopyableCode code="public_ip_address" /></td><td><code>string</code></td><td>Public IP Address of the Instance</td></tr>
<tr><td><CopyableCode code="ipv6_addresses" /></td><td><code>array</code></td><td>IPv6 addresses of the instance</td></tr>
<tr><td><CopyableCode code="location" /></td><td><code>Location of a resource.</code></td><td></td></tr>
<tr><td><CopyableCode code="hardware" /></td><td><code>Hardware of the Instance.</code></td><td></td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>Current State of the Instance.</code></td><td></td></tr>
<tr><td><CopyableCode code="networking" /></td><td><code>Networking of the Instance.</code></td><td></td></tr>
<tr><td><CopyableCode code="user_name" /></td><td><code>string</code></td><td>Username of the  Lightsail instance.</td></tr>
<tr><td><CopyableCode code="ssh_key_name" /></td><td><code>string</code></td><td>SSH Key Name of the  Lightsail instance.</td></tr>
<tr><td><CopyableCode code="instance_name" /></td><td><code>string</code></td><td>The names to use for your new Lightsail instance.</td></tr>
<tr><td><CopyableCode code="availability_zone" /></td><td><code>string</code></td><td>The Availability Zone in which to create your instance. Use the following format: us-east-2a (case sensitive). Be sure to add the include Availability Zones parameter to your request.</td></tr>
<tr><td><CopyableCode code="bundle_id" /></td><td><code>string</code></td><td>The bundle of specification information for your virtual private server (or instance ), including the pricing plan (e.g., micro_1_0 ).</td></tr>
<tr><td><CopyableCode code="blueprint_id" /></td><td><code>string</code></td><td>The ID for a virtual private server image (e.g., app_wordpress_4_4 or app_lamp_7_0 ). Use the get blueprints operation to return a list of available images (or blueprints ).</td></tr>
<tr><td><CopyableCode code="add_ons" /></td><td><code>array</code></td><td>An array of objects representing the add-ons to enable for the new instance.</td></tr>
<tr><td><CopyableCode code="user_data" /></td><td><code>string</code></td><td>A launch script you can create that configures a server with additional user data. For example, you might want to run apt-get -y update.</td></tr>
<tr><td><CopyableCode code="key_pair_name" /></td><td><code>string</code></td><td>The name of your key pair.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="InstanceName, BlueprintId, BundleId, region" /></td>
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
List all <code>instances</code> in a region.
```sql
SELECT
region,
instance_name
FROM aws.lightsail.instances
WHERE region = 'us-east-1';
```
Gets all properties from an <code>instance</code>.
```sql
SELECT
region,
support_code,
resource_type,
is_static_ip,
private_ip_address,
public_ip_address,
ipv6_addresses,
location,
hardware,
state,
networking,
user_name,
ssh_key_name,
instance_name,
availability_zone,
bundle_id,
blueprint_id,
add_ons,
user_data,
key_pair_name,
tags,
instance_arn
FROM aws.lightsail.instances
WHERE region = 'us-east-1' AND data__Identifier = '<InstanceName>';
```


## `INSERT` example

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
INSERT INTO aws.lightsail.instances (
 InstanceName,
 BundleId,
 BlueprintId,
 region
)
SELECT 
'{{ InstanceName }}',
 '{{ BundleId }}',
 '{{ BlueprintId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.lightsail.instances (
 Location,
 Hardware,
 State,
 Networking,
 InstanceName,
 AvailabilityZone,
 BundleId,
 BlueprintId,
 AddOns,
 UserData,
 KeyPairName,
 Tags,
 region
)
SELECT 
 '{{ Location }}',
 '{{ Hardware }}',
 '{{ State }}',
 '{{ Networking }}',
 '{{ InstanceName }}',
 '{{ AvailabilityZone }}',
 '{{ BundleId }}',
 '{{ BlueprintId }}',
 '{{ AddOns }}',
 '{{ UserData }}',
 '{{ KeyPairName }}',
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
  - name: instance
    props:
      - name: Location
        value:
          AvailabilityZone: '{{ AvailabilityZone }}'
          RegionName: '{{ RegionName }}'
      - name: Hardware
        value:
          CpuCount: '{{ CpuCount }}'
          RamSizeInGb: '{{ RamSizeInGb }}'
          Disks:
            - DiskName: '{{ DiskName }}'
              SizeInGb: '{{ SizeInGb }}'
              IsSystemDisk: '{{ IsSystemDisk }}'
              IOPS: '{{ IOPS }}'
              Path: '{{ Path }}'
              AttachedTo: '{{ AttachedTo }}'
              AttachmentState: '{{ AttachmentState }}'
      - name: State
        value:
          Code: '{{ Code }}'
          Name: '{{ Name }}'
      - name: Networking
        value:
          Ports:
            - FromPort: '{{ FromPort }}'
              ToPort: '{{ ToPort }}'
              Protocol: '{{ Protocol }}'
              AccessFrom: '{{ AccessFrom }}'
              AccessType: '{{ AccessType }}'
              CommonName: '{{ CommonName }}'
              AccessDirection: '{{ AccessDirection }}'
              Ipv6Cidrs:
                - '{{ Ipv6Cidrs[0] }}'
              CidrListAliases:
                - '{{ CidrListAliases[0] }}'
              Cidrs:
                - '{{ Cidrs[0] }}'
          MonthlyTransfer:
            GbPerMonthAllocated: '{{ GbPerMonthAllocated }}'
      - name: InstanceName
        value: '{{ InstanceName }}'
      - name: AvailabilityZone
        value: '{{ AvailabilityZone }}'
      - name: BundleId
        value: '{{ BundleId }}'
      - name: BlueprintId
        value: '{{ BlueprintId }}'
      - name: AddOns
        value:
          - AddOnType: '{{ AddOnType }}'
            Status: '{{ Status }}'
            AutoSnapshotAddOnRequest:
              SnapshotTimeOfDay: '{{ SnapshotTimeOfDay }}'
      - name: UserData
        value: '{{ UserData }}'
      - name: KeyPairName
        value: '{{ KeyPairName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.lightsail.instances
WHERE data__Identifier = '<InstanceName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>instances</code> resource, the following permissions are required:

### Create
```json
lightsail:CreateInstances,
lightsail:GetInstances,
lightsail:EnableAddOn,
lightsail:GetInstance,
lightsail:DisableAddOn,
lightsail:PutInstancePublicPorts,
lightsail:AttachDisk,
lightsail:DetachDisk,
lightsail:StartInstance,
lightsail:StopInstance,
lightsail:GetDisk,
lightsail:GetRegions,
lightsail:TagResource,
lightsail:UntagResource
```

### Read
```json
lightsail:GetInstances,
lightsail:GetInstance
```

### Delete
```json
lightsail:GetInstances,
lightsail:GetInstance,
lightsail:DeleteInstance
```

### List
```json
lightsail:GetInstances
```

### Update
```json
lightsail:GetInstances,
lightsail:GetInstance,
lightsail:DeleteInstance,
lightsail:EnableAddOn,
lightsail:DisableAddOn,
lightsail:PutInstancePublicPorts,
lightsail:AttachDisk,
lightsail:DetachDisk,
lightsail:StartInstance,
lightsail:StopInstance,
lightsail:GetDisk,
lightsail:TagResource,
lightsail:UntagResource
```


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


Used to retrieve a list of <code>instances</code> in a region or to create or delete a <code>instances</code> resource, use <code>instance</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Instance</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.instances" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="instance_name" /></td><td><code>string</code></td><td>The names to use for your new Lightsail instance.</td></tr>
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
instance_name
FROM aws.lightsail.instances
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>instance</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- instance.iql (required properties only)
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
-- instance.iql (all properties)
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

## `DELETE` Example

```sql
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


---
title: fuota_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - fuota_tasks
  - iotwireless
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

Creates, updates, deletes or gets a <code>fuota_task</code> resource or lists <code>fuota_tasks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fuota_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage FUOTA tasks.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.fuota_tasks" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of FUOTA task</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>FUOTA task description</td></tr>
<tr><td><CopyableCode code="lo_ra_wan" /></td><td><code>object</code></td><td>FUOTA task LoRaWAN</td></tr>
<tr><td><CopyableCode code="firmware_update_image" /></td><td><code>string</code></td><td>FUOTA task firmware update image binary S3 link</td></tr>
<tr><td><CopyableCode code="firmware_update_role" /></td><td><code>string</code></td><td>FUOTA task firmware IAM role for reading S3</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>FUOTA task arn. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>FUOTA task id. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the FUOTA task.</td></tr>
<tr><td><CopyableCode code="fuota_task_status" /></td><td><code>string</code></td><td>FUOTA task status. Returned after successful read.</td></tr>
<tr><td><CopyableCode code="associate_wireless_device" /></td><td><code>string</code></td><td>Wireless device to associate. Only for update request.</td></tr>
<tr><td><CopyableCode code="disassociate_wireless_device" /></td><td><code>string</code></td><td>Wireless device to disassociate. Only for update request.</td></tr>
<tr><td><CopyableCode code="associate_multicast_group" /></td><td><code>string</code></td><td>Multicast group to associate. Only for update request.</td></tr>
<tr><td><CopyableCode code="disassociate_multicast_group" /></td><td><code>string</code></td><td>Multicast group to disassociate. Only for update request.</td></tr>
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
    <td><CopyableCode code="LoRaWAN, FirmwareUpdateImage, FirmwareUpdateRole, region" /></td>
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
Gets all <code>fuota_tasks</code> in a region.
```sql
SELECT
region,
name,
description,
lo_ra_wan,
firmware_update_image,
firmware_update_role,
arn,
id,
tags,
fuota_task_status,
associate_wireless_device,
disassociate_wireless_device,
associate_multicast_group,
disassociate_multicast_group
FROM aws.iotwireless.fuota_tasks
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>fuota_task</code>.
```sql
SELECT
region,
name,
description,
lo_ra_wan,
firmware_update_image,
firmware_update_role,
arn,
id,
tags,
fuota_task_status,
associate_wireless_device,
disassociate_wireless_device,
associate_multicast_group,
disassociate_multicast_group
FROM aws.iotwireless.fuota_tasks
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>fuota_task</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotwireless.fuota_tasks (
 LoRaWAN,
 FirmwareUpdateImage,
 FirmwareUpdateRole,
 region
)
SELECT 
'{{ LoRaWAN }}',
 '{{ FirmwareUpdateImage }}',
 '{{ FirmwareUpdateRole }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotwireless.fuota_tasks (
 Name,
 Description,
 LoRaWAN,
 FirmwareUpdateImage,
 FirmwareUpdateRole,
 Tags,
 AssociateWirelessDevice,
 DisassociateWirelessDevice,
 AssociateMulticastGroup,
 DisassociateMulticastGroup,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ LoRaWAN }}',
 '{{ FirmwareUpdateImage }}',
 '{{ FirmwareUpdateRole }}',
 '{{ Tags }}',
 '{{ AssociateWirelessDevice }}',
 '{{ DisassociateWirelessDevice }}',
 '{{ AssociateMulticastGroup }}',
 '{{ DisassociateMulticastGroup }}',
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
  - name: fuota_task
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: LoRaWAN
        value:
          RfRegion: '{{ RfRegion }}'
          DlClass: '{{ DlClass }}'
          NumberOfDevicesRequested: '{{ NumberOfDevicesRequested }}'
          NumberOfDevicesInGroup: '{{ NumberOfDevicesInGroup }}'
      - name: FirmwareUpdateImage
        value: '{{ FirmwareUpdateImage }}'
      - name: FirmwareUpdateRole
        value: '{{ FirmwareUpdateRole }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: AssociateWirelessDevice
        value: '{{ AssociateWirelessDevice }}'
      - name: DisassociateWirelessDevice
        value: '{{ DisassociateWirelessDevice }}'
      - name: AssociateMulticastGroup
        value: '{{ AssociateMulticastGroup }}'
      - name: DisassociateMulticastGroup
        value: '{{ DisassociateMulticastGroup }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iotwireless.fuota_tasks
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>fuota_tasks</code> resource, the following permissions are required:

### Create
```json
iotwireless:CreateFuotaTask,
iotwireless:TagResource,
iotwireless:ListTagsForResource,
iam:GetRole,
iam:PassRole
```

### Read
```json
iotwireless:GetFuotaTask,
iotwireless:ListTagsForResource
```

### Update
```json
iam:PassRole,
iotwireless:UpdateFuotaTask,
iotwireless:UntagResource,
iotwireless:ListTagsForResource,
iotwireless:AssociateMulticastGroupWithFuotaTask,
iotwireless:DisassociateMulticastGroupFromFuotaTask,
iotwireless:AssociateWirelessDeviceWithFuotaTask,
iotwireless:DisassociateWirelessDeviceFromFuotaTask
```

### Delete
```json
iotwireless:DeleteFuotaTask
```

### List
```json
iotwireless:ListFuotaTasks,
iotwireless:ListTagsForResource
```


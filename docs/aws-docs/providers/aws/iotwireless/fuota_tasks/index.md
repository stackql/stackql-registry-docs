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


Used to retrieve a list of <code>fuota_tasks</code> in a region or to create or delete a <code>fuota_tasks</code> resource, use <code>fuota_task</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fuota_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage FUOTA tasks.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.fuota_tasks" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>FUOTA task id. Returned after successful create.</td></tr>
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
id
FROM aws.iotwireless.fuota_tasks
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
 "LoRaWAN": {
  "RfRegion": "{{ RfRegion }}",
  "DlClass": "{{ DlClass }}",
  "NumberOfDevicesRequested": "{{ NumberOfDevicesRequested }}",
  "NumberOfDevicesInGroup": "{{ NumberOfDevicesInGroup }}"
 },
 "FirmwareUpdateImage": "{{ FirmwareUpdateImage }}",
 "FirmwareUpdateRole": "{{ FirmwareUpdateRole }}"
}
>>>
--required properties only
INSERT INTO aws.iotwireless.fuota_tasks (
 LoRaWAN,
 FirmwareUpdateImage,
 FirmwareUpdateRole,
 region
)
SELECT 
{{ .LoRaWAN }},
 {{ .FirmwareUpdateImage }},
 {{ .FirmwareUpdateRole }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "LoRaWAN": {
  "RfRegion": "{{ RfRegion }}",
  "DlClass": "{{ DlClass }}",
  "NumberOfDevicesRequested": "{{ NumberOfDevicesRequested }}",
  "NumberOfDevicesInGroup": "{{ NumberOfDevicesInGroup }}"
 },
 "FirmwareUpdateImage": "{{ FirmwareUpdateImage }}",
 "FirmwareUpdateRole": "{{ FirmwareUpdateRole }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "AssociateWirelessDevice": "{{ AssociateWirelessDevice }}",
 "DisassociateWirelessDevice": "{{ DisassociateWirelessDevice }}",
 "AssociateMulticastGroup": "{{ AssociateMulticastGroup }}",
 "DisassociateMulticastGroup": "{{ DisassociateMulticastGroup }}"
}
>>>
--all properties
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
 {{ .Name }},
 {{ .Description }},
 {{ .LoRaWAN }},
 {{ .FirmwareUpdateImage }},
 {{ .FirmwareUpdateRole }},
 {{ .Tags }},
 {{ .AssociateWirelessDevice }},
 {{ .DisassociateWirelessDevice }},
 {{ .AssociateMulticastGroup }},
 {{ .DisassociateMulticastGroup }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
iotwireless:DeleteFuotaTask
```

### List
```json
iotwireless:ListFuotaTasks,
iotwireless:ListTagsForResource
```


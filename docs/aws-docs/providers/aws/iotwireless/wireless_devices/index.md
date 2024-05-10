---
title: wireless_devices
hide_title: false
hide_table_of_contents: false
keywords:
  - wireless_devices
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


Used to retrieve a list of <code>wireless_devices</code> in a region or to create or delete a <code>wireless_devices</code> resource, use <code>wireless_device</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wireless_devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage wireless gateways, including LoRa gateways.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.wireless_devices" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Wireless device Id. Returned after successful create.</td></tr>
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
FROM aws.iotwireless.wireless_devices
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>wireless_device</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- wireless_device.iql (required properties only)
INSERT INTO aws.iotwireless.wireless_devices (
 Type,
 DestinationName,
 region
)
SELECT 
'{{ Type }}',
 '{{ DestinationName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- wireless_device.iql (all properties)
INSERT INTO aws.iotwireless.wireless_devices (
 Type,
 Name,
 Description,
 DestinationName,
 LoRaWAN,
 Tags,
 ThingArn,
 LastUplinkReceivedAt,
 Positioning,
 region
)
SELECT 
 '{{ Type }}',
 '{{ Name }}',
 '{{ Description }}',
 '{{ DestinationName }}',
 '{{ LoRaWAN }}',
 '{{ Tags }}',
 '{{ ThingArn }}',
 '{{ LastUplinkReceivedAt }}',
 '{{ Positioning }}',
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
  - name: wireless_device
    props:
      - name: Type
        value: '{{ Type }}'
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: DestinationName
        value: '{{ DestinationName }}'
      - name: LoRaWAN
        value:
          DevEui: '{{ DevEui }}'
          DeviceProfileId: '{{ DeviceProfileId }}'
          ServiceProfileId: '{{ ServiceProfileId }}'
          OtaaV11:
            AppKey: '{{ AppKey }}'
            NwkKey: '{{ NwkKey }}'
            JoinEui: '{{ JoinEui }}'
          OtaaV10x:
            AppKey: '{{ AppKey }}'
            AppEui: '{{ AppEui }}'
          AbpV11:
            DevAddr: '{{ DevAddr }}'
            SessionKeys:
              FNwkSIntKey: '{{ FNwkSIntKey }}'
              SNwkSIntKey: '{{ SNwkSIntKey }}'
              NwkSEncKey: '{{ NwkSEncKey }}'
              AppSKey: '{{ AppSKey }}'
          AbpV10x:
            DevAddr: '{{ DevAddr }}'
            SessionKeys:
              NwkSKey: '{{ NwkSKey }}'
              AppSKey: '{{ AppSKey }}'
          FPorts:
            Applications:
              - DestinationName: '{{ DestinationName }}'
                FPort: '{{ FPort }}'
                Type: '{{ Type }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: ThingArn
        value: '{{ ThingArn }}'
      - name: LastUplinkReceivedAt
        value: '{{ LastUplinkReceivedAt }}'
      - name: Positioning
        value: '{{ Positioning }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iotwireless.wireless_devices
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>wireless_devices</code> resource, the following permissions are required:

### Create
```json
iotwireless:CreateWirelessDevice,
iotwireless:TagResource,
iotwireless:ListTagsForResource
```

### Delete
```json
iotwireless:DeleteWirelessDevice,
iotwireless:DisassociateWirelessDeviceFromThing
```

### List
```json
iotwireless:ListWirelessDevices,
iotwireless:ListTagsForResource
```


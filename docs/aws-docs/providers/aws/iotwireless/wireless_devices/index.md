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

Creates, updates, deletes or gets a <code>wireless_device</code> resource or lists <code>wireless_devices</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wireless_devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage wireless gateways, including LoRa gateways.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.wireless_devices" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>Wireless device type, currently only Sidewalk and LoRa</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Wireless device name</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Wireless device description</td></tr>
<tr><td><CopyableCode code="destination_name" /></td><td><code>string</code></td><td>Wireless device destination name</td></tr>
<tr><td><CopyableCode code="lo_ra_wan" /></td><td><code>object</code></td><td>The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Device.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the device. Currently not supported, will not create if tags are passed.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Wireless device arn. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Wireless device Id. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="thing_arn" /></td><td><code>string</code></td><td>Thing arn. Passed into update to associate Thing with Wireless device.</td></tr>
<tr><td><CopyableCode code="thing_name" /></td><td><code>string</code></td><td>Thing Arn. If there is a Thing created, this can be returned with a Get call.</td></tr>
<tr><td><CopyableCode code="last_uplink_received_at" /></td><td><code>string</code></td><td>The date and time when the most recent uplink was received.</td></tr>
<tr><td><CopyableCode code="positioning" /></td><td><code>string</code></td><td>FPort values for the GNSS, stream, and ClockSync functions of the positioning information.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-wirelessdevice.html"><code>AWS::IoTWireless::WirelessDevice</code></a>.

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
    <td><CopyableCode code="Type, DestinationName, region" /></td>
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
Gets all <code>wireless_devices</code> in a region.
```sql
SELECT
region,
type,
name,
description,
destination_name,
lo_ra_wan,
tags,
arn,
id,
thing_arn,
thing_name,
last_uplink_received_at,
positioning
FROM aws.iotwireless.wireless_devices
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>wireless_device</code>.
```sql
SELECT
region,
type,
name,
description,
destination_name,
lo_ra_wan,
tags,
arn,
id,
thing_arn,
thing_name,
last_uplink_received_at,
positioning
FROM aws.iotwireless.wireless_devices
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iotwireless.wireless_devices
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>wireless_devices</code> resource, the following permissions are required:

### Create
```json
iotwireless:CreateWirelessDevice,
iotwireless:TagResource
```

### Read
```json
iotwireless:GetWirelessDevice,
iotwireless:ListTagsForResource
```

### Update
```json
iotwireless:UpdateWirelessDevice,
iotwireless:GetWirelessDevice,
iotwireless:AssociateWirelessDeviceWithThing,
iotwireless:TagResource,
iotwireless:UntagResource
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

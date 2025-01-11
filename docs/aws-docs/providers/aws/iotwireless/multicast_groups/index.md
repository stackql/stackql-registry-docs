---
title: multicast_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - multicast_groups
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

Creates, updates, deletes or gets a <code>multicast_group</code> resource or lists <code>multicast_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multicast_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage Multicast groups.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.multicast_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of Multicast group</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Multicast group description</td></tr>
<tr><td><CopyableCode code="lo_ra_wan" /></td><td><code>object</code></td><td>Multicast group LoRaWAN</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Multicast group arn. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Multicast group id. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the Multicast group.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Multicast group status. Returned after successful read.</td></tr>
<tr><td><CopyableCode code="associate_wireless_device" /></td><td><code>string</code></td><td>Wireless device to associate. Only for update request.</td></tr>
<tr><td><CopyableCode code="disassociate_wireless_device" /></td><td><code>string</code></td><td>Wireless device to disassociate. Only for update request.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotwireless-multicastgroup.html"><code>AWS::IoTWireless::MulticastGroup</code></a>.

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
    <td><CopyableCode code="LoRaWAN, region" /></td>
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
Gets all <code>multicast_groups</code> in a region.
```sql
SELECT
region,
name,
description,
lo_ra_wan,
arn,
id,
tags,
status,
associate_wireless_device,
disassociate_wireless_device
FROM aws.iotwireless.multicast_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>multicast_group</code>.
```sql
SELECT
region,
name,
description,
lo_ra_wan,
arn,
id,
tags,
status,
associate_wireless_device,
disassociate_wireless_device
FROM aws.iotwireless.multicast_groups
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>multicast_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotwireless.multicast_groups (
 LoRaWAN,
 region
)
SELECT 
'{{ LoRaWAN }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotwireless.multicast_groups (
 Name,
 Description,
 LoRaWAN,
 Tags,
 AssociateWirelessDevice,
 DisassociateWirelessDevice,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ LoRaWAN }}',
 '{{ Tags }}',
 '{{ AssociateWirelessDevice }}',
 '{{ DisassociateWirelessDevice }}',
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
  - name: multicast_group
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
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: AssociateWirelessDevice
        value: '{{ AssociateWirelessDevice }}'
      - name: DisassociateWirelessDevice
        value: '{{ DisassociateWirelessDevice }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iotwireless.multicast_groups
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>multicast_groups</code> resource, the following permissions are required:

### Create
```json
iotwireless:CreateMulticastGroup,
iotwireless:TagResource
```

### Read
```json
iotwireless:GetMulticastGroup,
iotwireless:ListTagsForResource
```

### Update
```json
iotwireless:UpdateMulticastGroup,
iotwireless:GetMulticastGroup,
iotwireless:TagResource,
iotwireless:UntagResource,
iotwireless:AssociateWirelessDeviceWithMulticastGroup,
iotwireless:DisassociateWirelessDeviceFromMulticastGroup
```

### Delete
```json
iotwireless:DeleteMulticastGroup
```

### List
```json
iotwireless:ListMulticastGroups,
iotwireless:ListTagsForResource
```

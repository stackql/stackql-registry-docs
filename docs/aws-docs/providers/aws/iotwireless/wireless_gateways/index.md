---
title: wireless_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - wireless_gateways
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


Used to retrieve a list of <code>wireless_gateways</code> in a region or to create or delete a <code>wireless_gateways</code> resource, use <code>wireless_gateway</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wireless_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage wireless gateways, including LoRa gateways.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.wireless_gateways" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id for Wireless Gateway. Returned upon successful create.</td></tr>
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
FROM aws.iotwireless.wireless_gateways
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
  "GatewayEui": "{{ GatewayEui }}",
  "RfRegion": "{{ RfRegion }}"
 }
}
>>>
--required properties only
INSERT INTO aws.iotwireless.wireless_gateways (
 LoRaWAN,
 region
)
SELECT 
{{ LoRaWAN }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "LoRaWAN": {
  "GatewayEui": "{{ GatewayEui }}",
  "RfRegion": "{{ RfRegion }}"
 },
 "ThingArn": "{{ ThingArn }}",
 "ThingName": "{{ ThingName }}",
 "LastUplinkReceivedAt": "{{ LastUplinkReceivedAt }}"
}
>>>
--all properties
INSERT INTO aws.iotwireless.wireless_gateways (
 Name,
 Description,
 Tags,
 LoRaWAN,
 ThingArn,
 ThingName,
 LastUplinkReceivedAt,
 region
)
SELECT 
 {{ Name }},
 {{ Description }},
 {{ Tags }},
 {{ LoRaWAN }},
 {{ ThingArn }},
 {{ ThingName }},
 {{ LastUplinkReceivedAt }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iotwireless.wireless_gateways
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>wireless_gateways</code> resource, the following permissions are required:

### Create
```json
iotwireless:CreateWirelessGateway,
iotwireless:TagResource,
iotwireless:ListTagsForResource
```

### Delete
```json
iotwireless:DeleteWirelessGateway,
iotwireless:DisassociateWirelessGatewayFromThing
```

### List
```json
iotwireless:ListWirelessGateways,
iotwireless:ListTagsForResource
```


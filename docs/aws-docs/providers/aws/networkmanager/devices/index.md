---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - networkmanager
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


Used to retrieve a list of <code>devices</code> in a region or to create or delete a <code>devices</code> resource, use <code>device</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::Device type describes a device.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.devices" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="global_network_id" /></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><CopyableCode code="device_id" /></td><td><code>string</code></td><td>The ID of the device.</td></tr>
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
global_network_id,
device_id
FROM aws.networkmanager.devices
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
 "GlobalNetworkId": "{{ GlobalNetworkId }}"
}
>>>
--required properties only
INSERT INTO aws.networkmanager.devices (
 GlobalNetworkId,
 region
)
SELECT 
{{ GlobalNetworkId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "GlobalNetworkId": "{{ GlobalNetworkId }}",
 "AWSLocation": {
  "Zone": "{{ Zone }}",
  "SubnetArn": "{{ SubnetArn }}"
 },
 "Location": {
  "Address": "{{ Address }}",
  "Latitude": "{{ Latitude }}",
  "Longitude": "{{ Longitude }}"
 },
 "Model": "{{ Model }}",
 "SerialNumber": "{{ SerialNumber }}",
 "SiteId": "{{ SiteId }}",
 "Type": "{{ Type }}",
 "Vendor": "{{ Vendor }}"
}
>>>
--all properties
INSERT INTO aws.networkmanager.devices (
 Description,
 Tags,
 GlobalNetworkId,
 AWSLocation,
 Location,
 Model,
 SerialNumber,
 SiteId,
 Type,
 Vendor,
 region
)
SELECT 
 {{ Description }},
 {{ Tags }},
 {{ GlobalNetworkId }},
 {{ AWSLocation }},
 {{ Location }},
 {{ Model }},
 {{ SerialNumber }},
 {{ SiteId }},
 {{ Type }},
 {{ Vendor }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.networkmanager.devices
WHERE data__Identifier = '<GlobalNetworkId|DeviceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>devices</code> resource, the following permissions are required:

### Create
```json
networkmanager:CreateDevice,
networkmanager:GetDevices,
networkmanager:TagResource
```

### Delete
```json
networkmanager:GetDevices,
networkmanager:DeleteDevice
```

### List
```json
networkmanager:GetDevices
```


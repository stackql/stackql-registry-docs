---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - sagemaker
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
<tr><td><b>Description</b></td><td>Resource schema for AWS::SageMaker::Device</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.devices" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="device/device_name" /></td><td><code>string</code></td><td></td></tr>
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
device/device_name
FROM aws.sagemaker.devices
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
 "DeviceFleetName": "{{ DeviceFleetName }}"
}
>>>
--required properties only
INSERT INTO aws.sagemaker.devices (
 DeviceFleetName,
 region
)
SELECT 
{{ DeviceFleetName }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DeviceFleetName": "{{ DeviceFleetName }}",
 "Device": {
  "DeviceFleetName": "{{ DeviceFleetName }}",
  "Device": null,
  "Tags": [
   {
    "Value": "{{ Value }}",
    "Key": "{{ Key }}"
   }
  ]
 },
 "Tags": [
  null
 ]
}
>>>
--all properties
INSERT INTO aws.sagemaker.devices (
 DeviceFleetName,
 Device,
 Tags,
 region
)
SELECT 
 {{ DeviceFleetName }},
 {{ Device }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.sagemaker.devices
WHERE data__Identifier = '<Device/DeviceName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>devices</code> resource, the following permissions are required:

### Create
```json
sagemaker:RegisterDevices
```

### Delete
```json
sagemaker:DeregisterDevices
```


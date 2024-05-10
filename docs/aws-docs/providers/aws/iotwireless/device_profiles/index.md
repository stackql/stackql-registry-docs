---
title: device_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - device_profiles
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


Used to retrieve a list of <code>device_profiles</code> in a region or to create or delete a <code>device_profiles</code> resource, use <code>device_profile</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Device Profile's resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.device_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Service profile Id. Returned after successful create.</td></tr>
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
FROM aws.iotwireless.device_profiles
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
{}
>>>
--required properties only
INSERT INTO aws.iotwireless.device_profiles (
 ,
 region
)
SELECT 
{{ . }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "LoRaWAN": {
  "SupportsClassB": "{{ SupportsClassB }}",
  "ClassBTimeout": "{{ ClassBTimeout }}",
  "PingSlotPeriod": "{{ PingSlotPeriod }}",
  "PingSlotDr": "{{ PingSlotDr }}",
  "PingSlotFreq": "{{ PingSlotFreq }}",
  "SupportsClassC": "{{ SupportsClassC }}",
  "ClassCTimeout": "{{ ClassCTimeout }}",
  "MacVersion": "{{ MacVersion }}",
  "RegParamsRevision": "{{ RegParamsRevision }}",
  "RxDelay1": "{{ RxDelay1 }}",
  "RxDrOffset1": "{{ RxDrOffset1 }}",
  "RxFreq2": "{{ RxFreq2 }}",
  "RxDataRate2": "{{ RxDataRate2 }}",
  "FactoryPresetFreqsList": [
   "{{ FactoryPresetFreqsList[0] }}"
  ],
  "MaxEirp": "{{ MaxEirp }}",
  "MaxDutyCycle": "{{ MaxDutyCycle }}",
  "SupportsJoin": "{{ SupportsJoin }}",
  "RfRegion": "{{ RfRegion }}",
  "Supports32BitFCnt": "{{ Supports32BitFCnt }}"
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.iotwireless.device_profiles (
 Name,
 LoRaWAN,
 Tags,
 region
)
SELECT 
 {{ .Name }},
 {{ .LoRaWAN }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iotwireless.device_profiles
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>device_profiles</code> resource, the following permissions are required:

### Create
```json
iotwireless:CreateDeviceProfile,
iotwireless:TagResource,
iotwireless:ListTagsForResource
```

### Delete
```json
iotwireless:DeleteDeviceProfile
```

### List
```json
iotwireless:ListDeviceProfiles,
iotwireless:ListTagsForResource
```


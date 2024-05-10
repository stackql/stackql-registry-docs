---
title: service_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - service_profiles
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


Used to retrieve a list of <code>service_profiles</code> in a region or to create or delete a <code>service_profiles</code> resource, use <code>service_profile</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.service_profiles" /></td></tr>
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
FROM aws.iotwireless.service_profiles
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
INSERT INTO aws.iotwireless.service_profiles (
 ,
 region
)
SELECT 
{{  }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "LoRaWAN": {
  "UlRate": "{{ UlRate }}",
  "UlBucketSize": "{{ UlBucketSize }}",
  "UlRatePolicy": "{{ UlRatePolicy }}",
  "DlRate": "{{ DlRate }}",
  "DlBucketSize": "{{ DlBucketSize }}",
  "DlRatePolicy": "{{ DlRatePolicy }}",
  "AddGwMetadata": "{{ AddGwMetadata }}",
  "DevStatusReqFreq": "{{ DevStatusReqFreq }}",
  "ReportDevStatusBattery": "{{ ReportDevStatusBattery }}",
  "ReportDevStatusMargin": "{{ ReportDevStatusMargin }}",
  "DrMin": "{{ DrMin }}",
  "DrMax": "{{ DrMax }}",
  "ChannelMask": "{{ ChannelMask }}",
  "PrAllowed": "{{ PrAllowed }}",
  "HrAllowed": "{{ HrAllowed }}",
  "RaAllowed": "{{ RaAllowed }}",
  "NwkGeoLoc": "{{ NwkGeoLoc }}",
  "TargetPer": "{{ TargetPer }}",
  "MinGwDiversity": "{{ MinGwDiversity }}"
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
INSERT INTO aws.iotwireless.service_profiles (
 Name,
 LoRaWAN,
 Tags,
 region
)
SELECT 
 {{ Name }},
 {{ LoRaWAN }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iotwireless.service_profiles
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>service_profiles</code> resource, the following permissions are required:

### Create
```json
iotwireless:CreateServiceProfile,
iotwireless:TagResource,
iotwireless:ListTagsForResource
```

### Delete
```json
iotwireless:DeleteServiceProfile
```

### List
```json
iotwireless:ListServiceProfiles,
iotwireless:ListTagsForResource
```


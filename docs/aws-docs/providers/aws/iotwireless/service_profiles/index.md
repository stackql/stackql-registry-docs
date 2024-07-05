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

Creates, updates, deletes or gets a <code>service_profile</code> resource or lists <code>service_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.service_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of service profile</td></tr>
<tr><td><CopyableCode code="lo_ra_wan" /></td><td><code>object</code></td><td>LoRaWAN supports all LoRa specific attributes for service profile for CreateServiceProfile operation</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the service profile.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Service profile Arn. Returned after successful create.</td></tr>
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
    <td><CopyableCode code=", region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>service_profiles</code> in a region.
```sql
SELECT
region,
name,
lo_ra_wan,
tags,
arn,
id
FROM aws.iotwireless.service_profiles
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>service_profile</code>.
```sql
SELECT
region,
name,
lo_ra_wan,
tags,
arn,
id
FROM aws.iotwireless.service_profiles
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotwireless.service_profiles (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotwireless.service_profiles (
 Name,
 LoRaWAN,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ LoRaWAN }}',
 '{{ Tags }}',
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
  - name: service_profile
    props:
      - name: Name
        value: '{{ Name }}'
      - name: LoRaWAN
        value:
          UlRate: '{{ UlRate }}'
          UlBucketSize: '{{ UlBucketSize }}'
          UlRatePolicy: '{{ UlRatePolicy }}'
          DlRate: '{{ DlRate }}'
          DlBucketSize: '{{ DlBucketSize }}'
          DlRatePolicy: '{{ DlRatePolicy }}'
          AddGwMetadata: '{{ AddGwMetadata }}'
          DevStatusReqFreq: '{{ DevStatusReqFreq }}'
          ReportDevStatusBattery: '{{ ReportDevStatusBattery }}'
          ReportDevStatusMargin: '{{ ReportDevStatusMargin }}'
          DrMin: '{{ DrMin }}'
          DrMax: '{{ DrMax }}'
          ChannelMask: '{{ ChannelMask }}'
          PrAllowed: '{{ PrAllowed }}'
          HrAllowed: '{{ HrAllowed }}'
          RaAllowed: '{{ RaAllowed }}'
          NwkGeoLoc: '{{ NwkGeoLoc }}'
          TargetPer: '{{ TargetPer }}'
          MinGwDiversity: '{{ MinGwDiversity }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
iotwireless:GetServiceProfile,
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


---
title: device_fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - device_fleets
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


Used to retrieve a list of <code>device_fleets</code> in a region or to create or delete a <code>device_fleets</code> resource, use <code>device_fleet</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device_fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::SageMaker::DeviceFleet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.device_fleets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="device_fleet_name" /></td><td><code>string</code></td><td>The name of the edge device fleet</td></tr>
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
device_fleet_name
FROM aws.sagemaker.device_fleets
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
 "DeviceFleetName": "{{ DeviceFleetName }}",
 "OutputConfig": {
  "S3OutputLocation": "{{ S3OutputLocation }}",
  "KmsKeyId": "{{ KmsKeyId }}"
 },
 "RoleArn": "{{ RoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.sagemaker.device_fleets (
 DeviceFleetName,
 OutputConfig,
 RoleArn,
 region
)
SELECT 
{{ DeviceFleetName }},
 {{ OutputConfig }},
 {{ RoleArn }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "DeviceFleetName": "{{ DeviceFleetName }}",
 "OutputConfig": {
  "S3OutputLocation": "{{ S3OutputLocation }}",
  "KmsKeyId": "{{ KmsKeyId }}"
 },
 "RoleArn": "{{ RoleArn }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.sagemaker.device_fleets (
 Description,
 DeviceFleetName,
 OutputConfig,
 RoleArn,
 Tags,
 region
)
SELECT 
 {{ Description }},
 {{ DeviceFleetName }},
 {{ OutputConfig }},
 {{ RoleArn }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.sagemaker.device_fleets
WHERE data__Identifier = '<DeviceFleetName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>device_fleets</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateDeviceFleet,
iam:PassRole
```

### Delete
```json
sagemaker:DeleteDeviceFleet
```


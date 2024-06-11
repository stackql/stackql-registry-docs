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

Creates, updates, deletes or gets a <code>device</code> resource or lists <code>devices</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::SageMaker::Device</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.devices" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="device_fleet_name" /></td><td><code>string</code></td><td>The name of the edge device fleet</td></tr>
<tr><td><CopyableCode code="device" /></td><td><code>object</code></td><td>The Edge Device you want to register against a device fleet</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Associate tags with the resource</td></tr>
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
    <td><CopyableCode code="DeviceFleetName, region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from a <code>device</code>.
```sql
SELECT
region,
device_fleet_name,
device,
tags
FROM aws.sagemaker.devices
WHERE region = 'us-east-1' AND data__Identifier = '<Device/DeviceName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>device</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.devices (
 DeviceFleetName,
 region
)
SELECT 
'{{ DeviceFleetName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.devices (
 DeviceFleetName,
 Device,
 Tags,
 region
)
SELECT 
 '{{ DeviceFleetName }}',
 '{{ Device }}',
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
  - name: device
    props:
      - name: DeviceFleetName
        value: '{{ DeviceFleetName }}'
      - name: Device
        value:
          DeviceFleetName: '{{ DeviceFleetName }}'
          Device: null
          Tags:
            - Value: '{{ Value }}'
              Key: '{{ Key }}'
      - name: Tags
        value:
          - null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
sagemaker:DescribeDevice
```

### Update
```json
sagemaker:UpdateDevices
```

### Delete
```json
sagemaker:DeregisterDevices
```


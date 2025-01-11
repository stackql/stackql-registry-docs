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

Creates, updates, deletes or gets a <code>device</code> resource or lists <code>devices</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::Device type describes a device.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.devices" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="device_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the device.</td></tr>
<tr><td><CopyableCode code="device_id" /></td><td><code>string</code></td><td>The ID of the device.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the device.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the device.</td></tr>
<tr><td><CopyableCode code="global_network_id" /></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><CopyableCode code="aws_location" /></td><td><code>object</code></td><td>The Amazon Web Services location of the device, if applicable.</td></tr>
<tr><td><CopyableCode code="location" /></td><td><code>object</code></td><td>The site location.</td></tr>
<tr><td><CopyableCode code="model" /></td><td><code>string</code></td><td>The device model</td></tr>
<tr><td><CopyableCode code="serial_number" /></td><td><code>string</code></td><td>The device serial number.</td></tr>
<tr><td><CopyableCode code="site_id" /></td><td><code>string</code></td><td>The site ID.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The device type.</td></tr>
<tr><td><CopyableCode code="vendor" /></td><td><code>string</code></td><td>The device vendor.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The date and time that the device was created.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the device.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html"><code>AWS::NetworkManager::Device</code></a>.

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
    <td><CopyableCode code="GlobalNetworkId, region" /></td>
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
Gets all <code>devices</code> in a region.
```sql
SELECT
region,
device_arn,
device_id,
description,
tags,
global_network_id,
aws_location,
location,
model,
serial_number,
site_id,
type,
vendor,
created_at,
state
FROM aws.networkmanager.devices
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>device</code>.
```sql
SELECT
region,
device_arn,
device_id,
description,
tags,
global_network_id,
aws_location,
location,
model,
serial_number,
site_id,
type,
vendor,
created_at,
state
FROM aws.networkmanager.devices
WHERE region = 'us-east-1' AND data__Identifier = '<GlobalNetworkId>|<DeviceId>';
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
INSERT INTO aws.networkmanager.devices (
 GlobalNetworkId,
 region
)
SELECT 
'{{ GlobalNetworkId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ Description }}',
 '{{ Tags }}',
 '{{ GlobalNetworkId }}',
 '{{ AWSLocation }}',
 '{{ Location }}',
 '{{ Model }}',
 '{{ SerialNumber }}',
 '{{ SiteId }}',
 '{{ Type }}',
 '{{ Vendor }}',
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
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: GlobalNetworkId
        value: '{{ GlobalNetworkId }}'
      - name: AWSLocation
        value:
          Zone: '{{ Zone }}'
          SubnetArn: '{{ SubnetArn }}'
      - name: Location
        value:
          Address: '{{ Address }}'
          Latitude: '{{ Latitude }}'
          Longitude: '{{ Longitude }}'
      - name: Model
        value: '{{ Model }}'
      - name: SerialNumber
        value: '{{ SerialNumber }}'
      - name: SiteId
        value: '{{ SiteId }}'
      - name: Type
        value: '{{ Type }}'
      - name: Vendor
        value: '{{ Vendor }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
networkmanager:GetDevices
```

### Update
```json
networkmanager:UpdateDevice,
networkmanager:ListTagsForResource,
networkmanager:GetDevices,
networkmanager:TagResource,
networkmanager:UntagResource
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

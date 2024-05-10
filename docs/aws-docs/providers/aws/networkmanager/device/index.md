---
title: device
hide_title: false
hide_table_of_contents: false
keywords:
  - device
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


Gets or updates an individual <code>device</code> resource, use <code>devices</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::Device type describes a device.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.device" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="device_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the device.</td></tr>
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

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
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

## `SELECT` Example
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
FROM aws.networkmanager.device
WHERE region = 'us-east-1' AND data__Identifier = '<GlobalNetworkId>|<DeviceId>';
```


## Permissions

To operate on the <code>device</code> resource, the following permissions are required:

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


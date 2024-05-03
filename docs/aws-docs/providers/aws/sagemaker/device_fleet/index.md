---
title: device_fleet
hide_title: false
hide_table_of_contents: false
keywords:
  - device_fleet
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

Gets or operates on an individual <code>device_fleet</code> resource, use <code>device_fleets</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device_fleet</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::SageMaker::DeviceFleet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.device_fleet" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description for the edge device fleet</td></tr>
<tr><td><CopyableCode code="device_fleet_name" /></td><td><code>string</code></td><td>The name of the edge device fleet</td></tr>
<tr><td><CopyableCode code="output_config" /></td><td><code>object</code></td><td>S3 bucket and an ecryption key id (if available) to store outputs for the fleet</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>Role associated with the device fleet</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
description,
device_fleet_name,
output_config,
role_arn,
tags
FROM aws.sagemaker.device_fleet
WHERE data__Identifier = '<DeviceFleetName>';
```

## Permissions

To operate on the <code>device_fleet</code> resource, the following permissions are required:

### Read
```json
sagemaker:DescribeDeviceFleet
```

### Update
```json
sagemaker:UpdateDeviceFleet,
iam:PassRole
```

### Delete
```json
sagemaker:DeleteDeviceFleet
```


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

Creates, updates, deletes or gets a <code>device_fleet</code> resource or lists <code>device_fleets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device_fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::SageMaker::DeviceFleet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.device_fleets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description for the edge device fleet</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="DeviceFleetName, OutputConfig, RoleArn, region" /></td>
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

Gets all properties from a <code>device_fleet</code>.
```sql
SELECT
region,
description,
device_fleet_name,
output_config,
role_arn,
tags
FROM aws.sagemaker.device_fleets
WHERE region = 'us-east-1' AND data__Identifier = '<DeviceFleetName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>device_fleet</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.device_fleets (
 DeviceFleetName,
 OutputConfig,
 RoleArn,
 region
)
SELECT 
'{{ DeviceFleetName }}',
 '{{ OutputConfig }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.device_fleets (
 Description,
 DeviceFleetName,
 OutputConfig,
 RoleArn,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ DeviceFleetName }}',
 '{{ OutputConfig }}',
 '{{ RoleArn }}',
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
  - name: device_fleet
    props:
      - name: Description
        value: '{{ Description }}'
      - name: DeviceFleetName
        value: '{{ DeviceFleetName }}'
      - name: OutputConfig
        value:
          S3OutputLocation: '{{ S3OutputLocation }}'
          KmsKeyId: '{{ KmsKeyId }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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


---
title: wireless_device_import_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - wireless_device_import_tasks
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


Used to retrieve a list of <code>wireless_device_import_tasks</code> in a region or to create or delete a <code>wireless_device_import_tasks</code> resource, use <code>wireless_device_import_task</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wireless_device_import_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Wireless Device Import Tasks</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.wireless_device_import_tasks" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id for Wireless Device Import Task, Returned upon successful start.</td></tr>
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
FROM aws.iotwireless.wireless_device_import_tasks
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>wireless_device_import_task</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- wireless_device_import_task.iql (required properties only)
INSERT INTO aws.iotwireless.wireless_device_import_tasks (
 DestinationName,
 Sidewalk,
 region
)
SELECT 
'{{ DestinationName }}',
 '{{ Sidewalk }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- wireless_device_import_task.iql (all properties)
INSERT INTO aws.iotwireless.wireless_device_import_tasks (
 DestinationName,
 Sidewalk,
 Tags,
 region
)
SELECT 
 '{{ DestinationName }}',
 '{{ Sidewalk }}',
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
  - name: wireless_device_import_task
    props:
      - name: DestinationName
        value: '{{ DestinationName }}'
      - name: Sidewalk
        value:
          SidewalkManufacturingSn: '{{ SidewalkManufacturingSn }}'
          DeviceCreationFile: '{{ DeviceCreationFile }}'
          DeviceCreationFileList:
            - '{{ DeviceCreationFileList[0] }}'
          Role: '{{ Role }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iotwireless.wireless_device_import_tasks
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>wireless_device_import_tasks</code> resource, the following permissions are required:

### Create
```json
iotwireless:StartWirelessDeviceImportTask,
iotwireless:StartSingleWirelessDeviceImportTask,
iotwireless:TagResource,
iotwireless:ListTagsForResource,
iam:PassRole
```

### Delete
```json
iotwireless:DeleteWirelessDeviceImportTask
```

### List
```json
iotwireless:ListWirelessDeviceImportTasks,
iotwireless:ListTagsForResource
```


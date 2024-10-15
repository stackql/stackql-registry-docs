---
title: firmwares
hide_title: false
hide_table_of_contents: false
keywords:
  - firmwares
  - iot_firmware_defense
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>firmwares</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firmwares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_firmware_defense.firmwares" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_firmwares', value: 'view', },
        { label: 'firmwares', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="firmwareId" /> | `text` | field from the `properties` object |
| <CopyableCode code="model" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_messages" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="vendor" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Firmware properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | Get firmware. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists all of firmwares inside a workspace. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to create a firmware. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to delete a firmware. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to update firmware. |
| <CopyableCode code="generate_download_url" /> | `EXEC` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to a url for file download. |
| <CopyableCode code="generate_filesystem_download_url" /> | `EXEC` | <CopyableCode code="firmwareId, resourceGroupName, subscriptionId, workspaceName" /> | The operation to a url for tar file download. |

## `SELECT` examples

Lists all of firmwares inside a workspace.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_firmwares', value: 'view', },
        { label: 'firmwares', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
file_name,
file_size,
firmwareId,
model,
provisioning_state,
resourceGroupName,
status,
status_messages,
subscriptionId,
system_data,
type,
vendor,
version,
workspaceName
FROM azure.iot_firmware_defense.vw_firmwares
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.iot_firmware_defense.firmwares
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>firmwares</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.iot_firmware_defense.firmwares (
firmwareId,
resourceGroupName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ firmwareId }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: fileName
          value: string
        - name: vendor
          value: string
        - name: model
          value: string
        - name: version
          value: string
        - name: description
          value: string
        - name: fileSize
          value: integer
        - name: status
          value: string
        - name: statusMessages
          value:
            - - name: errorCode
                value: integer
              - name: message
                value: string
        - name: provisioningState
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>firmwares</code> resource.

```sql
/*+ update */
UPDATE azure.iot_firmware_defense.firmwares
SET 
properties = '{{ properties }}'
WHERE 
firmwareId = '{{ firmwareId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>firmwares</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_firmware_defense.firmwares
WHERE firmwareId = '{{ firmwareId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

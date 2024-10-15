---
title: catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs
  - dev_center
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

Creates, updates, deletes, gets or lists a <code>catalogs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.catalogs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_catalogs', value: 'view', },
        { label: 'catalogs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="ado_git" /> | `text` | field from the `properties` object |
| <CopyableCode code="catalogName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="devCenterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="git_hub" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_connection_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_sync_stats" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_sync_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of a catalog. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, devCenterName, resourceGroupName, subscriptionId" /> | Gets a catalog |
| <CopyableCode code="list_by_dev_center" /> | `SELECT` | <CopyableCode code="devCenterName, resourceGroupName, subscriptionId" /> | Lists catalogs for a devcenter. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="catalogName, devCenterName, resourceGroupName, subscriptionId" /> | Creates or updates a catalog. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogName, devCenterName, resourceGroupName, subscriptionId" /> | Deletes a catalog resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="catalogName, devCenterName, resourceGroupName, subscriptionId" /> | Partially updates a catalog. |
| <CopyableCode code="connect" /> | `EXEC` | <CopyableCode code="catalogName, devCenterName, resourceGroupName, subscriptionId" /> | Connects a catalog to enable syncing. |
| <CopyableCode code="sync" /> | `EXEC` | <CopyableCode code="catalogName, devCenterName, resourceGroupName, subscriptionId" /> | Syncs templates for a template source. |

## `SELECT` examples

Lists catalogs for a devcenter.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_catalogs', value: 'view', },
        { label: 'catalogs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
ado_git,
catalogName,
connection_state,
devCenterName,
git_hub,
last_connection_time,
last_sync_stats,
last_sync_time,
provisioning_state,
resourceGroupName,
subscriptionId,
sync_state,
sync_type,
system_data,
tags,
type
FROM azure.dev_center.vw_catalogs
WHERE devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
FROM azure.dev_center.catalogs
WHERE devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>catalogs</code> resource.

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
INSERT INTO azure.dev_center.catalogs (
catalogName,
devCenterName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ catalogName }}',
'{{ devCenterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
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
    - name: properties
      value:
        - name: gitHub
          value:
            - name: uri
              value: string
            - name: branch
              value: string
            - name: secretIdentifier
              value: string
            - name: path
              value: string
        - name: syncType
          value: string
        - name: tags
          value: object
        - name: provisioningState
          value: []
        - name: syncState
          value: string
        - name: lastSyncStats
          value:
            - name: added
              value: integer
            - name: updated
              value: integer
            - name: unchanged
              value: integer
            - name: removed
              value: integer
            - name: validationErrors
              value: integer
            - name: synchronizationErrors
              value: integer
            - name: syncedCatalogItemTypes
              value:
                - []
        - name: connectionState
          value: string
        - name: lastConnectionTime
          value: string
        - name: lastSyncTime
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>catalogs</code> resource.

```sql
/*+ update */
UPDATE azure.dev_center.catalogs
SET 
properties = '{{ properties }}'
WHERE 
catalogName = '{{ catalogName }}'
AND devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>catalogs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_center.catalogs
WHERE catalogName = '{{ catalogName }}'
AND devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

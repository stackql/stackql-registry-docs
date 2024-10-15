---
title: creators
hide_title: false
hide_table_of_contents: false
keywords:
  - creators
  - maps
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

Creates, updates, deletes, gets or lists a <code>creators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>creators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maps.creators" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_creators', value: 'view', },
        { label: 'creators', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="consumed_storage_unit_size_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="creatorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_units" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="total_storage_unit_size_in_bytes" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Creator resource properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, creatorName, resourceGroupName, subscriptionId" /> | Get a Maps Creator resource. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Get all Creator instances for an Azure Maps Account |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, creatorName, resourceGroupName, subscriptionId, data__properties" /> | Create or update a Maps Creator resource. Creator resource will manage Azure resources required to populate a custom set of mapping data. It requires an account to exist before it can be created. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, creatorName, resourceGroupName, subscriptionId" /> | Delete a Maps Creator resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, creatorName, resourceGroupName, subscriptionId" /> | Updates the Maps Creator resource. Only a subset of the parameters may be updated after creation, such as Tags. |

## `SELECT` examples

Get all Creator instances for an Azure Maps Account

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_creators', value: 'view', },
        { label: 'creators', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
consumed_storage_unit_size_in_bytes,
creatorName,
location,
provisioning_state,
resourceGroupName,
storage_units,
subscriptionId,
system_data,
tags,
total_storage_unit_size_in_bytes
FROM azure.maps.vw_creators
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
systemData,
tags
FROM azure.maps.creators
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>creators</code> resource.

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
INSERT INTO azure.maps.creators (
accountName,
creatorName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ accountName }}',
'{{ creatorName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: storageUnits
          value: integer
        - name: totalStorageUnitSizeInBytes
          value: integer
        - name: consumedStorageUnitSizeInBytes
          value: integer
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
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>creators</code> resource.

```sql
/*+ update */
UPDATE azure.maps.creators
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND creatorName = '{{ creatorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>creators</code> resource.

```sql
/*+ delete */
DELETE FROM azure.maps.creators
WHERE accountName = '{{ accountName }}'
AND creatorName = '{{ creatorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

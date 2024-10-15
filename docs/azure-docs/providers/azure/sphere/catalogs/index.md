---
title: catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs
  - sphere
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sphere.catalogs" /></td></tr>
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
| <CopyableCode code="catalogName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Catalog properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | Get a Catalog |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List Catalog resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Catalog resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | Create a Catalog |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | Delete a Catalog |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | Update a Catalog |
| <CopyableCode code="count_devices" /> | `EXEC` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | Counts devices in catalog. |
| <CopyableCode code="upload_image" /> | `EXEC` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | Creates an image. Use this action when the image ID is unknown. |

## `SELECT` examples

List Catalog resources by subscription ID

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
catalogName,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
tenant_id
FROM azure.sphere.vw_catalogs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.sphere.catalogs
WHERE subscriptionId = '{{ subscriptionId }}';
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
INSERT INTO azure.sphere.catalogs (
catalogName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ catalogName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: tenantId
          value: string
        - name: provisioningState
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>catalogs</code> resource.

```sql
/*+ update */
UPDATE azure.sphere.catalogs
SET 
tags = '{{ tags }}'
WHERE 
catalogName = '{{ catalogName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>catalogs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sphere.catalogs
WHERE catalogName = '{{ catalogName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

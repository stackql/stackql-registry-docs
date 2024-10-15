---
title: adc_catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - adc_catalogs
  - data_catalog
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

Creates, updates, deletes, gets or lists a <code>adc_catalogs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>adc_catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_catalog.adc_catalogs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_adc_catalogs', value: 'view', },
        { label: 'adc_catalogs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="admins" /> | `text` | field from the `properties` object |
| <CopyableCode code="catalogName" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_automatic_unit_adjustment" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource etag |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="successfully_provisioned" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="units" /> | `text` | field from the `properties` object |
| <CopyableCode code="users" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="etag" /> | `string` | Resource etag |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Properties of the data catalog. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | The Get Azure Data Catalog Service operation retrieves a json representation of the data catalog. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | The Create Azure Data Catalog service operation creates a new data catalog service with the specified parameters. If the specific service already exists, then any patchable properties will be updated and any immutable properties will remain unchanged. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | The Delete Azure Data Catalog Service operation deletes an existing data catalog. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | The Update Azure Data Catalog Service operation can be used to update the existing deployment. The update call only supports the properties listed in the PATCH body. |

## `SELECT` examples

The Get Azure Data Catalog Service operation retrieves a json representation of the data catalog.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_adc_catalogs', value: 'view', },
        { label: 'adc_catalogs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
admins,
catalogName,
enable_automatic_unit_adjustment,
etag,
location,
resourceGroupName,
sku,
subscriptionId,
successfully_provisioned,
tags,
type,
units,
users
FROM azure.data_catalog.vw_adc_catalogs
WHERE catalogName = '{{ catalogName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
tags,
type
FROM azure.data_catalog.adc_catalogs
WHERE catalogName = '{{ catalogName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>adc_catalogs</code> resource.

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
INSERT INTO azure.data_catalog.adc_catalogs (
catalogName,
resourceGroupName,
subscriptionId,
properties,
location,
tags,
etag
)
SELECT 
'{{ catalogName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: sku
          value: string
        - name: units
          value: integer
        - name: admins
          value:
            - - name: upn
                value: string
              - name: objectId
                value: string
        - name: users
          value:
            - - name: upn
                value: string
              - name: objectId
                value: string
        - name: successfullyProvisioned
          value: boolean
        - name: enableAutomaticUnitAdjustment
          value: boolean
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>adc_catalogs</code> resource.

```sql
/*+ update */
UPDATE azure.data_catalog.adc_catalogs
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}',
etag = '{{ etag }}'
WHERE 
catalogName = '{{ catalogName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>adc_catalogs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_catalog.adc_catalogs
WHERE catalogName = '{{ catalogName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

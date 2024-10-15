---
title: data_types
hide_title: false
hide_table_of_contents: false
keywords:
  - data_types
  - network_analytics
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

Creates, updates, deletes, gets or lists a <code>data_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network_analytics.data_types" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_types', value: 'view', },
        { label: 'data_types', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dataProductName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataTypeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_cache_retention" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_retention" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="state_reason" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_output_retention" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="visualization_url" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The data type properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataProductName, dataTypeName, resourceGroupName, subscriptionId" /> | Retrieve data type resource. |
| <CopyableCode code="list_by_data_product" /> | `SELECT` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId" /> | List data type by parent resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="dataProductName, dataTypeName, resourceGroupName, subscriptionId" /> | Create data type resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataProductName, dataTypeName, resourceGroupName, subscriptionId" /> | Delete data type resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dataProductName, dataTypeName, resourceGroupName, subscriptionId" /> | Update data type resource. |
| <CopyableCode code="generate_storage_container_sas_token" /> | `EXEC` | <CopyableCode code="dataProductName, dataTypeName, resourceGroupName, subscriptionId, data__expiryTimeStamp, data__ipAddress, data__startTimeStamp" /> | Generate sas token for storage container. |

## `SELECT` examples

List data type by parent resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_types', value: 'view', },
        { label: 'data_types', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dataProductName,
dataTypeName,
database_cache_retention,
database_retention,
provisioning_state,
resourceGroupName,
state,
state_reason,
storage_output_retention,
subscriptionId,
visualization_url
FROM azure.network_analytics.vw_data_types
WHERE dataProductName = '{{ dataProductName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.network_analytics.data_types
WHERE dataProductName = '{{ dataProductName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_types</code> resource.

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
INSERT INTO azure.network_analytics.data_types (
dataProductName,
dataTypeName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ dataProductName }}',
'{{ dataTypeName }}',
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
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: state
          value: []
        - name: stateReason
          value: string
        - name: storageOutputRetention
          value: integer
        - name: databaseCacheRetention
          value: integer
        - name: databaseRetention
          value: integer
        - name: visualizationUrl
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>data_types</code> resource.

```sql
/*+ update */
UPDATE azure.network_analytics.data_types
SET 
properties = '{{ properties }}'
WHERE 
dataProductName = '{{ dataProductName }}'
AND dataTypeName = '{{ dataTypeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>data_types</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network_analytics.data_types
WHERE dataProductName = '{{ dataProductName }}'
AND dataTypeName = '{{ dataTypeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

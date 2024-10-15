---
title: inventories
hide_title: false
hide_table_of_contents: false
keywords:
  - inventories
  - hybrid_connectivity
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

Creates, updates, deletes, gets or lists a <code>inventories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inventories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_connectivity.inventories" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_inventories', value: 'view', },
        { label: 'inventories', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azure_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_native_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_native_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="inventoryId" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="solutionConfiguration" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_details" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Definition of inventory. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="inventoryId, resourceUri, solutionConfiguration" /> | Get a InventoryResource |
| <CopyableCode code="list_by_widget" /> | `SELECT` | <CopyableCode code="resourceUri, solutionConfiguration" /> | List InventoryResource resources by SolutionConfiguration |

## `SELECT` examples

List InventoryResource resources by SolutionConfiguration

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_inventories', value: 'view', },
        { label: 'inventories', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
azure_resource_id,
cloud_native_resource_id,
cloud_native_type,
inventoryId,
provisioning_state,
resourceUri,
solutionConfiguration,
status,
status_details
FROM azure.hybrid_connectivity.vw_inventories
WHERE resourceUri = '{{ resourceUri }}'
AND solutionConfiguration = '{{ solutionConfiguration }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.hybrid_connectivity.inventories
WHERE resourceUri = '{{ resourceUri }}'
AND solutionConfiguration = '{{ solutionConfiguration }}';
```
</TabItem></Tabs>


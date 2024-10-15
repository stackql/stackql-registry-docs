---
title: patches
hide_title: false
hide_table_of_contents: false
keywords:
  - patches
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>patches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>patches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.patches" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_patches', value: 'view', },
        { label: 'patches', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="containerAppName" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="patchName" /> | `text` | field from the `properties` object |
| <CopyableCode code="patch_apply_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="patch_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_container_app_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_environment_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_revision_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Top level properties that describes current states of the patch resource |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerAppName, patchName, resourceGroupName, subscriptionId" /> | Get details for specific Container Apps Patch by patch name. |
| <CopyableCode code="list_by_container_app" /> | `SELECT` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> | List Container Apps Patch resources by ContainerApp. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="containerAppName, patchName, resourceGroupName, subscriptionId" /> | Delete specific Container Apps Patch by patch name. |
| <CopyableCode code="apply" /> | `EXEC` | <CopyableCode code="containerAppName, patchName, resourceGroupName, subscriptionId" /> | Apply a Container Apps Patch resource with patch name. |
| <CopyableCode code="skip_configure" /> | `EXEC` | <CopyableCode code="containerAppName, patchName, resourceGroupName, subscriptionId" /> | Configure the Container Apps Patch skip option by patch name. |

## `SELECT` examples

List Container Apps Patch resources by ContainerApp.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_patches', value: 'view', },
        { label: 'patches', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
containerAppName,
created_at,
last_modified_at,
patchName,
patch_apply_status,
patch_details,
resourceGroupName,
subscriptionId,
target_container_app_id,
target_environment_id,
target_revision_id
FROM azure.container_apps.vw_patches
WHERE containerAppName = '{{ containerAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.container_apps.patches
WHERE containerAppName = '{{ containerAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>patches</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.patches
WHERE containerAppName = '{{ containerAppName }}'
AND patchName = '{{ patchName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

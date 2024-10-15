---
title: galleries
hide_title: false
hide_table_of_contents: false
keywords:
  - galleries
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

Creates, updates, deletes, gets or lists a <code>galleries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>galleries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.galleries" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_galleries', value: 'view', },
        { label: 'galleries', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="devCenterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="gallery_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of a gallery. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="devCenterName, galleryName, resourceGroupName, subscriptionId" /> | Gets a gallery |
| <CopyableCode code="list_by_dev_center" /> | `SELECT` | <CopyableCode code="devCenterName, resourceGroupName, subscriptionId" /> | Lists galleries for a devcenter. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="devCenterName, galleryName, resourceGroupName, subscriptionId" /> | Creates or updates a gallery. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="devCenterName, galleryName, resourceGroupName, subscriptionId" /> | Deletes a gallery resource. |

## `SELECT` examples

Lists galleries for a devcenter.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_galleries', value: 'view', },
        { label: 'galleries', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
devCenterName,
galleryName,
gallery_resource_id,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
type
FROM azure.dev_center.vw_galleries
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
FROM azure.dev_center.galleries
WHERE devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>galleries</code> resource.

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
INSERT INTO azure.dev_center.galleries (
devCenterName,
galleryName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ devCenterName }}',
'{{ galleryName }}',
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
        - name: provisioningState
          value: []
        - name: galleryResourceId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>galleries</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_center.galleries
WHERE devCenterName = '{{ devCenterName }}'
AND galleryName = '{{ galleryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

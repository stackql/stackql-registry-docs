---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - aks
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

Creates, updates, deletes, gets or lists a <code>snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aks.snapshots" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_snapshots', value: 'view', },
        { label: 'snapshots', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creation_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_fips" /> | `text` | field from the `properties` object |
| <CopyableCode code="kubernetes_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="node_image_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="snapshot_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="vm_size" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties used to configure a node pool snapshot. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_snapshots', value: 'view', },
        { label: 'snapshots', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
creation_data,
enable_fips,
kubernetes_version,
location,
node_image_version,
os_sku,
os_type,
resourceGroupName,
resourceName,
snapshot_type,
subscriptionId,
tags,
vm_size
FROM azure.aks.vw_snapshots
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.aks.snapshots
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>snapshots</code> resource.

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
INSERT INTO azure.aks.snapshots (
resourceGroupName,
resourceName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
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
        - name: creationData
          value:
            - name: sourceResourceId
              value: string
        - name: snapshotType
          value: []
        - name: kubernetesVersion
          value: string
        - name: nodeImageVersion
          value: string
        - name: osType
          value: []
        - name: osSku
          value: []
        - name: vmSize
          value: string
        - name: enableFIPS
          value: boolean
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>snapshots</code> resource.

```sql
/*+ delete */
DELETE FROM azure.aks.snapshots
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

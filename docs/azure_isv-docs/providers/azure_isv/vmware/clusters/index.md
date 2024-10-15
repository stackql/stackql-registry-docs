---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - vmware
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware.clusters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_clusters', value: 'view', },
        { label: 'clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="hosts" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateCloudName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The properties of a cluster |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, privateCloudName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, privateCloudName, resourceGroupName, subscriptionId, data__properties, data__sku" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, privateCloudName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, privateCloudName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_clusters', value: 'view', },
        { label: 'clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
clusterName,
cluster_id,
hosts,
privateCloudName,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
type
FROM azure_isv.vmware.vw_clusters
WHERE privateCloudName = '{{ privateCloudName }}'
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
sku,
type
FROM azure_isv.vmware.clusters
WHERE privateCloudName = '{{ privateCloudName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clusters</code> resource.

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
INSERT INTO azure_isv.vmware.clusters (
clusterName,
privateCloudName,
resourceGroupName,
subscriptionId,
data__properties,
data__sku,
sku,
properties
)
SELECT 
'{{ clusterName }}',
'{{ privateCloudName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ data__sku }}',
'{{ sku }}',
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
    - name: sku
      value:
        - name: name
          value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: clusterId
          value: integer
        - name: hosts
          value:
            - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>clusters</code> resource.

```sql
/*+ update */
UPDATE azure_isv.vmware.clusters
SET 
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND privateCloudName = '{{ privateCloudName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.vmware.clusters
WHERE clusterName = '{{ clusterName }}'
AND privateCloudName = '{{ privateCloudName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

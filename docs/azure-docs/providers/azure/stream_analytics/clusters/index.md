---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - stream_analytics
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.stream_analytics.clusters" /></td></tr>
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
| <CopyableCode code="capacity_allocated" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacity_assigned" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The current entity tag for the cluster. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The SKU of the cluster. This determines the size/capacity of the cluster. Required on PUT (CreateOrUpdate) requests. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The current entity tag for the cluster. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties associated with a Stream Analytics cluster. |
| <CopyableCode code="sku" /> | `object` | The SKU of the cluster. This determines the size/capacity of the cluster. Required on PUT (CreateOrUpdate) requests. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets information about the specified cluster. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the clusters in the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the clusters in the given subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Creates a Stream Analytics Cluster or replaces an already existing cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Deletes the specified cluster. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Updates an existing cluster. This can be used to partially update (ie. update one or two properties) a cluster without affecting the rest of the cluster definition. |

## `SELECT` examples

Lists all of the clusters in the given subscription.

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
capacity_allocated,
capacity_assigned,
clusterName,
cluster_id,
created_date,
etag,
location,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
tags
FROM azure.stream_analytics.vw_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
sku,
tags
FROM azure.stream_analytics.clusters
WHERE subscriptionId = '{{ subscriptionId }}';
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
INSERT INTO azure.stream_analytics.clusters (
clusterName,
resourceGroupName,
subscriptionId,
tags,
location,
sku,
properties
)
SELECT 
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ sku }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: capacity
          value: integer
    - name: etag
      value: string
    - name: properties
      value:
        - name: createdDate
          value: string
        - name: clusterId
          value: string
        - name: provisioningState
          value: []
        - name: capacityAllocated
          value: integer
        - name: capacityAssigned
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>clusters</code> resource.

```sql
/*+ update */
UPDATE azure.stream_analytics.clusters
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure.stream_analytics.clusters
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

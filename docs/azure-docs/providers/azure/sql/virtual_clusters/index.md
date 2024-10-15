---
title: virtual_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_clusters
  - sql
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

Creates, updates, deletes, gets or lists a <code>virtual_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.virtual_clusters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_clusters', value: 'view', },
        { label: 'virtual_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="child_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualClusterName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The properties of a virtual cluster. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualClusterName" /> | Gets a virtual cluster. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of all virtualClusters in the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of virtual clusters in a resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualClusterName" /> | Deletes a virtual cluster. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualClusterName" /> | Updates an existing virtual cluster. |

## `SELECT` examples

Gets a list of all virtualClusters in the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_clusters', value: 'view', },
        { label: 'virtual_clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
child_resources,
location,
resourceGroupName,
subnet_id,
subscriptionId,
tags,
version,
virtualClusterName
FROM azure.sql.vw_virtual_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.sql.virtual_clusters
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>virtual_clusters</code> resource.

```sql
/*+ update */
UPDATE azure.sql.virtual_clusters
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualClusterName = '{{ virtualClusterName }}';
```

## `DELETE` example

Deletes the specified <code>virtual_clusters</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.virtual_clusters
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualClusterName = '{{ virtualClusterName }}';
```

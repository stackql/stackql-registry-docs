---
title: environments_worker_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_worker_pools
  - app_service
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

Creates, updates, deletes, gets or lists a <code>environments_worker_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments_worker_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.environments_worker_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_environments_worker_pools', value: 'view', },
        { label: 'environments_worker_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id. |
| <CopyableCode code="name" /> | `text` | Resource Name. |
| <CopyableCode code="compute_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of resource. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Description of a SKU for a scalable resource. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="workerPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="worker_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="worker_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="worker_size_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | Worker pool of an App Service Environment. |
| <CopyableCode code="sku" /> | `object` | Description of a SKU for a scalable resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId, workerPoolName" /> | Description for Get properties of a worker pool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Get all worker pools of an App Service Environment. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId, workerPoolName" /> | Description for Create or update a worker pool. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, subscriptionId, workerPoolName" /> | Description for Create or update a worker pool. |

## `SELECT` examples

Description for Get all worker pools of an App Service Environment.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_environments_worker_pools', value: 'view', },
        { label: 'environments_worker_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
compute_mode,
instance_names,
kind,
resourceGroupName,
sku,
subscriptionId,
type,
workerPoolName,
worker_count,
worker_size,
worker_size_id
FROM azure.app_service.vw_environments_worker_pools
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
kind,
properties,
sku,
type
FROM azure.app_service.environments_worker_pools
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environments_worker_pools</code> resource.

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
INSERT INTO azure.app_service.environments_worker_pools (
name,
resourceGroupName,
subscriptionId,
workerPoolName,
kind,
properties,
sku
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workerPoolName }}',
'{{ kind }}',
'{{ properties }}',
'{{ sku }}'
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
    - name: kind
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: workerSizeId
          value: integer
        - name: computeMode
          value: string
        - name: workerSize
          value: string
        - name: workerCount
          value: integer
        - name: instanceNames
          value:
            - string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
        - name: skuCapacity
          value:
            - name: minimum
              value: integer
            - name: maximum
              value: integer
            - name: elasticMaximum
              value: integer
            - name: default
              value: integer
            - name: scaleType
              value: string
        - name: locations
          value:
            - string
        - name: capabilities
          value:
            - - name: name
                value: string
              - name: value
                value: string
              - name: reason
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>environments_worker_pools</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.environments_worker_pools
SET 
kind = '{{ kind }}',
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workerPoolName = '{{ workerPoolName }}';
```

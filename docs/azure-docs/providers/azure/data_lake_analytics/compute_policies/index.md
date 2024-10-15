---
title: compute_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - compute_policies
  - data_lake_analytics
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

Creates, updates, deletes, gets or lists a <code>compute_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>compute_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_lake_analytics.compute_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_compute_policies', value: 'view', },
        { label: 'compute_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="computePolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_degree_of_parallelism_per_job" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_priority_per_job" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="properties" /> | `object` | The compute policy properties. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, computePolicyName, resourceGroupName, subscriptionId" /> | Gets the specified Data Lake Analytics compute policy. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the Data Lake Analytics compute policies within the specified Data Lake Analytics account. An account supports, at most, 50 policies |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, computePolicyName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the specified compute policy. During update, the compute policy with the specified name will be replaced with this new compute policy. An account supports, at most, 50 policies |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, computePolicyName, resourceGroupName, subscriptionId" /> | Deletes the specified compute policy from the specified Data Lake Analytics account |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, computePolicyName, resourceGroupName, subscriptionId" /> | Updates the specified compute policy. |

## `SELECT` examples

Lists the Data Lake Analytics compute policies within the specified Data Lake Analytics account. An account supports, at most, 50 policies

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_compute_policies', value: 'view', },
        { label: 'compute_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
computePolicyName,
max_degree_of_parallelism_per_job,
min_priority_per_job,
object_id,
object_type,
resourceGroupName,
subscriptionId,
type
FROM azure.data_lake_analytics.vw_compute_policies
WHERE accountName = '{{ accountName }}'
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
type
FROM azure.data_lake_analytics.compute_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>compute_policies</code> resource.

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
INSERT INTO azure.data_lake_analytics.compute_policies (
accountName,
computePolicyName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ accountName }}',
'{{ computePolicyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: objectId
          value: string
        - name: objectType
          value: string
        - name: maxDegreeOfParallelismPerJob
          value: integer
        - name: minPriorityPerJob
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>compute_policies</code> resource.

```sql
/*+ update */
UPDATE azure.data_lake_analytics.compute_policies
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND computePolicyName = '{{ computePolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>compute_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_lake_analytics.compute_policies
WHERE accountName = '{{ accountName }}'
AND computePolicyName = '{{ computePolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

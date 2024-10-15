---
title: caches
hide_title: false
hide_table_of_contents: false
keywords:
  - caches
  - api_management
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

Creates, updates, deletes, gets or lists a <code>caches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>caches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.caches" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_caches', value: 'view', },
        { label: 'caches', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="cacheId" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_string" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_from_location" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of the Cache contract. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cacheId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the Cache specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of all external Caches in the specified service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cacheId, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates an External Cache to be used in Api Management instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, cacheId, resourceGroupName, serviceName, subscriptionId" /> | Deletes specific Cache. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, cacheId, resourceGroupName, serviceName, subscriptionId" /> | Updates the details of the cache specified by its identifier. |

## `SELECT` examples

Lists a collection of all external Caches in the specified service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_caches', value: 'view', },
        { label: 'caches', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
cacheId,
connection_string,
resourceGroupName,
resource_id,
serviceName,
subscriptionId,
use_from_location
FROM azure.api_management.vw_caches
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.caches
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>caches</code> resource.

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
INSERT INTO azure.api_management.caches (
cacheId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ cacheId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
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
        - name: description
          value: string
        - name: connectionString
          value: string
        - name: useFromLocation
          value: string
        - name: resourceId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>caches</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.caches
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND cacheId = '{{ cacheId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>caches</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.caches
WHERE If-Match = '{{ If-Match }}'
AND cacheId = '{{ cacheId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

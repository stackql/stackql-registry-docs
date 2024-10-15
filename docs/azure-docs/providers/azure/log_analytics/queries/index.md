---
title: queries
hide_title: false
hide_table_of_contents: false
keywords:
  - queries
  - log_analytics
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

Creates, updates, deletes, gets or lists a <code>queries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.queries" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_queries', value: 'view', },
        { label: 'queries', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="author" /> | `text` | field from the `properties` object |
| <CopyableCode code="body" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="properties" /> | `text` | Properties that define an Log Analytics QueryPack-Query resource. |
| <CopyableCode code="queryPackName" /> | `text` | field from the `properties` object |
| <CopyableCode code="related" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_modified" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Azure resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="properties" /> | `object` | Properties that define an Log Analytics QueryPack-Query resource. |
| <CopyableCode code="systemData" /> | `object` | Read only system data |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, queryPackName, resourceGroupName, subscriptionId" /> | Gets a specific Log Analytics Query defined within a Log Analytics QueryPack. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="queryPackName, resourceGroupName, subscriptionId" /> | Gets a list of Queries defined within a Log Analytics QueryPack. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="id, queryPackName, resourceGroupName, subscriptionId" /> | Deletes a specific Query defined within an Log Analytics QueryPack. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="id, queryPackName, resourceGroupName, subscriptionId" /> | Adds or Updates a specific Query within a Log Analytics QueryPack. |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="id, queryPackName, resourceGroupName, subscriptionId" /> | Adds or Updates a specific Query within a Log Analytics QueryPack. |
| <CopyableCode code="search" /> | `EXEC` | <CopyableCode code="queryPackName, resourceGroupName, subscriptionId" /> | Search a list of Queries defined within a Log Analytics QueryPack according to given search properties. |

## `SELECT` examples

Gets a list of Queries defined within a Log Analytics QueryPack.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_queries', value: 'view', },
        { label: 'queries', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
author,
body,
display_name,
properties,
queryPackName,
related,
resourceGroupName,
subscriptionId,
system_data,
tags,
time_created,
time_modified,
type
FROM azure.log_analytics.vw_queries
WHERE queryPackName = '{{ queryPackName }}'
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
FROM azure.log_analytics.queries
WHERE queryPackName = '{{ queryPackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>queries</code> resource.

```sql
/*+ update */
UPDATE azure.log_analytics.queries
SET 
properties = '{{ properties }}'
WHERE 
id = '{{ id }}'
AND queryPackName = '{{ queryPackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>queries</code> resource.

```sql
/*+ update */
REPLACE azure.log_analytics.queries
SET 
properties = '{{ properties }}'
WHERE 
id = '{{ id }}'
AND queryPackName = '{{ queryPackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>queries</code> resource.

```sql
/*+ delete */
DELETE FROM azure.log_analytics.queries
WHERE id = '{{ id }}'
AND queryPackName = '{{ queryPackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

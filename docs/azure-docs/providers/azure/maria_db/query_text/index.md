---
title: query_text
hide_title: false
hide_table_of_contents: false
keywords:
  - query_text
  - maria_db
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

Creates, updates, deletes, gets or lists a <code>query_text</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>query_text</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maria_db.query_text" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_query_text', value: 'view', },
        { label: 'query_text', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="queryId" /> | `text` | field from the `properties` object |
| <CopyableCode code="queryIds" /> | `text` | field from the `properties` object |
| <CopyableCode code="query_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="query_text" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a query text. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="queryId, resourceGroupName, serverName, subscriptionId" /> | Retrieve the Query-Store query texts for the queryId. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="queryIds, resourceGroupName, serverName, subscriptionId" /> | Retrieve the Query-Store query texts for specified queryIds. |

## `SELECT` examples

Retrieve the Query-Store query texts for the queryId.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_query_text', value: 'view', },
        { label: 'query_text', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
queryId,
queryIds,
query_id,
query_text,
resourceGroupName,
serverName,
subscriptionId
FROM azure.maria_db.vw_query_text
WHERE queryId = '{{ queryId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.maria_db.query_text
WHERE queryId = '{{ queryId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


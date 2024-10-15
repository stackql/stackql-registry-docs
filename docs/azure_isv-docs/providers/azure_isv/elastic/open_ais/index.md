---
title: open_ais
hide_title: false
hide_table_of_contents: false
keywords:
  - open_ais
  - elastic
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

Creates, updates, deletes, gets or lists a <code>open_ais</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>open_ais</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.elastic.open_ais" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_open_ais', value: 'view', },
        { label: 'open_ais', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The id of the integration. |
| <CopyableCode code="name" /> | `text` | Name of the integration. |
| <CopyableCode code="integrationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="key" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_refresh_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="open_ai_connector_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="open_ai_resource_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="open_ai_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the integration. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The id of the integration. |
| <CopyableCode code="name" /> | `string` | Name of the integration. |
| <CopyableCode code="properties" /> | `object` | Open AI Integration details. |
| <CopyableCode code="type" /> | `string` | The type of the integration. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="integrationName, monitorName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="integrationName, monitorName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="integrationName, monitorName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_open_ais', value: 'view', },
        { label: 'open_ais', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
integrationName,
key,
last_refresh_at,
monitorName,
open_ai_connector_id,
open_ai_resource_endpoint,
open_ai_resource_id,
resourceGroupName,
subscriptionId,
type
FROM azure_isv.elastic.vw_open_ais
WHERE monitorName = '{{ monitorName }}'
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
FROM azure_isv.elastic.open_ais
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>open_ais</code> resource.

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
INSERT INTO azure_isv.elastic.open_ais (
integrationName,
monitorName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ integrationName }}',
'{{ monitorName }}',
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
    - name: name
      value: string
    - name: id
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: openAIResourceId
          value: string
        - name: openAIResourceEndpoint
          value: string
        - name: openAIConnectorId
          value: string
        - name: key
          value: string
        - name: lastRefreshAt
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>open_ais</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.elastic.open_ais
WHERE integrationName = '{{ integrationName }}'
AND monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

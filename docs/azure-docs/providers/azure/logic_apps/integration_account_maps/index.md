---
title: integration_account_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_maps
  - logic_apps
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

Creates, updates, deletes, gets or lists a <code>integration_account_maps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_account_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_account_maps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_account_maps', value: 'view', },
        { label: 'integration_account_maps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the resource name. |
| <CopyableCode code="changed_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="content" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="integrationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="mapName" /> | `text` | field from the `properties` object |
| <CopyableCode code="map_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters_schema" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | Gets the resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The integration account map. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="integrationAccountName, mapName, resourceGroupName, subscriptionId" /> | Gets an integration account map. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="integrationAccountName, resourceGroupName, subscriptionId" /> | Gets a list of integration account maps. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="integrationAccountName, mapName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an integration account map. If the map is larger than 4 MB, you need to store the map in an Azure blob and use the blob's Shared Access Signature (SAS) URL as the 'contentLink' property value. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="integrationAccountName, mapName, resourceGroupName, subscriptionId" /> | Deletes an integration account map. |

## `SELECT` examples

Gets a list of integration account maps.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_account_maps', value: 'view', },
        { label: 'integration_account_maps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
changed_time,
content,
content_link,
content_type,
created_time,
integrationAccountName,
location,
mapName,
map_type,
metadata,
parameters_schema,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure.logic_apps.vw_integration_account_maps
WHERE integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.logic_apps.integration_account_maps
WHERE integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>integration_account_maps</code> resource.

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
INSERT INTO azure.logic_apps.integration_account_maps (
integrationAccountName,
mapName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
location,
tags
)
SELECT 
'{{ integrationAccountName }}',
'{{ mapName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: mapType
          value: []
        - name: parametersSchema
          value:
            - name: ref
              value: string
        - name: createdTime
          value: string
        - name: changedTime
          value: string
        - name: content
          value: string
        - name: contentType
          value: string
        - name: contentLink
          value:
            - name: uri
              value: string
            - name: contentVersion
              value: string
            - name: contentSize
              value: integer
            - name: contentHash
              value:
                - name: algorithm
                  value: string
                - name: value
                  value: string
            - name: metadata
              value: []
        - name: metadata
          value: []
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>integration_account_maps</code> resource.

```sql
/*+ delete */
DELETE FROM azure.logic_apps.integration_account_maps
WHERE integrationAccountName = '{{ integrationAccountName }}'
AND mapName = '{{ mapName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

---
title: api_tag_descriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - api_tag_descriptions
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

Creates, updates, deletes, gets or lists a <code>api_tag_descriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_tag_descriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.api_tag_descriptions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_tag_descriptions', value: 'view', },
        { label: 'api_tag_descriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="apiId" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="external_docs_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="external_docs_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tagDescriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tag_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | TagDescription contract Properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, tagDescriptionId" /> | Get Tag description in scope of API |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Lists all Tags descriptions in scope of API. Model similar to swagger - tagDescription is defined on API level but tag may be assigned to the Operations |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, tagDescriptionId" /> | Create/Update tag description in scope of the Api. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, resourceGroupName, serviceName, subscriptionId, tagDescriptionId" /> | Delete tag description for the Api. |

## `SELECT` examples

Lists all Tags descriptions in scope of API. Model similar to swagger - tagDescription is defined on API level but tag may be assigned to the Operations

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_tag_descriptions', value: 'view', },
        { label: 'api_tag_descriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
apiId,
display_name,
external_docs_description,
external_docs_url,
resourceGroupName,
serviceName,
subscriptionId,
tagDescriptionId,
tag_id
FROM azure.api_management.vw_api_tag_descriptions
WHERE apiId = '{{ apiId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.api_tag_descriptions
WHERE apiId = '{{ apiId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_tag_descriptions</code> resource.

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
INSERT INTO azure.api_management.api_tag_descriptions (
apiId,
resourceGroupName,
serviceName,
subscriptionId,
tagDescriptionId,
properties
)
SELECT 
'{{ apiId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ tagDescriptionId }}',
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
        - name: externalDocsUrl
          value: string
        - name: externalDocsDescription
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>api_tag_descriptions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.api_tag_descriptions
WHERE If-Match = '{{ If-Match }}'
AND apiId = '{{ apiId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tagDescriptionId = '{{ tagDescriptionId }}';
```

---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
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

Creates, updates, deletes, gets or lists a <code>tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.tags" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tags', value: 'view', },
        { label: 'tags', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiId" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tagId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Tag contract Properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, tagId" /> | Gets the details of the tag specified by its identifier. |
| <CopyableCode code="get_by_api" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Get tag associated with the API. |
| <CopyableCode code="get_by_operation" /> | `SELECT` | <CopyableCode code="apiId, operationId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Get tag associated with the Operation. |
| <CopyableCode code="get_by_product" /> | `SELECT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Get tag associated with the Product. |
| <CopyableCode code="list_by_api" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Lists all Tags associated with the API. |
| <CopyableCode code="list_by_operation" /> | `SELECT` | <CopyableCode code="apiId, operationId, resourceGroupName, serviceName, subscriptionId" /> | Lists all Tags associated with the Operation. |
| <CopyableCode code="list_by_product" /> | `SELECT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId" /> | Lists all Tags associated with the Product. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of tags defined within a service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, tagId" /> | Creates a tag. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, resourceGroupName, serviceName, subscriptionId, tagId" /> | Deletes specific tag of the API Management service instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, resourceGroupName, serviceName, subscriptionId, tagId" /> | Updates the details of the tag specified by its identifier. |
| <CopyableCode code="assign_to_api" /> | `EXEC` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Assign tag to the Api. |
| <CopyableCode code="assign_to_operation" /> | `EXEC` | <CopyableCode code="apiId, operationId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Assign tag to the Operation. |
| <CopyableCode code="assign_to_product" /> | `EXEC` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Assign tag to the Product. |
| <CopyableCode code="detach_from_api" /> | `EXEC` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Detach the tag from the Api. |
| <CopyableCode code="detach_from_operation" /> | `EXEC` | <CopyableCode code="apiId, operationId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Detach the tag from the Operation. |
| <CopyableCode code="detach_from_product" /> | `EXEC` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Detach the tag from the Product. |

## `SELECT` examples

Lists a collection of tags defined within a service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tags', value: 'view', },
        { label: 'tags', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
apiId,
display_name,
operationId,
resourceGroupName,
serviceName,
subscriptionId,
tagId
FROM azure.api_management.vw_tags
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.tags
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tags</code> resource.

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
INSERT INTO azure.api_management.tags (
resourceGroupName,
serviceName,
subscriptionId,
tagId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ tagId }}',
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
        - name: displayName
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tags</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.tags
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tagId = '{{ tagId }}';
```

## `DELETE` example

Deletes the specified <code>tags</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.tags
WHERE If-Match = '{{ If-Match }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tagId = '{{ tagId }}';
```

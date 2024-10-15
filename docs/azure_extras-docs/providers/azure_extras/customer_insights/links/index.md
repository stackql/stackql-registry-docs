---
title: links
hide_title: false
hide_table_of_contents: false
keywords:
  - links
  - customer_insights
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

Creates, updates, deletes, gets or lists a <code>links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.links" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_links', value: 'view', },
        { label: 'links', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="hubName" /> | `text` | field from the `properties` object |
| <CopyableCode code="linkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="link_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="mappings" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="participant_property_references" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="reference_only" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_entity_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_entity_type_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_entity_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_entity_type_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The definition of Link. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, linkName, resourceGroupName, subscriptionId" /> | Gets a link in the hub. |
| <CopyableCode code="list_by_hub" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all the links in the specified hub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hubName, linkName, resourceGroupName, subscriptionId" /> | Creates a link or updates an existing link in the hub. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hubName, linkName, resourceGroupName, subscriptionId" /> | Deletes a link in the hub. |

## `SELECT` examples

Gets all the links in the specified hub.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_links', value: 'view', },
        { label: 'links', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
display_name,
hubName,
linkName,
link_name,
mappings,
operation_type,
participant_property_references,
provisioning_state,
reference_only,
resourceGroupName,
source_entity_type,
source_entity_type_name,
subscriptionId,
target_entity_type,
target_entity_type_name,
tenant_id,
type
FROM azure_extras.customer_insights.vw_links
WHERE hubName = '{{ hubName }}'
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
FROM azure_extras.customer_insights.links
WHERE hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>links</code> resource.

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
INSERT INTO azure_extras.customer_insights.links (
hubName,
linkName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ hubName }}',
'{{ linkName }}',
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
    - name: properties
      value:
        - name: tenantId
          value: string
        - name: linkName
          value: string
        - name: sourceEntityType
          value: string
        - name: targetEntityType
          value: string
        - name: sourceEntityTypeName
          value: string
        - name: targetEntityTypeName
          value: string
        - name: displayName
          value: object
        - name: description
          value: object
        - name: mappings
          value:
            - - name: sourcePropertyName
                value: string
              - name: targetPropertyName
                value: string
              - name: linkType
                value: string
        - name: participantPropertyReferences
          value:
            - - name: sourcePropertyName
                value: string
              - name: targetPropertyName
                value: string
        - name: provisioningState
          value: []
        - name: referenceOnly
          value: boolean
        - name: operationType
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>links</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.customer_insights.links
WHERE hubName = '{{ hubName }}'
AND linkName = '{{ linkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

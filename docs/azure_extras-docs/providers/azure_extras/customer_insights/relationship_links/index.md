---
title: relationship_links
hide_title: false
hide_table_of_contents: false
keywords:
  - relationship_links
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

Creates, updates, deletes, gets or lists a <code>relationship_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>relationship_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.relationship_links" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_relationship_links', value: 'view', },
        { label: 'relationship_links', value: 'resource', },
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
| <CopyableCode code="interaction_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="link_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="mappings" /> | `text` | field from the `properties` object |
| <CopyableCode code="profile_property_references" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="related_profile_property_references" /> | `text` | field from the `properties` object |
| <CopyableCode code="relationshipLinkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="relationship_guid_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="relationship_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The definition of relationship link. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, relationshipLinkName, resourceGroupName, subscriptionId" /> | Gets information about the specified relationship Link. |
| <CopyableCode code="list_by_hub" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all relationship links in the hub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hubName, relationshipLinkName, resourceGroupName, subscriptionId" /> | Creates a relationship link or updates an existing relationship link within a hub. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hubName, relationshipLinkName, resourceGroupName, subscriptionId" /> | Deletes a relationship link within a hub. |

## `SELECT` examples

Gets all relationship links in the hub.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_relationship_links', value: 'view', },
        { label: 'relationship_links', value: 'resource', },
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
interaction_type,
link_name,
mappings,
profile_property_references,
provisioning_state,
related_profile_property_references,
relationshipLinkName,
relationship_guid_id,
relationship_name,
resourceGroupName,
subscriptionId,
tenant_id,
type
FROM azure_extras.customer_insights.vw_relationship_links
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
FROM azure_extras.customer_insights.relationship_links
WHERE hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>relationship_links</code> resource.

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
INSERT INTO azure_extras.customer_insights.relationship_links (
hubName,
relationshipLinkName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ hubName }}',
'{{ relationshipLinkName }}',
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
        - name: displayName
          value: object
        - name: description
          value: object
        - name: interactionType
          value: string
        - name: linkName
          value: string
        - name: mappings
          value:
            - - name: interactionFieldName
                value: string
              - name: linkType
                value: string
              - name: relationshipFieldName
                value: string
        - name: profilePropertyReferences
          value:
            - - name: interactionPropertyName
                value: string
              - name: profilePropertyName
                value: string
        - name: provisioningState
          value: []
        - name: relatedProfilePropertyReferences
          value:
            - - name: interactionPropertyName
                value: string
              - name: profilePropertyName
                value: string
        - name: relationshipName
          value: string
        - name: relationshipGuidId
          value: string
        - name: tenantId
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

Deletes the specified <code>relationship_links</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.customer_insights.relationship_links
WHERE hubName = '{{ hubName }}'
AND relationshipLinkName = '{{ relationshipLinkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

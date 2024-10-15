---
title: relationships
hide_title: false
hide_table_of_contents: false
keywords:
  - relationships
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

Creates, updates, deletes, gets or lists a <code>relationships</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>relationships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.relationships" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_relationships', value: 'view', },
        { label: 'relationships', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="cardinality" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiry_date_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="fields" /> | `text` | field from the `properties` object |
| <CopyableCode code="hubName" /> | `text` | field from the `properties` object |
| <CopyableCode code="lookup_mappings" /> | `text` | field from the `properties` object |
| <CopyableCode code="profile_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="related_profile_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="relationshipName" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | The definition of Relationship. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, relationshipName, resourceGroupName, subscriptionId" /> | Gets information about the specified relationship. |
| <CopyableCode code="list_by_hub" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all relationships in the hub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hubName, relationshipName, resourceGroupName, subscriptionId" /> | Creates a relationship or updates an existing relationship within a hub. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hubName, relationshipName, resourceGroupName, subscriptionId" /> | Deletes a relationship within a hub. |

## `SELECT` examples

Gets all relationships in the hub.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_relationships', value: 'view', },
        { label: 'relationships', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
cardinality,
display_name,
expiry_date_time_utc,
fields,
hubName,
lookup_mappings,
profile_type,
provisioning_state,
related_profile_type,
relationshipName,
relationship_guid_id,
relationship_name,
resourceGroupName,
subscriptionId,
tenant_id,
type
FROM azure_extras.customer_insights.vw_relationships
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
FROM azure_extras.customer_insights.relationships
WHERE hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>relationships</code> resource.

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
INSERT INTO azure_extras.customer_insights.relationships (
hubName,
relationshipName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ hubName }}',
'{{ relationshipName }}',
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
        - name: cardinality
          value: string
        - name: displayName
          value: object
        - name: description
          value: object
        - name: expiryDateTimeUtc
          value: string
        - name: fields
          value:
            - - name: arrayValueSeparator
                value: string
              - name: enumValidValues
                value:
                  - - name: value
                      value: integer
                    - name: localizedValueNames
                      value: object
              - name: fieldName
                value: string
              - name: fieldType
                value: string
              - name: isArray
                value: boolean
              - name: isEnum
                value: boolean
              - name: isFlagEnum
                value: boolean
              - name: isImage
                value: boolean
              - name: isLocalizedString
                value: boolean
              - name: isName
                value: boolean
              - name: isRequired
                value: boolean
              - name: propertyId
                value: string
              - name: schemaItemPropLink
                value: string
              - name: maxLength
                value: integer
              - name: isAvailableInGraph
                value: boolean
              - name: dataSourcePrecedenceRules
                value:
                  - - name: dataSource
                      value:
                        - name: name
                          value: string
                        - name: dataSourceType
                          value: string
                        - name: status
                          value: string
                        - name: id
                          value: integer
                        - name: dataSourceReferenceId
                          value: string
                    - name: precedence
                      value: integer
        - name: lookupMappings
          value:
            - - name: fieldMappings
                value:
                  - - name: profileFieldName
                      value: string
                    - name: relatedProfileKeyProperty
                      value: string
        - name: profileType
          value: string
        - name: provisioningState
          value: []
        - name: relationshipName
          value: string
        - name: relatedProfileType
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

Deletes the specified <code>relationships</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.customer_insights.relationships
WHERE hubName = '{{ hubName }}'
AND relationshipName = '{{ relationshipName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
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

Creates, updates, deletes, gets or lists a <code>profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.profiles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_profiles', value: 'view', },
        { label: 'profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="api_entity_set_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="entity_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="fields" /> | `text` | field from the `properties` object |
| <CopyableCode code="hubName" /> | `text` | field from the `properties` object |
| <CopyableCode code="instances_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_changed_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schema_item_type_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="strong_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="timestamp_field_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="type_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The profile type definition. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, profileName, resourceGroupName, subscriptionId" /> | Gets information about the specified profile. |
| <CopyableCode code="list_by_hub" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all profile in the hub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hubName, profileName, resourceGroupName, subscriptionId" /> | Creates a profile within a Hub, or updates an existing profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hubName, profileName, resourceGroupName, subscriptionId" /> | Deletes a profile within a hub |

## `SELECT` examples

Gets all profile in the hub.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_profiles', value: 'view', },
        { label: 'profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
api_entity_set_name,
entity_type,
fields,
hubName,
instances_count,
last_changed_utc,
profileName,
provisioning_state,
resourceGroupName,
schema_item_type_link,
strong_ids,
subscriptionId,
tenant_id,
timestamp_field_name,
type,
type_name
FROM azure_extras.customer_insights.vw_profiles
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
FROM azure_extras.customer_insights.profiles
WHERE hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>profiles</code> resource.

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
INSERT INTO azure_extras.customer_insights.profiles (
hubName,
profileName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ hubName }}',
'{{ profileName }}',
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
        - name: strongIds
          value:
            - - name: keyPropertyNames
                value:
                  - string
              - name: strongIdName
                value: string
              - name: displayName
                value: object
              - name: description
                value: object
        - name: apiEntitySetName
          value: string
        - name: entityType
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
        - name: instancesCount
          value: integer
        - name: lastChangedUtc
          value: string
        - name: provisioningState
          value: []
        - name: schemaItemTypeLink
          value: string
        - name: tenantId
          value: string
        - name: timestampFieldName
          value: string
        - name: typeName
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

Deletes the specified <code>profiles</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.customer_insights.profiles
WHERE hubName = '{{ hubName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

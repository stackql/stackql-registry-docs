---
title: connector_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_mappings
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

Creates, updates, deletes, gets or lists a <code>connector_mappings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.connector_mappings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connector_mappings', value: 'view', },
        { label: 'connector_mappings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connector_mapping_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="connector_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="connector_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_format_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="entity_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="entity_type_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="hubName" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified" /> | `text` | field from the `properties` object |
| <CopyableCode code="mappingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="mapping_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_run_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The connector mapping definition. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectorName, hubName, mappingName, resourceGroupName, subscriptionId" /> | Gets a connector mapping in the connector. |
| <CopyableCode code="list_by_connector" /> | `SELECT` | <CopyableCode code="connectorName, hubName, resourceGroupName, subscriptionId" /> | Gets all the connector mappings in the specified connector. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectorName, hubName, mappingName, resourceGroupName, subscriptionId" /> | Creates a connector mapping or updates an existing connector mapping in the connector. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectorName, hubName, mappingName, resourceGroupName, subscriptionId" /> | Deletes a connector mapping in the connector. |

## `SELECT` examples

Gets all the connector mappings in the specified connector.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connector_mappings', value: 'view', },
        { label: 'connector_mappings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
connectorName,
connector_mapping_name,
connector_name,
connector_type,
created,
data_format_id,
display_name,
entity_type,
entity_type_name,
hubName,
last_modified,
mappingName,
mapping_properties,
next_run_time,
resourceGroupName,
run_id,
state,
subscriptionId,
tenant_id,
type
FROM azure_extras.customer_insights.vw_connector_mappings
WHERE connectorName = '{{ connectorName }}'
AND hubName = '{{ hubName }}'
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
FROM azure_extras.customer_insights.connector_mappings
WHERE connectorName = '{{ connectorName }}'
AND hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connector_mappings</code> resource.

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
INSERT INTO azure_extras.customer_insights.connector_mappings (
connectorName,
hubName,
mappingName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ connectorName }}',
'{{ hubName }}',
'{{ mappingName }}',
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
        - name: connectorName
          value: string
        - name: connectorType
          value: []
        - name: created
          value: string
        - name: lastModified
          value: string
        - name: entityType
          value: string
        - name: entityTypeName
          value: string
        - name: connectorMappingName
          value: string
        - name: displayName
          value: string
        - name: description
          value: string
        - name: dataFormatId
          value: string
        - name: mappingProperties
          value:
            - name: folderPath
              value: string
            - name: fileFilter
              value: string
            - name: hasHeader
              value: boolean
            - name: errorManagement
              value:
                - name: errorManagementType
                  value: string
                - name: errorLimit
                  value: integer
            - name: format
              value:
                - name: formatType
                  value: string
                - name: columnDelimiter
                  value: string
                - name: acceptLanguage
                  value: string
                - name: quoteCharacter
                  value: string
                - name: quoteEscapeCharacter
                  value: string
                - name: arraySeparator
                  value: string
            - name: availability
              value:
                - name: frequency
                  value: string
                - name: interval
                  value: integer
            - name: structure
              value:
                - - name: propertyName
                    value: string
                  - name: columnName
                    value: string
                  - name: customFormatSpecifier
                    value: string
                  - name: isEncrypted
                    value: boolean
            - name: completeOperation
              value:
                - name: completionOperationType
                  value: string
                - name: destinationFolder
                  value: string
        - name: nextRunTime
          value: string
        - name: runId
          value: string
        - name: state
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

Deletes the specified <code>connector_mappings</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.customer_insights.connector_mappings
WHERE connectorName = '{{ connectorName }}'
AND hubName = '{{ hubName }}'
AND mappingName = '{{ mappingName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

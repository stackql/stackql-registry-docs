---
title: change_data_captures
hide_title: false
hide_table_of_contents: false
keywords:
  - change_data_captures
  - data_factory
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

Creates, updates, deletes, gets or lists a <code>change_data_captures</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>change_data_captures</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.change_data_captures" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_change_data_captures', value: 'view', },
        { label: 'change_data_captures', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_v_net_override" /> | `text` | field from the `properties` object |
| <CopyableCode code="changeDataCaptureName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag identifies change in the resource. |
| <CopyableCode code="factoryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="folder" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_connections_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_connections_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | Etag identifies change in the resource. |
| <CopyableCode code="properties" /> | `object` | A Azure Data Factory object which automatically detects data changes at the source and then sends the updated data to the destination. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="changeDataCaptureName, factoryName, resourceGroupName, subscriptionId" /> | Gets a change data capture. |
| <CopyableCode code="list_by_factory" /> | `SELECT` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Lists all resources of type change data capture. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="changeDataCaptureName, factoryName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a change data capture resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="changeDataCaptureName, factoryName, resourceGroupName, subscriptionId" /> | Deletes a change data capture. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="changeDataCaptureName, factoryName, resourceGroupName, subscriptionId" /> | Starts a change data capture. |
| <CopyableCode code="status" /> | `EXEC` | <CopyableCode code="changeDataCaptureName, factoryName, resourceGroupName, subscriptionId" /> | Gets the current status for the change data capture resource. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="changeDataCaptureName, factoryName, resourceGroupName, subscriptionId" /> | Stops a change data capture. |

## `SELECT` examples

Lists all resources of type change data capture.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_change_data_captures', value: 'view', },
        { label: 'change_data_captures', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
allow_v_net_override,
changeDataCaptureName,
etag,
factoryName,
folder,
policy,
resourceGroupName,
source_connections_info,
status,
subscriptionId,
target_connections_info,
type
FROM azure.data_factory.vw_change_data_captures
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.data_factory.change_data_captures
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>change_data_captures</code> resource.

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
INSERT INTO azure.data_factory.change_data_captures (
changeDataCaptureName,
factoryName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ changeDataCaptureName }}',
'{{ factoryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: etag
      value: string
    - name: properties
      value:
        - name: folder
          value:
            - name: name
              value: string
        - name: description
          value: string
        - name: sourceConnectionsInfo
          value:
            - - name: sourceEntities
                value:
                  - - name: name
                      value: string
                    - name: properties
                      value:
                        - name: schema
                          value:
                            - - name: name
                                value: string
                              - name: dataType
                                value: string
                        - name: dslConnectorProperties
                          value:
                            - - name: name
                                value: string
                              - name: value
                                value: object
              - name: connection
                value:
                  - name: linkedService
                    value:
                      - name: type
                        value: string
                      - name: referenceName
                        value: string
                      - name: parameters
                        value: []
                  - name: linkedServiceType
                    value: string
                  - name: type
                    value: string
                  - name: isInlineDataset
                    value: boolean
                  - name: commonDslConnectorProperties
                    value:
                      - - name: name
                          value: string
                        - name: value
                          value: object
        - name: targetConnectionsInfo
          value:
            - - name: targetEntities
                value:
                  - - name: name
                      value: string
              - name: dataMapperMappings
                value:
                  - - name: targetEntityName
                      value: string
                    - name: sourceEntityName
                      value: string
                    - name: sourceConnectionReference
                      value:
                        - name: connectionName
                          value: string
                        - name: type
                          value: string
                    - name: attributeMappingInfo
                      value:
                        - name: attributeMappings
                          value:
                            - - name: name
                                value: string
                              - name: type
                                value: string
                              - name: functionName
                                value: string
                              - name: expression
                                value: string
                              - name: attributeReference
                                value:
                                  - name: name
                                    value: string
                                  - name: entity
                                    value: string
                              - name: attributeReferences
                                value:
                                  - - name: name
                                      value: string
                                    - name: entity
                                      value: string
                    - name: sourceDenormalizeInfo
                      value: object
              - name: relationships
                value:
                  - object
        - name: policy
          value:
            - name: mode
              value: string
            - name: recurrence
              value:
                - name: frequency
                  value: string
                - name: interval
                  value: integer
        - name: allowVNetOverride
          value: boolean
        - name: status
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>change_data_captures</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_factory.change_data_captures
WHERE changeDataCaptureName = '{{ changeDataCaptureName }}'
AND factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

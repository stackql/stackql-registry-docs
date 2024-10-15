---
title: rules_engines
hide_title: false
hide_table_of_contents: false
keywords:
  - rules_engines
  - front_door
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

Creates, updates, deletes, gets or lists a <code>rules_engines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rules_engines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.front_door.rules_engines" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_rules_engines', value: 'view', },
        { label: 'rules_engines', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="frontDoorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="rulesEngineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties required to create a Rules Engine Configuration. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="frontDoorName, resourceGroupName, rulesEngineName, subscriptionId" /> | Gets a Rules Engine Configuration with the specified name within the specified Front Door. |
| <CopyableCode code="list_by_front_door" /> | `SELECT` | <CopyableCode code="frontDoorName, resourceGroupName, subscriptionId" /> | Lists all of the Rules Engine Configurations within a Front Door. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="frontDoorName, resourceGroupName, rulesEngineName, subscriptionId" /> | Creates a new Rules Engine Configuration with the specified name within the specified Front Door. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="frontDoorName, resourceGroupName, rulesEngineName, subscriptionId" /> | Deletes an existing Rules Engine Configuration with the specified parameters. |

## `SELECT` examples

Lists all of the Rules Engine Configurations within a Front Door.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_rules_engines', value: 'view', },
        { label: 'rules_engines', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
frontDoorName,
resourceGroupName,
resource_state,
rules,
rulesEngineName,
subscriptionId,
type
FROM azure.front_door.vw_rules_engines
WHERE frontDoorName = '{{ frontDoorName }}'
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
FROM azure.front_door.rules_engines
WHERE frontDoorName = '{{ frontDoorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rules_engines</code> resource.

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
INSERT INTO azure.front_door.rules_engines (
frontDoorName,
resourceGroupName,
rulesEngineName,
subscriptionId,
properties
)
SELECT 
'{{ frontDoorName }}',
'{{ resourceGroupName }}',
'{{ rulesEngineName }}',
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
        - name: rules
          value:
            - - name: name
                value: string
              - name: priority
                value: integer
              - name: action
                value:
                  - name: requestHeaderActions
                    value:
                      - - name: headerActionType
                          value: string
                        - name: headerName
                          value: string
                        - name: value
                          value: string
                  - name: responseHeaderActions
                    value:
                      - - name: headerActionType
                          value: string
                        - name: headerName
                          value: string
                        - name: value
                          value: string
                  - name: routeConfigurationOverride
                    value:
                      - name: '@odata.type'
                        value: string
              - name: matchConditions
                value:
                  - - name: rulesEngineMatchVariable
                      value: string
                    - name: selector
                      value: string
                    - name: rulesEngineOperator
                      value: string
                    - name: negateCondition
                      value: boolean
                    - name: rulesEngineMatchValue
                      value:
                        - string
                    - name: transforms
                      value:
                        - []
              - name: matchProcessingBehavior
                value: string
        - name: resourceState
          value: []
    - name: name
      value: string
    - name: type
      value: string
    - name: id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>rules_engines</code> resource.

```sql
/*+ delete */
DELETE FROM azure.front_door.rules_engines
WHERE frontDoorName = '{{ frontDoorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND rulesEngineName = '{{ rulesEngineName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

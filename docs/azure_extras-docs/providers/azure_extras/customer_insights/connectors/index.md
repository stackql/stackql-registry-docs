---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
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

Creates, updates, deletes, gets or lists a <code>connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.connectors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connectors', value: 'view', },
        { label: 'connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connector_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="connector_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="connector_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="connector_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="hubName" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_internal" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | Properties of connector. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectorName, hubName, resourceGroupName, subscriptionId" /> | Gets a connector in the hub. |
| <CopyableCode code="list_by_hub" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all the connectors in the specified hub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectorName, hubName, resourceGroupName, subscriptionId" /> | Creates a connector or updates an existing connector in the hub. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectorName, hubName, resourceGroupName, subscriptionId" /> | Deletes a connector in the hub. |

## `SELECT` examples

Gets all the connectors in the specified hub.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connectors', value: 'view', },
        { label: 'connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
connectorName,
connector_id,
connector_name,
connector_properties,
connector_type,
created,
display_name,
hubName,
is_internal,
last_modified,
resourceGroupName,
state,
subscriptionId,
tenant_id,
type
FROM azure_extras.customer_insights.vw_connectors
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
FROM azure_extras.customer_insights.connectors
WHERE hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connectors</code> resource.

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
INSERT INTO azure_extras.customer_insights.connectors (
connectorName,
hubName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ connectorName }}',
'{{ hubName }}',
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
        - name: connectorId
          value: integer
        - name: connectorName
          value: string
        - name: connectorType
          value: []
        - name: displayName
          value: string
        - name: description
          value: string
        - name: connectorProperties
          value: object
        - name: created
          value: string
        - name: lastModified
          value: string
        - name: state
          value: string
        - name: tenantId
          value: string
        - name: isInternal
          value: boolean
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

Deletes the specified <code>connectors</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.customer_insights.connectors
WHERE connectorName = '{{ connectorName }}'
AND hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

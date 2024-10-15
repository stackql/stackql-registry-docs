---
title: kpis
hide_title: false
hide_table_of_contents: false
keywords:
  - kpis
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

Creates, updates, deletes, gets or lists a <code>kpis</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kpis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.kpis" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kpis', value: 'view', },
        { label: 'kpis', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="aliases" /> | `text` | field from the `properties` object |
| <CopyableCode code="calculation_window" /> | `text` | field from the `properties` object |
| <CopyableCode code="calculation_window_field_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="entity_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="entity_type_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="expression" /> | `text` | field from the `properties` object |
| <CopyableCode code="extracts" /> | `text` | field from the `properties` object |
| <CopyableCode code="filter" /> | `text` | field from the `properties` object |
| <CopyableCode code="function" /> | `text` | field from the `properties` object |
| <CopyableCode code="group_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="group_by_metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="hubName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kpiName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kpi_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="participant_profiles_metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="thres_holds" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="unit" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | Defines the KPI Threshold limits. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, kpiName, resourceGroupName, subscriptionId" /> | Gets a KPI in the hub. |
| <CopyableCode code="list_by_hub" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all the KPIs in the specified hub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hubName, kpiName, resourceGroupName, subscriptionId" /> | Creates a KPI or updates an existing KPI in the hub. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hubName, kpiName, resourceGroupName, subscriptionId" /> | Deletes a KPI in the hub. |
| <CopyableCode code="reprocess" /> | `EXEC` | <CopyableCode code="hubName, kpiName, resourceGroupName, subscriptionId" /> | Reprocesses the Kpi values of the specified KPI. |

## `SELECT` examples

Gets all the KPIs in the specified hub.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kpis', value: 'view', },
        { label: 'kpis', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
aliases,
calculation_window,
calculation_window_field_name,
display_name,
entity_type,
entity_type_name,
expression,
extracts,
filter,
function,
group_by,
group_by_metadata,
hubName,
kpiName,
kpi_name,
participant_profiles_metadata,
provisioning_state,
resourceGroupName,
subscriptionId,
tenant_id,
thres_holds,
type,
unit
FROM azure_extras.customer_insights.vw_kpis
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
FROM azure_extras.customer_insights.kpis
WHERE hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>kpis</code> resource.

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
INSERT INTO azure_extras.customer_insights.kpis (
hubName,
kpiName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ hubName }}',
'{{ kpiName }}',
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
        - name: entityType
          value: string
        - name: entityTypeName
          value: string
        - name: tenantId
          value: string
        - name: kpiName
          value: string
        - name: displayName
          value: object
        - name: description
          value: object
        - name: calculationWindow
          value: string
        - name: calculationWindowFieldName
          value: string
        - name: function
          value: string
        - name: expression
          value: string
        - name: unit
          value: string
        - name: filter
          value: string
        - name: groupBy
          value:
            - string
        - name: groupByMetadata
          value:
            - - name: displayName
                value: object
              - name: fieldName
                value: string
              - name: fieldType
                value: string
        - name: participantProfilesMetadata
          value:
            - - name: typeName
                value: string
        - name: provisioningState
          value: []
        - name: thresHolds
          value:
            - name: lowerLimit
              value: number
            - name: upperLimit
              value: number
            - name: increasingKpi
              value: boolean
        - name: aliases
          value:
            - - name: aliasName
                value: string
              - name: expression
                value: string
        - name: extracts
          value:
            - - name: extractName
                value: string
              - name: expression
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

Deletes the specified <code>kpis</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.customer_insights.kpis
WHERE hubName = '{{ hubName }}'
AND kpiName = '{{ kpiName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

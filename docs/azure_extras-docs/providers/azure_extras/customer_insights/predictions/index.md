---
title: predictions
hide_title: false
hide_table_of_contents: false
keywords:
  - predictions
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

Creates, updates, deletes, gets or lists a <code>predictions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>predictions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.predictions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_predictions', value: 'view', },
        { label: 'predictions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_analyze" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="grades" /> | `text` | field from the `properties` object |
| <CopyableCode code="hubName" /> | `text` | field from the `properties` object |
| <CopyableCode code="involved_interaction_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="involved_kpi_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="involved_relationships" /> | `text` | field from the `properties` object |
| <CopyableCode code="mappings" /> | `text` | field from the `properties` object |
| <CopyableCode code="negative_outcome_expression" /> | `text` | field from the `properties` object |
| <CopyableCode code="positive_outcome_expression" /> | `text` | field from the `properties` object |
| <CopyableCode code="predictionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="prediction_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_profile_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope_expression" /> | `text` | field from the `properties` object |
| <CopyableCode code="score_label" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_generated_entities" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The prediction definition. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, predictionName, resourceGroupName, subscriptionId" /> | Gets a Prediction in the hub. |
| <CopyableCode code="list_by_hub" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all the predictions in the specified hub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hubName, predictionName, resourceGroupName, subscriptionId" /> | Creates a Prediction or updates an existing Prediction in the hub. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hubName, predictionName, resourceGroupName, subscriptionId" /> | Deletes a Prediction in the hub. |
| <CopyableCode code="model_status" /> | `EXEC` | <CopyableCode code="hubName, predictionName, resourceGroupName, subscriptionId, data__status" /> | Creates or updates the model status of prediction. |

## `SELECT` examples

Gets all the predictions in the specified hub.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_predictions', value: 'view', },
        { label: 'predictions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
auto_analyze,
display_name,
grades,
hubName,
involved_interaction_types,
involved_kpi_types,
involved_relationships,
mappings,
negative_outcome_expression,
positive_outcome_expression,
predictionName,
prediction_name,
primary_profile_type,
provisioning_state,
resourceGroupName,
scope_expression,
score_label,
subscriptionId,
system_generated_entities,
tenant_id,
type
FROM azure_extras.customer_insights.vw_predictions
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
FROM azure_extras.customer_insights.predictions
WHERE hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>predictions</code> resource.

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
INSERT INTO azure_extras.customer_insights.predictions (
hubName,
predictionName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ hubName }}',
'{{ predictionName }}',
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
        - name: description
          value: object
        - name: displayName
          value: object
        - name: involvedInteractionTypes
          value:
            - string
        - name: involvedKpiTypes
          value:
            - string
        - name: involvedRelationships
          value:
            - string
        - name: negativeOutcomeExpression
          value: string
        - name: positiveOutcomeExpression
          value: string
        - name: primaryProfileType
          value: string
        - name: provisioningState
          value: []
        - name: predictionName
          value: string
        - name: scopeExpression
          value: string
        - name: tenantId
          value: string
        - name: autoAnalyze
          value: boolean
        - name: mappings
          value:
            - name: score
              value: string
            - name: grade
              value: string
            - name: reason
              value: string
        - name: scoreLabel
          value: string
        - name: grades
          value:
            - - name: gradeName
                value: string
              - name: minScoreThreshold
                value: integer
              - name: maxScoreThreshold
                value: integer
        - name: systemGeneratedEntities
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

Deletes the specified <code>predictions</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.customer_insights.predictions
WHERE hubName = '{{ hubName }}'
AND predictionName = '{{ predictionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

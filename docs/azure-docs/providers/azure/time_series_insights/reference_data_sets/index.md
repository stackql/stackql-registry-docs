---
title: reference_data_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - reference_data_sets
  - time_series_insights
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

Creates, updates, deletes, gets or lists a <code>reference_data_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reference_data_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.time_series_insights.reference_data_sets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reference_data_sets', value: 'view', },
        { label: 'reference_data_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_string_comparison_behavior" /> | `text` | field from the `properties` object |
| <CopyableCode code="environmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="referenceDataSetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Properties of the reference data set. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, referenceDataSetName, resourceGroupName, subscriptionId" /> | Gets the reference data set with the specified name in the specified environment. |
| <CopyableCode code="list_by_environment" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Lists all the available reference data sets associated with the subscription and within the specified resource group and environment. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, referenceDataSetName, resourceGroupName, subscriptionId, data__properties" /> | Create or update a reference data set in the specified environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, referenceDataSetName, resourceGroupName, subscriptionId" /> | Deletes the reference data set with the specified name in the specified subscription, resource group, and environment |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="environmentName, referenceDataSetName, resourceGroupName, subscriptionId" /> | Updates the reference data set with the specified name in the specified subscription, resource group, and environment. |

## `SELECT` examples

Lists all the available reference data sets associated with the subscription and within the specified resource group and environment.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reference_data_sets', value: 'view', },
        { label: 'reference_data_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
creation_time,
data_string_comparison_behavior,
environmentName,
key_properties,
location,
provisioning_state,
referenceDataSetName,
resourceGroupName,
subscriptionId,
tags
FROM azure.time_series_insights.vw_reference_data_sets
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.time_series_insights.reference_data_sets
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>reference_data_sets</code> resource.

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
INSERT INTO azure.time_series_insights.reference_data_sets (
environmentName,
referenceDataSetName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
location,
tags
)
SELECT 
'{{ environmentName }}',
'{{ referenceDataSetName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: keyProperties
          value:
            - - name: name
                value: string
              - name: type
                value: string
        - name: dataStringComparisonBehavior
          value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>reference_data_sets</code> resource.

```sql
/*+ update */
UPDATE azure.time_series_insights.reference_data_sets
SET 
tags = '{{ tags }}'
WHERE 
environmentName = '{{ environmentName }}'
AND referenceDataSetName = '{{ referenceDataSetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>reference_data_sets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.time_series_insights.reference_data_sets
WHERE environmentName = '{{ environmentName }}'
AND referenceDataSetName = '{{ referenceDataSetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

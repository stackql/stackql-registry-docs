---
title: budgets
hide_title: false
hide_table_of_contents: false
keywords:
  - budgets
  - consumption
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

Creates, updates, deletes, gets or lists a <code>budgets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>budgets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.budgets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_budgets', value: 'view', },
        { label: 'budgets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="amount" /> | `text` | field from the `properties` object |
| <CopyableCode code="budgetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="category" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_spend" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="filter" /> | `text` | field from the `properties` object |
| <CopyableCode code="forecast_spend" /> | `text` | field from the `properties` object |
| <CopyableCode code="notifications" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_grain" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_period" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="eTag" /> | `string` | eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not. |
| <CopyableCode code="properties" /> | `object` | The properties of the budget. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="budgetName, scope" /> | Gets the budget for the scope by budget name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Lists all budgets for the defined scope. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="budgetName, scope" /> | The operation to create or update a budget. You can optionally provide an eTag if desired as a form of concurrency control. To obtain the latest eTag for a given budget, perform a get operation prior to your put operation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="budgetName, scope" /> | The operation to delete a budget. |

## `SELECT` examples

Lists all budgets for the defined scope.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_budgets', value: 'view', },
        { label: 'budgets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
amount,
budgetName,
category,
current_spend,
e_tag,
filter,
forecast_spend,
notifications,
scope,
time_grain,
time_period,
type
FROM azure.consumption.vw_budgets
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
eTag,
properties,
type
FROM azure.consumption.budgets
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>budgets</code> resource.

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
INSERT INTO azure.consumption.budgets (
budgetName,
scope,
eTag,
properties
)
SELECT 
'{{ budgetName }}',
'{{ scope }}',
'{{ eTag }}',
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
    - name: eTag
      value: string
    - name: properties
      value:
        - name: category
          value: string
        - name: amount
          value: number
        - name: timeGrain
          value: string
        - name: timePeriod
          value:
            - name: startDate
              value: string
            - name: endDate
              value: string
        - name: filter
          value:
            - name: and
              value:
                - - name: dimensions
                    value:
                      - name: name
                        value: string
                      - name: operator
                        value: string
                      - name: values
                        value:
                          - string
        - name: currentSpend
          value:
            - name: amount
              value: number
            - name: unit
              value: string
        - name: notifications
          value: object
        - name: forecastSpend
          value:
            - name: amount
              value: number
            - name: unit
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>budgets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.consumption.budgets
WHERE budgetName = '{{ budgetName }}'
AND scope = '{{ scope }}';
```

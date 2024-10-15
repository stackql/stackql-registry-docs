---
title: costs
hide_title: false
hide_table_of_contents: false
keywords:
  - costs
  - dev_test_labs
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

Creates, updates, deletes, gets or lists a <code>costs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>costs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.costs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_costs', value: 'view', },
        { label: 'costs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="currency_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="labName" /> | `text` | field from the `properties` object |
| <CopyableCode code="lab_cost_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="lab_cost_summary" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_costs" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="target_cost" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="unique_identifier" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a cost item. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Get cost. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, data__properties" /> | Create or replace an existing cost. |

## `SELECT` examples

Get cost.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_costs', value: 'view', },
        { label: 'costs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
created_date,
currency_code,
end_date_time,
labName,
lab_cost_details,
lab_cost_summary,
location,
provisioning_state,
resourceGroupName,
resource_costs,
start_date_time,
subscriptionId,
tags,
target_cost,
type,
unique_identifier
FROM azure.dev_test_labs.vw_costs
WHERE labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.dev_test_labs.costs
WHERE labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>costs</code> resource.

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
INSERT INTO azure.dev_test_labs.costs (
labName,
name,
resourceGroupName,
subscriptionId,
data__properties,
location,
tags,
properties
)
SELECT 
'{{ labName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ location }}',
'{{ tags }}',
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
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: targetCost
          value:
            - name: status
              value: string
            - name: target
              value: integer
            - name: costThresholds
              value:
                - - name: thresholdId
                    value: string
                  - name: percentageThreshold
                    value:
                      - name: thresholdValue
                        value: number
                  - name: displayOnChart
                    value: string
                  - name: sendNotificationWhenExceeded
                    value: string
                  - name: notificationSent
                    value: string
            - name: cycleStartDateTime
              value: string
            - name: cycleEndDateTime
              value: string
            - name: cycleType
              value: string
        - name: labCostSummary
          value:
            - name: estimatedLabCost
              value: number
        - name: labCostDetails
          value:
            - - name: date
                value: string
              - name: cost
                value: number
              - name: costType
                value: string
        - name: resourceCosts
          value:
            - - name: resourcename
                value: string
              - name: resourceUId
                value: string
              - name: resourceCost
                value: number
              - name: resourceType
                value: string
              - name: resourceOwner
                value: string
              - name: resourcePricingTier
                value: string
              - name: resourceStatus
                value: string
              - name: resourceId
                value: string
              - name: externalResourceId
                value: string
        - name: currencyCode
          value: string
        - name: startDateTime
          value: string
        - name: endDateTime
          value: string
        - name: createdDate
          value: string
        - name: provisioningState
          value: string
        - name: uniqueIdentifier
          value: string

```
</TabItem>
</Tabs>

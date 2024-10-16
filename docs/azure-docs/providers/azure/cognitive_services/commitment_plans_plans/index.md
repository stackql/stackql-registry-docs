---
title: commitment_plans_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - commitment_plans_plans
  - cognitive_services
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

Creates, updates, deletes, gets or lists a <code>commitment_plans_plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>commitment_plans_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.commitment_plans_plans" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_commitment_plans_plans', value: 'view', },
        { label: 'commitment_plans_plans', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="auto_renew" /> | `text` | field from the `properties` object |
| <CopyableCode code="commitmentPlanName" /> | `text` | field from the `properties` object |
| <CopyableCode code="commitment_plan_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="current" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource Etag. |
| <CopyableCode code="hosting_model" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The kind (type) of cognitive service account. |
| <CopyableCode code="last" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="next" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_issues" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource Etag. |
| <CopyableCode code="kind" /> | `string` | The kind (type) of cognitive service account. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of Cognitive Services account commitment plan. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="commitmentPlanName, resourceGroupName, subscriptionId" /> | Returns a Cognitive Services commitment plan specified by the parameters. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="commitmentPlanName, resourceGroupName, subscriptionId" /> | Create Cognitive Services commitment plan. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="commitmentPlanName, resourceGroupName, subscriptionId" /> | Deletes a Cognitive Services commitment plan from the resource group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="commitmentPlanName, resourceGroupName, subscriptionId" /> | Create Cognitive Services commitment plan. |

## `SELECT` examples

Returns a Cognitive Services commitment plan specified by the parameters.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_commitment_plans_plans', value: 'view', },
        { label: 'commitment_plans_plans', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
auto_renew,
commitmentPlanName,
commitment_plan_guid,
current,
etag,
hosting_model,
kind,
last,
location,
next,
plan_type,
provisioning_issues,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
system_data,
tags
FROM azure.cognitive_services.vw_commitment_plans_plans
WHERE commitmentPlanName = '{{ commitmentPlanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
kind,
location,
properties,
sku,
systemData,
tags
FROM azure.cognitive_services.commitment_plans_plans
WHERE commitmentPlanName = '{{ commitmentPlanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>commitment_plans_plans</code> resource.

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
INSERT INTO azure.cognitive_services.commitment_plans_plans (
commitmentPlanName,
resourceGroupName,
subscriptionId,
kind,
sku,
tags,
location,
properties
)
SELECT 
'{{ commitmentPlanName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ sku }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: etag
      value: string
    - name: kind
      value: []
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: commitmentPlanGuid
          value: string
        - name: hostingModel
          value: []
        - name: planType
          value: string
        - name: current
          value:
            - name: tier
              value: string
            - name: count
              value: integer
            - name: quota
              value:
                - name: quantity
                  value: integer
                - name: unit
                  value: string
            - name: startDate
              value: string
            - name: endDate
              value: string
        - name: autoRenew
          value: boolean
        - name: provisioningIssues
          value:
            - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>commitment_plans_plans</code> resource.

```sql
/*+ update */
UPDATE azure.cognitive_services.commitment_plans_plans
SET 
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
commitmentPlanName = '{{ commitmentPlanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>commitment_plans_plans</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cognitive_services.commitment_plans_plans
WHERE commitmentPlanName = '{{ commitmentPlanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

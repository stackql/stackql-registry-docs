---
title: solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions
  - ag_food_platform
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

Creates, updates, deletes, gets or lists a <code>solutions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.ag_food_platform.solutions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_solutions', value: 'view', },
        { label: 'solutions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dataManagerForAgricultureResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="marketplace_publisher_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="offer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_assignment_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="saas_subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="saas_subscription_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="solutionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="term_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="eTag" /> | `string` | The ETag value to implement optimistic concurrency. |
| <CopyableCode code="properties" /> | `object` | Solution resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerForAgricultureResourceName, resourceGroupName, solutionId, subscriptionId" /> | Get installed Solution details by Solution id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId" /> | Get installed Solutions details. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataManagerForAgricultureResourceName, resourceGroupName, solutionId, subscriptionId" /> | Install Or Update Solution. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataManagerForAgricultureResourceName, resourceGroupName, solutionId, subscriptionId" /> | Uninstall Solution. |

## `SELECT` examples

Get installed Solutions details.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_solutions', value: 'view', },
        { label: 'solutions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dataManagerForAgricultureResourceName,
e_tag,
marketplace_publisher_id,
offer_id,
partner_id,
plan_id,
resourceGroupName,
role_assignment_id,
saas_subscription_id,
saas_subscription_name,
solutionId,
subscriptionId,
system_data,
term_id
FROM azure_extras.ag_food_platform.vw_solutions
WHERE dataManagerForAgricultureResourceName = '{{ dataManagerForAgricultureResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
eTag,
properties,
systemData
FROM azure_extras.ag_food_platform.solutions
WHERE dataManagerForAgricultureResourceName = '{{ dataManagerForAgricultureResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>solutions</code> resource.

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
INSERT INTO azure_extras.ag_food_platform.solutions (
dataManagerForAgricultureResourceName,
resourceGroupName,
solutionId,
subscriptionId,
systemData,
properties
)
SELECT 
'{{ dataManagerForAgricultureResourceName }}',
'{{ resourceGroupName }}',
'{{ solutionId }}',
'{{ subscriptionId }}',
'{{ systemData }}',
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
    - name: properties
      value:
        - name: partnerId
          value: string
        - name: saasSubscriptionId
          value: string
        - name: saasSubscriptionName
          value: string
        - name: marketplacePublisherId
          value: string
        - name: planId
          value: string
        - name: roleAssignmentId
          value: string
        - name: offerId
          value: string
        - name: termId
          value: string
    - name: eTag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>solutions</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.ag_food_platform.solutions
WHERE dataManagerForAgricultureResourceName = '{{ dataManagerForAgricultureResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND solutionId = '{{ solutionId }}'
AND subscriptionId = '{{ subscriptionId }}';
```

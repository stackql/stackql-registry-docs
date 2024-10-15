---
title: commitment_plans_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - commitment_plans_associations
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

Creates, updates, deletes, gets or lists a <code>commitment_plans_associations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>commitment_plans_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.commitment_plans_associations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_commitment_plans_associations', value: 'view', },
        { label: 'commitment_plans_associations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="commitmentPlanAssociationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="commitmentPlanName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource Etag. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource Etag. |
| <CopyableCode code="properties" /> | `object` | The commitment plan account association properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="commitmentPlanAssociationName, commitmentPlanName, resourceGroupName, subscriptionId" /> | Gets the association of the Cognitive Services commitment plan. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="commitmentPlanName, resourceGroupName, subscriptionId" /> | Gets the associations of the Cognitive Services commitment plan. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="commitmentPlanAssociationName, commitmentPlanName, resourceGroupName, subscriptionId" /> | Create or update the association of the Cognitive Services commitment plan. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="commitmentPlanAssociationName, commitmentPlanName, resourceGroupName, subscriptionId" /> | Deletes the association of the Cognitive Services commitment plan. |

## `SELECT` examples

Gets the associations of the Cognitive Services commitment plan.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_commitment_plans_associations', value: 'view', },
        { label: 'commitment_plans_associations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
account_id,
commitmentPlanAssociationName,
commitmentPlanName,
etag,
resourceGroupName,
subscriptionId,
system_data,
tags
FROM azure.cognitive_services.vw_commitment_plans_associations
WHERE commitmentPlanName = '{{ commitmentPlanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties,
systemData,
tags
FROM azure.cognitive_services.commitment_plans_associations
WHERE commitmentPlanName = '{{ commitmentPlanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>commitment_plans_associations</code> resource.

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
INSERT INTO azure.cognitive_services.commitment_plans_associations (
commitmentPlanAssociationName,
commitmentPlanName,
resourceGroupName,
subscriptionId,
tags,
properties
)
SELECT 
'{{ commitmentPlanAssociationName }}',
'{{ commitmentPlanName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
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
    - name: tags
      value: object
    - name: properties
      value:
        - name: accountId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>commitment_plans_associations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cognitive_services.commitment_plans_associations
WHERE commitmentPlanAssociationName = '{{ commitmentPlanAssociationName }}'
AND commitmentPlanName = '{{ commitmentPlanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

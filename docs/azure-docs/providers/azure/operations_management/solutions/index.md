---
title: solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions
  - operations_management
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.operations_management.solutions" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="contained_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="plan" /> | `text` | Plan for solution object supported by the OperationsManagement resource provider. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="referenced_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="solutionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="workspace_resource_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="plan" /> | `object` | Plan for solution object supported by the OperationsManagement resource provider. |
| <CopyableCode code="properties" /> | `object` | Solution properties supported by the OperationsManagement resource provider. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, solutionName, subscriptionId" /> | Retrieves the user solution. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieves the solution list. It will retrieve both first party and third party solutions |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieves the solution list. It will retrieve both first party and third party solutions |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, solutionName, subscriptionId" /> | Creates or updates the Solution. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, solutionName, subscriptionId" /> | Deletes the solution in the subscription. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, solutionName, subscriptionId" /> | Patch a Solution. Only updating tags supported. |

## `SELECT` examples

Retrieves the solution list. It will retrieve both first party and third party solutions

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
id,
name,
contained_resources,
location,
plan,
provisioning_state,
referenced_resources,
resourceGroupName,
solutionName,
subscriptionId,
tags,
type,
workspace_resource_id
FROM azure.operations_management.vw_solutions
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
plan,
properties,
tags,
type
FROM azure.operations_management.solutions
WHERE subscriptionId = '{{ subscriptionId }}';
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
INSERT INTO azure.operations_management.solutions (
resourceGroupName,
solutionName,
subscriptionId,
location,
tags,
plan,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ solutionName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ plan }}',
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
    - name: plan
      value:
        - name: name
          value: string
        - name: publisher
          value: string
        - name: promotionCode
          value: string
        - name: product
          value: string
    - name: properties
      value:
        - name: workspaceResourceId
          value: string
        - name: provisioningState
          value: string
        - name: containedResources
          value:
            - string
        - name: referencedResources
          value:
            - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>solutions</code> resource.

```sql
/*+ update */
UPDATE azure.operations_management.solutions
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND solutionName = '{{ solutionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>solutions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.operations_management.solutions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND solutionName = '{{ solutionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

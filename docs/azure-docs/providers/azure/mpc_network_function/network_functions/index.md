---
title: network_functions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_functions
  - mpc_network_function
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

Creates, updates, deletes, gets or lists a <code>network_functions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mpc_network_function.network_functions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_functions', value: 'view', },
        { label: 'network_functions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capacity" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_notes" /> | `text` | field from the `properties` object |
| <CopyableCode code="infrastructure_element_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="networkFunctionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_function_administrative_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_function_operational_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_function_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="user_description" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network Function Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Get a NetworkFunctionResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List NetworkFunctionResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List NetworkFunctionResource resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Create a NetworkFunctionResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Delete a NetworkFunctionResource |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Update a NetworkFunctionResource |

## `SELECT` examples

List NetworkFunctionResource resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_functions', value: 'view', },
        { label: 'network_functions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
capacity,
deployment_notes,
infrastructure_element_count,
location,
networkFunctionName,
network_function_administrative_state,
network_function_operational_status,
network_function_type,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
tags,
user_description
FROM azure.mpc_network_function.vw_network_functions
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.mpc_network_function.network_functions
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_functions</code> resource.

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
INSERT INTO azure.mpc_network_function.network_functions (
networkFunctionName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ networkFunctionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: sku
          value: []
        - name: networkFunctionType
          value: []
        - name: networkFunctionAdministrativeState
          value: []
        - name: networkFunctionOperationalStatus
          value: []
        - name: infrastructureElementCount
          value: integer
        - name: capacity
          value: integer
        - name: userDescription
          value: string
        - name: deploymentNotes
          value: string
        - name: provisioningState
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>network_functions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.mpc_network_function.network_functions
WHERE networkFunctionName = '{{ networkFunctionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

---
title: registered_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - registered_prefixes
  - peering
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

Creates, updates, deletes, gets or lists a <code>registered_prefixes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registered_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.registered_prefixes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registered_prefixes', value: 'view', },
        { label: 'registered_prefixes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="error_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="peeringName" /> | `text` | field from the `properties` object |
| <CopyableCode code="peering_service_prefix_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="prefix_validation_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registeredPrefixName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties that define a registered prefix. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peeringName, registeredPrefixName, resourceGroupName, subscriptionId" /> | Gets an existing registered prefix with the specified name under the given subscription, resource group and peering. |
| <CopyableCode code="list_by_peering" /> | `SELECT` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId" /> | Lists all registered prefixes under the given subscription, resource group and peering. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="peeringName, registeredPrefixName, resourceGroupName, subscriptionId" /> | Creates a new registered prefix with the specified name under the given subscription, resource group and peering. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peeringName, registeredPrefixName, resourceGroupName, subscriptionId" /> | Deletes an existing registered prefix with the specified name under the given subscription, resource group and peering. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="peeringName, registeredPrefixName, resourceGroupName, subscriptionId" /> | Validates an existing registered prefix with the specified name under the given subscription, resource group and peering. |

## `SELECT` examples

Lists all registered prefixes under the given subscription, resource group and peering.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registered_prefixes', value: 'view', },
        { label: 'registered_prefixes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
error_message,
peeringName,
peering_service_prefix_key,
prefix,
prefix_validation_state,
provisioning_state,
registeredPrefixName,
resourceGroupName,
subscriptionId,
type
FROM azure.peering.vw_registered_prefixes
WHERE peeringName = '{{ peeringName }}'
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
FROM azure.peering.registered_prefixes
WHERE peeringName = '{{ peeringName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>registered_prefixes</code> resource.

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
INSERT INTO azure.peering.registered_prefixes (
peeringName,
registeredPrefixName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ peeringName }}',
'{{ registeredPrefixName }}',
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
    - name: name
      value: string
    - name: id
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: prefix
          value: string
        - name: prefixValidationState
          value: string
        - name: peeringServicePrefixKey
          value: string
        - name: errorMessage
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>registered_prefixes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.peering.registered_prefixes
WHERE peeringName = '{{ peeringName }}'
AND registeredPrefixName = '{{ registeredPrefixName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

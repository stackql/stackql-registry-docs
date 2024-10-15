---
title: registered_asns
hide_title: false
hide_table_of_contents: false
keywords:
  - registered_asns
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

Creates, updates, deletes, gets or lists a <code>registered_asns</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registered_asns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.registered_asns" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registered_asns', value: 'view', },
        { label: 'registered_asns', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="asn" /> | `text` | field from the `properties` object |
| <CopyableCode code="peeringName" /> | `text` | field from the `properties` object |
| <CopyableCode code="peering_service_prefix_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registeredAsnName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties that define a registered ASN. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peeringName, registeredAsnName, resourceGroupName, subscriptionId" /> | Gets an existing registered ASN with the specified name under the given subscription, resource group and peering. |
| <CopyableCode code="list_by_peering" /> | `SELECT` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId" /> | Lists all registered ASNs under the given subscription, resource group and peering. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="peeringName, registeredAsnName, resourceGroupName, subscriptionId" /> | Creates a new registered ASN with the specified name under the given subscription, resource group and peering. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peeringName, registeredAsnName, resourceGroupName, subscriptionId" /> | Deletes an existing registered ASN with the specified name under the given subscription, resource group and peering. |

## `SELECT` examples

Lists all registered ASNs under the given subscription, resource group and peering.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registered_asns', value: 'view', },
        { label: 'registered_asns', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
asn,
peeringName,
peering_service_prefix_key,
provisioning_state,
registeredAsnName,
resourceGroupName,
subscriptionId,
type
FROM azure.peering.vw_registered_asns
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
FROM azure.peering.registered_asns
WHERE peeringName = '{{ peeringName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>registered_asns</code> resource.

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
INSERT INTO azure.peering.registered_asns (
peeringName,
registeredAsnName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ peeringName }}',
'{{ registeredAsnName }}',
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
        - name: asn
          value: integer
        - name: peeringServicePrefixKey
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>registered_asns</code> resource.

```sql
/*+ delete */
DELETE FROM azure.peering.registered_asns
WHERE peeringName = '{{ peeringName }}'
AND registeredAsnName = '{{ registeredAsnName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

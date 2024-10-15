---
title: ddos_protection_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - ddos_protection_plans
  - network
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

Creates, updates, deletes, gets or lists a <code>ddos_protection_plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ddos_protection_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.ddos_protection_plans" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ddos_protection_plans', value: 'view', },
        { label: 'ddos_protection_plans', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="ddosProtectionPlanName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtual_networks" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | DDoS protection plan properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ddosProtectionPlanName, resourceGroupName, subscriptionId" /> | Gets information about the specified DDoS protection plan. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all DDoS protection plans in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the DDoS protection plans in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="ddosProtectionPlanName, resourceGroupName, subscriptionId" /> | Creates or updates a DDoS protection plan. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="ddosProtectionPlanName, resourceGroupName, subscriptionId" /> | Deletes the specified DDoS protection plan. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="ddosProtectionPlanName, resourceGroupName, subscriptionId" /> | Update a DDoS protection plan tags. |

## `SELECT` examples

Gets all DDoS protection plans in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ddos_protection_plans', value: 'view', },
        { label: 'ddos_protection_plans', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
ddosProtectionPlanName,
etag,
location,
provisioning_state,
public_ip_addresses,
resourceGroupName,
resource_guid,
subscriptionId,
tags,
type,
virtual_networks
FROM azure.network.vw_ddos_protection_plans
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
tags,
type
FROM azure.network.ddos_protection_plans
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ddos_protection_plans</code> resource.

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
INSERT INTO azure.network.ddos_protection_plans (
ddosProtectionPlanName,
resourceGroupName,
subscriptionId,
location,
tags,
properties
)
SELECT 
'{{ ddosProtectionPlanName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: resourceGuid
          value: string
        - name: provisioningState
          value: []
        - name: publicIPAddresses
          value:
            - - name: id
                value: string
        - name: virtualNetworks
          value:
            - - name: id
                value: string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>ddos_protection_plans</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.ddos_protection_plans
WHERE ddosProtectionPlanName = '{{ ddosProtectionPlanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

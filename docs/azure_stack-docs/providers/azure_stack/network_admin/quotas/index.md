---
title: quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - quotas
  - network_admin
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

Creates, updates, deletes, gets or lists a <code>quotas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.network_admin.quotas" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_quotas', value: 'view', },
        { label: 'quotas', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="location" /> | `text` | Region location of resource. |
| <CopyableCode code="max_load_balancers_per_subscription" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_nics_per_subscription" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_public_ips_per_subscription" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_security_groups_per_subscription" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_virtual_network_gateway_connections_per_subscription" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_virtual_network_gateways_per_subscription" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_vnets_per_subscription" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_phase" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Region location of resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a quota. |
| <CopyableCode code="tags" /> | `object` | List of key value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, resourceName, subscriptionId" /> | Get a quota by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List all quotas. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="location, resourceName, subscriptionId" /> | Create or update a quota. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="location, resourceName, subscriptionId" /> | Delete a quota by name. |

## `SELECT` examples

List all quotas.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_quotas', value: 'view', },
        { label: 'quotas', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
location,
max_load_balancers_per_subscription,
max_nics_per_subscription,
max_public_ips_per_subscription,
max_security_groups_per_subscription,
max_virtual_network_gateway_connections_per_subscription,
max_virtual_network_gateways_per_subscription,
max_vnets_per_subscription,
migration_phase,
provisioning_state,
resourceName,
subscriptionId,
tags,
type
FROM azure_stack.network_admin.vw_quotas
WHERE location = '{{ location }}'
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
FROM azure_stack.network_admin.quotas
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>quotas</code> resource.

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
INSERT INTO azure_stack.network_admin.quotas (
location,
resourceName,
subscriptionId,
properties,
tags
)
SELECT 
'{{ location }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: maxPublicIpsPerSubscription
          value: integer
        - name: maxVnetsPerSubscription
          value: integer
        - name: maxVirtualNetworkGatewaysPerSubscription
          value: integer
        - name: maxVirtualNetworkGatewayConnectionsPerSubscription
          value: integer
        - name: maxLoadBalancersPerSubscription
          value: integer
        - name: maxNicsPerSubscription
          value: integer
        - name: maxSecurityGroupsPerSubscription
          value: integer
        - name: migrationPhase
          value: []
        - name: provisioningState
          value: string
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>quotas</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.network_admin.quotas
WHERE location = '{{ location }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

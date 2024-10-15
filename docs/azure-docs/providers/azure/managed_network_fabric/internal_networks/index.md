---
title: internal_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - internal_networks
  - managed_network_fabric
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

Creates, updates, deletes, gets or lists a <code>internal_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>internal_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.internal_networks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_internal_networks', value: 'view', },
        { label: 'internal_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrative_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="bgp_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="connected_ipv4_subnets" /> | `text` | field from the `properties` object |
| <CopyableCode code="connected_ipv6_subnets" /> | `text` | field from the `properties` object |
| <CopyableCode code="egress_acl_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="export_route_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="export_route_policy_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="extension" /> | `text` | field from the `properties` object |
| <CopyableCode code="import_route_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="import_route_policy_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="ingress_acl_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="internalNetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_monitoring_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="l3IsolationDomainName" /> | `text` | field from the `properties` object |
| <CopyableCode code="mtu" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="static_route_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="vlan_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Internal Network Properties defines the properties of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="internalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Gets a InternalNetworks. |
| <CopyableCode code="list_by_l3_isolation_domain" /> | `SELECT` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Displays InternalNetworks list by resource group GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="internalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId, data__properties" /> | Creates InternalNetwork PUT method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="internalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Implements InternalNetworks DELETE method. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="internalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Updates a InternalNetworks. |

## `SELECT` examples

Displays InternalNetworks list by resource group GET method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_internal_networks', value: 'view', },
        { label: 'internal_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrative_state,
annotation,
bgp_configuration,
configuration_state,
connected_ipv4_subnets,
connected_ipv6_subnets,
egress_acl_id,
export_route_policy,
export_route_policy_id,
extension,
import_route_policy,
import_route_policy_id,
ingress_acl_id,
internalNetworkName,
is_monitoring_enabled,
l3IsolationDomainName,
mtu,
provisioning_state,
resourceGroupName,
static_route_configuration,
subscriptionId,
vlan_id
FROM azure.managed_network_fabric.vw_internal_networks
WHERE l3IsolationDomainName = '{{ l3IsolationDomainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.managed_network_fabric.internal_networks
WHERE l3IsolationDomainName = '{{ l3IsolationDomainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>internal_networks</code> resource.

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
INSERT INTO azure.managed_network_fabric.internal_networks (
internalNetworkName,
l3IsolationDomainName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ internalNetworkName }}',
'{{ l3IsolationDomainName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: annotation
          value: string
        - name: mtu
          value: integer
        - name: connectedIPv4Subnets
          value:
            - - name: annotation
                value: string
              - name: prefix
                value: string
        - name: connectedIPv6Subnets
          value:
            - - name: annotation
                value: string
              - name: prefix
                value: string
        - name: importRoutePolicyId
          value: []
        - name: importRoutePolicy
          value: []
        - name: exportRoutePolicy
          value: []
        - name: ingressAclId
          value: []
        - name: isMonitoringEnabled
          value: string
        - name: extension
          value: string
        - name: vlanId
          value: integer
        - name: bgpConfiguration
          value: object
        - name: staticRouteConfiguration
          value: string
        - name: configurationState
          value: []
        - name: provisioningState
          value: []
        - name: administrativeState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>internal_networks</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.internal_networks
SET 
properties = '{{ properties }}'
WHERE 
internalNetworkName = '{{ internalNetworkName }}'
AND l3IsolationDomainName = '{{ l3IsolationDomainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>internal_networks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.internal_networks
WHERE internalNetworkName = '{{ internalNetworkName }}'
AND l3IsolationDomainName = '{{ l3IsolationDomainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

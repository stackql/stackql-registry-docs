---
title: external_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - external_networks
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

Creates, updates, deletes, gets or lists a <code>external_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>external_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.external_networks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_external_networks', value: 'view', },
        { label: 'external_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrative_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="export_route_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="export_route_policy_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="externalNetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="import_route_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="import_route_policy_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="l3IsolationDomainName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_to_network_interconnect_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="option_a_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="option_b_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="peering_option" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | External Network Properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="externalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Implements ExternalNetworks GET method. |
| <CopyableCode code="list_by_l3_isolation_domain" /> | `SELECT` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Implements External Networks list by resource group GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="externalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId, data__properties" /> | Creates ExternalNetwork PUT method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="externalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Implements ExternalNetworks DELETE method. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="externalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId" /> | API to update certain properties of the ExternalNetworks resource. |

## `SELECT` examples

Implements External Networks list by resource group GET method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_external_networks', value: 'view', },
        { label: 'external_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrative_state,
annotation,
configuration_state,
export_route_policy,
export_route_policy_id,
externalNetworkName,
import_route_policy,
import_route_policy_id,
l3IsolationDomainName,
network_to_network_interconnect_id,
option_a_properties,
option_b_properties,
peering_option,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.managed_network_fabric.vw_external_networks
WHERE l3IsolationDomainName = '{{ l3IsolationDomainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.managed_network_fabric.external_networks
WHERE l3IsolationDomainName = '{{ l3IsolationDomainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>external_networks</code> resource.

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
INSERT INTO azure.managed_network_fabric.external_networks (
externalNetworkName,
l3IsolationDomainName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ externalNetworkName }}',
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
        - name: networkToNetworkInterconnectId
          value: []
        - name: importRoutePolicyId
          value: []
        - name: importRoutePolicy
          value: []
        - name: exportRoutePolicy
          value: []
        - name: peeringOption
          value: []
        - name: optionBProperties
          value:
            - name: importRouteTargets
              value:
                - string
            - name: exportRouteTargets
              value:
                - string
            - name: routeTargets
              value:
                - name: importIpv4RouteTargets
                  value:
                    - string
                - name: importIpv6RouteTargets
                  value:
                    - string
                - name: exportIpv4RouteTargets
                  value:
                    - string
                - name: exportIpv6RouteTargets
                  value:
                    - string
        - name: optionAProperties
          value: object
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

Updates a <code>external_networks</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.external_networks
SET 
properties = '{{ properties }}'
WHERE 
externalNetworkName = '{{ externalNetworkName }}'
AND l3IsolationDomainName = '{{ l3IsolationDomainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>external_networks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.external_networks
WHERE externalNetworkName = '{{ externalNetworkName }}'
AND l3IsolationDomainName = '{{ l3IsolationDomainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

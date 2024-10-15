---
title: network_to_network_interconnects
hide_title: false
hide_table_of_contents: false
keywords:
  - network_to_network_interconnects
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

Creates, updates, deletes, gets or lists a <code>network_to_network_interconnects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_to_network_interconnects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_to_network_interconnects" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_to_network_interconnects', value: 'view', },
        { label: 'network_to_network_interconnects', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrative_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="egress_acl_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="export_route_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="import_route_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="ingress_acl_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_management_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="layer2_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkFabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkToNetworkInterconnectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="nni_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="npb_static_route_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="option_b_layer3_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="use_optionb" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Configuration used to setup CE-PE connectivity. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkFabricName, networkToNetworkInterconnectName, resourceGroupName, subscriptionId" /> | Implements NetworkToNetworkInterconnects GET method. |
| <CopyableCode code="list_by_network_fabric" /> | `SELECT` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Implements Network To Network Interconnects list by Network Fabric GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkFabricName, networkToNetworkInterconnectName, resourceGroupName, subscriptionId, data__properties" /> | Configuration used to setup CE-PE connectivity PUT Method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkFabricName, networkToNetworkInterconnectName, resourceGroupName, subscriptionId" /> | Implements NetworkToNetworkInterconnects DELETE method. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="networkFabricName, networkToNetworkInterconnectName, resourceGroupName, subscriptionId" /> | Update certain properties of the Network To NetworkInterconnects resource. |
| <CopyableCode code="update_administrative_state" /> | `EXEC` | <CopyableCode code="networkFabricName, networkToNetworkInterconnectName, resourceGroupName, subscriptionId" /> | Updates the Admin State. |
| <CopyableCode code="update_npb_static_route_bfd_administrative_state" /> | `EXEC` | <CopyableCode code="networkFabricName, networkToNetworkInterconnectName, resourceGroupName, subscriptionId" /> | Updates the NPB Static Route BFD Administrative State. |

## `SELECT` examples

Implements Network To Network Interconnects list by Network Fabric GET method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_to_network_interconnects', value: 'view', },
        { label: 'network_to_network_interconnects', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrative_state,
configuration_state,
egress_acl_id,
export_route_policy,
import_route_policy,
ingress_acl_id,
is_management_type,
layer2_configuration,
networkFabricName,
networkToNetworkInterconnectName,
nni_type,
npb_static_route_configuration,
option_b_layer3_configuration,
provisioning_state,
resourceGroupName,
subscriptionId,
use_optionb
FROM azure.managed_network_fabric.vw_network_to_network_interconnects
WHERE networkFabricName = '{{ networkFabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.managed_network_fabric.network_to_network_interconnects
WHERE networkFabricName = '{{ networkFabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_to_network_interconnects</code> resource.

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
INSERT INTO azure.managed_network_fabric.network_to_network_interconnects (
networkFabricName,
networkToNetworkInterconnectName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ networkFabricName }}',
'{{ networkToNetworkInterconnectName }}',
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
        - name: nniType
          value: string
        - name: isManagementType
          value: string
        - name: useOptionB
          value: []
        - name: layer2Configuration
          value:
            - name: mtu
              value: integer
            - name: interfaces
              value:
                - []
        - name: optionBLayer3Configuration
          value: object
        - name: npbStaticRouteConfiguration
          value:
            - name: bfdConfiguration
              value:
                - name: administrativeState
                  value: string
                - name: intervalInMilliSeconds
                  value: integer
                - name: multiplier
                  value: integer
            - name: ipv4Routes
              value:
                - - name: prefix
                    value: string
                  - name: nextHop
                    value:
                      - string
            - name: ipv6Routes
              value:
                - - name: prefix
                    value: string
                  - name: nextHop
                    value:
                      - string
        - name: importRoutePolicy
          value:
            - name: importIpv4RoutePolicyId
              value: []
        - name: exportRoutePolicy
          value: []
        - name: egressAclId
          value: []
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

Updates a <code>network_to_network_interconnects</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.network_to_network_interconnects
SET 
properties = '{{ properties }}'
WHERE 
networkFabricName = '{{ networkFabricName }}'
AND networkToNetworkInterconnectName = '{{ networkToNetworkInterconnectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>network_to_network_interconnects</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.network_to_network_interconnects
WHERE networkFabricName = '{{ networkFabricName }}'
AND networkToNetworkInterconnectName = '{{ networkToNetworkInterconnectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

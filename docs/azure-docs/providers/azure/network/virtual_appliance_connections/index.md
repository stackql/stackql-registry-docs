---
title: virtual_appliance_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_appliance_connections
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

Creates, updates, deletes, gets or lists a <code>virtual_appliance_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_appliance_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_appliance_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_appliance_connections', value: 'view', },
        { label: 'virtual_appliance_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="asn" /> | `text` | field from the `properties` object |
| <CopyableCode code="bgp_peer_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_internet_security" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkVirtualApplianceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routing_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tunnel_identifier" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the NetworkVirtualApplianceConnection subresource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Retrieves the details of specified NVA connection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Lists NetworkVirtualApplianceConnections under the NVA. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectionName, networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Creates a connection to Network Virtual Appliance, if it doesn't exist else updates the existing NVA connection' |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionName, networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Deletes a NVA connection. |

## `SELECT` examples

Lists NetworkVirtualApplianceConnections under the NVA.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_appliance_connections', value: 'view', },
        { label: 'virtual_appliance_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
asn,
bgp_peer_address,
connectionName,
enable_internet_security,
networkVirtualApplianceName,
provisioning_state,
resourceGroupName,
routing_configuration,
subscriptionId,
tunnel_identifier
FROM azure.network.vw_virtual_appliance_connections
WHERE networkVirtualApplianceName = '{{ networkVirtualApplianceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties
FROM azure.network.virtual_appliance_connections
WHERE networkVirtualApplianceName = '{{ networkVirtualApplianceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_appliance_connections</code> resource.

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
INSERT INTO azure.network.virtual_appliance_connections (
connectionName,
networkVirtualApplianceName,
resourceGroupName,
subscriptionId,
properties,
name,
id
)
SELECT 
'{{ connectionName }}',
'{{ networkVirtualApplianceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ name }}',
'{{ id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: name
          value: string
        - name: provisioningState
          value: []
        - name: asn
          value: integer
        - name: tunnelIdentifier
          value: integer
        - name: bgpPeerAddress
          value:
            - string
        - name: enableInternetSecurity
          value: boolean
        - name: routingConfiguration
          value:
            - name: associatedRouteTable
              value:
                - name: id
                  value: string
            - name: propagatedRouteTables
              value:
                - name: labels
                  value:
                    - string
                - name: ids
                  value:
                    - - name: id
                        value: string
            - name: vnetRoutes
              value:
                - name: staticRoutesConfig
                  value:
                    - name: propagateStaticRoutes
                      value: boolean
                    - name: vnetLocalRouteOverrideCriteria
                      value: []
                - name: staticRoutes
                  value:
                    - - name: name
                        value: string
                      - name: addressPrefixes
                        value:
                          - string
                      - name: nextHopIpAddress
                        value: string
                - name: bgpConnections
                  value:
                    - - name: id
                        value: string
    - name: name
      value: string
    - name: id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>virtual_appliance_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.virtual_appliance_connections
WHERE connectionName = '{{ connectionName }}'
AND networkVirtualApplianceName = '{{ networkVirtualApplianceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

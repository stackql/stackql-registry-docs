---
title: logical_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - logical_networks
  - azure_stack_hci
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

Creates, updates, deletes, gets or lists a <code>logical_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logical_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.logical_networks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_logical_networks', value: 'view', },
        { label: 'logical_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dhcp_options" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="logicalNetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnets" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="vm_switch_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties under the logical network resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="logicalNetworkName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the logical networks in the specified resource group. Use the nextLink property in the response to get the next page of logical networks. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the logical networks in the specified subscription. Use the nextLink property in the response to get the next page of logical networks. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="logicalNetworkName, resourceGroupName, subscriptionId" /> | The operation to create or update a logical network. Please note some properties can be set only during logical network creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="logicalNetworkName, resourceGroupName, subscriptionId" /> | The operation to delete a logical network. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="logicalNetworkName, resourceGroupName, subscriptionId" /> | The operation to update a logical network. |

## `SELECT` examples

Lists all of the logical networks in the specified subscription. Use the nextLink property in the response to get the next page of logical networks.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_logical_networks', value: 'view', },
        { label: 'logical_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dhcp_options,
extended_location,
location,
logicalNetworkName,
provisioning_state,
resourceGroupName,
status,
subnets,
subscriptionId,
tags,
vm_switch_name
FROM azure_stack.azure_stack_hci.vw_logical_networks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure_stack.azure_stack_hci.logical_networks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>logical_networks</code> resource.

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
INSERT INTO azure_stack.azure_stack_hci.logical_networks (
logicalNetworkName,
resourceGroupName,
subscriptionId,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ logicalNetworkName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ extendedLocation }}',
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
        - name: dhcpOptions
          value:
            - name: dnsServers
              value:
                - string
        - name: subnets
          value:
            - - name: properties
                value:
                  - name: addressPrefix
                    value: string
                  - name: addressPrefixes
                    value:
                      - string
                  - name: ipAllocationMethod
                    value: string
                  - name: ipConfigurationReferences
                    value:
                      - - name: ID
                          value: string
                  - name: routeTable
                    value:
                      - name: etag
                        value: string
                      - name: name
                        value: string
                      - name: type
                        value: string
                      - name: properties
                        value:
                          - name: routes
                            value:
                              - - name: properties
                                  value:
                                    - name: addressPrefix
                                      value: string
                                    - name: nextHopIpAddress
                                      value: string
                                - name: name
                                  value: string
                  - name: ipPools
                    value:
                      - - name: name
                          value: string
                        - name: ipPoolType
                          value: string
                        - name: start
                          value: string
                        - name: end
                          value: string
                        - name: info
                          value:
                            - name: used
                              value: string
                            - name: available
                              value: string
                  - name: vlan
                    value: integer
              - name: name
                value: string
        - name: provisioningState
          value: string
        - name: vmSwitchName
          value: string
        - name: status
          value:
            - name: errorCode
              value: string
            - name: errorMessage
              value: string
            - name: provisioningStatus
              value:
                - name: operationId
                  value: string
                - name: status
                  value: string
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>logical_networks</code> resource.

```sql
/*+ update */
UPDATE azure_stack.azure_stack_hci.logical_networks
SET 
tags = '{{ tags }}'
WHERE 
logicalNetworkName = '{{ logicalNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>logical_networks</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack_hci.logical_networks
WHERE logicalNetworkName = '{{ logicalNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

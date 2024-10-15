---
title: network_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interfaces
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

Creates, updates, deletes, gets or lists a <code>network_interfaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.network_interfaces" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_interfaces', value: 'view', },
        { label: 'network_interfaces', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dns_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="mac_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkInterfaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties under the network interface resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId" /> | Gets a network interface |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the network interfaces in the specified resource group. Use the nextLink property in the response to get the next page of network interfaces. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the network interfaces in the specified subscription. Use the nextLink property in the response to get the next page of network interfaces. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId" /> | The operation to create or update a network interface. Please note some properties can be set only during network interface creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId" /> | The operation to delete a network interface. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId" /> | The operation to update a network interface. |

## `SELECT` examples

Lists all of the network interfaces in the specified subscription. Use the nextLink property in the response to get the next page of network interfaces.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_interfaces', value: 'view', },
        { label: 'network_interfaces', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dns_settings,
extended_location,
ip_configurations,
location,
mac_address,
networkInterfaceName,
provisioning_state,
resourceGroupName,
status,
subscriptionId,
tags
FROM azure_stack.azure_stack_hci.vw_network_interfaces
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
FROM azure_stack.azure_stack_hci.network_interfaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_interfaces</code> resource.

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
INSERT INTO azure_stack.azure_stack_hci.network_interfaces (
networkInterfaceName,
resourceGroupName,
subscriptionId,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ networkInterfaceName }}',
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
        - name: ipConfigurations
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: gateway
                    value: string
                  - name: prefixLength
                    value: string
                  - name: privateIPAddress
                    value: string
                  - name: subnet
                    value:
                      - name: id
                        value: string
        - name: macAddress
          value: string
        - name: dnsSettings
          value:
            - name: dnsServers
              value:
                - string
        - name: provisioningState
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

Updates a <code>network_interfaces</code> resource.

```sql
/*+ update */
UPDATE azure_stack.azure_stack_hci.network_interfaces
SET 
tags = '{{ tags }}'
WHERE 
networkInterfaceName = '{{ networkInterfaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>network_interfaces</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack_hci.network_interfaces
WHERE networkInterfaceName = '{{ networkInterfaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

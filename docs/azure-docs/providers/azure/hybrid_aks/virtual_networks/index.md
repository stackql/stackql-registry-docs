---
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
  - hybrid_aks
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

Creates, updates, deletes, gets or lists a <code>virtual_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_aks.virtual_networks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location pointing to the underlying infrastructure |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the virtual network resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the virtual networks in the specified resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the virtual networks in the specified subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName" /> | Creates or updates the virtual network resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName" /> | Deletes the specified virtual network resource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName" /> | Patches the virtual network resource |
| <CopyableCode code="retrieve" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName" /> | Gets the specified virtual network resource |

## `SELECT` examples

Lists the virtual networks in the specified subscription


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.hybrid_aks.virtual_networks
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_networks</code> resource.

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
INSERT INTO azure.hybrid_aks.virtual_networks (
resourceGroupName,
subscriptionId,
virtualNetworkName,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualNetworkName }}',
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
        - name: infraVnetProfile
          value:
            - name: hci
              value:
                - name: mocGroup
                  value: string
                - name: mocLocation
                  value: string
                - name: mocVnetName
                  value: string
        - name: vipPool
          value:
            - - name: endIP
                value: string
              - name: startIP
                value: string
        - name: vmipPool
          value:
            - - name: endIP
                value: string
              - name: startIP
                value: string
        - name: dnsServers
          value:
            - string
        - name: gateway
          value: string
        - name: ipAddressPrefix
          value: string
        - name: vlanID
          value: integer
        - name: provisioningState
          value: string
        - name: status
          value:
            - name: operationStatus
              value:
                - name: error
                  value:
                    - name: code
                      value: string
                    - name: message
                      value: string
                - name: operationId
                  value: string
                - name: status
                  value: string
    - name: extendedLocation
      value:
        - name: type
          value: string
        - name: name
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_networks</code> resource.

```sql
/*+ update */
UPDATE azure.hybrid_aks.virtual_networks
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkName = '{{ virtualNetworkName }}';
```

## `DELETE` example

Deletes the specified <code>virtual_networks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_aks.virtual_networks
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkName = '{{ virtualNetworkName }}';
```

---
title: private_endpoint_connection_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connection_proxies
  - device_update
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

Creates, updates, deletes, gets or lists a <code>private_endpoint_connection_proxies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_endpoint_connection_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.device_update.private_endpoint_connection_proxies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="eTag" /> | `string` | ETag from NRP. |
| <CopyableCode code="properties" /> | `object` | Private endpoint connection proxy object property bag. |
| <CopyableCode code="remotePrivateEndpoint" /> | `object` | Remote private endpoint details. |
| <CopyableCode code="status" /> | `string` | Operation status. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, privateEndpointConnectionProxyId, resourceGroupName, subscriptionId" /> | (INTERNAL - DO NOT USE) Get the specified private endpoint connection proxy associated with the device update account. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | (INTERNAL - DO NOT USE) List all private endpoint connection proxies in a device update account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, privateEndpointConnectionProxyId, resourceGroupName, subscriptionId" /> | (INTERNAL - DO NOT USE) Creates or updates the specified private endpoint connection proxy resource associated with the device update account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, privateEndpointConnectionProxyId, resourceGroupName, subscriptionId" /> | (INTERNAL - DO NOT USE) Deletes the specified private endpoint connection proxy associated with the device update account. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="accountName, privateEndpointConnectionProxyId, resourceGroupName, subscriptionId" /> | (INTERNAL - DO NOT USE) Validates a private endpoint connection proxy object. |

## `SELECT` examples

(INTERNAL - DO NOT USE) List all private endpoint connection proxies in a device update account.


```sql
SELECT
eTag,
properties,
remotePrivateEndpoint,
status
FROM azure.device_update.private_endpoint_connection_proxies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_endpoint_connection_proxies</code> resource.

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
INSERT INTO azure.device_update.private_endpoint_connection_proxies (
accountName,
privateEndpointConnectionProxyId,
resourceGroupName,
subscriptionId,
remotePrivateEndpoint,
status,
properties
)
SELECT 
'{{ accountName }}',
'{{ privateEndpointConnectionProxyId }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ remotePrivateEndpoint }}',
'{{ status }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: eTag
      value: string
    - name: remotePrivateEndpoint
      value:
        - name: id
          value: string
        - name: location
          value: string
        - name: immutableSubscriptionId
          value: string
        - name: immutableResourceId
          value: string
        - name: vnetTrafficTag
          value: string
        - name: manualPrivateLinkServiceConnections
          value:
            - - name: name
                value: string
              - name: groupIds
                value:
                  - string
              - name: requestMessage
                value: string
        - name: privateLinkServiceConnections
          value:
            - - name: name
                value: string
              - name: groupIds
                value:
                  - string
              - name: requestMessage
                value: string
        - name: privateLinkServiceProxies
          value:
            - - name: id
                value: string
              - name: remotePrivateLinkServiceConnectionState
                value:
                  - name: status
                    value: []
                  - name: description
                    value: string
                  - name: actionsRequired
                    value: string
              - name: remotePrivateEndpointConnection
                value: string
              - name: groupConnectivityInformation
                value:
                  - - name: groupId
                      value: string
                    - name: memberName
                      value: string
                    - name: customerVisibleFqdns
                      value:
                        - string
                    - name: internalFqdn
                      value: string
                    - name: redirectMapId
                      value: string
                    - name: privateLinkServiceArmRegion
                      value: string
        - name: connectionDetails
          value:
            - - name: id
                value: string
              - name: privateIpAddress
                value: string
              - name: linkIdentifier
                value: string
              - name: groupId
                value: string
              - name: memberName
                value: string
    - name: status
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>private_endpoint_connection_proxies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.device_update.private_endpoint_connection_proxies
WHERE accountName = '{{ accountName }}'
AND privateEndpointConnectionProxyId = '{{ privateEndpointConnectionProxyId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

---
title: connected_registries
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_registries
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>connected_registries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connected_registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.connected_registries" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connected_registries', value: 'view', },
        { label: 'connected_registries', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activation" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_token_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectedRegistryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_activity_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="logging" /> | `text` | field from the `properties` object |
| <CopyableCode code="login_server" /> | `text` | field from the `properties` object |
| <CopyableCode code="mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="notifications_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="parent" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a connected registry. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectedRegistryName, registryName, resourceGroupName, subscriptionId" /> | Gets the properties of the connected registry. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all connected registries for the specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="connectedRegistryName, registryName, resourceGroupName, subscriptionId" /> | Creates a connected registry for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectedRegistryName, registryName, resourceGroupName, subscriptionId" /> | Deletes a connected registry from a container registry. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="connectedRegistryName, registryName, resourceGroupName, subscriptionId" /> | Updates a connected registry with the specified parameters. |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="connectedRegistryName, registryName, resourceGroupName, subscriptionId" /> | Deactivates the connected registry instance. |

## `SELECT` examples

Lists all connected registries for the specified container registry.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connected_registries', value: 'view', },
        { label: 'connected_registries', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
activation,
client_token_ids,
connectedRegistryName,
connection_state,
last_activity_time,
logging,
login_server,
mode,
notifications_list,
parent,
provisioning_state,
registryName,
resourceGroupName,
status_details,
subscriptionId,
version
FROM azure.container_registry.vw_connected_registries
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.container_registry.connected_registries
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connected_registries</code> resource.

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
INSERT INTO azure.container_registry.connected_registries (
connectedRegistryName,
registryName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ connectedRegistryName }}',
'{{ registryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: provisioningState
          value: string
        - name: mode
          value: string
        - name: version
          value: string
        - name: connectionState
          value: string
        - name: lastActivityTime
          value: string
        - name: activation
          value:
            - name: status
              value: string
        - name: parent
          value:
            - name: id
              value: string
            - name: syncProperties
              value:
                - name: tokenId
                  value: string
                - name: schedule
                  value: string
                - name: syncWindow
                  value: string
                - name: messageTtl
                  value: string
                - name: lastSyncTime
                  value: string
                - name: gatewayEndpoint
                  value: string
        - name: clientTokenIds
          value:
            - string
        - name: loginServer
          value:
            - name: host
              value: string
            - name: tls
              value:
                - name: status
                  value: string
                - name: certificate
                  value:
                    - name: type
                      value: string
                    - name: location
                      value: string
        - name: logging
          value:
            - name: logLevel
              value: string
            - name: auditLogStatus
              value: string
        - name: statusDetails
          value:
            - - name: type
                value: string
              - name: code
                value: string
              - name: description
                value: string
              - name: timestamp
                value: string
              - name: correlationId
                value: string
        - name: notificationsList
          value:
            - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>connected_registries</code> resource.

```sql
/*+ update */
UPDATE azure.container_registry.connected_registries
SET 
properties = '{{ properties }}'
WHERE 
connectedRegistryName = '{{ connectedRegistryName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>connected_registries</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_registry.connected_registries
WHERE connectedRegistryName = '{{ connectedRegistryName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

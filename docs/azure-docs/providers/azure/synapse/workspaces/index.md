---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - synapse
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

Creates, updates, deletes, gets or lists a <code>workspaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.workspaces" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspaces', value: 'view', },
        { label: 'workspaces', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="adla_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_ad_only_authentication" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectivity_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="csp_workspace_admin_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_data_lake_storage" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="extra_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | The workspace managed identity |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="managed_resource_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_virtual_network" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_virtual_network_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="purview_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="sql_administrator_login" /> | `text` | field from the `properties` object |
| <CopyableCode code="sql_administrator_login_password" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="trusted_service_bypass_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspace_repository_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspace_uid" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | The workspace managed identity |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Workspace properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets a workspace |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns a list of workspaces in a subscription |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns a list of workspaces in a resource group |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates a workspace |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Deletes a workspace |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Updates a workspace |

## `SELECT` examples

Returns a list of workspaces in a subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspaces', value: 'view', },
        { label: 'workspaces', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
adla_resource_id,
azure_ad_only_authentication,
connectivity_endpoints,
csp_workspace_admin_properties,
default_data_lake_storage,
encryption,
extra_properties,
identity,
location,
managed_resource_group_name,
managed_virtual_network,
managed_virtual_network_settings,
private_endpoint_connections,
provisioning_state,
public_network_access,
purview_configuration,
resourceGroupName,
settings,
sql_administrator_login,
sql_administrator_login_password,
subscriptionId,
tags,
trusted_service_bypass_enabled,
virtual_network_profile,
workspaceName,
workspace_repository_configuration,
workspace_uid
FROM azure.synapse.vw_workspaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.synapse.workspaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspaces</code> resource.

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
INSERT INTO azure.synapse.workspaces (
resourceGroupName,
subscriptionId,
workspaceName,
tags,
location,
properties,
identity
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: defaultDataLakeStorage
          value:
            - name: accountUrl
              value: string
            - name: filesystem
              value: string
            - name: resourceId
              value: string
            - name: createManagedPrivateEndpoint
              value: boolean
        - name: sqlAdministratorLoginPassword
          value: string
        - name: managedResourceGroupName
          value: string
        - name: provisioningState
          value: string
        - name: sqlAdministratorLogin
          value: string
        - name: virtualNetworkProfile
          value:
            - name: computeSubnetId
              value: string
        - name: connectivityEndpoints
          value: object
        - name: managedVirtualNetwork
          value: string
        - name: privateEndpointConnections
          value:
            - - name: properties
                value:
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: string
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: provisioningState
                    value: string
        - name: encryption
          value:
            - name: doubleEncryptionEnabled
              value: boolean
            - name: cmk
              value:
                - name: status
                  value: string
                - name: key
                  value:
                    - name: name
                      value: string
                    - name: keyVaultUrl
                      value: string
                - name: kekIdentity
                  value:
                    - name: userAssignedIdentity
                      value: string
                    - name: useSystemAssignedIdentity
                      value: string
        - name: workspaceUID
          value: string
        - name: extraProperties
          value: object
        - name: managedVirtualNetworkSettings
          value:
            - name: preventDataExfiltration
              value: boolean
            - name: linkedAccessCheckOnTargetResource
              value: boolean
            - name: allowedAadTenantIdsForLinking
              value:
                - string
        - name: workspaceRepositoryConfiguration
          value:
            - name: type
              value: string
            - name: hostName
              value: string
            - name: accountName
              value: string
            - name: projectName
              value: string
            - name: repositoryName
              value: string
            - name: collaborationBranch
              value: string
            - name: rootFolder
              value: string
            - name: lastCommitId
              value: string
            - name: tenantId
              value: string
        - name: purviewConfiguration
          value:
            - name: purviewResourceId
              value: string
        - name: adlaResourceId
          value: string
        - name: publicNetworkAccess
          value: string
        - name: cspWorkspaceAdminProperties
          value:
            - name: initialWorkspaceAdminObjectId
              value: string
        - name: settings
          value: object
        - name: azureADOnlyAuthentication
          value: boolean
        - name: trustedServiceBypassEnabled
          value: boolean
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workspaces</code> resource.

```sql
/*+ update */
UPDATE azure.synapse.workspaces
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>workspaces</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.workspaces
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

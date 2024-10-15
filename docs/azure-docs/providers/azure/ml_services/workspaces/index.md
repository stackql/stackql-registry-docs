---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - ml_services
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.workspaces" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_public_access_when_behind_vnet" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_role_assignment_on_rg" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_insights" /> | `text` | field from the `properties` object |
| <CopyableCode code="associated_workspaces" /> | `text` | field from the `properties` object |
| <CopyableCode code="container_registries" /> | `text` | field from the `properties` object |
| <CopyableCode code="container_registry" /> | `text` | field from the `properties` object |
| <CopyableCode code="discovery_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_data_isolation" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_service_side_cmk_encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_simplified_cmk" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_software_bill_of_materials" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="existing_workspaces" /> | `text` | field from the `properties` object |
| <CopyableCode code="feature_store_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="hbi_workspace" /> | `text` | field from the `properties` object |
| <CopyableCode code="hub_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="image_build_compute" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_allowlist" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vaults" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_network" /> | `text` | field from the `properties` object |
| <CopyableCode code="ml_flow_tracking_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="notebook_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_user_assigned_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverless_compute_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_managed_resources_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_provisioned_resource_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="shared_private_link_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="soft_delete_retention_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_accounts" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_hns_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_datastores_auth_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="v1_legacy_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspace_hub_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspace_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="location" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | The properties of a machine learning workspace. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName, data__properties" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="diagnose" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="prepare_notebook" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="resync_keys" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |

## `SELECT` examples



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
id,
name,
description,
allow_public_access_when_behind_vnet,
allow_role_assignment_on_rg,
application_insights,
associated_workspaces,
container_registries,
container_registry,
discovery_url,
enable_data_isolation,
enable_service_side_cmk_encryption,
enable_simplified_cmk,
enable_software_bill_of_materials,
encryption,
existing_workspaces,
feature_store_settings,
friendly_name,
hbi_workspace,
hub_resource_id,
identity,
image_build_compute,
ip_allowlist,
key_vault,
key_vaults,
kind,
location,
managed_network,
ml_flow_tracking_uri,
notebook_info,
primary_user_assigned_identity,
private_endpoint_connections,
private_link_count,
provisioning_state,
public_network_access,
resourceGroupName,
serverless_compute_settings,
service_managed_resources_settings,
service_provisioned_resource_group,
shared_private_link_resources,
sku,
soft_delete_retention_in_days,
storage_account,
storage_accounts,
storage_hns_enabled,
subscriptionId,
system_data,
system_datastores_auth_mode,
tags,
tenant_id,
type,
v1_legacy_mode,
workspaceName,
workspace_hub_config,
workspace_id
FROM azure.ml_services.vw_workspaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
kind,
location,
properties,
sku,
systemData,
tags,
type
FROM azure.ml_services.workspaces
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
INSERT INTO azure.ml_services.workspaces (
resourceGroupName,
subscriptionId,
workspaceName,
data__properties,
identity,
kind,
location,
properties,
sku,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__properties }}',
'{{ identity }}',
'{{ kind }}',
'{{ location }}',
'{{ properties }}',
'{{ sku }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: kind
      value: string
    - name: location
      value: string
    - name: properties
      value:
        - name: allowPublicAccessWhenBehindVnet
          value: boolean
        - name: allowRoleAssignmentOnRG
          value: boolean
        - name: applicationInsights
          value: string
        - name: associatedWorkspaces
          value:
            - string
        - name: containerRegistries
          value:
            - string
        - name: containerRegistry
          value: string
        - name: description
          value: string
        - name: discoveryUrl
          value: string
        - name: enableDataIsolation
          value: boolean
        - name: enableServiceSideCMKEncryption
          value: boolean
        - name: enableSimplifiedCmk
          value: boolean
        - name: enableSoftwareBillOfMaterials
          value: boolean
        - name: encryption
          value:
            - name: cosmosDbResourceId
              value: string
            - name: identity
              value:
                - name: userAssignedIdentity
                  value: string
            - name: keyVaultProperties
              value:
                - name: identityClientId
                  value: string
                - name: keyIdentifier
                  value: string
                - name: keyVaultArmId
                  value: string
            - name: searchAccountResourceId
              value: string
            - name: status
              value: []
            - name: storageAccountResourceId
              value: string
        - name: existingWorkspaces
          value:
            - string
        - name: featureStoreSettings
          value:
            - name: computeRuntime
              value:
                - name: sparkRuntimeVersion
                  value: string
            - name: offlineStoreConnectionName
              value: string
            - name: onlineStoreConnectionName
              value: string
        - name: friendlyName
          value: string
        - name: hbiWorkspace
          value: boolean
        - name: hubResourceId
          value: string
        - name: imageBuildCompute
          value: string
        - name: ipAllowlist
          value:
            - string
        - name: keyVault
          value: string
        - name: keyVaults
          value:
            - string
        - name: managedNetwork
          value:
            - name: isolationMode
              value: []
            - name: networkId
              value: string
            - name: outboundRules
              value: object
            - name: status
              value:
                - name: sparkReady
                  value: boolean
                - name: status
                  value: []
            - name: changeableIsolationModes
              value:
                - []
        - name: mlFlowTrackingUri
          value: string
        - name: notebookInfo
          value:
            - name: fqdn
              value: string
            - name: isPrivateLinkEnabled
              value: boolean
            - name: notebookPreparationError
              value:
                - name: errorMessage
                  value: string
                - name: statusCode
                  value: integer
            - name: resourceId
              value: string
        - name: primaryUserAssignedIdentity
          value: string
        - name: privateEndpointConnections
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: location
                value: string
              - name: properties
                value:
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                      - name: subnetArmId
                        value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: actionsRequired
                        value: string
                      - name: description
                        value: string
                      - name: status
                        value: []
                  - name: provisioningState
                    value: []
              - name: sku
                value:
                  - name: name
                    value: string
                  - name: tier
                    value: []
                  - name: size
                    value: string
                  - name: family
                    value: string
                  - name: capacity
                    value: integer
              - name: tags
                value: object
        - name: privateLinkCount
          value: integer
        - name: provisioningState
          value: []
        - name: publicNetworkAccess
          value: []
        - name: serverlessComputeSettings
          value:
            - name: serverlessComputeCustomSubnet
              value: string
            - name: serverlessComputeNoPublicIP
              value: boolean
        - name: serviceManagedResourcesSettings
          value:
            - name: cosmosDb
              value:
                - name: collectionsThroughput
                  value: integer
        - name: serviceProvisionedResourceGroup
          value: string
        - name: sharedPrivateLinkResources
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: groupId
                    value: string
                  - name: privateLinkResourceId
                    value: string
                  - name: requestMessage
                    value: string
        - name: softDeleteRetentionInDays
          value: integer
        - name: storageAccount
          value: string
        - name: storageAccounts
          value:
            - string
        - name: storageHnsEnabled
          value: boolean
        - name: systemDatastoresAuthMode
          value: string
        - name: tenantId
          value: string
        - name: v1LegacyMode
          value: boolean
        - name: workspaceHubConfig
          value:
            - name: additionalWorkspaceStorageAccounts
              value:
                - string
            - name: defaultWorkspaceResourceGroup
              value: string
        - name: workspaceId
          value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workspaces</code> resource.

```sql
/*+ update */
UPDATE azure.ml_services.workspaces
SET 
identity = '{{ identity }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>workspaces</code> resource.

```sql
/*+ delete */
DELETE FROM azure.ml_services.workspaces
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

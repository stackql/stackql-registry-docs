---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - databricks
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.databricks.workspaces" /></td></tr>
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
| <CopyableCode code="access_connector" /> | `text` | field from the `properties` object |
| <CopyableCode code="authorizations" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_catalog" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_storage_firewall" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_encryption_set_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="enhanced_security_compliance" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_uc_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="managed_disk_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_resource_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="required_nsg_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | SKU for the resource. |
| <CopyableCode code="storage_account_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="ui_definition_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspace_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspace_url" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The workspace properties. |
| <CopyableCode code="sku" /> | `object` | SKU for the resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets the workspace. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the workspaces within a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the workspaces within a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName, data__properties" /> | Creates a new workspace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Deletes the workspace. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Updates a workspace. |

## `SELECT` examples

Gets all the workspaces within a subscription.

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
access_connector,
authorizations,
created_by,
created_date_time,
default_catalog,
default_storage_firewall,
disk_encryption_set_id,
encryption,
enhanced_security_compliance,
is_uc_enabled,
location,
managed_disk_identity,
managed_resource_group_id,
parameters,
private_endpoint_connections,
provisioning_state,
public_network_access,
required_nsg_rules,
resourceGroupName,
sku,
storage_account_identity,
subscriptionId,
system_data,
tags,
ui_definition_uri,
updated_by,
workspaceName,
workspace_id,
workspace_url
FROM azure_isv.databricks.vw_workspaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
systemData,
tags
FROM azure_isv.databricks.workspaces
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
INSERT INTO azure_isv.databricks.workspaces (
resourceGroupName,
subscriptionId,
workspaceName,
data__properties,
properties,
sku,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ sku }}',
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
        - name: managedResourceGroupId
          value: string
        - name: parameters
          value:
            - name: amlWorkspaceId
              value:
                - name: type
                  value: []
                - name: value
                  value: string
            - name: enableNoPublicIp
              value:
                - name: value
                  value: boolean
            - name: prepareEncryption
              value:
                - name: value
                  value: boolean
            - name: encryption
              value:
                - name: value
                  value:
                    - name: keySource
                      value: string
                    - name: KeyName
                      value: string
                    - name: keyversion
                      value: string
                    - name: keyvaulturi
                      value: string
            - name: resourceTags
              value:
                - name: value
                  value: object
        - name: provisioningState
          value: []
        - name: uiDefinitionUri
          value: string
        - name: authorizations
          value:
            - - name: principalId
                value: string
              - name: roleDefinitionId
                value: string
        - name: createdBy
          value:
            - name: oid
              value: string
            - name: puid
              value: string
            - name: applicationId
              value: string
        - name: createdDateTime
          value: []
        - name: workspaceId
          value: string
        - name: workspaceUrl
          value: string
        - name: storageAccountIdentity
          value:
            - name: principalId
              value: string
            - name: tenantId
              value: string
            - name: type
              value: string
        - name: diskEncryptionSetId
          value: string
        - name: encryption
          value:
            - name: entities
              value:
                - name: managedServices
                  value:
                    - name: keySource
                      value: string
                    - name: keyVaultProperties
                      value: string
                - name: managedDisk
                  value:
                    - name: keySource
                      value: string
                    - name: keyVaultProperties
                      value:
                        - name: keyVaultUri
                          value: string
                        - name: keyName
                          value: string
                        - name: keyVersion
                          value: string
                    - name: rotationToLatestKeyVersionEnabled
                      value: boolean
        - name: enhancedSecurityCompliance
          value:
            - name: automaticClusterUpdate
              value:
                - name: value
                  value: string
            - name: complianceSecurityProfile
              value:
                - name: complianceStandards
                  value:
                    - []
                - name: value
                  value: string
            - name: enhancedSecurityMonitoring
              value:
                - name: value
                  value: string
        - name: privateEndpointConnections
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: properties
                value:
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: groupIds
                    value:
                      - string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: string
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: provisioningState
                    value: []
        - name: publicNetworkAccess
          value: string
        - name: requiredNsgRules
          value: string
        - name: defaultCatalog
          value:
            - name: initialType
              value: string
            - name: initialName
              value: string
        - name: isUcEnabled
          value: boolean
        - name: accessConnector
          value:
            - name: id
              value: string
            - name: identityType
              value: string
            - name: userAssignedIdentityId
              value: string
        - name: defaultStorageFirewall
          value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
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
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workspaces</code> resource.

```sql
/*+ update */
UPDATE azure_isv.databricks.workspaces
SET 
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
DELETE FROM azure_isv.databricks.workspaces
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

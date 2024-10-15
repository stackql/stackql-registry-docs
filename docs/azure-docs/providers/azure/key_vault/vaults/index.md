---
title: vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - vaults
  - key_vault
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

Creates, updates, deletes, gets or lists a <code>vaults</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vaults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.vaults" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vaults', value: 'view', },
        { label: 'vaults', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified identifier of the key vault resource. |
| <CopyableCode code="name" /> | `text` | Name of the key vault resource. |
| <CopyableCode code="access_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_purge_protection" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_rbac_authorization" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_soft_delete" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_for_deployment" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_for_disk_encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_for_template_deployment" /> | `text` | field from the `properties` object |
| <CopyableCode code="hsm_pool_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Azure location of the key vault resource. |
| <CopyableCode code="network_acls" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="soft_delete_retention_in_days" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Tags assigned to the key vault resource. |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type of the key vault resource. |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vault_uri" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier of the key vault resource. |
| <CopyableCode code="name" /> | `string` | Name of the key vault resource. |
| <CopyableCode code="location" /> | `string` | Azure location of the key vault resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the vault |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the key vault resource. |
| <CopyableCode code="tags" /> | `object` | Tags assigned to the key vault resource. |
| <CopyableCode code="type" /> | `string` | Resource type of the key vault resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Gets the specified Azure key vault. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="$filter, subscriptionId" /> | The List operation gets information about the vaults associated with the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The List operation gets information about the vaults associated with the subscription and within the specified resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The List operation gets information about the vaults associated with the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName, data__location, data__properties" /> | Create or update a key vault in the specified subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Deletes the specified Azure key vault. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Update a key vault in the specified subscription. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Checks that the vault name is valid and is not already in use. |
| <CopyableCode code="purge_deleted" /> | `EXEC` | <CopyableCode code="location, subscriptionId, vaultName" /> | Permanently deletes the specified vault. aka Purges the deleted Azure key vault. |

## `SELECT` examples

The List operation gets information about the vaults associated with the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vaults', value: 'view', },
        { label: 'vaults', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
access_policies,
create_mode,
enable_purge_protection,
enable_rbac_authorization,
enable_soft_delete,
enabled_for_deployment,
enabled_for_disk_encryption,
enabled_for_template_deployment,
hsm_pool_resource_id,
location,
network_acls,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
sku,
soft_delete_retention_in_days,
subscriptionId,
system_data,
tags,
tenant_id,
type,
vaultName,
vault_uri
FROM azure.key_vault.vw_vaults
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
systemData,
tags,
type
FROM azure.key_vault.vaults
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vaults</code> resource.

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
INSERT INTO azure.key_vault.vaults (
resourceGroupName,
subscriptionId,
vaultName,
data__location,
data__properties,
location,
tags,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vaultName }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: tenantId
          value: string
        - name: sku
          value:
            - name: family
              value: string
            - name: name
              value: string
        - name: accessPolicies
          value:
            - - name: tenantId
                value: string
              - name: objectId
                value: string
              - name: applicationId
                value: string
              - name: permissions
                value:
                  - name: keys
                    value:
                      - string
                  - name: secrets
                    value:
                      - string
                  - name: certificates
                    value:
                      - string
                  - name: storage
                    value:
                      - string
        - name: vaultUri
          value: string
        - name: hsmPoolResourceId
          value: string
        - name: enabledForDeployment
          value: boolean
        - name: enabledForDiskEncryption
          value: boolean
        - name: enabledForTemplateDeployment
          value: boolean
        - name: enableSoftDelete
          value: boolean
        - name: softDeleteRetentionInDays
          value: integer
        - name: enableRbacAuthorization
          value: boolean
        - name: createMode
          value: string
        - name: enablePurgeProtection
          value: boolean
        - name: networkAcls
          value:
            - name: bypass
              value: string
            - name: defaultAction
              value: string
            - name: ipRules
              value:
                - - name: value
                    value: string
            - name: virtualNetworkRules
              value:
                - - name: id
                    value: string
                  - name: ignoreMissingVnetServiceEndpoint
                    value: boolean
        - name: provisioningState
          value: string
        - name: privateEndpointConnections
          value:
            - - name: id
                value: string
              - name: etag
                value: string
              - name: properties
                value:
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: []
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: provisioningState
                    value: []
        - name: publicNetworkAccess
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>vaults</code> resource.

```sql
/*+ update */
UPDATE azure.key_vault.vaults
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```

## `DELETE` example

Deletes the specified <code>vaults</code> resource.

```sql
/*+ delete */
DELETE FROM azure.key_vault.vaults
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```

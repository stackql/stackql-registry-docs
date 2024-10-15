---
title: vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - vaults
  - recovery_services
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services.vaults" /></td></tr>
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
| <CopyableCode code="backup_storage_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="bcdr_security_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="monitoring_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="move_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="move_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_state_for_backup" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_state_for_site_recovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="redundancy_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guard_operation_requests" /> | `text` | field from the `properties` object |
| <CopyableCode code="restore_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="secure_score" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="upgrade_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the vault. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Get the Vault details. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieve a list of Vaults. |
| <CopyableCode code="list_by_subscription_id" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Fetches all the resources of the specified type in the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Creates or updates a Recovery Services vault. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Deletes a vault. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Updates the vault. |

## `SELECT` examples

Fetches all the resources of the specified type in the subscription.

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
backup_storage_version,
bcdr_security_level,
encryption,
identity,
location,
monitoring_settings,
move_details,
move_state,
private_endpoint_connections,
private_endpoint_state_for_backup,
private_endpoint_state_for_site_recovery,
provisioning_state,
public_network_access,
redundancy_settings,
resourceGroupName,
resource_guard_operation_requests,
restore_settings,
secure_score,
security_settings,
sku,
subscriptionId,
system_data,
tags,
upgrade_details,
vaultName
FROM azure.recovery_services.vw_vaults
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
sku,
systemData,
tags
FROM azure.recovery_services.vaults
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
INSERT INTO azure.recovery_services.vaults (
resourceGroupName,
subscriptionId,
vaultName,
tags,
location,
identity,
properties,
sku,
systemData
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vaultName }}',
'{{ tags }}',
'{{ location }}',
'{{ identity }}',
'{{ properties }}',
'{{ sku }}',
'{{ systemData }}'
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
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: upgradeDetails
          value:
            - name: operationId
              value: string
            - name: startTimeUtc
              value: string
            - name: lastUpdatedTimeUtc
              value: string
            - name: endTimeUtc
              value: string
            - name: status
              value: string
            - name: message
              value: string
            - name: triggerType
              value: string
            - name: upgradedResourceId
              value: string
            - name: previousResourceId
              value: string
        - name: privateEndpointConnections
          value:
            - - name: id
                value: string
              - name: properties
                value:
                  - name: provisioningState
                    value: string
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
                  - name: groupIds
                    value:
                      - string
              - name: name
                value: string
              - name: type
                value: string
              - name: location
                value: string
        - name: privateEndpointStateForBackup
          value: string
        - name: privateEndpointStateForSiteRecovery
          value: string
        - name: encryption
          value:
            - name: keyVaultProperties
              value:
                - name: keyUri
                  value: string
            - name: kekIdentity
              value:
                - name: useSystemAssignedIdentity
                  value: boolean
                - name: userAssignedIdentity
                  value: string
            - name: infrastructureEncryption
              value: string
        - name: moveDetails
          value:
            - name: operationId
              value: string
            - name: startTimeUtc
              value: string
            - name: completionTimeUtc
              value: string
            - name: sourceResourceId
              value: string
            - name: targetResourceId
              value: string
        - name: moveState
          value: string
        - name: backupStorageVersion
          value: string
        - name: publicNetworkAccess
          value: string
        - name: monitoringSettings
          value:
            - name: azureMonitorAlertSettings
              value:
                - name: alertsForAllJobFailures
                  value: string
                - name: alertsForAllReplicationIssues
                  value: string
                - name: alertsForAllFailoverIssues
                  value: string
            - name: classicAlertSettings
              value:
                - name: alertsForCriticalOperations
                  value: string
                - name: emailNotificationsForSiteRecovery
                  value: string
        - name: restoreSettings
          value:
            - name: crossSubscriptionRestoreSettings
              value:
                - name: crossSubscriptionRestoreState
                  value: string
        - name: redundancySettings
          value:
            - name: standardTierStorageRedundancy
              value: string
            - name: crossRegionRestore
              value: string
        - name: securitySettings
          value:
            - name: immutabilitySettings
              value:
                - name: state
                  value: string
            - name: softDeleteSettings
              value:
                - name: softDeleteState
                  value: string
                - name: softDeleteRetentionPeriodInDays
                  value: integer
                - name: enhancedSecurityState
                  value: string
            - name: multiUserAuthorization
              value: []
        - name: secureScore
          value: string
        - name: bcdrSecurityLevel
          value: string
        - name: resourceGuardOperationRequests
          value:
            - string
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>vaults</code> resource.

```sql
/*+ update */
UPDATE azure.recovery_services.vaults
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
identity = '{{ identity }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```

## `DELETE` example

Deletes the specified <code>vaults</code> resource.

```sql
/*+ delete */
DELETE FROM azure.recovery_services.vaults
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```

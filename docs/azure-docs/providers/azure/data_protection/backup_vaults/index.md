---
title: backup_vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_vaults
  - data_protection
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

Creates, updates, deletes, gets or lists a <code>backup_vaults</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_vaults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.backup_vaults" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_vaults', value: 'view', },
        { label: 'backup_vaults', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="bcdr_security_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="feature_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity details |
| <CopyableCode code="is_vault_protected_by_resource_guard" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitoring_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="replicated_regions" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guard_operation_requests" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_move_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_move_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="secure_score" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity details |
| <CopyableCode code="properties" /> | `object` | Backup Vault |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Returns a resource belonging to a resource group. |
| <CopyableCode code="get_in_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns resource collection belonging to a resource group. |
| <CopyableCode code="get_in_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns resource collection belonging to a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName, data__properties" /> | Creates or updates a BackupVault resource belonging to a resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Deletes a BackupVault resource from the resource group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Updates a BackupVault resource belonging to a resource group. For example, updating tags for a resource. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples

Returns resource collection belonging to a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_vaults', value: 'view', },
        { label: 'backup_vaults', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
bcdr_security_level,
feature_settings,
identity,
is_vault_protected_by_resource_guard,
monitoring_settings,
provisioning_state,
replicated_regions,
resourceGroupName,
resource_guard_operation_requests,
resource_move_details,
resource_move_state,
secure_score,
security_settings,
storage_settings,
subscriptionId,
vaultName
FROM azure.data_protection.vw_backup_vaults
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
properties
FROM azure.data_protection.backup_vaults
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backup_vaults</code> resource.

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
INSERT INTO azure.data_protection.backup_vaults (
resourceGroupName,
subscriptionId,
vaultName,
data__properties,
identity,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vaultName }}',
'{{ data__properties }}',
'{{ identity }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
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
        - name: monitoringSettings
          value:
            - name: azureMonitorAlertSettings
              value:
                - name: alertsForAllJobFailures
                  value: string
        - name: provisioningState
          value: string
        - name: resourceMoveState
          value: string
        - name: resourceMoveDetails
          value:
            - name: operationId
              value: string
            - name: startTimeUtc
              value: string
            - name: completionTimeUtc
              value: string
            - name: sourceResourcePath
              value: string
            - name: targetResourcePath
              value: string
        - name: securitySettings
          value:
            - name: softDeleteSettings
              value:
                - name: state
                  value: string
                - name: retentionDurationInDays
                  value: number
            - name: immutabilitySettings
              value:
                - name: state
                  value: string
            - name: encryptionSettings
              value:
                - name: state
                  value: string
                - name: keyVaultProperties
                  value:
                    - name: keyUri
                      value: string
                - name: kekIdentity
                  value:
                    - name: identityType
                      value: string
                    - name: identityId
                      value: string
                - name: infrastructureEncryption
                  value: string
        - name: storageSettings
          value:
            - - name: datastoreType
                value: string
              - name: type
                value: string
        - name: isVaultProtectedByResourceGuard
          value: boolean
        - name: featureSettings
          value:
            - name: crossSubscriptionRestoreSettings
              value:
                - name: state
                  value: string
            - name: crossRegionRestoreSettings
              value:
                - name: state
                  value: string
        - name: secureScore
          value: string
        - name: bcdrSecurityLevel
          value: string
        - name: resourceGuardOperationRequests
          value:
            - string
        - name: replicatedRegions
          value:
            - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>backup_vaults</code> resource.

```sql
/*+ update */
UPDATE azure.data_protection.backup_vaults
SET 
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```

## `DELETE` example

Deletes the specified <code>backup_vaults</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_protection.backup_vaults
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```

---
title: backup_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_instances
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

Creates, updates, deletes, gets or lists a <code>backup_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.backup_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_instances', value: 'view', },
        { label: 'backup_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Proxy Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `text` | Proxy Resource name associated with the resource. |
| <CopyableCode code="backupInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_protection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_source_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_source_set_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="datasource_auth_credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_error_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guard_operation_requests" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Proxy Resource tags. |
| <CopyableCode code="type" /> | `text` | Proxy Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| <CopyableCode code="validation_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Proxy Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `string` | Proxy Resource name associated with the resource. |
| <CopyableCode code="properties" /> | `object` | Backup Instance |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Proxy Resource tags. |
| <CopyableCode code="type" /> | `string` | Proxy Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | Gets a backup instance with name in a backup vault |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Gets a backup instances belonging to a backup vault |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | Create or update a backup instance in a backup vault |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | Delete a backup instance in a backup vault |
| <CopyableCode code="adhoc_backup" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName, data__backupRuleOptions" /> | Trigger adhoc backup  |
| <CopyableCode code="resume_backups" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | This operation will resume backups for backup instance |
| <CopyableCode code="resume_protection" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | This operation will resume protection for a stopped backup instance |
| <CopyableCode code="stop_protection" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | This operation will stop protection of a backup instance and data will be held forever |
| <CopyableCode code="suspend_backups" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | This operation will stop backup for a backup instance and retains the backup data as per the policy (except latest Recovery point, which will be retained forever) |
| <CopyableCode code="sync_backup_instance" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | Sync backup instance again in case of failure
This action will retry last failed operation and will bring backup instance to valid state |
| <CopyableCode code="trigger_cross_region_restore" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId, data__crossRegionRestoreDetails, data__restoreRequestObject" /> | Triggers Cross Region Restore for BackupInstance. |
| <CopyableCode code="trigger_rehydrate" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName, data__recoveryPointId, data__rehydrationRetentionDuration" /> | rehydrate recovery point for restore for a BackupInstance |
| <CopyableCode code="trigger_restore" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName, data__objectType, data__restoreTargetInfo, data__sourceDataStoreType" /> | Triggers restore for a BackupInstance |
| <CopyableCode code="validate_cross_region_restore" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId, data__crossRegionRestoreDetails, data__restoreRequestObject" /> | Validates whether Cross Region Restore can be triggered for DataSource. |
| <CopyableCode code="validate_for_backup" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName, data__backupInstance" /> | Validate whether adhoc backup will be successful or not |
| <CopyableCode code="validate_for_restore" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName, data__restoreRequestObject" /> | Validates if Restore can be triggered for a DataSource |

## `SELECT` examples

Gets a backup instances belonging to a backup vault

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backup_instances', value: 'view', },
        { label: 'backup_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backupInstanceName,
current_protection_state,
data_source_info,
data_source_set_info,
datasource_auth_credentials,
friendly_name,
identity_details,
object_type,
policy_info,
protection_error_details,
protection_status,
provisioning_state,
resourceGroupName,
resource_guard_operation_requests,
subscriptionId,
system_data,
tags,
type,
validation_type,
vaultName
FROM azure.data_protection.vw_backup_instances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
tags,
type
FROM azure.data_protection.backup_instances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backup_instances</code> resource.

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
INSERT INTO azure.data_protection.backup_instances (
backupInstanceName,
resourceGroupName,
subscriptionId,
vaultName,
tags,
systemData,
properties
)
SELECT 
'{{ backupInstanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vaultName }}',
'{{ tags }}',
'{{ systemData }}',
'{{ properties }}'
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
    - name: tags
      value: object
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
    - name: properties
      value:
        - name: friendlyName
          value: string
        - name: dataSourceInfo
          value:
            - name: datasourceType
              value: string
            - name: objectType
              value: string
            - name: resourceID
              value: string
            - name: resourceLocation
              value: string
            - name: resourceName
              value: string
            - name: resourceType
              value: string
            - name: resourceUri
              value: string
            - name: resourceProperties
              value:
                - name: objectType
                  value: string
        - name: dataSourceSetInfo
          value:
            - name: datasourceType
              value: string
            - name: objectType
              value: string
            - name: resourceID
              value: string
            - name: resourceLocation
              value: string
            - name: resourceName
              value: string
            - name: resourceType
              value: string
            - name: resourceUri
              value: string
        - name: policyInfo
          value:
            - name: policyId
              value: string
            - name: policyVersion
              value: string
            - name: policyParameters
              value:
                - name: dataStoreParametersList
                  value:
                    - - name: objectType
                        value: string
                      - name: dataStoreType
                        value: string
                - name: backupDatasourceParametersList
                  value:
                    - - name: objectType
                        value: string
        - name: resourceGuardOperationRequests
          value:
            - string
        - name: protectionStatus
          value:
            - name: errorDetails
              value:
                - name: code
                  value: string
                - name: details
                  value:
                    - - name: code
                        value: string
                      - name: details
                        value:
                          - - name: code
                              value: string
                            - name: details
                              value:
                                - - name: code
                                    value: string
                                  - name: details
                                    value:
                                      - - name: code
                                          value: string
                                        - name: details
                                          value:
                                            - - name: code
                                                value: string
                                              - name: details
                                                value:
                                                  - - name: code
                                                      value: string
                                                    - name: details
                                                      value:
                                                        - - name: code
                                                            value: string
                                                          - name: details
                                                            value:
                                                              - []
                                                          - name: innerError
                                                            value: []
                                                          - name: isRetryable
                                                            value: boolean
                                                          - name: isUserError
                                                            value: boolean
                                                          - name: properties
                                                            value: object
                                                          - name: message
                                                            value: string
                                                          - name: recommendedAction
                                                            value:
                                                              - string
                                                          - name: target
                                                            value: string
                                                    - name: isRetryable
                                                      value: boolean
                                                    - name: isUserError
                                                      value: boolean
                                                    - name: properties
                                                      value: object
                                                    - name: message
                                                      value: string
                                                    - name: recommendedAction
                                                      value:
                                                        - string
                                                    - name: target
                                                      value: string
                                              - name: isRetryable
                                                value: boolean
                                              - name: isUserError
                                                value: boolean
                                              - name: properties
                                                value: object
                                              - name: message
                                                value: string
                                              - name: recommendedAction
                                                value:
                                                  - string
                                              - name: target
                                                value: string
                                        - name: isRetryable
                                          value: boolean
                                        - name: isUserError
                                          value: boolean
                                        - name: properties
                                          value: object
                                        - name: message
                                          value: string
                                        - name: recommendedAction
                                          value:
                                            - string
                                        - name: target
                                          value: string
                                  - name: isRetryable
                                    value: boolean
                                  - name: isUserError
                                    value: boolean
                                  - name: properties
                                    value: object
                                  - name: message
                                    value: string
                                  - name: recommendedAction
                                    value:
                                      - string
                                  - name: target
                                    value: string
                            - name: isRetryable
                              value: boolean
                            - name: isUserError
                              value: boolean
                            - name: properties
                              value: object
                            - name: message
                              value: string
                            - name: recommendedAction
                              value:
                                - string
                            - name: target
                              value: string
                      - name: isRetryable
                        value: boolean
                      - name: isUserError
                        value: boolean
                      - name: properties
                        value: object
                      - name: message
                        value: string
                      - name: recommendedAction
                        value:
                          - string
                      - name: target
                        value: string
                - name: isRetryable
                  value: boolean
                - name: isUserError
                  value: boolean
                - name: properties
                  value: object
                - name: message
                  value: string
                - name: recommendedAction
                  value:
                    - string
                - name: target
                  value: string
            - name: status
              value: string
        - name: currentProtectionState
          value: string
        - name: provisioningState
          value: string
        - name: datasourceAuthCredentials
          value:
            - name: objectType
              value: string
        - name: validationType
          value: string
        - name: identityDetails
          value:
            - name: useSystemAssignedIdentity
              value: boolean
            - name: userAssignedIdentityArmUrl
              value: string
        - name: objectType
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>backup_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_protection.backup_instances
WHERE backupInstanceName = '{{ backupInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```

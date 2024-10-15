---
title: sql_virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_virtual_machines
  - sql_vm
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

Creates, updates, deletes, gets or lists a <code>sql_virtual_machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql_vm.sql_virtual_machines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Azure Active Directory identity configuration for a resource. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The SQL virtual machine properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId" /> | Gets a SQL virtual machine. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all SQL virtual machines in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all SQL virtual machines in a resource group. |
| <CopyableCode code="list_by_sql_vm_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Gets the list of sql virtual machines in a SQL virtual machine group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId, data__location" /> | Creates or updates a SQL virtual machine. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId" /> | Deletes a SQL virtual machine. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId" /> | Updates SQL virtual machine tags. |
| <CopyableCode code="fetch_dc_assessment" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId" /> | Starts SQL best practices Assessment with Disk Config rules on SQL virtual machine |
| <CopyableCode code="redeploy" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId" /> | Uninstalls and reinstalls the SQL IaaS Extension. |
| <CopyableCode code="start_assessment" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlVirtualMachineName, subscriptionId" /> | Starts SQL best practices Assessment on SQL virtual machine. |

## `SELECT` examples

Gets all SQL virtual machines in a subscription.


```sql
SELECT
identity,
location,
properties,
systemData,
tags
FROM azure.sql_vm.sql_virtual_machines
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_virtual_machines</code> resource.

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
INSERT INTO azure.sql_vm.sql_virtual_machines (
resourceGroupName,
sqlVirtualMachineName,
subscriptionId,
data__location,
location,
tags,
identity,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ sqlVirtualMachineName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ location }}',
'{{ tags }}',
'{{ identity }}',
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
    - name: identity
      value:
        - name: principalId
          value: string
        - name: type
          value: string
        - name: tenantId
          value: string
    - name: properties
      value:
        - name: virtualMachineResourceId
          value: string
        - name: provisioningState
          value: string
        - name: sqlImageOffer
          value: string
        - name: sqlServerLicenseType
          value: string
        - name: sqlManagement
          value: string
        - name: leastPrivilegeMode
          value: string
        - name: sqlImageSku
          value: string
        - name: sqlVirtualMachineGroupResourceId
          value: string
        - name: wsfcDomainCredentials
          value:
            - name: clusterBootstrapAccountPassword
              value: string
            - name: clusterOperatorAccountPassword
              value: string
            - name: sqlServiceAccountPassword
              value: string
        - name: wsfcStaticIp
          value: string
        - name: autoPatchingSettings
          value:
            - name: enable
              value: boolean
            - name: dayOfWeek
              value: string
            - name: maintenanceWindowStartingHour
              value: integer
            - name: maintenanceWindowDuration
              value: integer
            - name: additionalVmPatch
              value: string
        - name: autoBackupSettings
          value:
            - name: enable
              value: boolean
            - name: enableEncryption
              value: boolean
            - name: retentionPeriod
              value: integer
            - name: storageAccountUrl
              value: string
            - name: storageContainerName
              value: string
            - name: storageAccessKey
              value: string
            - name: password
              value: string
            - name: backupSystemDbs
              value: boolean
            - name: backupScheduleType
              value: string
            - name: fullBackupFrequency
              value: string
            - name: daysOfWeek
              value:
                - string
            - name: fullBackupStartTime
              value: integer
            - name: fullBackupWindowHours
              value: integer
            - name: logBackupFrequency
              value: integer
        - name: keyVaultCredentialSettings
          value:
            - name: enable
              value: boolean
            - name: credentialName
              value: string
            - name: azureKeyVaultUrl
              value: string
            - name: servicePrincipalName
              value: string
            - name: servicePrincipalSecret
              value: string
        - name: serverConfigurationsManagementSettings
          value:
            - name: sqlConnectivityUpdateSettings
              value:
                - name: connectivityType
                  value: string
                - name: port
                  value: integer
                - name: sqlAuthUpdateUserName
                  value: string
                - name: sqlAuthUpdatePassword
                  value: string
            - name: sqlWorkloadTypeUpdateSettings
              value:
                - name: sqlWorkloadType
                  value: string
            - name: sqlStorageUpdateSettings
              value:
                - name: diskCount
                  value: integer
                - name: startingDeviceId
                  value: integer
                - name: diskConfigurationType
                  value: string
            - name: additionalFeaturesServerConfigurations
              value:
                - name: isRServicesEnabled
                  value: boolean
            - name: sqlInstanceSettings
              value:
                - name: collation
                  value: string
                - name: maxDop
                  value: integer
                - name: isOptimizeForAdHocWorkloadsEnabled
                  value: boolean
                - name: minServerMemoryMB
                  value: integer
                - name: maxServerMemoryMB
                  value: integer
                - name: isLpimEnabled
                  value: boolean
                - name: isIfiEnabled
                  value: boolean
            - name: azureAdAuthenticationSettings
              value:
                - name: clientId
                  value: string
        - name: storageConfigurationSettings
          value:
            - name: sqlDataSettings
              value:
                - name: luns
                  value:
                    - integer
                - name: defaultFilePath
                  value: string
                - name: useStoragePool
                  value: boolean
            - name: sqlTempDbSettings
              value:
                - name: dataFileSize
                  value: integer
                - name: dataGrowth
                  value: integer
                - name: logFileSize
                  value: integer
                - name: logGrowth
                  value: integer
                - name: dataFileCount
                  value: integer
                - name: persistFolder
                  value: boolean
                - name: persistFolderPath
                  value: string
                - name: luns
                  value:
                    - integer
                - name: defaultFilePath
                  value: string
                - name: useStoragePool
                  value: boolean
            - name: sqlSystemDbOnDataDisk
              value: boolean
            - name: diskConfigurationType
              value: string
            - name: storageWorkloadType
              value: string
            - name: enableStorageConfigBlade
              value: boolean
        - name: troubleshootingStatus
          value:
            - name: rootCause
              value: string
            - name: lastTriggerTimeUtc
              value: string
            - name: startTimeUtc
              value: string
            - name: endTimeUtc
              value: string
            - name: troubleshootingScenario
              value: string
            - name: properties
              value:
                - name: unhealthyReplicaInfo
                  value:
                    - name: availabilityGroupName
                      value: string
        - name: assessmentSettings
          value:
            - name: enable
              value: boolean
            - name: runImmediately
              value: boolean
            - name: schedule
              value:
                - name: enable
                  value: boolean
                - name: weeklyInterval
                  value: integer
                - name: monthlyOccurrence
                  value: integer
                - name: dayOfWeek
                  value: string
                - name: startTime
                  value: string
        - name: enableAutomaticUpgrade
          value: boolean
        - name: additionalVmPatch
          value: string
        - name: virtualMachineIdentitySettings
          value:
            - name: type
              value: string
            - name: resourceId
              value: string
        - name: osType
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sql_virtual_machines</code> resource.

```sql
/*+ update */
UPDATE azure.sql_vm.sql_virtual_machines
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND sqlVirtualMachineName = '{{ sqlVirtualMachineName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sql_virtual_machines</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql_vm.sql_virtual_machines
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlVirtualMachineName = '{{ sqlVirtualMachineName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

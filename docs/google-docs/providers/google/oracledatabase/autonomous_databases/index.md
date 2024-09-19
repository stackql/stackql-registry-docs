---
title: autonomous_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - autonomous_databases
  - oracledatabase
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

Creates, updates, deletes, gets or lists a <code>autonomous_databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>autonomous_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.oracledatabase.autonomous_databases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The name of the Autonomous Database resource in the following format: projects/{project}/locations/{region}/autonomousDatabases/{autonomous_database} |
| <CopyableCode code="adminPassword" /> | `string` | Optional. The password for the default ADMIN user. |
| <CopyableCode code="cidr" /> | `string` | Required. The subnet CIDR range for the Autonmous Database. |
| <CopyableCode code="createTime" /> | `string` | Output only. The date and time that the Autonomous Database was created. |
| <CopyableCode code="database" /> | `string` | Optional. The name of the Autonomous Database. The database name must be unique in the project. The name must begin with a letter and can contain a maximum of 30 alphanumeric characters. |
| <CopyableCode code="displayName" /> | `string` | Optional. The display name for the Autonomous Database. The name does not have to be unique within your project. |
| <CopyableCode code="entitlementId" /> | `string` | Output only. The ID of the subscription entitlement associated with the Autonomous Database. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels or tags associated with the Autonomous Database. |
| <CopyableCode code="network" /> | `string` | Required. The name of the VPC network used by the Autonomous Database. Format: projects/{project}/global/networks/{network} |
| <CopyableCode code="properties" /> | `object` | The properties of an Autonomous Database. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="autonomousDatabasesId, locationsId, projectsId" /> | Gets the details of a single Autonomous Database. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists the Autonomous Databases in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Autonomous Database in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="autonomousDatabasesId, locationsId, projectsId" /> | Deletes a single Autonomous Database. |
| <CopyableCode code="generate_wallet" /> | `EXEC` | <CopyableCode code="autonomousDatabasesId, locationsId, projectsId" /> | Generates a wallet for a single Autonomous Database. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="autonomousDatabasesId, locationsId, projectsId" /> | Restores a single Autonomous Database. |

## `SELECT` examples

Lists the Autonomous Databases in a given project and location.

```sql
SELECT
name,
adminPassword,
cidr,
createTime,
database,
displayName,
entitlementId,
labels,
network,
properties
FROM google.oracledatabase.autonomous_databases
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>autonomous_databases</code> resource.

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
INSERT INTO google.oracledatabase.autonomous_databases (
locationsId,
projectsId,
name,
database,
displayName,
adminPassword,
properties,
labels,
network,
cidr
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ database }}',
'{{ displayName }}',
'{{ adminPassword }}',
'{{ properties }}',
'{{ labels }}',
'{{ network }}',
'{{ cidr }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: database
      value: string
    - name: displayName
      value: string
    - name: entitlementId
      value: string
    - name: adminPassword
      value: string
    - name: properties
      value:
        - name: ocid
          value: string
        - name: computeCount
          value: number
        - name: cpuCoreCount
          value: integer
        - name: dataStorageSizeTb
          value: integer
        - name: dataStorageSizeGb
          value: integer
        - name: dbWorkload
          value: string
        - name: dbEdition
          value: string
        - name: characterSet
          value: string
        - name: nCharacterSet
          value: string
        - name: privateEndpointIp
          value: string
        - name: privateEndpointLabel
          value: string
        - name: dbVersion
          value: string
        - name: isAutoScalingEnabled
          value: boolean
        - name: isStorageAutoScalingEnabled
          value: boolean
        - name: licenseType
          value: string
        - name: customerContacts
          value:
            - - name: email
                value: string
        - name: secretId
          value: string
        - name: vaultId
          value: string
        - name: maintenanceScheduleType
          value: string
        - name: mtlsConnectionRequired
          value: boolean
        - name: backupRetentionPeriodDays
          value: integer
        - name: actualUsedDataStorageSizeTb
          value: number
        - name: allocatedStorageSizeTb
          value: number
        - name: apexDetails
          value:
            - name: apexVersion
              value: string
            - name: ordsVersion
              value: string
        - name: arePrimaryAllowlistedIpsUsed
          value: boolean
        - name: lifecycleDetails
          value: string
        - name: state
          value: string
        - name: autonomousContainerDatabaseId
          value: string
        - name: availableUpgradeVersions
          value:
            - string
        - name: connectionStrings
          value:
            - name: allConnectionStrings
              value:
                - name: high
                  value: string
                - name: low
                  value: string
                - name: medium
                  value: string
            - name: dedicated
              value: string
            - name: high
              value: string
            - name: low
              value: string
            - name: medium
              value: string
            - name: profiles
              value:
                - - name: consumerGroup
                    value: string
                  - name: displayName
                    value: string
                  - name: hostFormat
                    value: string
                  - name: isRegional
                    value: boolean
                  - name: protocol
                    value: string
                  - name: sessionMode
                    value: string
                  - name: syntaxFormat
                    value: string
                  - name: tlsAuthentication
                    value: string
                  - name: value
                    value: string
        - name: connectionUrls
          value:
            - name: apexUri
              value: string
            - name: databaseTransformsUri
              value: string
            - name: graphStudioUri
              value: string
            - name: machineLearningNotebookUri
              value: string
            - name: machineLearningUserManagementUri
              value: string
            - name: mongoDbUri
              value: string
            - name: ordsUri
              value: string
            - name: sqlDevWebUri
              value: string
        - name: failedDataRecoveryDuration
          value: string
        - name: memoryTableGbs
          value: integer
        - name: isLocalDataGuardEnabled
          value: boolean
        - name: localAdgAutoFailoverMaxDataLossLimit
          value: integer
        - name: localStandbyDb
          value:
            - name: lagTimeDuration
              value: string
            - name: lifecycleDetails
              value: string
            - name: state
              value: string
            - name: dataGuardRoleChangedTime
              value: string
            - name: disasterRecoveryRoleChangedTime
              value: string
        - name: memoryPerOracleComputeUnitGbs
          value: integer
        - name: localDisasterRecoveryType
          value: string
        - name: dataSafeState
          value: string
        - name: databaseManagementState
          value: string
        - name: openMode
          value: string
        - name: operationsInsightsState
          value: string
        - name: peerDbIds
          value:
            - string
        - name: permissionLevel
          value: string
        - name: privateEndpoint
          value: string
        - name: refreshableMode
          value: string
        - name: refreshableState
          value: string
        - name: role
          value: string
        - name: scheduledOperationDetails
          value:
            - - name: dayOfWeek
                value: string
              - name: startTime
                value:
                  - name: hours
                    value: integer
                  - name: minutes
                    value: integer
                  - name: seconds
                    value: integer
                  - name: nanos
                    value: integer
        - name: sqlWebDeveloperUrl
          value: string
        - name: supportedCloneRegions
          value:
            - string
        - name: usedDataStorageSizeTbs
          value: integer
        - name: ociUrl
          value: string
        - name: totalAutoBackupStorageSizeGbs
          value: number
        - name: nextLongTermBackupTime
          value: string
        - name: maintenanceBeginTime
          value: string
        - name: maintenanceEndTime
          value: string
    - name: labels
      value: object
    - name: network
      value: string
    - name: cidr
      value: string
    - name: createTime
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>autonomous_databases</code> resource.

```sql
/*+ delete */
DELETE FROM google.oracledatabase.autonomous_databases
WHERE autonomousDatabasesId = '{{ autonomousDatabasesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

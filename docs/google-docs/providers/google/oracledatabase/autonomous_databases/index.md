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
name: string
database: string
displayName: string
entitlementId: string
adminPassword: string
properties:
  ocid: string
  computeCount: number
  cpuCoreCount: integer
  dataStorageSizeTb: integer
  dataStorageSizeGb: integer
  dbWorkload: string
  dbEdition: string
  characterSet: string
  nCharacterSet: string
  privateEndpointIp: string
  privateEndpointLabel: string
  dbVersion: string
  isAutoScalingEnabled: boolean
  isStorageAutoScalingEnabled: boolean
  licenseType: string
  customerContacts:
    - email: string
  secretId: string
  vaultId: string
  maintenanceScheduleType: string
  mtlsConnectionRequired: boolean
  backupRetentionPeriodDays: integer
  actualUsedDataStorageSizeTb: number
  allocatedStorageSizeTb: number
  apexDetails:
    apexVersion: string
    ordsVersion: string
  arePrimaryAllowlistedIpsUsed: boolean
  lifecycleDetails: string
  state: string
  autonomousContainerDatabaseId: string
  availableUpgradeVersions:
    - type: string
  connectionStrings:
    allConnectionStrings:
      high: string
      low: string
      medium: string
    dedicated: string
    high: string
    low: string
    medium: string
    profiles:
      - consumerGroup: string
        displayName: string
        hostFormat: string
        isRegional: boolean
        protocol: string
        sessionMode: string
        syntaxFormat: string
        tlsAuthentication: string
        value: string
  connectionUrls:
    apexUri: string
    databaseTransformsUri: string
    graphStudioUri: string
    machineLearningNotebookUri: string
    machineLearningUserManagementUri: string
    mongoDbUri: string
    ordsUri: string
    sqlDevWebUri: string
  failedDataRecoveryDuration: string
  memoryTableGbs: integer
  isLocalDataGuardEnabled: boolean
  localAdgAutoFailoverMaxDataLossLimit: integer
  localStandbyDb:
    lagTimeDuration: string
    lifecycleDetails: string
    state: string
    dataGuardRoleChangedTime: string
    disasterRecoveryRoleChangedTime: string
  memoryPerOracleComputeUnitGbs: integer
  localDisasterRecoveryType: string
  dataSafeState: string
  databaseManagementState: string
  openMode: string
  operationsInsightsState: string
  peerDbIds:
    - type: string
  permissionLevel: string
  privateEndpoint: string
  refreshableMode: string
  refreshableState: string
  role: string
  scheduledOperationDetails:
    - dayOfWeek: string
      startTime:
        hours: integer
        minutes: integer
        seconds: integer
        nanos: integer
  sqlWebDeveloperUrl: string
  supportedCloneRegions:
    - type: string
  usedDataStorageSizeTbs: integer
  ociUrl: string
  totalAutoBackupStorageSizeGbs: number
  nextLongTermBackupTime: string
  maintenanceBeginTime: string
  maintenanceEndTime: string
labels: object
network: string
cidr: string
createTime: string

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

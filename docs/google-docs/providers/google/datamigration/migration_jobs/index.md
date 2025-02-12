---
title: migration_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - migration_jobs
  - datamigration
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

Creates, updates, deletes, gets or lists a <code>migration_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>migration_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datamigration.migration_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name (URI) of this migration job resource, in the form of: projects/{project}/locations/{location}/migrationJobs/{migrationJob}. |
| <CopyableCode code="cmekKeyName" /> | `string` | The CMEK (customer-managed encryption key) fully qualified key name used for the migration job. This field supports all migration jobs types except for: * Mysql to Mysql (use the cmek field in the cloudsql connection profile instead). * PostrgeSQL to PostgreSQL (use the cmek field in the cloudsql connection profile instead). * PostgreSQL to AlloyDB (use the kms_key_name field in the alloydb connection profile instead). Each Cloud CMEK key has the following format: projects/[PROJECT]/locations/[REGION]/keyRings/[RING]/cryptoKeys/[KEY_NAME] |
| <CopyableCode code="conversionWorkspace" /> | `object` | A conversion workspace's version. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the migration job resource was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". |
| <CopyableCode code="destination" /> | `string` | Required. The resource name (URI) of the destination connection profile. |
| <CopyableCode code="destinationDatabase" /> | `object` | A message defining the database engine and provider. |
| <CopyableCode code="displayName" /> | `string` | The migration job display name. |
| <CopyableCode code="dumpFlags" /> | `object` | Dump flags definition. |
| <CopyableCode code="dumpPath" /> | `string` | The path to the dump file in Google Cloud Storage, in the format: (gs://[BUCKET_NAME]/[OBJECT_NAME]). This field and the "dump_flags" field are mutually exclusive. |
| <CopyableCode code="dumpType" /> | `string` | Optional. The type of the data dump. Supported for MySQL to CloudSQL for MySQL migrations only. |
| <CopyableCode code="duration" /> | `string` | Output only. The duration of the migration job (in seconds). A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". |
| <CopyableCode code="endTime" /> | `string` | Output only. If the migration job is completed, the time when it was completed. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="filter" /> | `string` | This field can be used to select the entities to migrate as part of the migration job. It uses AIP-160 notation to select a subset of the entities configured on the associated conversion-workspace. This field should not be set on migration-jobs that are not associated with a conversion workspace. |
| <CopyableCode code="labels" /> | `object` | The resource labels for migration job to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |
| <CopyableCode code="performanceConfig" /> | `object` | Performance configuration definition. |
| <CopyableCode code="phase" /> | `string` | Output only. The current migration job phase. |
| <CopyableCode code="reverseSshConnectivity" /> | `object` | The details needed to configure a reverse SSH tunnel between the source and destination databases. These details will be used when calling the generateSshScript method (see https://cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/generateSshScript) to produce the script that will help set up the reverse SSH tunnel, and to set up the VPC peering between the Cloud SQL private network and the VPC. |
| <CopyableCode code="source" /> | `string` | Required. The resource name (URI) of the source connection profile. |
| <CopyableCode code="sourceDatabase" /> | `object` | A message defining the database engine and provider. |
| <CopyableCode code="sqlserverHomogeneousMigrationJobConfig" /> | `object` | Configuration for homogeneous migration to Cloud SQL for SQL Server. |
| <CopyableCode code="state" /> | `string` | The current migration job state. |
| <CopyableCode code="staticIpConnectivity" /> | `object` | The source database will allow incoming connections from the public IP of the destination database. You can retrieve the public IP of the Cloud SQL instance from the Cloud SQL console or using Cloud SQL APIs. No additional configuration is required. |
| <CopyableCode code="type" /> | `string` | Required. The migration job type. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the migration job resource was last updated. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". |
| <CopyableCode code="vpcPeeringConnectivity" /> | `object` | The details of the VPC where the source database is located in Google Cloud. We will use this information to set up the VPC peering connection between Cloud SQL and this VPC. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, migrationJobsId, projectsId" /> | Gets details of a single migration job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists migration jobs in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new migration job in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, migrationJobsId, projectsId" /> | Deletes a single migration job. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, migrationJobsId, projectsId" /> | Updates the parameters of a single migration job. |
| <CopyableCode code="demote_destination" /> | `EXEC` | <CopyableCode code="locationsId, migrationJobsId, projectsId" /> | Demotes the destination database to become a read replica of the source. This is applicable for the following migrations: 1. MySQL to Cloud SQL for MySQL 2. PostgreSQL to Cloud SQL for PostgreSQL 3. PostgreSQL to AlloyDB for PostgreSQL. |
| <CopyableCode code="generate_ssh_script" /> | `EXEC` | <CopyableCode code="locationsId, migrationJobsId, projectsId" /> | Generate a SSH configuration script to configure the reverse SSH connectivity. |
| <CopyableCode code="generate_tcp_proxy_script" /> | `EXEC` | <CopyableCode code="locationsId, migrationJobsId, projectsId" /> | Generate a TCP Proxy configuration script to configure a cloud-hosted VM running a TCP Proxy. |
| <CopyableCode code="promote" /> | `EXEC` | <CopyableCode code="locationsId, migrationJobsId, projectsId" /> | Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="locationsId, migrationJobsId, projectsId" /> | Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="locationsId, migrationJobsId, projectsId" /> | Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase). |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="locationsId, migrationJobsId, projectsId" /> | Start an already created migration job. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="locationsId, migrationJobsId, projectsId" /> | Stops a running migration job. |
| <CopyableCode code="verify" /> | `EXEC` | <CopyableCode code="locationsId, migrationJobsId, projectsId" /> | Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met. |

## `SELECT` examples

Lists migration jobs in a given project and location.

```sql
SELECT
name,
cmekKeyName,
conversionWorkspace,
createTime,
destination,
destinationDatabase,
displayName,
dumpFlags,
dumpPath,
dumpType,
duration,
endTime,
error,
filter,
labels,
performanceConfig,
phase,
reverseSshConnectivity,
source,
sourceDatabase,
sqlserverHomogeneousMigrationJobConfig,
state,
staticIpConnectivity,
type,
updateTime,
vpcPeeringConnectivity
FROM google.datamigration.migration_jobs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>migration_jobs</code> resource.

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
INSERT INTO google.datamigration.migration_jobs (
locationsId,
projectsId,
name,
labels,
displayName,
state,
type,
dumpPath,
dumpFlags,
source,
destination,
reverseSshConnectivity,
vpcPeeringConnectivity,
staticIpConnectivity,
sourceDatabase,
destinationDatabase,
conversionWorkspace,
filter,
cmekKeyName,
performanceConfig,
sqlserverHomogeneousMigrationJobConfig,
dumpType
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ labels }}',
'{{ displayName }}',
'{{ state }}',
'{{ type }}',
'{{ dumpPath }}',
'{{ dumpFlags }}',
'{{ source }}',
'{{ destination }}',
'{{ reverseSshConnectivity }}',
'{{ vpcPeeringConnectivity }}',
'{{ staticIpConnectivity }}',
'{{ sourceDatabase }}',
'{{ destinationDatabase }}',
'{{ conversionWorkspace }}',
'{{ filter }}',
'{{ cmekKeyName }}',
'{{ performanceConfig }}',
'{{ sqlserverHomogeneousMigrationJobConfig }}',
'{{ dumpType }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: labels
      value: object
    - name: displayName
      value: string
    - name: state
      value: string
    - name: phase
      value: string
    - name: type
      value: string
    - name: dumpPath
      value: string
    - name: dumpFlags
      value:
        - name: dumpFlags
          value:
            - - name: name
                value: string
              - name: value
                value: string
    - name: source
      value: string
    - name: destination
      value: string
    - name: reverseSshConnectivity
      value:
        - name: vmIp
          value: string
        - name: vmPort
          value: integer
        - name: vm
          value: string
        - name: vpc
          value: string
    - name: vpcPeeringConnectivity
      value:
        - name: vpc
          value: string
    - name: staticIpConnectivity
      value: []
    - name: duration
      value: string
    - name: error
      value:
        - name: code
          value: integer
        - name: message
          value: string
        - name: details
          value:
            - object
    - name: sourceDatabase
      value:
        - name: provider
          value: string
        - name: engine
          value: string
    - name: endTime
      value: string
    - name: conversionWorkspace
      value:
        - name: name
          value: string
        - name: commitId
          value: string
    - name: filter
      value: string
    - name: cmekKeyName
      value: string
    - name: performanceConfig
      value:
        - name: dumpParallelLevel
          value: string
    - name: sqlserverHomogeneousMigrationJobConfig
      value:
        - name: backupFilePattern
          value: string
        - name: databaseBackups
          value:
            - - name: database
                value: string
              - name: encryptionOptions
                value:
                  - name: certPath
                    value: string
                  - name: pvkPath
                    value: string
                  - name: pvkPassword
                    value: string
        - name: useDiffBackup
          value: boolean
        - name: promoteWhenReady
          value: boolean
    - name: dumpType
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>migration_jobs</code> resource.

```sql
/*+ update */
UPDATE google.datamigration.migration_jobs
SET 
name = '{{ name }}',
labels = '{{ labels }}',
displayName = '{{ displayName }}',
state = '{{ state }}',
type = '{{ type }}',
dumpPath = '{{ dumpPath }}',
dumpFlags = '{{ dumpFlags }}',
source = '{{ source }}',
destination = '{{ destination }}',
reverseSshConnectivity = '{{ reverseSshConnectivity }}',
vpcPeeringConnectivity = '{{ vpcPeeringConnectivity }}',
staticIpConnectivity = '{{ staticIpConnectivity }}',
sourceDatabase = '{{ sourceDatabase }}',
destinationDatabase = '{{ destinationDatabase }}',
conversionWorkspace = '{{ conversionWorkspace }}',
filter = '{{ filter }}',
cmekKeyName = '{{ cmekKeyName }}',
performanceConfig = '{{ performanceConfig }}',
sqlserverHomogeneousMigrationJobConfig = '{{ sqlserverHomogeneousMigrationJobConfig }}',
dumpType = '{{ dumpType }}'
WHERE 
locationsId = '{{ locationsId }}'
AND migrationJobsId = '{{ migrationJobsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>migration_jobs</code> resource.

```sql
/*+ delete */
DELETE FROM google.datamigration.migration_jobs
WHERE locationsId = '{{ locationsId }}'
AND migrationJobsId = '{{ migrationJobsId }}'
AND projectsId = '{{ projectsId }}';
```

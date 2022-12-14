---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - sqladmin
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.sqladmin.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the Cloud SQL instance. This does not include the project ID. |
| `createTime` | `string` | Output only. The time when the instance was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
| `instanceType` | `string` | The instance type. |
| `serverCaCert` | `object` | SslCerts Resource |
| `diskEncryptionStatus` | `object` | Disk encryption status for an instance. |
| `state` | `string` | The current serving state of the Cloud SQL instance. |
| `backendType` | `string` | The backend type. `SECOND_GEN`: Cloud SQL database instance. `EXTERNAL`: A database server that is not managed by Google. This property is read-only; use the `tier` property in the `settings` object to determine the database type. |
| `maintenanceVersion` | `string` | The current software version on the instance. |
| `settings` | `object` | Database instance settings. |
| `gceZone` | `string` | The Compute Engine zone that the instance is currently serving from. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary zone. WARNING: Changing this might restart the instance. |
| `availableMaintenanceVersions` | `array` | List all maintenance versions applicable on the instance |
| `currentDiskSize` | `string` | The current disk usage of the instance in bytes. This property has been deprecated. Use the "cloudsql.googleapis.com/database/disk/bytes_used" metric in Cloud Monitoring API instead. Please see [this announcement](https://groups.google.com/d/msg/google-cloud-sql-announce/I_7-F9EBhT0/BtvFtdFeAgAJ) for details. |
| `onPremisesConfiguration` | `object` | On-premises instance configuration. |
| `failoverReplica` | `object` | The name and status of the failover replica. |
| `databaseInstalledVersion` | `string` | Output only. Stores the current database version running on the instance including minor version such as `MYSQL_8_0_18`. |
| `diskEncryptionConfiguration` | `object` | Disk encryption configuration for an instance. |
| `outOfDiskReport` | `object` | This message wraps up the information written by out-of-disk detection job. |
| `etag` | `string` | This field is deprecated and will be removed from a future version of the API. Use the `settings.settingsVersion` field instead. |
| `databaseVersion` | `string` | The database engine type and version. The `databaseVersion` field cannot be changed after instance creation. |
| `masterInstanceName` | `string` | The name of the instance which will act as primary in the replication setup. |
| `region` | `string` | The geographical region. Can be: * `us-central` (`FIRST_GEN` instances only) * `us-central1` (`SECOND_GEN` instances only) * `asia-east1` or `europe-west1`. Defaults to `us-central` or `us-central1` depending on the instance type. The region cannot be changed after instance creation. |
| `maxDiskSize` | `string` | The maximum disk size of the instance in bytes. |
| `secondaryGceZone` | `string` | The Compute Engine zone that the failover instance is currently serving from for a regional instance. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary/failover zone. |
| `serviceAccountEmailAddress` | `string` | The service account email address assigned to the instance.\This property is read-only. |
| `satisfiesPzs` | `boolean` | The status indicating if instance satisfiesPzs. Reserved for future use. |
| `selfLink` | `string` | The URI of this resource. |
| `connectionName` | `string` | Connection name of the Cloud SQL instance used in connection strings. |
| `replicaConfiguration` | `object` | Read-replica configuration for connecting to the primary instance. |
| `kind` | `string` | This is always `sql#instance`. |
| `project` | `string` | The project ID of the project containing the Cloud SQL instance. The Google apps domain is prefixed if applicable. |
| `scheduledMaintenance` | `object` | Any scheduled maintenance for this instance. |
| `suspensionReason` | `array` | If the instance state is SUSPENDED, the reason for the suspension. |
| `ipv6Address` | `string` | The IPv6 address assigned to the instance. (Deprecated) This property was applicable only to First Generation instances. |
| `ipAddresses` | `array` | The assigned IP addresses for the instance. |
| `rootPassword` | `string` | Initial root password. Use only on creation. You must set root passwords before you can connect to PostgreSQL instances. |
| `replicaNames` | `array` | The replicas of the instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `sql_instances_get` | `SELECT` | `instance, project` | Retrieves a resource containing information about a Cloud SQL instance. |
| `sql_instances_list` | `SELECT` | `project` | Lists instances under a given project. |
| `sql_instances_insert` | `INSERT` | `project` | Creates a new Cloud SQL instance. |
| `sql_instances_delete` | `DELETE` | `instance, project` | Deletes a Cloud SQL instance. |
| `sql_instances_clone` | `EXEC` | `instance, project` | Creates a Cloud SQL instance as a clone of the source instance. Using this operation might cause your instance to restart. |
| `sql_instances_demoteMaster` | `EXEC` | `instance, project` | Demotes the stand-alone instance to be a Cloud SQL read replica for an external database server. |
| `sql_instances_export` | `EXEC` | `instance, project` | Exports data from a Cloud SQL instance to a Cloud Storage bucket as a SQL dump or CSV file. |
| `sql_instances_failover` | `EXEC` | `instance, project` | Initiates a manual failover of a high availability (HA) primary instance to a standby instance, which becomes the primary instance. Users are then rerouted to the new primary. For more information, see the [Overview of high availability](https://cloud.google.com/sql/docs/mysql/high-availability) page in the Cloud SQL documentation. If using Legacy HA (MySQL only), this causes the instance to failover to its failover replica instance. |
| `sql_instances_import` | `EXEC` | `instance, project` | Imports data into a Cloud SQL instance from a SQL dump or CSV file in Cloud Storage. |
| `sql_instances_patch` | `EXEC` | `instance, project` | Partially updates settings of a Cloud SQL instance by merging the request with the current configuration. This method supports patch semantics. |
| `sql_instances_promoteReplica` | `EXEC` | `instance, project` | Promotes the read replica instance to be a stand-alone Cloud SQL instance. Using this operation might cause your instance to restart. |
| `sql_instances_resetSslConfig` | `EXEC` | `instance, project` | Deletes all client certificates and generates a new server SSL certificate for the instance. |
| `sql_instances_restart` | `EXEC` | `instance, project` | Restarts a Cloud SQL instance. |
| `sql_instances_restoreBackup` | `EXEC` | `instance, project` | Restores a backup of a Cloud SQL instance. Using this operation might cause your instance to restart. |
| `sql_instances_rotateServerCa` | `EXEC` | `instance, project` | Rotates the server certificate to one signed by the Certificate Authority (CA) version previously added with the addServerCA method. |
| `sql_instances_startReplica` | `EXEC` | `instance, project` | Starts the replication in the read replica instance. |
| `sql_instances_stopReplica` | `EXEC` | `instance, project` | Stops the replication in the read replica instance. |
| `sql_instances_truncateLog` | `EXEC` | `instance, project` | Truncate MySQL general and slow query log tables MySQL only. |
| `sql_instances_update` | `EXEC` | `instance, project` | Updates settings of a Cloud SQL instance. Using this operation might cause your instance to restart. |
| `sql_projects_instances_rescheduleMaintenance` | `EXEC` | `instance, project` | Reschedules the maintenance on the given instance. |
| `sql_projects_instances_startExternalSync` | `EXEC` | `instance, project` | Start External primary instance migration. |
| `sql_projects_instances_verifyExternalSyncSettings` | `EXEC` | `instance, project` | Verify External primary instance external sync settings. |

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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sqladmin.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the Cloud SQL instance. This does not include the project ID. |
| <CopyableCode code="availableMaintenanceVersions" /> | `array` | Output only. List all maintenance versions applicable on the instance |
| <CopyableCode code="backendType" /> | `string` | The backend type. `SECOND_GEN`: Cloud SQL database instance. `EXTERNAL`: A database server that is not managed by Google. This property is read-only; use the `tier` property in the `settings` object to determine the database type. |
| <CopyableCode code="connectionName" /> | `string` | Connection name of the Cloud SQL instance used in connection strings. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the instance was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
| <CopyableCode code="currentDiskSize" /> | `string` | The current disk usage of the instance in bytes. This property has been deprecated. Use the "cloudsql.googleapis.com/database/disk/bytes_used" metric in Cloud Monitoring API instead. Please see [this announcement](https://groups.google.com/d/msg/google-cloud-sql-announce/I_7-F9EBhT0/BtvFtdFeAgAJ) for details. |
| <CopyableCode code="databaseInstalledVersion" /> | `string` | Output only. Stores the current database version running on the instance including minor version such as `MYSQL_8_0_18`. |
| <CopyableCode code="databaseVersion" /> | `string` | The database engine type and version. The `databaseVersion` field cannot be changed after instance creation. |
| <CopyableCode code="diskEncryptionConfiguration" /> | `object` | Disk encryption configuration for an instance. |
| <CopyableCode code="diskEncryptionStatus" /> | `object` | Disk encryption status for an instance. |
| <CopyableCode code="dnsName" /> | `string` | Output only. The dns name of the instance. |
| <CopyableCode code="etag" /> | `string` | This field is deprecated and will be removed from a future version of the API. Use the `settings.settingsVersion` field instead. |
| <CopyableCode code="failoverReplica" /> | `object` | The name and status of the failover replica. |
| <CopyableCode code="gceZone" /> | `string` | The Compute Engine zone that the instance is currently serving from. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary zone. WARNING: Changing this might restart the instance. |
| <CopyableCode code="geminiConfig" /> | `object` | Gemini instance configuration. |
| <CopyableCode code="instanceType" /> | `string` | The instance type. |
| <CopyableCode code="ipAddresses" /> | `array` | The assigned IP addresses for the instance. |
| <CopyableCode code="ipv6Address" /> | `string` | The IPv6 address assigned to the instance. (Deprecated) This property was applicable only to First Generation instances. |
| <CopyableCode code="kind" /> | `string` | This is always `sql#instance`. |
| <CopyableCode code="maintenanceVersion" /> | `string` | The current software version on the instance. |
| <CopyableCode code="masterInstanceName" /> | `string` | The name of the instance which will act as primary in the replication setup. |
| <CopyableCode code="maxDiskSize" /> | `string` | The maximum disk size of the instance in bytes. |
| <CopyableCode code="onPremisesConfiguration" /> | `object` | On-premises instance configuration. |
| <CopyableCode code="outOfDiskReport" /> | `object` | This message wraps up the information written by out-of-disk detection job. |
| <CopyableCode code="primaryDnsName" /> | `string` | Output only. DEPRECATED: please use write_endpoint instead. |
| <CopyableCode code="project" /> | `string` | The project ID of the project containing the Cloud SQL instance. The Google apps domain is prefixed if applicable. |
| <CopyableCode code="pscServiceAttachmentLink" /> | `string` | Output only. The link to service attachment of PSC instance. |
| <CopyableCode code="region" /> | `string` | The geographical region of the Cloud SQL instance. It can be one of the [regions](https://cloud.google.com/sql/docs/mysql/locations#location-r) where Cloud SQL operates: For example, `asia-east1`, `europe-west1`, and `us-central1`. The default value is `us-central1`. |
| <CopyableCode code="replicaConfiguration" /> | `object` | Read-replica configuration for connecting to the primary instance. |
| <CopyableCode code="replicaNames" /> | `array` | The replicas of the instance. |
| <CopyableCode code="replicationCluster" /> | `object` | A primary instance and disaster recovery (DR) replica pair. A DR replica is a cross-region replica that you designate for failover in the event that the primary instance experiences regional failure. Only applicable to MySQL. |
| <CopyableCode code="rootPassword" /> | `string` | Initial root password. Use only on creation. You must set root passwords before you can connect to PostgreSQL instances. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | This status indicates whether the instance satisfies PZS. The status is reserved for future use. |
| <CopyableCode code="scheduledMaintenance" /> | `object` | Any scheduled maintenance for this instance. |
| <CopyableCode code="secondaryGceZone" /> | `string` | The Compute Engine zone that the failover instance is currently serving from for a regional instance. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary/failover zone. |
| <CopyableCode code="selfLink" /> | `string` | The URI of this resource. |
| <CopyableCode code="serverCaCert" /> | `object` | SslCerts Resource |
| <CopyableCode code="serviceAccountEmailAddress" /> | `string` | The service account email address assigned to the instance.\This property is read-only. |
| <CopyableCode code="settings" /> | `object` | Database instance settings. |
| <CopyableCode code="sqlNetworkArchitecture" /> | `string` |  |
| <CopyableCode code="state" /> | `string` | The current serving state of the Cloud SQL instance. |
| <CopyableCode code="suspensionReason" /> | `array` | If the instance state is SUSPENDED, the reason for the suspension. |
| <CopyableCode code="upgradableDatabaseVersions" /> | `array` | Output only. All database versions that are available for upgrade. |
| <CopyableCode code="writeEndpoint" /> | `string` | Output only. The dns name of the primary instance in a replication group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instance, project" /> | Retrieves a resource containing information about a Cloud SQL instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Lists instances under a given project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a new Cloud SQL instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instance, project" /> | Deletes a Cloud SQL instance. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="instance, project" /> | Partially updates settings of a Cloud SQL instance by merging the request with the current configuration. This method supports patch semantics. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="instance, project" /> | Updates settings of a Cloud SQL instance. Using this operation might cause your instance to restart. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="project" /> | Lists instances under a given project. |
| <CopyableCode code="acquire_ssrs_lease" /> | `EXEC` | <CopyableCode code="instance, project" /> | Acquire a lease for the setup of SQL Server Reporting Services (SSRS). |
| <CopyableCode code="clone" /> | `EXEC` | <CopyableCode code="instance, project" /> | Creates a Cloud SQL instance as a clone of the source instance. Using this operation might cause your instance to restart. |
| <CopyableCode code="demote" /> | `EXEC` | <CopyableCode code="instance, project" /> | Demotes an existing standalone instance to be a Cloud SQL read replica for an external database server. |
| <CopyableCode code="demote_master" /> | `EXEC` | <CopyableCode code="instance, project" /> | Demotes the stand-alone instance to be a Cloud SQL read replica for an external database server. |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="instance, project" /> | Exports data from a Cloud SQL instance to a Cloud Storage bucket as a SQL dump or CSV file. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="instance, project" /> | Initiates a manual failover of a high availability (HA) primary instance to a standby instance, which becomes the primary instance. Users are then rerouted to the new primary. For more information, see the [Overview of high availability](https://cloud.google.com/sql/docs/mysql/high-availability) page in the Cloud SQL documentation. If using Legacy HA (MySQL only), this causes the instance to failover to its failover replica instance. |
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="instance, project" /> | Imports data into a Cloud SQL instance from a SQL dump or CSV file in Cloud Storage. |
| <CopyableCode code="perform_disk_shrink" /> | `EXEC` | <CopyableCode code="instance, project" /> | Perform Disk Shrink on primary instance. |
| <CopyableCode code="promote_replica" /> | `EXEC` | <CopyableCode code="instance, project" /> | Promotes the read replica instance to be an independent Cloud SQL primary instance. Using this operation might cause your instance to restart. |
| <CopyableCode code="reencrypt" /> | `EXEC` | <CopyableCode code="instance, project" /> | Reencrypt CMEK instance with latest key version. |
| <CopyableCode code="release_ssrs_lease" /> | `EXEC` | <CopyableCode code="instance, project" /> | Release a lease for the setup of SQL Server Reporting Services (SSRS). |
| <CopyableCode code="reschedule_maintenance" /> | `EXEC` | <CopyableCode code="instance, project" /> | Reschedules the maintenance on the given instance. |
| <CopyableCode code="reset_replica_size" /> | `EXEC` | <CopyableCode code="instance, project" /> | Reset Replica Size to primary instance disk size. |
| <CopyableCode code="reset_ssl_config" /> | `EXEC` | <CopyableCode code="instance, project" /> | Deletes all client certificates and generates a new server SSL certificate for the instance. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="instance, project" /> | Restarts a Cloud SQL instance. |
| <CopyableCode code="restore_backup" /> | `EXEC` | <CopyableCode code="instance, project" /> | Restores a backup of a Cloud SQL instance. Using this operation might cause your instance to restart. |
| <CopyableCode code="rotate_server_ca" /> | `EXEC` | <CopyableCode code="instance, project" /> | Rotates the server certificate to one signed by the Certificate Authority (CA) version previously added with the addServerCA method. |
| <CopyableCode code="start_external_sync" /> | `EXEC` | <CopyableCode code="instance, project" /> | Start External primary instance migration. |
| <CopyableCode code="start_replica" /> | `EXEC` | <CopyableCode code="instance, project" /> | Starts the replication in the read replica instance. |
| <CopyableCode code="stop_replica" /> | `EXEC` | <CopyableCode code="instance, project" /> | Stops the replication in the read replica instance. |
| <CopyableCode code="switchover" /> | `EXEC` | <CopyableCode code="instance, project" /> | Switches over from the primary instance to the designated DR replica instance. |
| <CopyableCode code="truncate_log" /> | `EXEC` | <CopyableCode code="instance, project" /> | Truncate MySQL general and slow query log tables MySQL only. |
| <CopyableCode code="verify_external_sync_settings" /> | `EXEC` | <CopyableCode code="instance, project" /> | Verify External primary instance external sync settings. |

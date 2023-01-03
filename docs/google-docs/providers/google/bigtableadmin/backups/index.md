---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - bigtableadmin
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigtableadmin.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | A globally unique identifier for the backup which cannot be changed. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/ backups/_a-zA-Z0-9*` The final segment of the name must be between 1 and 50 characters in length. The backup is stored in the cluster identified by the prefix of the backup name of the form `projects/{project}/instances/{instance}/clusters/{cluster}`. |
| `expireTime` | `string` | Required. The expiration time of the backup, with microseconds granularity that must be at least 6 hours and at most 30 days from the time the request is received. Once the `expire_time` has passed, Cloud Bigtable will delete the backup and free the resources used by the backup. |
| `sizeBytes` | `string` | Output only. Size of the backup in bytes. |
| `sourceTable` | `string` | Required. Immutable. Name of the table from which this backup was created. This needs to be in the same instance as the backup. Values are of the form `projects/{project}/instances/{instance}/tables/{source_table}`. |
| `startTime` | `string` | Output only. `start_time` is the time that the backup was started (i.e. approximately the time the CreateBackup request is received). The row data in this backup will be no older than this timestamp. |
| `state` | `string` | Output only. The current state of the backup. |
| `encryptionInfo` | `object` | Encryption information for a given resource. If this resource is protected with customer managed encryption, the in-use Cloud Key Management Service (Cloud KMS) key version is specified along with its status. |
| `endTime` | `string` | Output only. `end_time` is the time that the backup was finished. The row data in the backup will be no newer than this timestamp. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_instances_clusters_backups_get` | `SELECT` | `backupsId, clustersId, instancesId, projectsId` | Gets metadata on a pending or completed Cloud Bigtable Backup. |
| `projects_instances_clusters_backups_list` | `SELECT` | `clustersId, instancesId, projectsId` | Lists Cloud Bigtable backups. Returns both completed and pending backups. |
| `projects_instances_clusters_backups_create` | `INSERT` | `clustersId, instancesId, projectsId` | Starts creating a new Cloud Bigtable Backup. The returned backup long-running operation can be used to track creation of the backup. The metadata field type is CreateBackupMetadata. The response field type is Backup, if successful. Cancelling the returned operation will stop the creation and delete the backup. |
| `projects_instances_clusters_backups_delete` | `DELETE` | `backupsId, clustersId, instancesId, projectsId` | Deletes a pending or completed Cloud Bigtable backup. |
| `projects_instances_clusters_backups_patch` | `EXEC` | `backupsId, clustersId, instancesId, projectsId` | Updates a pending or completed Cloud Bigtable Backup. |

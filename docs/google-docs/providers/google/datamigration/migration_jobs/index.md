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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>migration_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datamigration.migration_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name (URI) of this migration job resource, in the form of: projects/{project}/locations/{location}/migrationJobs/{migrationJob}. |
| `duration` | `string` | Output only. The duration of the migration job (in seconds). A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `vpcPeeringConnectivity` | `object` | The details of the VPC where the source database is located in Google Cloud. We will use this information to set up the VPC peering connection between Cloud SQL and this VPC. |
| `state` | `string` | The current migration job state. |
| `phase` | `string` | Output only. The current migration job phase. |
| `displayName` | `string` | The migration job display name. |
| `staticIpConnectivity` | `object` | The source database will allow incoming connections from the destination database's public IP. You can retrieve the Cloud SQL instance's public IP from the Cloud SQL console or using Cloud SQL APIs. No additional configuration is required. |
| `source` | `string` | Required. The resource name (URI) of the source connection profile. |
| `destinationDatabase` | `object` | A message defining the database engine and provider. |
| `endTime` | `string` | Output only. If the migration job is completed, the time when it was completed. |
| `type` | `string` | Required. The migration job type. |
| `createTime` | `string` | Output only. The timestamp when the migration job resource was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". |
| `destination` | `string` | Required. The resource name (URI) of the destination connection profile. |
| `updateTime` | `string` | Output only. The timestamp when the migration job resource was last updated. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". |
| `reverseSshConnectivity` | `object` | The details needed to configure a reverse SSH tunnel between the source and destination databases. These details will be used when calling the generateSshScript method (see https://cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/generateSshScript) to produce the script that will help set up the reverse SSH tunnel, and to set up the VPC peering between the Cloud SQL private network and the VPC. |
| `dumpFlags` | `object` | Dump flags definition. |
| `dumpPath` | `string` | The path to the dump file in Google Cloud Storage, in the format: (gs://[BUCKET_NAME]/[OBJECT_NAME]). This field and the "dump_flags" field are mutually exclusive. |
| `sourceDatabase` | `object` | A message defining the database engine and provider. |
| `labels` | `object` | The resource labels for migration job to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_migrationJobs_get` | `SELECT` | `locationsId, migrationJobsId, projectsId` | Gets details of a single migration job. |
| `projects_locations_migrationJobs_list` | `SELECT` | `locationsId, projectsId` | Lists migration jobs in a given project and location. |
| `projects_locations_migrationJobs_create` | `INSERT` | `locationsId, projectsId` | Creates a new migration job in a given project and location. |
| `projects_locations_migrationJobs_delete` | `DELETE` | `locationsId, migrationJobsId, projectsId` | Deletes a single migration job. |
| `projects_locations_migrationJobs_generateSshScript` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Generate a SSH configuration script to configure the reverse SSH connectivity. |
| `projects_locations_migrationJobs_patch` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Updates the parameters of a single migration job. |
| `projects_locations_migrationJobs_promote` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database. |
| `projects_locations_migrationJobs_restart` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch. |
| `projects_locations_migrationJobs_resume` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase). |
| `projects_locations_migrationJobs_start` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Start an already created migration job. |
| `projects_locations_migrationJobs_stop` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Stops a running migration job. |
| `projects_locations_migrationJobs_verify` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met. |

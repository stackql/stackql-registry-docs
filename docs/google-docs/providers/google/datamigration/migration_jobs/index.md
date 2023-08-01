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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>migration_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datamigration.migration_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `unreachable` | `array` | Locations that could not be reached. |
| `migrationJobs` | `array` | The list of migration jobs objects. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, migrationJobsId, projectsId` | Gets details of a single migration job. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists migration jobs in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new migration job in a given project and location. |
| `delete` | `DELETE` | `locationsId, migrationJobsId, projectsId` | Deletes a single migration job. |
| `generate_ssh_script` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Generate a SSH configuration script to configure the reverse SSH connectivity. |
| `generate_tcp_proxy_script` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Generate a TCP Proxy configuration script to configure a cloud-hosted VM running a TCP Proxy. |
| `patch` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Updates the parameters of a single migration job. |
| `promote` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database. |
| `restart` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch. |
| `resume` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase). |
| `start` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Start an already created migration job. |
| `stop` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Stops a running migration job. |
| `verify` | `EXEC` | `locationsId, migrationJobsId, projectsId` | Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met. |

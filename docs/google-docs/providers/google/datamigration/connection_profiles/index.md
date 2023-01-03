---
title: connection_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_profiles
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
<tr><td><b>Name</b></td><td><code>connection_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datamigration.connection_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of this connection profile resource in the form of projects/{project}/locations/{location}/connectionProfiles/{connectionProfile}. |
| `postgresql` | `object` | Specifies connection parameters required specifically for PostgreSQL databases. |
| `createTime` | `string` | Output only. The timestamp when the resource was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `displayName` | `string` | The connection profile display name. |
| `cloudsql` | `object` | Specifies required connection parameters, and, optionally, the parameters required to create a Cloud SQL destination database instance. |
| `mysql` | `object` | Specifies connection parameters required specifically for MySQL databases. |
| `labels` | `object` | The resource labels for connection profile to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |
| `state` | `string` | The current connection profile state (e.g. DRAFT, READY, or FAILED). |
| `provider` | `string` | The database provider. |
| `updateTime` | `string` | Output only. The timestamp when the resource was last updated. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_connectionProfiles_get` | `SELECT` | `connectionProfilesId, locationsId, projectsId` | Gets details of a single connection profile. |
| `projects_locations_connectionProfiles_list` | `SELECT` | `locationsId, projectsId` | Retrieves a list of all connection profiles in a given project and location. |
| `projects_locations_connectionProfiles_create` | `INSERT` | `locationsId, projectsId` | Creates a new connection profile in a given project and location. |
| `projects_locations_connectionProfiles_delete` | `DELETE` | `connectionProfilesId, locationsId, projectsId` | Deletes a single Database Migration Service connection profile. A connection profile can only be deleted if it is not in use by any active migration jobs. |
| `projects_locations_connectionProfiles_patch` | `EXEC` | `connectionProfilesId, locationsId, projectsId` | Update the configuration of a single connection profile. |

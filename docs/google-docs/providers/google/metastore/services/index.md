---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - metastore
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.metastore.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The relative resource name of the metastore service, in the following format:projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/services/&#123;service_id&#125;. |
| `scalingConfig` | `object` | Represents the scaling configuration of a metastore service. |
| `endpointUri` | `string` | Output only. The URI of the endpoint used to access the metastore service. |
| `databaseType` | `string` | Immutable. The database type that the Metastore service stores its data. |
| `state` | `string` | Output only. The current state of the metastore service. |
| `releaseChannel` | `string` | Immutable. The release channel of the service. If unspecified, defaults to STABLE. |
| `port` | `integer` | The TCP port at which the metastore service is reached. Default: 9083. |
| `createTime` | `string` | Output only. The time when the metastore service was created. |
| `stateMessage` | `string` | Output only. Additional information about the current state of the metastore service, if available. |
| `tier` | `string` | The tier of the service. |
| `networkConfig` | `object` | Network configuration for the Dataproc Metastore service.Next available ID: 4 |
| `hiveMetastoreConfig` | `object` | Specifies configuration information specific to running Hive metastore software as the metastore service. |
| `metadataManagementActivity` | `object` | The metadata management activities of the metastore service. |
| `artifactGcsUri` | `string` | Output only. A Cloud Storage URI (starting with gs://) that specifies where artifacts related to the metastore service are stored. |
| `labels` | `object` | User-defined labels for the metastore service. |
| `encryptionConfig` | `object` | Encryption settings for the service. |
| `telemetryConfig` | `object` | Telemetry Configuration for the Dataproc Metastore service. |
| `uid` | `string` | Output only. The globally unique resource identifier of the metastore service. |
| `updateTime` | `string` | Output only. The time when the metastore service was last updated. |
| `maintenanceWindow` | `object` | Maintenance window. This specifies when Dataproc Metastore may perform system maintenance operation to the service. |
| `network` | `string` | Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form:projects/&#123;project_number&#125;/global/networks/&#123;network_id&#125;. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, servicesId` | Gets the details of a single service. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists services in a project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a metastore service in a project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, servicesId` | Deletes a single service. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists services in a project and location. |
| `alter_location` | `EXEC` | `locationsId, projectsId, servicesId` | Alter metadata resource location. The metadata resource can be a database, table, or partition. This functionality only updates the parent directory for the respective metadata resource and does not transfer any existing data to the new location. |
| `export_metadata` | `EXEC` | `locationsId, projectsId, servicesId` | Exports metadata from a service. |
| `move_table_to_database` | `EXEC` | `locationsId, projectsId, servicesId` | Move a table to another database. |
| `patch` | `EXEC` | `locationsId, projectsId, servicesId` | Updates the parameters of a single service. |
| `query_metadata` | `EXEC` | `locationsId, projectsId, servicesId` | Query DPMS metadata. |
| `restore` | `EXEC` | `locationsId, projectsId, servicesId` | Restores a service from a backup. |

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
| `stateMessage` | `string` | Output only. Additional information about the current state of the metastore service, if available. |
| `labels` | `object` | User-defined labels for the metastore service. |
| `uid` | `string` | Output only. The globally unique resource identifier of the metastore service. |
| `createTime` | `string` | Output only. The time when the metastore service was created. |
| `databaseType` | `string` | Immutable. The database type that the Metastore service stores its data. |
| `state` | `string` | Output only. The current state of the metastore service. |
| `releaseChannel` | `string` | Immutable. The release channel of the service. If unspecified, defaults to STABLE. |
| `encryptionConfig` | `object` | Encryption settings for the service. |
| `telemetryConfig` | `object` | Telemetry Configuration for the Dataproc Metastore service. |
| `maintenanceWindow` | `object` | Maintenance window. This specifies when Dataproc Metastore may perform system maintenance operation to the service. |
| `tier` | `string` | The tier of the service. |
| `network` | `string` | Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form:projects/&#123;project_number&#125;/global/networks/&#123;network_id&#125;. |
| `port` | `integer` | The TCP port at which the metastore service is reached. Default: 9083. |
| `networkConfig` | `object` | Network configuration for the Dataproc Metastore service. |
| `updateTime` | `string` | Output only. The time when the metastore service was last updated. |
| `artifactGcsUri` | `string` | Output only. A Cloud Storage URI (starting with gs://) that specifies where artifacts related to the metastore service are stored. |
| `metadataManagementActivity` | `object` | The metadata management activities of the metastore service. |
| `hiveMetastoreConfig` | `object` | Specifies configuration information specific to running Hive metastore software as the metastore service. |
| `endpointUri` | `string` | Output only. The URI of the endpoint used to access the metastore service. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_services_get` | `SELECT` | `locationsId, projectsId, servicesId` | Gets the details of a single service. |
| `projects_locations_services_list` | `SELECT` | `locationsId, projectsId` | Lists services in a project and location. |
| `projects_locations_services_create` | `INSERT` | `locationsId, projectsId` | Creates a metastore service in a project and location. |
| `projects_locations_services_delete` | `DELETE` | `locationsId, projectsId, servicesId` | Deletes a single service. |
| `projects_locations_services_exportMetadata` | `EXEC` | `locationsId, projectsId, servicesId` | Exports metadata from a service. |
| `projects_locations_services_patch` | `EXEC` | `locationsId, projectsId, servicesId` | Updates the parameters of a single service. |
| `projects_locations_services_restore` | `EXEC` | `locationsId, projectsId, servicesId` | Restores a service from a backup. |

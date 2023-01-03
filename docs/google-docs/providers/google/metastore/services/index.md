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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Immutable. The relative resource name of the metastore service, of the form:projects/{project_number}/locations/{location_id}/services/{service_id}. |
| `databaseType` | `string` | Immutable. The database type that the Metastore service stores its data. |
| `artifactGcsUri` | `string` | Output only. A Cloud Storage URI (starting with gs://) that specifies where artifacts related to the metastore service are stored. |
| `uid` | `string` | Output only. The globally unique resource identifier of the metastore service. |
| `hiveMetastoreConfig` | `object` | Specifies configuration information specific to running Hive metastore software as the metastore service. |
| `endpointUri` | `string` | Output only. The URI of the endpoint used to access the metastore service. |
| `metadataIntegration` | `object` | Specifies how metastore metadata should be integrated with external services. |
| `releaseChannel` | `string` | Immutable. The release channel of the service. If unspecified, defaults to STABLE. |
| `updateTime` | `string` | Output only. The time when the metastore service was last updated. |
| `tier` | `string` | The tier of the service. |
| `maintenanceWindow` | `object` | Maintenance window. This specifies when Dataproc Metastore may perform system maintenance operation to the service. |
| `port` | `integer` | The TCP port at which the metastore service is reached. Default: 9083. |
| `stateMessage` | `string` | Output only. Additional information about the current state of the metastore service, if available. |
| `network` | `string` | Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form:projects/{project_number}/global/networks/{network_id}. |
| `createTime` | `string` | Output only. The time when the metastore service was created. |
| `encryptionConfig` | `object` | Encryption settings for the service. |
| `metadataManagementActivity` | `object` | The metadata management activities of the metastore service. |
| `networkConfig` | `object` | Network configuration for the Dataproc Metastore service. |
| `state` | `string` | Output only. The current state of the metastore service. |
| `labels` | `object` | User-defined labels for the metastore service. |
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

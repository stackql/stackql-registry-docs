---
title: datacenter_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - datacenter_connectors
  - vmmigration
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
<tr><td><b>Name</b></td><td><code>datacenter_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vmmigration.datacenter_connectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The connector's name. |
| `serviceAccount` | `string` | The service account to use in the connector when communicating with the cloud. |
| `stateTime` | `string` | Output only. The time the state was last set. |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `state` | `string` | Output only. State of the DatacenterConnector, as determined by the health checks. |
| `upgradeStatus` | `object` | UpgradeStatus contains information about upgradeAppliance operation. |
| `bucket` | `string` | Output only. The communication channel between the datacenter connector and GCP. |
| `createTime` | `string` | Output only. The time the connector was created (as an API call, not when it was actually installed). |
| `applianceSoftwareVersion` | `string` | Output only. Appliance last installed update bundle version. This is the version of the automatically updatable components on the appliance. |
| `registrationId` | `string` | Immutable. A unique key for this connector. This key is internal to the OVA connector and is supplied with its creation during the registration process and can not be modified. |
| `applianceInfrastructureVersion` | `string` | Output only. Appliance OVA version. This is the OVA which is manually installed by the user and contains the infrastructure for the automatically updatable components on the appliance. |
| `updateTime` | `string` | Output only. The last time the connector was updated with an API call. |
| `availableVersions` | `object` | Holds informatiom about the available versions for upgrade. |
| `version` | `string` | The version running in the DatacenterConnector. This is supplied by the OVA connector during the registration process and can not be modified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_sources_datacenterConnectors_get` | `SELECT` | `datacenterConnectorsId, locationsId, projectsId, sourcesId` | Gets details of a single DatacenterConnector. |
| `projects_locations_sources_datacenterConnectors_list` | `SELECT` | `locationsId, projectsId, sourcesId` | Lists DatacenterConnectors in a given Source. |
| `projects_locations_sources_datacenterConnectors_create` | `INSERT` | `locationsId, projectsId, sourcesId` | Creates a new DatacenterConnector in a given Source. |
| `projects_locations_sources_datacenterConnectors_delete` | `DELETE` | `datacenterConnectorsId, locationsId, projectsId, sourcesId` | Deletes a single DatacenterConnector. |
| `projects_locations_sources_datacenterConnectors_upgradeAppliance` | `EXEC` | `datacenterConnectorsId, locationsId, projectsId, sourcesId` | Upgrades the appliance relate to this DatacenterConnector to the in-place updateable version. |

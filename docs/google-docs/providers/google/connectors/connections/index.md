---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - connectors
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
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.connectors.connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the Connection. Format: projects/{project}/locations/{location}/connections/{connection} |
| `description` | `string` | Optional. Description of the resource. |
| `suspended` | `boolean` | Optional. Suspended indicates if a user has suspended a connection or not. |
| `serviceAccount` | `string` | Optional. Service account needed for runtime plane to access GCP resources. |
| `createTime` | `string` | Output only. Created time. |
| `imageLocation` | `string` | Output only. GCR location where the runtime image is stored. formatted like: gcr.io/{bucketName}/{imageName} |
| `status` | `object` | ConnectionStatus indicates the state of the connection. |
| `connectorVersion` | `string` | Required. Connector version on which the connection is created. The format is: projects/*/locations/global/providers/*/connectors/*/versions/* |
| `configVariables` | `array` | Optional. Configuration for configuring the connection with an external system. |
| `serviceDirectory` | `string` | Output only. The name of the Service Directory service name. Used for Private Harpoon to resolve the ILB address. e.g. "projects/cloud-connectors-e2e-testing/locations/us-central1/namespaces/istio-system/services/istio-ingressgateway-connectors" |
| `updateTime` | `string` | Output only. Updated time. |
| `authConfig` | `object` | AuthConfig defines details of a authentication type. |
| `labels` | `object` | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| `envoyImageLocation` | `string` | Output only. GCR location where the envoy image is stored. formatted like: gcr.io/{bucketName}/{imageName} |
| `lockConfig` | `object` | Determines whether or no a connection is locked. If locked, a reason must be specified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_connections_get` | `SELECT` | `connectionsId, locationsId, projectsId` | Gets details of a single Connection. |
| `projects_locations_connections_list` | `SELECT` | `locationsId, projectsId` | Lists Connections in a given project and location. |
| `projects_locations_connections_create` | `INSERT` | `locationsId, projectsId` | Creates a new Connection in a given project and location. |
| `projects_locations_connections_delete` | `DELETE` | `connectionsId, locationsId, projectsId` | Deletes a single Connection. |
| `projects_locations_connections_patch` | `EXEC` | `connectionsId, locationsId, projectsId` | Updates the parameters of a single Connection. |

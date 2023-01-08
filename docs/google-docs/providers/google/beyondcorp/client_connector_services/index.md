---
title: client_connector_services
hide_title: false
hide_table_of_contents: false
keywords:
  - client_connector_services
  - beyondcorp
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
<tr><td><b>Name</b></td><td><code>client_connector_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.beyondcorp.client_connector_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of resource. The name is ignored during creation. |
| `displayName` | `string` | Optional. User-provided name. The display name should follow certain format. * Must be 6 to 30 characters in length. * Can only contain lowercase letters, numbers, and hyphens. * Must start with a letter. |
| `egress` | `object` | The details of the egress info. One of the following options should be set. |
| `ingress` | `object` | Settings of how to connect to the ClientGateway. One of the following options should be set. |
| `state` | `string` | Output only. The operational state of the ClientConnectorService. |
| `updateTime` | `string` | Output only. [Output only] Update time stamp. |
| `createTime` | `string` | Output only. [Output only] Create time stamp. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_clientConnectorServices_get` | `SELECT` | `clientConnectorServicesId, locationsId, projectsId` | Gets details of a single ClientConnectorService. |
| `projects_locations_clientConnectorServices_list` | `SELECT` | `locationsId, projectsId` | Lists ClientConnectorServices in a given project and location. |
| `projects_locations_clientConnectorServices_create` | `INSERT` | `locationsId, projectsId` | Creates a new ClientConnectorService in a given project and location. |
| `projects_locations_clientConnectorServices_delete` | `DELETE` | `clientConnectorServicesId, locationsId, projectsId` | Deletes a single ClientConnectorService. |
| `projects_locations_clientConnectorServices_patch` | `EXEC` | `clientConnectorServicesId, locationsId, projectsId` | Updates the parameters of a single ClientConnectorService. |

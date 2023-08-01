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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `datacenterConnectors` | `array` | Output only. The list of sources response. |
| `nextPageToken` | `string` | Output only. A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `unreachable` | `array` | Output only. Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `datacenterConnectorsId, locationsId, projectsId, sourcesId` | Gets details of a single DatacenterConnector. |
| `list` | `SELECT` | `locationsId, projectsId, sourcesId` | Lists DatacenterConnectors in a given Source. |
| `create` | `INSERT` | `locationsId, projectsId, sourcesId` | Creates a new DatacenterConnector in a given Source. |
| `delete` | `DELETE` | `datacenterConnectorsId, locationsId, projectsId, sourcesId` | Deletes a single DatacenterConnector. |
| `upgrade_appliance` | `EXEC` | `datacenterConnectorsId, locationsId, projectsId, sourcesId` | Upgrades the appliance relate to this DatacenterConnector to the in-place updateable version. |

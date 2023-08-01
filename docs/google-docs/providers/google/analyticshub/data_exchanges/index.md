---
title: data_exchanges
hide_title: false
hide_table_of_contents: false
keywords:
  - data_exchanges
  - analyticshub
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
<tr><td><b>Name</b></td><td><code>data_exchanges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analyticshub.data_exchanges</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `dataExchanges` | `array` | The list of data exchanges. |
| `nextPageToken` | `string` | A token to request the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_locations_data_exchanges_list` | `SELECT` | `locationsId, organizationsId` | Lists all data exchanges from projects in a given organization and location. |
| `projects_locations_data_exchanges_get` | `SELECT` | `dataExchangesId, locationsId, projectsId` | Gets the details of a data exchange. |
| `projects_locations_data_exchanges_list` | `SELECT` | `locationsId, projectsId` | Lists all data exchanges in a given project and location. |
| `projects_locations_data_exchanges_create` | `INSERT` | `locationsId, projectsId` | Creates a new data exchange. |
| `projects_locations_data_exchanges_delete` | `DELETE` | `dataExchangesId, locationsId, projectsId` | Deletes an existing data exchange. |
| `projects_locations_data_exchanges_patch` | `EXEC` | `dataExchangesId, locationsId, projectsId` | Updates an existing data exchange. |

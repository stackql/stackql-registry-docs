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
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | A token that can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `services` | `array` | The services in the specified location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, servicesId` | Gets the details of a single service. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists services in a project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a metastore service in a project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, servicesId` | Deletes a single service. |
| `alter_location` | `EXEC` | `locationsId, projectsId, servicesId` | Alter metadata resource location. The metadata resource can be a database, table, or partition. This functionality only updates the parent directory for the respective metadata resource and does not transfer any existing data to the new location. |
| `export_metadata` | `EXEC` | `locationsId, projectsId, servicesId` | Exports metadata from a service. |
| `move_table_to_database` | `EXEC` | `locationsId, projectsId, servicesId` | Move a table to another database. |
| `patch` | `EXEC` | `locationsId, projectsId, servicesId` | Updates the parameters of a single service. |
| `query_metadata` | `EXEC` | `locationsId, projectsId, servicesId` | Query DPMS metadata. |
| `restore` | `EXEC` | `locationsId, projectsId, servicesId` | Restores a service from a backup. |

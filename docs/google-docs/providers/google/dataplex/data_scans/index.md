---
title: data_scans
hide_title: false
hide_table_of_contents: false
keywords:
  - data_scans
  - dataplex
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
<tr><td><b>Name</b></td><td><code>data_scans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.data_scans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `dataScans` | `array` | DataScans (BASIC view only) under the given parent location. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `unreachable` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_data_scans_list` | `SELECT` | `locationsId, projectsId` | Lists DataScans. |
| `projects_locations_data_scans_create` | `INSERT` | `locationsId, projectsId` | Creates a DataScan resource. |
| `projects_locations_data_scans_delete` | `DELETE` | `dataScansId, locationsId, projectsId` | Deletes a DataScan resource. |
| `projects_locations_data_scans_get` | `EXEC` | `dataScansId, locationsId, projectsId` | Gets a DataScan resource. |
| `projects_locations_data_scans_patch` | `EXEC` | `dataScansId, locationsId, projectsId` | Updates a DataScan resource. |
| `projects_locations_data_scans_run` | `EXEC` | `dataScansId, locationsId, projectsId` | Runs an on-demand execution of a DataScan |

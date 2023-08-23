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
| `name` | `string` | Output only. The relative resource name of the scan, of the form: projects/&#123;project&#125;/locations/&#123;location_id&#125;/dataScans/&#123;datascan_id&#125;, where project refers to a project_id or project_number and location_id refers to a GCP region. |
| `description` | `string` | Optional. Description of the scan. Must be between 1-1024 characters. |
| `createTime` | `string` | Output only. The time when the scan was created. |
| `state` | `string` | Output only. Current state of the DataScan. |
| `data` | `object` | The data source for DataScan. |
| `dataQualitySpec` | `object` | DataQualityScan related setting. |
| `displayName` | `string` | Optional. User friendly display name. Must be between 1-256 characters. |
| `uid` | `string` | Output only. System generated globally unique ID for the scan. This ID will be different if the scan is deleted and re-created with the same name. |
| `dataQualityResult` | `object` | The output of a DataQualityScan. |
| `updateTime` | `string` | Output only. The time when the scan was last updated. |
| `dataProfileResult` | `object` | DataProfileResult defines the output of DataProfileScan. Each field of the table will have field type specific profile result. |
| `type` | `string` | Output only. The type of DataScan. |
| `executionStatus` | `object` | Status of the data scan execution. |
| `executionSpec` | `object` | DataScan execution settings. |
| `dataProfileSpec` | `object` | DataProfileScan related setting. |
| `labels` | `object` | Optional. User-defined labels for the scan. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_data_scans_get` | `SELECT` | `dataScansId, locationsId, projectsId` | Gets a DataScan resource. |
| `projects_locations_data_scans_list` | `SELECT` | `locationsId, projectsId` | Lists DataScans. |
| `projects_locations_data_scans_create` | `INSERT` | `locationsId, projectsId` | Creates a DataScan resource. |
| `projects_locations_data_scans_delete` | `DELETE` | `dataScansId, locationsId, projectsId` | Deletes a DataScan resource. |
| `_projects_locations_data_scans_list` | `EXEC` | `locationsId, projectsId` | Lists DataScans. |
| `projects_locations_data_scans_patch` | `EXEC` | `dataScansId, locationsId, projectsId` | Updates a DataScan resource. |
| `projects_locations_data_scans_run` | `EXEC` | `dataScansId, locationsId, projectsId` | Runs an on-demand execution of a DataScan |

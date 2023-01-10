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
| `name` | `string` | Output only. The relative resource name of the scan, of the form: projects/&#123;project&#125;/locations/&#123;location_id&#125;/dataScans/&#123;datascan_id&#125;. where &#123;project&#125; refers to a project_id or project_number and location_id refers to a GCP region. |
| `description` | `string` | Optional. Description of the scan. * Must be between 1-1024 characters. |
| `updateTime` | `string` | Output only. The time when the scan was last updated. |
| `dataProfileSpec` | `object` | DataProfileScan related setting. |
| `uid` | `string` | Output only. System generated globally unique ID for the scan. This ID will be different if the scan is deleted and re-created with the same name. |
| `executionStatus` | `object` | Status of the data scan execution. |
| `displayName` | `string` | Optional. User friendly display name. * Must be between 1-256 characters. |
| `executionSpec` | `object` | DataScan execution settings. |
| `dataProfileResult` | `object` | DataProfileResult defines the output of DataProfileScan. Each field of the table will have field type specific profile result. |
| `data` | `object` | The data source for DataScan. |
| `dataQualityResult` | `object` | The output of a DataQualityScan. |
| `state` | `string` | Output only. Current state of the DataScan. |
| `labels` | `object` | Optional. User-defined labels for the scan. |
| `dataQualitySpec` | `object` | DataQualityScan related setting. |
| `type` | `string` | Output only. The type of DataScan. |
| `createTime` | `string` | Output only. The time when the scan was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_dataScans_get` | `SELECT` | `dataScansId, locationsId, projectsId` | Get dataScan resource. |
| `projects_locations_dataScans_list` | `SELECT` | `locationsId, projectsId` | Lists dataScans. |
| `projects_locations_dataScans_create` | `INSERT` | `locationsId, projectsId` | Creates a dataScan resource. |
| `projects_locations_dataScans_delete` | `DELETE` | `dataScansId, locationsId, projectsId` | Delete the dataScan resource. |
| `projects_locations_dataScans_patch` | `EXEC` | `dataScansId, locationsId, projectsId` | Update the dataScan resource. |
| `projects_locations_dataScans_run` | `EXEC` | `dataScansId, locationsId, projectsId` | Run an on demand execution of a DataScan. |

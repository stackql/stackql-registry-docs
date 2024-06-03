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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_scans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.data_scans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the scan, of the form: projects/&#123;project&#125;/locations/&#123;location_id&#125;/dataScans/&#123;datascan_id&#125;, where project refers to a project_id or project_number and location_id refers to a GCP region. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the scan. Must be between 1-1024 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the scan was created. |
| <CopyableCode code="data" /> | `object` | The data source for DataScan. |
| <CopyableCode code="dataProfileResult" /> | `object` | DataProfileResult defines the output of DataProfileScan. Each field of the table will have field type specific profile result. |
| <CopyableCode code="dataProfileSpec" /> | `object` | DataProfileScan related setting. |
| <CopyableCode code="dataQualityResult" /> | `object` | The output of a DataQualityScan. |
| <CopyableCode code="dataQualitySpec" /> | `object` | DataQualityScan related setting. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. Must be between 1-256 characters. |
| <CopyableCode code="executionSpec" /> | `object` | DataScan execution settings. |
| <CopyableCode code="executionStatus" /> | `object` | Status of the data scan execution. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the scan. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the DataScan. |
| <CopyableCode code="type" /> | `string` | Output only. The type of DataScan. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the scan. This ID will be different if the scan is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the scan was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_data_scans_get" /> | `SELECT` | <CopyableCode code="dataScansId, locationsId, projectsId" /> | Gets a DataScan resource. |
| <CopyableCode code="projects_locations_data_scans_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists DataScans. |
| <CopyableCode code="projects_locations_data_scans_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a DataScan resource. |
| <CopyableCode code="projects_locations_data_scans_delete" /> | `DELETE` | <CopyableCode code="dataScansId, locationsId, projectsId" /> | Deletes a DataScan resource. |
| <CopyableCode code="projects_locations_data_scans_patch" /> | `UPDATE` | <CopyableCode code="dataScansId, locationsId, projectsId" /> | Updates a DataScan resource. |
| <CopyableCode code="_projects_locations_data_scans_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists DataScans. |
| <CopyableCode code="projects_locations_data_scans_generate_data_quality_rules" /> | `EXEC` | <CopyableCode code="dataScansId, locationsId, projectsId" /> | Generates recommended DataQualityRule from a data profiling DataScan. |
| <CopyableCode code="projects_locations_data_scans_run" /> | `EXEC` | <CopyableCode code="dataScansId, locationsId, projectsId" /> | Runs an on-demand execution of a DataScan |

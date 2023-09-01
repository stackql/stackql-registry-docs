---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
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
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The relative resource name of the action, of the form: projects/&#123;project&#125;/locations/&#123;location&#125;/lakes/&#123;lake&#125;/actions/&#123;action&#125; projects/&#123;project&#125;/locations/&#123;location&#125;/lakes/&#123;lake&#125;/zones/&#123;zone&#125;/actions/&#123;action&#125; projects/&#123;project&#125;/locations/&#123;location&#125;/lakes/&#123;lake&#125;/zones/&#123;zone&#125;/assets/&#123;asset&#125;/actions/&#123;action&#125;. |
| `dataLocations` | `array` | The list of data locations associated with this action. Cloud Storage locations are represented as URI paths(E.g. gs://bucket/table1/year=2020/month=Jan/). BigQuery locations refer to resource names(E.g. bigquery.googleapis.com/projects/project-id/datasets/dataset-id). |
| `missingResource` | `object` | Action details for resource references in assets that cannot be located. |
| `issue` | `string` | Detailed description of the issue requiring action. |
| `missingData` | `object` | Action details for absence of data detected by discovery. |
| `unauthorizedResource` | `object` | Action details for unauthorized resource issues raised to indicate that the service account associated with the lake instance is not authorized to access or manage the resource associated with an asset. |
| `zone` | `string` | Output only. The relative resource name of the zone, of the form: projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/lakes/&#123;lake_id&#125;/zones/&#123;zone_id&#125;. |
| `incompatibleDataSchema` | `object` | Action details for incompatible schemas detected by discovery. |
| `asset` | `string` | Output only. The relative resource name of the asset, of the form: projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/lakes/&#123;lake_id&#125;/zones/&#123;zone_id&#125;/assets/&#123;asset_id&#125;. |
| `invalidDataPartition` | `object` | Action details for invalid or unsupported partitions detected by discovery. |
| `failedSecurityPolicyApply` | `object` | Failed to apply security policy to the managed resource(s) under a lake, zone or an asset. For a lake or zone resource, one or more underlying assets has a failure applying security policy to the associated managed resource. |
| `detectTime` | `string` | The time that the issue was detected. |
| `category` | `string` | The category of issue associated with the action. |
| `invalidDataFormat` | `object` | Action details for invalid or unsupported data files detected by discovery. |
| `invalidDataOrganization` | `object` | Action details for invalid data arrangement. |
| `lake` | `string` | Output only. The relative resource name of the lake, of the form: projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/lakes/&#123;lake_id&#125;. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_actions_list` | `SELECT` | `lakesId, locationsId, projectsId` | Lists action resources in a lake. |
| `projects_locations_lakes_zones_actions_list` | `SELECT` | `lakesId, locationsId, projectsId, zonesId` | Lists action resources in a zone. |
| `projects_locations_lakes_zones_assets_actions_list` | `SELECT` | `assetsId, lakesId, locationsId, projectsId, zonesId` | Lists action resources in an asset. |
| `_projects_locations_lakes_actions_list` | `EXEC` | `lakesId, locationsId, projectsId` | Lists action resources in a lake. |
| `_projects_locations_lakes_zones_actions_list` | `EXEC` | `lakesId, locationsId, projectsId, zonesId` | Lists action resources in a zone. |
| `_projects_locations_lakes_zones_assets_actions_list` | `EXEC` | `assetsId, lakesId, locationsId, projectsId, zonesId` | Lists action resources in an asset. |

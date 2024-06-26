---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
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
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.assets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the asset, of the form: projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/lakes/&#123;lake_id&#125;/zones/&#123;zone_id&#125;/assets/&#123;asset_id&#125;. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the asset. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the asset was created. |
| <CopyableCode code="discoverySpec" /> | `object` | Settings to manage the metadata discovery and publishing for an asset. |
| <CopyableCode code="discoveryStatus" /> | `object` | Status of discovery for an asset. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="labels" /> | `object` | Optional. User defined labels for the asset. |
| <CopyableCode code="resourceSpec" /> | `object` | Identifies the cloud resource that is referenced by this asset. |
| <CopyableCode code="resourceStatus" /> | `object` | Status of the resource referenced by an asset. |
| <CopyableCode code="securityStatus" /> | `object` | Security policy status of the asset. Data security policy, i.e., readers, writers & owners, should be specified in the lake/zone/asset IAM policy. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the asset. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the asset. This ID will be different if the asset is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the asset was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_lakes_zones_assets_get" /> | `SELECT` | <CopyableCode code="assetsId, lakesId, locationsId, projectsId, zonesId" /> | Retrieves an asset resource. |
| <CopyableCode code="projects_locations_lakes_zones_assets_list" /> | `SELECT` | <CopyableCode code="lakesId, locationsId, projectsId, zonesId" /> | Lists asset resources in a zone. |
| <CopyableCode code="projects_locations_lakes_zones_assets_create" /> | `INSERT` | <CopyableCode code="lakesId, locationsId, projectsId, zonesId" /> | Creates an asset resource. |
| <CopyableCode code="projects_locations_lakes_zones_assets_delete" /> | `DELETE` | <CopyableCode code="assetsId, lakesId, locationsId, projectsId, zonesId" /> | Deletes an asset resource. The referenced storage resource is detached (default) or deleted based on the associated Lifecycle policy. |
| <CopyableCode code="projects_locations_lakes_zones_assets_patch" /> | `UPDATE` | <CopyableCode code="assetsId, lakesId, locationsId, projectsId, zonesId" /> | Updates an asset resource. |
| <CopyableCode code="_projects_locations_lakes_zones_assets_list" /> | `EXEC` | <CopyableCode code="lakesId, locationsId, projectsId, zonesId" /> | Lists asset resources in a zone. |

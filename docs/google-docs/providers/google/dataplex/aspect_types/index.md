---
title: aspect_types
hide_title: false
hide_table_of_contents: false
keywords:
  - aspect_types
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
<tr><td><b>Name</b></td><td><code>aspect_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.aspect_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the AspectType, of the form: projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/aspectTypes/&#123;aspect_type_id&#125;. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the AspectType. |
| <CopyableCode code="authorization" /> | `object` | Autorization for an Aspect Type. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the AspectType was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the AspectType. |
| <CopyableCode code="metadataTemplate" /> | `object` | MetadataTemplate definition for AspectType |
| <CopyableCode code="transferStatus" /> | `string` | Output only. Denotes the transfer status of the Aspect Type. It is unspecified for Aspect Types created from Dataplex API. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the AspectType. This ID will be different if the AspectType is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the AspectType was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_aspect_types_get" /> | `SELECT` | <CopyableCode code="aspectTypesId, locationsId, projectsId" /> | Retrieves a AspectType resource. |
| <CopyableCode code="projects_locations_aspect_types_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists AspectType resources in a project and location. |
| <CopyableCode code="projects_locations_aspect_types_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an AspectType |
| <CopyableCode code="projects_locations_aspect_types_delete" /> | `DELETE` | <CopyableCode code="aspectTypesId, locationsId, projectsId" /> | Deletes a AspectType resource. |
| <CopyableCode code="projects_locations_aspect_types_patch" /> | `UPDATE` | <CopyableCode code="aspectTypesId, locationsId, projectsId" /> | Updates a AspectType resource. |
| <CopyableCode code="_projects_locations_aspect_types_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists AspectType resources in a project and location. |

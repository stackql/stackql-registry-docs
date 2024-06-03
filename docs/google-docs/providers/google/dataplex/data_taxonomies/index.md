---
title: data_taxonomies
hide_title: false
hide_table_of_contents: false
keywords:
  - data_taxonomies
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
<tr><td><b>Name</b></td><td><code>data_taxonomies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.data_taxonomies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the DataTaxonomy, of the form: projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/dataTaxonomies/&#123;data_taxonomy_id&#125;. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the DataTaxonomy. |
| <CopyableCode code="attributeCount" /> | `integer` | Output only. The number of attributes in the DataTaxonomy. |
| <CopyableCode code="classCount" /> | `integer` | Output only. The number of classes in the DataTaxonomy. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the DataTaxonomy was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the DataTaxonomy. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the dataTaxonomy. This ID will be different if the DataTaxonomy is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the DataTaxonomy was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_data_taxonomies_get" /> | `SELECT` | <CopyableCode code="dataTaxonomiesId, locationsId, projectsId" /> | Retrieves a DataTaxonomy resource. |
| <CopyableCode code="projects_locations_data_taxonomies_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists DataTaxonomy resources in a project and location. |
| <CopyableCode code="projects_locations_data_taxonomies_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a DataTaxonomy resource. |
| <CopyableCode code="projects_locations_data_taxonomies_delete" /> | `DELETE` | <CopyableCode code="dataTaxonomiesId, locationsId, projectsId" /> | Deletes a DataTaxonomy resource. All attributes within the DataTaxonomy must be deleted before the DataTaxonomy can be deleted. |
| <CopyableCode code="projects_locations_data_taxonomies_patch" /> | `UPDATE` | <CopyableCode code="dataTaxonomiesId, locationsId, projectsId" /> | Updates a DataTaxonomy resource. |
| <CopyableCode code="_projects_locations_data_taxonomies_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists DataTaxonomy resources in a project and location. |

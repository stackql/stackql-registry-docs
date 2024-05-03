---
title: attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - attributes
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
<tr><td><b>Name</b></td><td><code>attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.attributes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the dataAttribute, of the form: projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/dataTaxonomies/&#123;dataTaxonomy&#125;/attributes/&#123;data_attribute_id&#125;. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the DataAttribute. |
| <CopyableCode code="attributeCount" /> | `integer` | Output only. The number of child attributes present for this attribute. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the DataAttribute was created. |
| <CopyableCode code="dataAccessSpec" /> | `object` | DataAccessSpec holds the access control configuration to be enforced on data stored within resources (eg: rows, columns in BigQuery Tables). When associated with data, the data is only accessible to principals explicitly granted access through the DataAccessSpec. Principals with access to the containing resource are not implicitly granted access. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the DataAttribute. |
| <CopyableCode code="parentId" /> | `string` | Optional. The ID of the parent DataAttribute resource, should belong to the same data taxonomy. Circular dependency in parent chain is not valid. Maximum depth of the hierarchy allowed is 4. a -&gt; b -&gt; c -&gt; d -&gt; e, depth = 4 |
| <CopyableCode code="resourceAccessSpec" /> | `object` | ResourceAccessSpec holds the access control configuration to be enforced on the resources, for example, Cloud Storage bucket, BigQuery dataset, BigQuery table. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the DataAttribute. This ID will be different if the DataAttribute is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the DataAttribute was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_data_taxonomies_attributes_get" /> | `SELECT` | <CopyableCode code="attributesId, dataTaxonomiesId, locationsId, projectsId" /> | Retrieves a Data Attribute resource. |
| <CopyableCode code="projects_locations_data_taxonomies_attributes_list" /> | `SELECT` | <CopyableCode code="dataTaxonomiesId, locationsId, projectsId" /> | Lists Data Attribute resources in a DataTaxonomy. |
| <CopyableCode code="projects_locations_data_taxonomies_attributes_create" /> | `INSERT` | <CopyableCode code="dataTaxonomiesId, locationsId, projectsId" /> | Create a DataAttribute resource. |
| <CopyableCode code="projects_locations_data_taxonomies_attributes_delete" /> | `DELETE` | <CopyableCode code="attributesId, dataTaxonomiesId, locationsId, projectsId" /> | Deletes a Data Attribute resource. |
| <CopyableCode code="_projects_locations_data_taxonomies_attributes_list" /> | `EXEC` | <CopyableCode code="dataTaxonomiesId, locationsId, projectsId" /> | Lists Data Attribute resources in a DataTaxonomy. |
| <CopyableCode code="projects_locations_data_taxonomies_attributes_patch" /> | `EXEC` | <CopyableCode code="attributesId, dataTaxonomiesId, locationsId, projectsId" /> | Updates a DataAttribute resource. |

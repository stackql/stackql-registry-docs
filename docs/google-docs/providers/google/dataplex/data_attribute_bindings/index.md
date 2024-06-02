---
title: data_attribute_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - data_attribute_bindings
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
<tr><td><b>Name</b></td><td><code>data_attribute_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="dataplex.data_attribute_bindings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the Data Attribute Binding, of the form: projects/&#123;project_number&#125;/locations/&#123;location&#125;/dataAttributeBindings/&#123;data_attribute_binding_id&#125; |
| <CopyableCode code="description" /> | `string` | Optional. Description of the DataAttributeBinding. |
| <CopyableCode code="attributes" /> | `array` | Optional. List of attributes to be associated with the resource, provided in the form: projects/&#123;project&#125;/locations/&#123;location&#125;/dataTaxonomies/&#123;dataTaxonomy&#125;/attributes/&#123;data_attribute_id&#125; |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the DataAttributeBinding was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Etags must be used when calling the DeleteDataAttributeBinding and the UpdateDataAttributeBinding method. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the DataAttributeBinding. |
| <CopyableCode code="paths" /> | `array` | Optional. The list of paths for items within the associated resource (eg. columns and partitions within a table) along with attribute bindings. |
| <CopyableCode code="resource" /> | `string` | Optional. Immutable. The resource name of the resource that is associated to attributes. Presently, only entity resource is supported in the form: projects/&#123;project&#125;/locations/&#123;location&#125;/lakes/&#123;lake&#125;/zones/&#123;zone&#125;/entities/&#123;entity_id&#125; Must belong in the same project and region as the attribute binding, and there can only exist one active binding for a resource. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the DataAttributeBinding. This ID will be different if the DataAttributeBinding is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the DataAttributeBinding was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_data_attribute_bindings_get" /> | `SELECT` | <CopyableCode code="dataAttributeBindingsId, locationsId, projectsId" /> | Retrieves a DataAttributeBinding resource. |
| <CopyableCode code="projects_locations_data_attribute_bindings_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists DataAttributeBinding resources in a project and location. |
| <CopyableCode code="projects_locations_data_attribute_bindings_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a DataAttributeBinding resource. |
| <CopyableCode code="projects_locations_data_attribute_bindings_delete" /> | `DELETE` | <CopyableCode code="dataAttributeBindingsId, locationsId, projectsId" /> | Deletes a DataAttributeBinding resource. All attributes within the DataAttributeBinding must be deleted before the DataAttributeBinding can be deleted. |
| <CopyableCode code="_projects_locations_data_attribute_bindings_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists DataAttributeBinding resources in a project and location. |
| <CopyableCode code="projects_locations_data_attribute_bindings_patch" /> | `EXEC` | <CopyableCode code="dataAttributeBindingsId, locationsId, projectsId" /> | Updates a DataAttributeBinding resource. |

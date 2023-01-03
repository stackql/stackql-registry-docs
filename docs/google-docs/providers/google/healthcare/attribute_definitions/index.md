---
title: attribute_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - attribute_definitions
  - healthcare
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attribute_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.healthcare.attribute_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the Attribute definition, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/attributeDefinitions/{attribute_definition_id}`. Cannot be changed after creation. |
| `description` | `string` | Optional. A description of the attribute. |
| `allowedValues` | `array` | Required. Possible values for the attribute. The number of allowed values must not exceed 500. An empty list is invalid. The list can only be expanded after creation. |
| `category` | `string` | Required. The category of the attribute. The value of this field cannot be changed after creation. |
| `consentDefaultValues` | `array` | Optional. Default values of the attribute in Consents. If no default values are specified, it defaults to an empty value. |
| `dataMappingDefaultValue` | `string` | Optional. Default value of the attribute in User data mappings. If no default value is specified, it defaults to an empty value. This field is only applicable to attributes of the category `RESOURCE`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_datasets_consentStores_attributeDefinitions_get` | `SELECT` | `attributeDefinitionsId, consentStoresId, datasetsId, locationsId, projectsId` | Gets the specified Attribute definition. |
| `projects_locations_datasets_consentStores_attributeDefinitions_list` | `SELECT` | `consentStoresId, datasetsId, locationsId, projectsId` | Lists the Attribute definitions in the specified consent store. |
| `projects_locations_datasets_consentStores_attributeDefinitions_create` | `INSERT` | `consentStoresId, datasetsId, locationsId, projectsId` | Creates a new Attribute definition in the parent consent store. |
| `projects_locations_datasets_consentStores_attributeDefinitions_delete` | `DELETE` | `attributeDefinitionsId, consentStoresId, datasetsId, locationsId, projectsId` | Deletes the specified Attribute definition. Fails if the Attribute definition is referenced by any User data mapping, or the latest revision of any Consent. |
| `projects_locations_datasets_consentStores_attributeDefinitions_patch` | `EXEC` | `attributeDefinitionsId, consentStoresId, datasetsId, locationsId, projectsId` | Updates the specified Attribute definition. |

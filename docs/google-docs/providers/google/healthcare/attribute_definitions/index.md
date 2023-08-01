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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `attributeDefinitions` | `array` | The returned Attribute definitions. The maximum number of attributes returned is determined by the value of page_size in the ListAttributeDefinitionsRequest. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `attributeDefinitionsId, consentStoresId, datasetsId, locationsId, projectsId` | Gets the specified Attribute definition. |
| `list` | `SELECT` | `consentStoresId, datasetsId, locationsId, projectsId` | Lists the Attribute definitions in the specified consent store. |
| `create` | `INSERT` | `consentStoresId, datasetsId, locationsId, projectsId` | Creates a new Attribute definition in the parent consent store. |
| `delete` | `DELETE` | `attributeDefinitionsId, consentStoresId, datasetsId, locationsId, projectsId` | Deletes the specified Attribute definition. Fails if the Attribute definition is referenced by any User data mapping, or the latest revision of any Consent. |
| `patch` | `EXEC` | `attributeDefinitionsId, consentStoresId, datasetsId, locationsId, projectsId` | Updates the specified Attribute definition. |

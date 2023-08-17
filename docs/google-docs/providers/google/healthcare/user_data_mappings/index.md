---
title: user_data_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - user_data_mappings
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
<tr><td><b>Name</b></td><td><code>user_data_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.healthcare.user_data_mappings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the User data mapping, of the form `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;/consentStores/&#123;consent_store_id&#125;/userDataMappings/&#123;user_data_mapping_id&#125;`. |
| `archived` | `boolean` | Output only. Indicates whether this mapping is archived. |
| `dataId` | `string` | Required. A unique identifier for the mapped resource. |
| `resourceAttributes` | `array` | Attributes of the resource. Only explicitly set attributes are displayed here. Attribute definitions with defaults set implicitly apply to these User data mappings. Attributes listed here must be single valued, that is, exactly one value is specified for the field "values" in each Attribute. |
| `userId` | `string` | Required. User's UUID provided by the client. |
| `archiveTime` | `string` | Output only. Indicates the time when this mapping was archived. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `consentStoresId, datasetsId, locationsId, projectsId, userDataMappingsId` | Gets the specified User data mapping. |
| `list` | `SELECT` | `consentStoresId, datasetsId, locationsId, projectsId` | Lists the User data mappings in the specified consent store. |
| `create` | `INSERT` | `consentStoresId, datasetsId, locationsId, projectsId` | Creates a new User data mapping in the parent consent store. |
| `delete` | `DELETE` | `consentStoresId, datasetsId, locationsId, projectsId, userDataMappingsId` | Deletes the specified User data mapping. |
| `_list` | `EXEC` | `consentStoresId, datasetsId, locationsId, projectsId` | Lists the User data mappings in the specified consent store. |
| `archive` | `EXEC` | `consentStoresId, datasetsId, locationsId, projectsId, userDataMappingsId` | Archives the specified User data mapping. |
| `patch` | `EXEC` | `consentStoresId, datasetsId, locationsId, projectsId, userDataMappingsId` | Updates the specified User data mapping. |

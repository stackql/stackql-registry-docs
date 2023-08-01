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
| `userDataMappings` | `array` | The returned User data mappings. The maximum number of User data mappings returned is determined by the value of page_size in the ListUserDataMappingsRequest. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `consentStoresId, datasetsId, locationsId, projectsId, userDataMappingsId` | Gets the specified User data mapping. |
| `list` | `SELECT` | `consentStoresId, datasetsId, locationsId, projectsId` | Lists the User data mappings in the specified consent store. |
| `create` | `INSERT` | `consentStoresId, datasetsId, locationsId, projectsId` | Creates a new User data mapping in the parent consent store. |
| `delete` | `DELETE` | `consentStoresId, datasetsId, locationsId, projectsId, userDataMappingsId` | Deletes the specified User data mapping. |
| `archive` | `EXEC` | `consentStoresId, datasetsId, locationsId, projectsId, userDataMappingsId` | Archives the specified User data mapping. |
| `patch` | `EXEC` | `consentStoresId, datasetsId, locationsId, projectsId, userDataMappingsId` | Updates the specified User data mapping. |

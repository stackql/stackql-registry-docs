---
title: service_classes
hide_title: false
hide_table_of_contents: false
keywords:
  - service_classes
  - networkconnectivity
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
<tr><td><b>Name</b></td><td><code>service_classes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.service_classes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | The next pagination token in the List response. It should be used as page_token for the following request. An empty value means no more result. |
| `serviceClasses` | `array` | ServiceClasses to be returned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, serviceClassesId` | Gets details of a single ServiceClass. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists ServiceClasses in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, serviceClassesId` | Deletes a single ServiceClass. |
| `patch` | `EXEC` | `locationsId, projectsId, serviceClassesId` | Updates the parameters of a single ServiceClass. |

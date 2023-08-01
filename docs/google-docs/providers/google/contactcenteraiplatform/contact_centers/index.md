---
title: contact_centers
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_centers
  - contactcenteraiplatform
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
<tr><td><b>Name</b></td><td><code>contact_centers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contactcenteraiplatform.contact_centers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `contactCenters` | `array` | The list of ContactCenter |
| `nextPageToken` | `string` | A token identifying a page of results the server should return. |
| `unreachable` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `contactCentersId, locationsId, projectsId` | Gets details of a single ContactCenter. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists ContactCenters in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new ContactCenter in a given project and location. |
| `delete` | `DELETE` | `contactCentersId, locationsId, projectsId` | Deletes a single ContactCenter. |
| `patch` | `EXEC` | `contactCentersId, locationsId, projectsId` | Updates the parameters of a single ContactCenter. |

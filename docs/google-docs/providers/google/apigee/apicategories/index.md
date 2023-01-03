---
title: apicategories
hide_title: false
hide_table_of_contents: false
keywords:
  - apicategories
  - apigee
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
<tr><td><b>Name</b></td><td><code>apicategories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.apicategories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `requestId` | `string` | ID that can be used to find request details in the log files. |
| `status` | `string` | Status of the operation. |
| `data` | `object` | the Api category resource. |
| `errorCode` | `string` | ID that can be used to find errors in the log files. |
| `message` | `string` | Description of the operation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_sites_apicategories_get` | `SELECT` | `apicategoriesId, organizationsId, sitesId` | Gets a category on the portal. |
| `organizations_sites_apicategories_list` | `SELECT` | `organizationsId, sitesId` | Lists the categories on the portal. |
| `organizations_sites_apicategories_create` | `INSERT` | `organizationsId, sitesId` | Creates a new category on the portal. |
| `organizations_sites_apicategories_delete` | `DELETE` | `apicategoriesId, organizationsId, sitesId` | Deletes a category from the portal. |
| `organizations_sites_apicategories_patch` | `EXEC` | `apicategoriesId, organizationsId, sitesId` | Updates a category on the portal. |

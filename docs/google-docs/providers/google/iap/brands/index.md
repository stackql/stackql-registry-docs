---
title: brands
hide_title: false
hide_table_of_contents: false
keywords:
  - brands
  - iap
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
<tr><td><b>Name</b></td><td><code>brands</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iap.brands</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Identifier of the brand. NOTE: GCP project number achieves the same brand identification purpose as only one brand per project can be created. |
| `applicationTitle` | `string` | Application name displayed on OAuth consent screen. |
| `orgInternalOnly` | `boolean` | Output only. Whether the brand is only intended for usage inside the G Suite organization only. |
| `supportEmail` | `string` | Support email displayed on the OAuth consent screen. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_brands_get` | `SELECT` | `brandsId, projectsId` | Retrieves the OAuth brand of the project. |
| `projects_brands_list` | `SELECT` | `projectsId` | Lists the existing brands for the project. |
| `projects_brands_create` | `INSERT` | `projectsId` | Constructs a new OAuth brand for the project if one does not exist. The created brand is "internal only", meaning that OAuth clients created under it only accept requests from users who belong to the same Google Workspace organization as the project. The brand is created in an un-reviewed status. NOTE: The "internal only" status can be manually changed in the Google Cloud Console. Requires that a brand does not already exist for the project, and that the specified support email is owned by the caller. |

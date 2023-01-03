---
title: custom_classes
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_classes
  - speech
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
<tr><td><b>Name</b></td><td><code>custom_classes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.speech.custom_classes</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_customClasses_get` | `SELECT` | `customClassesId, locationsId, projectsId` | Get a custom class. |
| `projects_locations_customClasses_list` | `SELECT` | `locationsId, projectsId` | List custom classes. |
| `projects_locations_customClasses_create` | `INSERT` | `locationsId, projectsId` | Create a custom class. |
| `projects_locations_customClasses_delete` | `DELETE` | `customClassesId, locationsId, projectsId` | Delete a custom class. |
| `projects_locations_customClasses_patch` | `EXEC` | `customClassesId, locationsId, projectsId` | Update a custom class. |

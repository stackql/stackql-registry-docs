---
title: serving_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - serving_configs
  - retail
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
<tr><td><b>Name</b></td><td><code>serving_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.retail.serving_configs</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_servingConfigs_predict` | `EXEC` | `catalogsId, locationsId, projectsId, servingConfigsId` | Makes a recommendation prediction. |
| `projects_locations_catalogs_servingConfigs_search` | `EXEC` | `catalogsId, locationsId, projectsId, servingConfigsId` | Performs a search. This feature is only available for users who have Retail Search enabled. Please enable Retail Search on Cloud Console before using this feature. |

---
title: url_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - url_lists
  - networksecurity
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
<tr><td><b>Name</b></td><td><code>url_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networksecurity.url_lists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the resource provided by the user. Name is of the form projects/&#123;project&#125;/locations/&#123;location&#125;/urlLists/&#123;url_list&#125; url_list should match the pattern:(^[a-z]([a-z0-9-]&#123;0,61&#125;[a-z0-9])?$). |
| `description` | `string` | Optional. Free-text description of the resource. |
| `updateTime` | `string` | Output only. Time when the security policy was updated. |
| `values` | `array` | Required. FQDNs and URLs. |
| `createTime` | `string` | Output only. Time when the security policy was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_url_lists_get` | `SELECT` | `locationsId, projectsId, urlListsId` | Gets details of a single UrlList. |
| `projects_locations_url_lists_list` | `SELECT` | `locationsId, projectsId` | Lists UrlLists in a given project and location. |
| `projects_locations_url_lists_create` | `INSERT` | `locationsId, projectsId` | Creates a new UrlList in a given project and location. |
| `projects_locations_url_lists_delete` | `DELETE` | `locationsId, projectsId, urlListsId` | Deletes a single UrlList. |
| `projects_locations_url_lists_patch` | `EXEC` | `locationsId, projectsId, urlListsId` | Updates the parameters of a single UrlList. |

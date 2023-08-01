---
title: address_groups_references
hide_title: false
hide_table_of_contents: false
keywords:
  - address_groups_references
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
<tr><td><b>Name</b></td><td><code>address_groups_references</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networksecurity.address_groups_references</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`. |
| `addressGroupReferences` | `array` | A list of references that matches the specified filter in the request. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_locations_address_groups_list_references` | `SELECT` | `addressGroupsId, locationsId, organizationsId` |
| `projects_locations_address_groups_list_references` | `SELECT` | `addressGroupsId, locationsId, projectsId` |

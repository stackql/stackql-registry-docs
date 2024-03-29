---
title: address_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - address_groups
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
<tr><td><b>Name</b></td><td><code>address_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networksecurity.address_groups</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_locations_address_groups_get` | `SELECT` | `addressGroupsId, locationsId, organizationsId` | Gets details of a single address group. |
| `organizations_locations_address_groups_list` | `SELECT` | `locationsId, organizationsId` | Lists address groups in a given project and location. |
| `projects_locations_address_groups_get` | `SELECT` | `addressGroupsId, locationsId, projectsId` | Gets details of a single address group. |
| `projects_locations_address_groups_list` | `SELECT` | `locationsId, projectsId` | Lists address groups in a given project and location. |
| `organizations_locations_address_groups_create` | `INSERT` | `locationsId, organizationsId` | Creates a new address group in a given project and location. |
| `projects_locations_address_groups_create` | `INSERT` | `locationsId, projectsId` | Creates a new address group in a given project and location. |
| `organizations_locations_address_groups_delete` | `DELETE` | `addressGroupsId, locationsId, organizationsId` | Deletes an address group. |
| `projects_locations_address_groups_delete` | `DELETE` | `addressGroupsId, locationsId, projectsId` | Deletes a single address group. |
| `_organizations_locations_address_groups_list` | `EXEC` | `locationsId, organizationsId` | Lists address groups in a given project and location. |
| `_projects_locations_address_groups_list` | `EXEC` | `locationsId, projectsId` | Lists address groups in a given project and location. |
| `organizations_locations_address_groups_clone_items` | `EXEC` | `addressGroupsId, locationsId, organizationsId` | Clones items from one address group to another. |
| `organizations_locations_address_groups_patch` | `EXEC` | `addressGroupsId, locationsId, organizationsId` | Updates parameters of an address group. |
| `projects_locations_address_groups_clone_items` | `EXEC` | `addressGroupsId, locationsId, projectsId` | Clones items from one address group to another. |
| `projects_locations_address_groups_patch` | `EXEC` | `addressGroupsId, locationsId, projectsId` | Updates the parameters of a single address group. |

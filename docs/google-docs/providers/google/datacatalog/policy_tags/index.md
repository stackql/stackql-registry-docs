---
title: policy_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_tags
  - datacatalog
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
<tr><td><b>Name</b></td><td><code>policy_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datacatalog.policy_tags</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Pagination token of the next results page. Empty if there are no more results in the list. |
| `policyTags` | `array` | The policy tags that belong to the taxonomy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_taxonomies_policy_tags_get` | `SELECT` | `locationsId, policyTagsId, projectsId, taxonomiesId` | Gets a policy tag. |
| `projects_locations_taxonomies_policy_tags_list` | `SELECT` | `locationsId, projectsId, taxonomiesId` | Lists all policy tags in a taxonomy. |
| `projects_locations_taxonomies_policy_tags_create` | `INSERT` | `locationsId, projectsId, taxonomiesId` | Creates a policy tag in a taxonomy. |
| `projects_locations_taxonomies_policy_tags_delete` | `DELETE` | `locationsId, policyTagsId, projectsId, taxonomiesId` | Deletes a policy tag together with the following: * All of its descendant policy tags, if any * Policies associated with the policy tag and its descendants * References from BigQuery table schema of the policy tag and its descendants |
| `projects_locations_taxonomies_policy_tags_patch` | `EXEC` | `locationsId, policyTagsId, projectsId, taxonomiesId` | Updates a policy tag, including its display name, description, and parent policy tag. |

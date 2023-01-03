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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Output only. Resource name of this policy tag in the URL format. The policy tag manager generates unique taxonomy IDs and policy tag IDs. |
| `description` | `string` | Description of this policy tag. If not set, defaults to empty. The description must contain only Unicode characters, tabs, newlines, carriage returns and page breaks, and be at most 2000 bytes long when encoded in UTF-8. |
| `childPolicyTags` | `array` | Output only. Resource names of child policy tags of this policy tag. |
| `displayName` | `string` | Required. User-defined name of this policy tag. The name can't start or end with spaces and must be unique within the parent taxonomy, contain only Unicode letters, numbers, underscores, dashes and spaces, and be at most 200 bytes long when encoded in UTF-8. |
| `parentPolicyTag` | `string` | Resource name of this policy tag's parent policy tag. If empty, this is a top level tag. If not set, defaults to an empty string. For example, for the "LatLong" policy tag in the example above, this field contains the resource name of the "Geolocation" policy tag, and, for "Geolocation", this field is empty. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_taxonomies_policyTags_get` | `SELECT` | `locationsId, policyTagsId, projectsId, taxonomiesId` | Gets a policy tag. |
| `projects_locations_taxonomies_policyTags_list` | `SELECT` | `locationsId, projectsId, taxonomiesId` | Lists all policy tags in a taxonomy. |
| `projects_locations_taxonomies_policyTags_create` | `INSERT` | `locationsId, projectsId, taxonomiesId` | Creates a policy tag in a taxonomy. |
| `projects_locations_taxonomies_policyTags_delete` | `DELETE` | `locationsId, policyTagsId, projectsId, taxonomiesId` | Deletes a policy tag together with the following: * All of its descendant policy tags, if any * Policies associated with the policy tag and its descendants * References from BigQuery table schema of the policy tag and its descendants |
| `projects_locations_taxonomies_policyTags_patch` | `EXEC` | `locationsId, policyTagsId, projectsId, taxonomiesId` | Updates a policy tag, including its display name, description, and parent policy tag. |

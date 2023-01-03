---
title: taxonomies
hide_title: false
hide_table_of_contents: false
keywords:
  - taxonomies
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
<tr><td><b>Name</b></td><td><code>taxonomies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datacatalog.taxonomies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of this taxonomy in URL format. Note: Policy tag manager generates unique taxonomy IDs. |
| `description` | `string` | Optional. Description of this taxonomy. If not set, defaults to empty. The description must contain only Unicode characters, tabs, newlines, carriage returns, and page breaks, and be at most 2000 bytes long when encoded in UTF-8. |
| `displayName` | `string` | Required. User-defined name of this taxonomy. The name can't start or end with spaces, must contain only Unicode letters, numbers, underscores, dashes, and spaces, and be at most 200 bytes long when encoded in UTF-8. The taxonomy display name must be unique within an organization. |
| `policyTagCount` | `integer` | Output only. Number of policy tags in this taxonomy. |
| `taxonomyTimestamps` | `object` | Timestamps associated with this resource in a particular system. |
| `activatedPolicyTypes` | `array` | Optional. A list of policy types that are activated for this taxonomy. If not set, defaults to an empty list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_taxonomies_get` | `SELECT` | `locationsId, projectsId, taxonomiesId` | Gets a taxonomy. |
| `projects_locations_taxonomies_list` | `SELECT` | `locationsId, projectsId` | Lists all taxonomies in a project in a particular location that you have a permission to view. |
| `projects_locations_taxonomies_create` | `INSERT` | `locationsId, projectsId` | Creates a taxonomy in a specified project. The taxonomy is initially empty, that is, it doesn't contain policy tags. |
| `projects_locations_taxonomies_delete` | `DELETE` | `locationsId, projectsId, taxonomiesId` | Deletes a taxonomy, including all policy tags in this taxonomy, their associated policies, and the policy tags references from BigQuery columns. |
| `projects_locations_taxonomies_export` | `EXEC` | `locationsId, projectsId` | Exports taxonomies in the requested type and returns them, including their policy tags. The requested taxonomies must belong to the same project. This method generates `SerializedTaxonomy` protocol buffers with nested policy tags that can be used as input for `ImportTaxonomies` calls. |
| `projects_locations_taxonomies_import` | `EXEC` | `locationsId, projectsId` | Creates new taxonomies (including their policy tags) in a given project by importing from inlined or cross-regional sources. For a cross-regional source, new taxonomies are created by copying from a source in another region. For an inlined source, taxonomies and policy tags are created in bulk using nested protocol buffer structures. |
| `projects_locations_taxonomies_patch` | `EXEC` | `locationsId, projectsId, taxonomiesId` | Updates a taxonomy, including its display name, description, and activated policy types. |
| `projects_locations_taxonomies_replace` | `EXEC` | `locationsId, projectsId, taxonomiesId` | Replaces (updates) a taxonomy and all its policy tags. The taxonomy and its entire hierarchy of policy tags must be represented literally by `SerializedTaxonomy` and the nested `SerializedPolicyTag` messages. This operation automatically does the following: - Deletes the existing policy tags that are missing from the `SerializedPolicyTag`. - Creates policy tags that don't have resource names. They are considered new. - Updates policy tags with valid resources names accordingly. |

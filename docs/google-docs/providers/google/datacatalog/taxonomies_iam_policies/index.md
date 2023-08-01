---
title: taxonomies_iam_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - taxonomies_iam_policies
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
<tr><td><b>Name</b></td><td><code>taxonomies_iam_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datacatalog.taxonomies_iam_policies</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_taxonomies_get_iam_policy` | `EXEC` | `locationsId, projectsId, taxonomiesId` | Gets the IAM policy for a policy tag or a taxonomy. |
| `projects_locations_taxonomies_set_iam_policy` | `EXEC` | `locationsId, projectsId, taxonomiesId` | Sets the IAM policy for a policy tag or a taxonomy. |
| `projects_locations_taxonomies_test_iam_permissions` | `EXEC` | `locationsId, projectsId, taxonomiesId` | Returns your permissions on a specified policy tag or taxonomy. |

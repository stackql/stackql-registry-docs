---
title: catalogs_default_branch
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs_default_branch
  - retail
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
<tr><td><b>Name</b></td><td><code>catalogs_default_branch</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.retail.catalogs_default_branch</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `note` | `string` | This corresponds to SetDefaultBranchRequest.note field, when this branch was set as default. |
| `setTime` | `string` | The time when this branch is set to default. |
| `branch` | `string` | Full resource name of the branch id currently set as default branch. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_catalogs_get_default_branch` | `SELECT` | `catalogsId, locationsId, projectsId` |

---
title: constraints
hide_title: false
hide_table_of_contents: false
keywords:
  - constraints
  - orgpolicy
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
<tr><td><b>Name</b></td><td><code>constraints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.orgpolicy.constraints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Page token used to retrieve the next page. This is currently not used. |
| `constraints` | `array` | The collection of constraints that are available on the targeted resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `folders_constraints_list` | `SELECT` | `foldersId` |
| `organizations_constraints_list` | `SELECT` | `organizationsId` |
| `projects_constraints_list` | `SELECT` | `projectsId` |

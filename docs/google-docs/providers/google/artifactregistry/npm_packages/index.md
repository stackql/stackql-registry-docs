---
title: npm_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - npm_packages
  - artifactregistry
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
<tr><td><b>Name</b></td><td><code>npm_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.artifactregistry.npm_packages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The token to retrieve the next page of artifacts, or empty if there are no more artifacts to return. |
| `npmPackages` | `array` | The npm packages returned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, npmPackagesId, projectsId, repositoriesId` | Gets a npm package. |
| `list` | `SELECT` | `locationsId, projectsId, repositoriesId` | Lists npm packages. |

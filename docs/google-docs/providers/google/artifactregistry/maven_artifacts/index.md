---
title: maven_artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - maven_artifacts
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
<tr><td><b>Name</b></td><td><code>maven_artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.artifactregistry.maven_artifacts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The token to retrieve the next page of artifacts, or empty if there are no more artifacts to return. |
| `mavenArtifacts` | `array` | The maven artifacts returned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, mavenArtifactsId, projectsId, repositoriesId` | Gets a maven artifact. |
| `list` | `SELECT` | `locationsId, projectsId, repositoriesId` | Lists maven artifacts. |

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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Required. registry_location, project_id, repository_name and maven_artifact forms a unique artifact For example, "projects/test-project/locations/us-west4/repositories/test-repo/mavenArtifacts/ com.google.guava:guava:31.0-jre", where "us-west4" is the registry_location, "test-project" is the project_id, "test-repo" is the repository_name and "com.google.guava:guava:31.0-jre" is the maven artifact. |
| `groupId` | `string` | Group ID for the artifact. Example: com.google.guava |
| `pomUri` | `string` | Required. URL to access the pom file of the artifact. Example: us-west4-maven.pkg.dev/test-project/test-repo/com/google/guava/guava/31.0/guava-31.0.pom |
| `updateTime` | `string` | Output only. Time the artifact was updated. |
| `version` | `string` | Version of this artifact. |
| `artifactId` | `string` | Artifact ID for the artifact. |
| `createTime` | `string` | Output only. Time the artifact was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_repositories_mavenArtifacts_get` | `SELECT` | `locationsId, mavenArtifactsId, projectsId, repositoriesId` | Gets a maven artifact. |
| `projects_locations_repositories_mavenArtifacts_list` | `SELECT` | `locationsId, projectsId, repositoriesId` | Lists maven artifacts. |

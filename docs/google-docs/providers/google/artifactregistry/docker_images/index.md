---
title: docker_images
hide_title: false
hide_table_of_contents: false
keywords:
  - docker_images
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
<tr><td><b>Name</b></td><td><code>docker_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.artifactregistry.docker_images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. registry_location, project_id, repository_name and image id forms a unique image name:`projects//locations//repository//dockerImages/`. For example, "projects/test-project/locations/us-west4/repositories/test-repo/dockerImages/ nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf", where "us-west4" is the registry_location, "test-project" is the project_id, "test-repo" is the repository_name and "nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf" is the image's digest. |
| `mediaType` | `string` | Media type of this image, e.g. "application/vnd.docker.distribution.manifest.v2+json". This field is returned as the 'metadata.mediaType' field in the Version resource. |
| `tags` | `array` | Tags attached to this image. |
| `updateTime` | `string` | Output only. The time when the docker image was last updated. |
| `uploadTime` | `string` | Time the image was uploaded. |
| `uri` | `string` | Required. URL to access the image. Example: us-west4-docker.pkg.dev/test-project/test-repo/nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf |
| `buildTime` | `string` | The time this image was built. This field is returned as the 'metadata.buildTime' field in the Version resource. The build time is returned to the client as an RFC 3339 string, which can be easily used with the JavaScript Date constructor. |
| `imageSizeBytes` | `string` | Calculated size of the image. This field is returned as the 'metadata.imageSizeBytes' field in the Version resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dockerImagesId, locationsId, projectsId, repositoriesId` | Gets a docker image. |
| `list` | `SELECT` | `locationsId, projectsId, repositoriesId` | Lists docker images. |
| `_list` | `EXEC` | `locationsId, projectsId, repositoriesId` | Lists docker images. |

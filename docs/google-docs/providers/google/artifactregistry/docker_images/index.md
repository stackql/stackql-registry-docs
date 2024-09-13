
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>docker_image</code> resource or lists <code>docker_images</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>docker_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.artifactregistry.docker_images" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. registry_location, project_id, repository_name and image id forms a unique image name:`projects//locations//repository//dockerImages/`. For example, "projects/test-project/locations/us-west4/repositories/test-repo/dockerImages/ nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf", where "us-west4" is the registry_location, "test-project" is the project_id, "test-repo" is the repository_name and "nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf" is the image's digest. |
| <CopyableCode code="buildTime" /> | `string` | The time this image was built. This field is returned as the 'metadata.buildTime' field in the Version resource. The build time is returned to the client as an RFC 3339 string, which can be easily used with the JavaScript Date constructor. |
| <CopyableCode code="imageSizeBytes" /> | `string` | Calculated size of the image. This field is returned as the 'metadata.imageSizeBytes' field in the Version resource. |
| <CopyableCode code="mediaType" /> | `string` | Media type of this image, e.g. "application/vnd.docker.distribution.manifest.v2+json". This field is returned as the 'metadata.mediaType' field in the Version resource. |
| <CopyableCode code="tags" /> | `array` | Tags attached to this image. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the docker image was last updated. |
| <CopyableCode code="uploadTime" /> | `string` | Time the image was uploaded. |
| <CopyableCode code="uri" /> | `string` | Required. URL to access the image. Example: us-west4-docker.pkg.dev/test-project/test-repo/nginx@sha256:e9954c1fc875017be1c3e36eca16be2d9e9bccc4bf072163515467d6a823c7cf |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dockerImagesId, locationsId, projectsId, repositoriesId" /> | Gets a docker image. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Lists docker images. |

## `SELECT` examples

Lists docker images.

```sql
SELECT
name,
buildTime,
imageSizeBytes,
mediaType,
tags,
updateTime,
uploadTime,
uri
FROM google.artifactregistry.docker_images
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'; 
```

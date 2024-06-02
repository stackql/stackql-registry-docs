---
title: artifacts_contents
hide_title: false
hide_table_of_contents: false
keywords:
  - artifacts_contents
  - apigeeregistry
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>artifacts_contents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigeeregistry.artifacts_contents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="contentType" /> | `string` | The HTTP Content-Type header value specifying the content type of the body. |
| <CopyableCode code="data" /> | `string` | The HTTP request/response body as raw binary. |
| <CopyableCode code="extensions" /> | `array` | Application specific response metadata. Must be set in the first response for streaming APIs. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_locations_apis_artifacts_get_contents" /> | `SELECT` | <CopyableCode code="apisId, artifactsId, locationsId, projectsId" /> |
| <CopyableCode code="projects_locations_apis_deployments_artifacts_get_contents" /> | `SELECT` | <CopyableCode code="apisId, artifactsId, deploymentsId, locationsId, projectsId" /> |
| <CopyableCode code="projects_locations_apis_versions_artifacts_get_contents" /> | `SELECT` | <CopyableCode code="apisId, artifactsId, locationsId, projectsId, versionsId" /> |
| <CopyableCode code="projects_locations_apis_versions_specs_artifacts_get_contents" /> | `SELECT` | <CopyableCode code="apisId, artifactsId, locationsId, projectsId, specsId, versionsId" /> |
| <CopyableCode code="projects_locations_artifacts_get_contents" /> | `SELECT` | <CopyableCode code="artifactsId, locationsId, projectsId" /> |

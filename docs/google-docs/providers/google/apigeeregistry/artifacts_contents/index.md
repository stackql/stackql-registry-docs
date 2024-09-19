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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>artifacts_contents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>artifacts_contents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigeeregistry.artifacts_contents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="contentType" /> | `string` | The HTTP Content-Type header value specifying the content type of the body. |
| <CopyableCode code="data" /> | `string` | The HTTP request/response body as raw binary. |
| <CopyableCode code="extensions" /> | `array` | Application specific response metadata. Must be set in the first response for streaming APIs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_apis_artifacts_get_contents" /> | `SELECT` | <CopyableCode code="apisId, artifactsId, locationsId, projectsId" /> | Returns the contents of a specified artifact. If artifacts are stored with GZip compression, the default behavior is to return the artifact uncompressed (the mime_type response field indicates the exact format returned). |
| <CopyableCode code="projects_locations_apis_deployments_artifacts_get_contents" /> | `SELECT` | <CopyableCode code="apisId, artifactsId, deploymentsId, locationsId, projectsId" /> | Returns the contents of a specified artifact. If artifacts are stored with GZip compression, the default behavior is to return the artifact uncompressed (the mime_type response field indicates the exact format returned). |
| <CopyableCode code="projects_locations_apis_versions_artifacts_get_contents" /> | `SELECT` | <CopyableCode code="apisId, artifactsId, locationsId, projectsId, versionsId" /> | Returns the contents of a specified artifact. If artifacts are stored with GZip compression, the default behavior is to return the artifact uncompressed (the mime_type response field indicates the exact format returned). |
| <CopyableCode code="projects_locations_apis_versions_specs_artifacts_get_contents" /> | `SELECT` | <CopyableCode code="apisId, artifactsId, locationsId, projectsId, specsId, versionsId" /> | Returns the contents of a specified artifact. If artifacts are stored with GZip compression, the default behavior is to return the artifact uncompressed (the mime_type response field indicates the exact format returned). |
| <CopyableCode code="projects_locations_artifacts_get_contents" /> | `SELECT` | <CopyableCode code="artifactsId, locationsId, projectsId" /> | Returns the contents of a specified artifact. If artifacts are stored with GZip compression, the default behavior is to return the artifact uncompressed (the mime_type response field indicates the exact format returned). |

## `SELECT` examples

Returns the contents of a specified artifact. If artifacts are stored with GZip compression, the default behavior is to return the artifact uncompressed (the mime_type response field indicates the exact format returned).

```sql
SELECT
contentType,
data,
extensions
FROM google.apigeeregistry.artifacts_contents
WHERE artifactsId = '{{ artifactsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

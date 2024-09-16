---
title: artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - artifacts
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

Creates, updates, deletes, gets or lists a <code>artifacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigeeregistry.artifacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="annotations" /> | `object` | Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts. |
| <CopyableCode code="contents" /> | `string` | Input only. The contents of the artifact. Provided by API callers when artifacts are created or replaced. To access the contents of an artifact, use GetArtifactContents. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation timestamp. |
| <CopyableCode code="hash" /> | `string` | Output only. A SHA-256 hash of the artifact's contents. If the artifact is gzipped, this is the hash of the uncompressed artifact. |
| <CopyableCode code="labels" /> | `object` | Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "registry.googleapis.com/" and cannot be changed. |
| <CopyableCode code="mimeType" /> | `string` | A content type specifier for the artifact. Content type specifiers are Media Types (https://en.wikipedia.org/wiki/Media_type) with a possible "schema" parameter that specifies a schema for the stored information. Content types can specify compression. Currently only GZip compression is supported (indicated with "+gzip"). |
| <CopyableCode code="sizeBytes" /> | `integer` | Output only. The size of the artifact in bytes. If the artifact is gzipped, this is the size of the uncompressed artifact. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update timestamp. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_apis_artifacts_get" /> | `SELECT` | <CopyableCode code="apisId, artifactsId, locationsId, projectsId" /> | Returns a specified artifact. |
| <CopyableCode code="projects_locations_apis_artifacts_list" /> | `SELECT` | <CopyableCode code="apisId, locationsId, projectsId" /> | Returns matching artifacts. |
| <CopyableCode code="projects_locations_apis_deployments_artifacts_get" /> | `SELECT` | <CopyableCode code="apisId, artifactsId, deploymentsId, locationsId, projectsId" /> | Returns a specified artifact. |
| <CopyableCode code="projects_locations_apis_deployments_artifacts_list" /> | `SELECT` | <CopyableCode code="apisId, deploymentsId, locationsId, projectsId" /> | Returns matching artifacts. |
| <CopyableCode code="projects_locations_apis_versions_artifacts_get" /> | `SELECT` | <CopyableCode code="apisId, artifactsId, locationsId, projectsId, versionsId" /> | Returns a specified artifact. |
| <CopyableCode code="projects_locations_apis_versions_artifacts_list" /> | `SELECT` | <CopyableCode code="apisId, locationsId, projectsId, versionsId" /> | Returns matching artifacts. |
| <CopyableCode code="projects_locations_apis_versions_specs_artifacts_get" /> | `SELECT` | <CopyableCode code="apisId, artifactsId, locationsId, projectsId, specsId, versionsId" /> | Returns a specified artifact. |
| <CopyableCode code="projects_locations_apis_versions_specs_artifacts_list" /> | `SELECT` | <CopyableCode code="apisId, locationsId, projectsId, specsId, versionsId" /> | Returns matching artifacts. |
| <CopyableCode code="projects_locations_artifacts_get" /> | `SELECT` | <CopyableCode code="artifactsId, locationsId, projectsId" /> | Returns a specified artifact. |
| <CopyableCode code="projects_locations_artifacts_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns matching artifacts. |
| <CopyableCode code="projects_locations_apis_artifacts_create" /> | `INSERT` | <CopyableCode code="apisId, locationsId, projectsId" /> | Creates a specified artifact. |
| <CopyableCode code="projects_locations_apis_deployments_artifacts_create" /> | `INSERT` | <CopyableCode code="apisId, deploymentsId, locationsId, projectsId" /> | Creates a specified artifact. |
| <CopyableCode code="projects_locations_apis_versions_artifacts_create" /> | `INSERT` | <CopyableCode code="apisId, locationsId, projectsId, versionsId" /> | Creates a specified artifact. |
| <CopyableCode code="projects_locations_apis_versions_specs_artifacts_create" /> | `INSERT` | <CopyableCode code="apisId, locationsId, projectsId, specsId, versionsId" /> | Creates a specified artifact. |
| <CopyableCode code="projects_locations_artifacts_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a specified artifact. |
| <CopyableCode code="projects_locations_apis_artifacts_delete" /> | `DELETE` | <CopyableCode code="apisId, artifactsId, locationsId, projectsId" /> | Removes a specified artifact. |
| <CopyableCode code="projects_locations_apis_deployments_artifacts_delete" /> | `DELETE` | <CopyableCode code="apisId, artifactsId, deploymentsId, locationsId, projectsId" /> | Removes a specified artifact. |
| <CopyableCode code="projects_locations_apis_versions_artifacts_delete" /> | `DELETE` | <CopyableCode code="apisId, artifactsId, locationsId, projectsId, versionsId" /> | Removes a specified artifact. |
| <CopyableCode code="projects_locations_apis_versions_specs_artifacts_delete" /> | `DELETE` | <CopyableCode code="apisId, artifactsId, locationsId, projectsId, specsId, versionsId" /> | Removes a specified artifact. |
| <CopyableCode code="projects_locations_artifacts_delete" /> | `DELETE` | <CopyableCode code="artifactsId, locationsId, projectsId" /> | Removes a specified artifact. |
| <CopyableCode code="projects_locations_apis_artifacts_replace_artifact" /> | `REPLACE` | <CopyableCode code="apisId, artifactsId, locationsId, projectsId" /> | Used to replace a specified artifact. |
| <CopyableCode code="projects_locations_apis_deployments_artifacts_replace_artifact" /> | `REPLACE` | <CopyableCode code="apisId, artifactsId, deploymentsId, locationsId, projectsId" /> | Used to replace a specified artifact. |
| <CopyableCode code="projects_locations_apis_versions_artifacts_replace_artifact" /> | `REPLACE` | <CopyableCode code="apisId, artifactsId, locationsId, projectsId, versionsId" /> | Used to replace a specified artifact. |
| <CopyableCode code="projects_locations_apis_versions_specs_artifacts_replace_artifact" /> | `REPLACE` | <CopyableCode code="apisId, artifactsId, locationsId, projectsId, specsId, versionsId" /> | Used to replace a specified artifact. |
| <CopyableCode code="projects_locations_artifacts_replace_artifact" /> | `REPLACE` | <CopyableCode code="artifactsId, locationsId, projectsId" /> | Used to replace a specified artifact. |

## `SELECT` examples

Returns matching artifacts.

```sql
SELECT
name,
annotations,
contents,
createTime,
hash,
labels,
mimeType,
sizeBytes,
updateTime
FROM google.apigeeregistry.artifacts
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>artifacts</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.apigeeregistry.artifacts (
locationsId,
projectsId,
name,
createTime,
updateTime,
mimeType,
sizeBytes,
hash,
contents,
labels,
annotations
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ mimeType }}',
'{{ sizeBytes }}',
'{{ hash }}',
'{{ contents }}',
'{{ labels }}',
'{{ annotations }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: mimeType
      value: '{{ mimeType }}'
    - name: sizeBytes
      value: '{{ sizeBytes }}'
    - name: hash
      value: '{{ hash }}'
    - name: contents
      value: '{{ contents }}'
    - name: labels
      value: '{{ labels }}'
    - name: annotations
      value: '{{ annotations }}'

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>artifacts</code> resource.

```sql
/*+ update */
REPLACE google.apigeeregistry.artifacts
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
mimeType = '{{ mimeType }}',
sizeBytes = '{{ sizeBytes }}',
hash = '{{ hash }}',
contents = '{{ contents }}',
labels = '{{ labels }}',
annotations = '{{ annotations }}'
WHERE 
artifactsId = '{{ artifactsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>artifacts</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigeeregistry.artifacts
WHERE artifactsId = '{{ artifactsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

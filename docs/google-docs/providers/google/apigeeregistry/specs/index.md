---
title: specs
hide_title: false
hide_table_of_contents: false
keywords:
  - specs
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

Creates, updates, deletes, gets or lists a <code>specs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>specs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigeeregistry.specs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="description" /> | `string` | A detailed description. |
| <CopyableCode code="annotations" /> | `object` | Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts. |
| <CopyableCode code="contents" /> | `string` | Input only. The contents of the spec. Provided by API callers when specs are created or updated. To access the contents of a spec, use GetApiSpecContents. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation timestamp; when the spec resource was created. |
| <CopyableCode code="filename" /> | `string` | A possibly-hierarchical name used to refer to the spec from other specs. |
| <CopyableCode code="hash" /> | `string` | Output only. A SHA-256 hash of the spec's contents. If the spec is gzipped, this is the hash of the uncompressed spec. |
| <CopyableCode code="labels" /> | `object` | Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with `apigeeregistry.googleapis.com/` and cannot be changed. |
| <CopyableCode code="mimeType" /> | `string` | A style (format) descriptor for this spec that is specified as a [Media Type](https://en.wikipedia.org/wiki/Media_type). Possible values include `application/vnd.apigee.proto`, `application/vnd.apigee.openapi`, and `application/vnd.apigee.graphql`, with possible suffixes representing compression types. These hypothetical names are defined in the vendor tree defined in RFC6838 (https://tools.ietf.org/html/rfc6838) and are not final. Content types can specify compression. Currently only GZip compression is supported (indicated with "+gzip"). |
| <CopyableCode code="revisionCreateTime" /> | `string` | Output only. Revision creation timestamp; when the represented revision was created. |
| <CopyableCode code="revisionId" /> | `string` | Output only. Immutable. The revision ID of the spec. A new revision is committed whenever the spec contents are changed. The format is an 8-character hexadecimal string. |
| <CopyableCode code="revisionUpdateTime" /> | `string` | Output only. Last update timestamp: when the represented revision was last modified. |
| <CopyableCode code="sizeBytes" /> | `integer` | Output only. The size of the spec file in bytes. If the spec is gzipped, this is the size of the uncompressed spec. |
| <CopyableCode code="sourceUri" /> | `string` | The original source URI of the spec (if one exists). This is an external location that can be used for reference purposes but which may not be authoritative since this external resource may change after the spec is retrieved. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_apis_versions_specs_get" /> | `SELECT` | <CopyableCode code="apisId, locationsId, projectsId, specsId, versionsId" /> | Returns a specified spec. |
| <CopyableCode code="projects_locations_apis_versions_specs_list" /> | `SELECT` | <CopyableCode code="apisId, locationsId, projectsId, versionsId" /> | Returns matching specs. |
| <CopyableCode code="projects_locations_apis_versions_specs_create" /> | `INSERT` | <CopyableCode code="apisId, locationsId, projectsId, versionsId" /> | Creates a specified spec. |
| <CopyableCode code="projects_locations_apis_versions_specs_delete" /> | `DELETE` | <CopyableCode code="apisId, locationsId, projectsId, specsId, versionsId" /> | Removes a specified spec, all revisions, and all child resources (e.g., artifacts). |
| <CopyableCode code="projects_locations_apis_versions_specs_patch" /> | `UPDATE` | <CopyableCode code="apisId, locationsId, projectsId, specsId, versionsId" /> | Used to modify a specified spec. |
| <CopyableCode code="projects_locations_apis_versions_specs_rollback" /> | `EXEC` | <CopyableCode code="apisId, locationsId, projectsId, specsId, versionsId" /> | Sets the current revision to a specified prior revision. Note that this creates a new revision with a new revision ID. |
| <CopyableCode code="projects_locations_apis_versions_specs_tag_revision" /> | `EXEC` | <CopyableCode code="apisId, locationsId, projectsId, specsId, versionsId" /> | Adds a tag to a specified revision of a spec. |

## `SELECT` examples

Returns matching specs.

```sql
SELECT
name,
description,
annotations,
contents,
createTime,
filename,
hash,
labels,
mimeType,
revisionCreateTime,
revisionId,
revisionUpdateTime,
sizeBytes,
sourceUri
FROM google.apigeeregistry.specs
WHERE apisId = '{{ apisId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND versionsId = '{{ versionsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>specs</code> resource.

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
INSERT INTO google.apigeeregistry.specs (
apisId,
locationsId,
projectsId,
versionsId,
name,
filename,
description,
revisionId,
createTime,
revisionCreateTime,
revisionUpdateTime,
mimeType,
sizeBytes,
hash,
sourceUri,
contents,
labels,
annotations
)
SELECT 
'{{ apisId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ versionsId }}',
'{{ name }}',
'{{ filename }}',
'{{ description }}',
'{{ revisionId }}',
'{{ createTime }}',
'{{ revisionCreateTime }}',
'{{ revisionUpdateTime }}',
'{{ mimeType }}',
'{{ sizeBytes }}',
'{{ hash }}',
'{{ sourceUri }}',
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
    - name: filename
      value: '{{ filename }}'
    - name: description
      value: '{{ description }}'
    - name: revisionId
      value: '{{ revisionId }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: revisionCreateTime
      value: '{{ revisionCreateTime }}'
    - name: revisionUpdateTime
      value: '{{ revisionUpdateTime }}'
    - name: mimeType
      value: '{{ mimeType }}'
    - name: sizeBytes
      value: '{{ sizeBytes }}'
    - name: hash
      value: '{{ hash }}'
    - name: sourceUri
      value: '{{ sourceUri }}'
    - name: contents
      value: '{{ contents }}'
    - name: labels
      value: '{{ labels }}'
    - name: annotations
      value: '{{ annotations }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>specs</code> resource.

```sql
/*+ update */
UPDATE google.apigeeregistry.specs
SET 
name = '{{ name }}',
filename = '{{ filename }}',
description = '{{ description }}',
revisionId = '{{ revisionId }}',
createTime = '{{ createTime }}',
revisionCreateTime = '{{ revisionCreateTime }}',
revisionUpdateTime = '{{ revisionUpdateTime }}',
mimeType = '{{ mimeType }}',
sizeBytes = '{{ sizeBytes }}',
hash = '{{ hash }}',
sourceUri = '{{ sourceUri }}',
contents = '{{ contents }}',
labels = '{{ labels }}',
annotations = '{{ annotations }}'
WHERE 
apisId = '{{ apisId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND specsId = '{{ specsId }}'
AND versionsId = '{{ versionsId }}';
```

## `DELETE` example

Deletes the specified <code>specs</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigeeregistry.specs
WHERE apisId = '{{ apisId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND specsId = '{{ specsId }}'
AND versionsId = '{{ versionsId }}';
```

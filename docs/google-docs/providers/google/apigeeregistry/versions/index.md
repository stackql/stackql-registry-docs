---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
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

Creates, updates, deletes, gets or lists a <code>versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigeeregistry.versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="description" /> | `string` | A detailed description. |
| <CopyableCode code="annotations" /> | `object` | Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation timestamp. |
| <CopyableCode code="displayName" /> | `string` | Human-meaningful name. |
| <CopyableCode code="labels" /> | `object` | Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with `apigeeregistry.googleapis.com/` and cannot be changed. |
| <CopyableCode code="primarySpec" /> | `string` | The primary spec for this version. Format: projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec} |
| <CopyableCode code="state" /> | `string` | A user-definable description of the lifecycle phase of this API version. Format: free-form, but we expect single words that describe API maturity, e.g., "CONCEPT", "DESIGN", "DEVELOPMENT", "STAGING", "PRODUCTION", "DEPRECATED", "RETIRED". |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update timestamp. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_apis_versions_get" /> | `SELECT` | <CopyableCode code="apisId, locationsId, projectsId, versionsId" /> | Returns a specified version. |
| <CopyableCode code="projects_locations_apis_versions_list" /> | `SELECT` | <CopyableCode code="apisId, locationsId, projectsId" /> | Returns matching versions. |
| <CopyableCode code="projects_locations_apis_versions_create" /> | `INSERT` | <CopyableCode code="apisId, locationsId, projectsId" /> | Creates a specified version. |
| <CopyableCode code="projects_locations_apis_versions_delete" /> | `DELETE` | <CopyableCode code="apisId, locationsId, projectsId, versionsId" /> | Removes a specified version and all of the resources that it owns. |
| <CopyableCode code="projects_locations_apis_versions_patch" /> | `UPDATE` | <CopyableCode code="apisId, locationsId, projectsId, versionsId" /> | Used to modify a specified version. |

## `SELECT` examples

Returns matching versions.

```sql
SELECT
name,
description,
annotations,
createTime,
displayName,
labels,
primarySpec,
state,
updateTime
FROM google.apigeeregistry.versions
WHERE apisId = '{{ apisId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>versions</code> resource.

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
INSERT INTO google.apigeeregistry.versions (
apisId,
locationsId,
projectsId,
name,
displayName,
description,
createTime,
updateTime,
state,
labels,
annotations,
primarySpec
)
SELECT 
'{{ apisId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ state }}',
'{{ labels }}',
'{{ annotations }}',
'{{ primarySpec }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: description
      value: '{{ description }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: state
      value: '{{ state }}'
    - name: labels
      value: '{{ labels }}'
    - name: annotations
      value: '{{ annotations }}'
    - name: primarySpec
      value: '{{ primarySpec }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>versions</code> resource.

```sql
/*+ update */
UPDATE google.apigeeregistry.versions
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
state = '{{ state }}',
labels = '{{ labels }}',
annotations = '{{ annotations }}',
primarySpec = '{{ primarySpec }}'
WHERE 
apisId = '{{ apisId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND versionsId = '{{ versionsId }}';
```

## `DELETE` example

Deletes the specified <code>versions</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigeeregistry.versions
WHERE apisId = '{{ apisId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND versionsId = '{{ versionsId }}';
```

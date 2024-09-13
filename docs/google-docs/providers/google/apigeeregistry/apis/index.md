---
title: apis
hide_title: false
hide_table_of_contents: false
keywords:
  - apis
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

Creates, updates, deletes, gets or lists a <code>apis</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigeeregistry.apis" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="description" /> | `string` | A detailed description. |
| <CopyableCode code="annotations" /> | `object` | Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts. |
| <CopyableCode code="availability" /> | `string` | A user-definable description of the availability of this service. Format: free-form, but we expect single words that describe availability, e.g., "NONE", "TESTING", "PREVIEW", "GENERAL", "DEPRECATED", "SHUTDOWN". |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation timestamp. |
| <CopyableCode code="displayName" /> | `string` | Human-meaningful name. |
| <CopyableCode code="labels" /> | `object` | Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with `apigeeregistry.googleapis.com/` and cannot be changed. |
| <CopyableCode code="recommendedDeployment" /> | `string` | The recommended deployment of the API. Format: `projects/{project}/locations/{location}/apis/{api}/deployments/{deployment}` |
| <CopyableCode code="recommendedVersion" /> | `string` | The recommended version of the API. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}` |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update timestamp. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_apis_get" /> | `SELECT` | <CopyableCode code="apisId, locationsId, projectsId" /> | Returns a specified API. |
| <CopyableCode code="projects_locations_apis_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns matching APIs. |
| <CopyableCode code="projects_locations_apis_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a specified API. |
| <CopyableCode code="projects_locations_apis_delete" /> | `DELETE` | <CopyableCode code="apisId, locationsId, projectsId" /> | Removes a specified API and all of the resources that it owns. |
| <CopyableCode code="projects_locations_apis_patch" /> | `UPDATE` | <CopyableCode code="apisId, locationsId, projectsId" /> | Used to modify a specified API. |

## `SELECT` examples

Returns matching APIs.

```sql
SELECT
name,
description,
annotations,
availability,
createTime,
displayName,
labels,
recommendedDeployment,
recommendedVersion,
updateTime
FROM google.apigeeregistry.apis
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>apis</code> resource.

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
INSERT INTO google.apigeeregistry.apis (
locationsId,
projectsId,
name,
displayName,
description,
createTime,
updateTime,
availability,
recommendedVersion,
recommendedDeployment,
labels,
annotations
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ availability }}',
'{{ recommendedVersion }}',
'{{ recommendedDeployment }}',
'{{ labels }}',
'{{ annotations }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
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
      - name: availability
        value: '{{ availability }}'
      - name: recommendedVersion
        value: '{{ recommendedVersion }}'
      - name: recommendedDeployment
        value: '{{ recommendedDeployment }}'
      - name: labels
        value: '{{ labels }}'
      - name: annotations
        value: '{{ annotations }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>apis</code> resource.

```sql
/*+ update */
UPDATE google.apigeeregistry.apis
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
availability = '{{ availability }}',
recommendedVersion = '{{ recommendedVersion }}',
recommendedDeployment = '{{ recommendedDeployment }}',
labels = '{{ labels }}',
annotations = '{{ annotations }}'
WHERE 
apisId = '{{ apisId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>apis</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigeeregistry.apis
WHERE apisId = '{{ apisId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

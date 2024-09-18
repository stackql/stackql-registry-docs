---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
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

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigeeregistry.deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="description" /> | `string` | A detailed description. |
| <CopyableCode code="accessGuidance" /> | `string` | Text briefly describing how to access the endpoint. Changes to this value will not affect the revision. |
| <CopyableCode code="annotations" /> | `object` | Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts. |
| <CopyableCode code="apiSpecRevision" /> | `string` | The full resource name (including revision ID) of the spec of the API being served by the deployment. Changes to this value will update the revision. Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec@revision}` |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation timestamp; when the deployment resource was created. |
| <CopyableCode code="displayName" /> | `string` | Human-meaningful name. |
| <CopyableCode code="endpointUri" /> | `string` | The address where the deployment is serving. Changes to this value will update the revision. |
| <CopyableCode code="externalChannelUri" /> | `string` | The address of the external channel of the API (e.g., the Developer Portal). Changes to this value will not affect the revision. |
| <CopyableCode code="intendedAudience" /> | `string` | Text briefly identifying the intended audience of the API. Changes to this value will not affect the revision. |
| <CopyableCode code="labels" /> | `object` | Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with `apigeeregistry.googleapis.com/` and cannot be changed. |
| <CopyableCode code="revisionCreateTime" /> | `string` | Output only. Revision creation timestamp; when the represented revision was created. |
| <CopyableCode code="revisionId" /> | `string` | Output only. Immutable. The revision ID of the deployment. A new revision is committed whenever the deployment contents are changed. The format is an 8-character hexadecimal string. |
| <CopyableCode code="revisionUpdateTime" /> | `string` | Output only. Last update timestamp: when the represented revision was last modified. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_apis_deployments_get" /> | `SELECT` | <CopyableCode code="apisId, deploymentsId, locationsId, projectsId" /> | Returns a specified deployment. |
| <CopyableCode code="projects_locations_apis_deployments_list" /> | `SELECT` | <CopyableCode code="apisId, locationsId, projectsId" /> | Returns matching deployments. |
| <CopyableCode code="projects_locations_apis_deployments_create" /> | `INSERT` | <CopyableCode code="apisId, locationsId, projectsId" /> | Creates a specified deployment. |
| <CopyableCode code="projects_locations_apis_deployments_delete" /> | `DELETE` | <CopyableCode code="apisId, deploymentsId, locationsId, projectsId" /> | Removes a specified deployment, all revisions, and all child resources (e.g., artifacts). |
| <CopyableCode code="projects_locations_apis_deployments_patch" /> | `UPDATE` | <CopyableCode code="apisId, deploymentsId, locationsId, projectsId" /> | Used to modify a specified deployment. |
| <CopyableCode code="projects_locations_apis_deployments_rollback" /> | `EXEC` | <CopyableCode code="apisId, deploymentsId, locationsId, projectsId" /> | Sets the current revision to a specified prior revision. Note that this creates a new revision with a new revision ID. |
| <CopyableCode code="projects_locations_apis_deployments_tag_revision" /> | `EXEC` | <CopyableCode code="apisId, deploymentsId, locationsId, projectsId" /> | Adds a tag to a specified revision of a deployment. |

## `SELECT` examples

Returns matching deployments.

```sql
SELECT
name,
description,
accessGuidance,
annotations,
apiSpecRevision,
createTime,
displayName,
endpointUri,
externalChannelUri,
intendedAudience,
labels,
revisionCreateTime,
revisionId,
revisionUpdateTime
FROM google.apigeeregistry.deployments
WHERE apisId = '{{ apisId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployments</code> resource.

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
INSERT INTO google.apigeeregistry.deployments (
apisId,
locationsId,
projectsId,
name,
displayName,
description,
apiSpecRevision,
endpointUri,
externalChannelUri,
intendedAudience,
accessGuidance,
labels,
annotations
)
SELECT 
'{{ apisId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ apiSpecRevision }}',
'{{ endpointUri }}',
'{{ externalChannelUri }}',
'{{ intendedAudience }}',
'{{ accessGuidance }}',
'{{ labels }}',
'{{ annotations }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
displayName: string
description: string
revisionId: string
createTime: string
revisionCreateTime: string
revisionUpdateTime: string
apiSpecRevision: string
endpointUri: string
externalChannelUri: string
intendedAudience: string
accessGuidance: string
labels: object
annotations: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>deployments</code> resource.

```sql
/*+ update */
UPDATE google.apigeeregistry.deployments
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
apiSpecRevision = '{{ apiSpecRevision }}',
endpointUri = '{{ endpointUri }}',
externalChannelUri = '{{ externalChannelUri }}',
intendedAudience = '{{ intendedAudience }}',
accessGuidance = '{{ accessGuidance }}',
labels = '{{ labels }}',
annotations = '{{ annotations }}'
WHERE 
apisId = '{{ apisId }}'
AND deploymentsId = '{{ deploymentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>deployments</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigeeregistry.deployments
WHERE apisId = '{{ apisId }}'
AND deploymentsId = '{{ deploymentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

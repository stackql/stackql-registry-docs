---
title: deployments_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments_revisions
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

Creates, updates, deletes, gets or lists a <code>deployments_revisions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigeeregistry.deployments_revisions" /></td></tr>
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
| <CopyableCode code="projects_locations_apis_deployments_list_revisions" /> | `SELECT` | <CopyableCode code="apisId, deploymentsId, locationsId, projectsId" /> | Lists all revisions of a deployment. Revisions are returned in descending order of revision creation time. |

## `SELECT` examples

Lists all revisions of a deployment. Revisions are returned in descending order of revision creation time.

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
FROM google.apigeeregistry.deployments_revisions
WHERE apisId = '{{ apisId }}'
AND deploymentsId = '{{ deploymentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

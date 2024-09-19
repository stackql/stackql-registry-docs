---
title: issues
hide_title: false
hide_table_of_contents: false
keywords:
  - issues
  - contactcenterinsights
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

Creates, updates, deletes, gets or lists a <code>issues</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>issues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contactcenterinsights.issues" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the issue. Format: projects/{project}/locations/{location}/issueModels/{issue_model}/issues/{issue} |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which this issue was created. |
| <CopyableCode code="displayDescription" /> | `string` | Representative description of the issue. |
| <CopyableCode code="displayName" /> | `string` | The representative name for the issue. |
| <CopyableCode code="sampleUtterances" /> | `array` | Output only. Resource names of the sample representative utterances that match to this issue. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The most recent time that this issue was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="issueModelsId, issuesId, locationsId, projectsId" /> | Gets an issue. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="issueModelsId, locationsId, projectsId" /> | Lists issues. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="issueModelsId, issuesId, locationsId, projectsId" /> | Deletes an issue. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="issueModelsId, issuesId, locationsId, projectsId" /> | Updates an issue. |

## `SELECT` examples

Lists issues.

```sql
SELECT
name,
createTime,
displayDescription,
displayName,
sampleUtterances,
updateTime
FROM google.contactcenterinsights.issues
WHERE issueModelsId = '{{ issueModelsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `UPDATE` example

Updates a <code>issues</code> resource.

```sql
/*+ update */
UPDATE google.contactcenterinsights.issues
SET 
name = '{{ name }}',
displayDescription = '{{ displayDescription }}',
displayName = '{{ displayName }}'
WHERE 
issueModelsId = '{{ issueModelsId }}'
AND issuesId = '{{ issuesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>issues</code> resource.

```sql
/*+ delete */
DELETE FROM google.contactcenterinsights.issues
WHERE issueModelsId = '{{ issueModelsId }}'
AND issuesId = '{{ issuesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

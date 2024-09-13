---
title: changelogs
hide_title: false
hide_table_of_contents: false
keywords:
  - changelogs
  - dialogflow
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

Creates, updates, deletes, gets or lists a <code>changelogs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>changelogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.changelogs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique identifier of the changelog. Format: `projects//locations//agents//changelogs/`. |
| <CopyableCode code="action" /> | `string` | The action of the change. |
| <CopyableCode code="createTime" /> | `string` | The timestamp of the change. |
| <CopyableCode code="displayName" /> | `string` | The affected resource display name of the change. |
| <CopyableCode code="languageCode" /> | `string` | The affected language code of the change. |
| <CopyableCode code="resource" /> | `string` | The affected resource name of the change. |
| <CopyableCode code="type" /> | `string` | The affected resource type. |
| <CopyableCode code="userEmail" /> | `string` | Email address of the authenticated user. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_changelogs_get" /> | `SELECT` | <CopyableCode code="agentsId, changelogsId, locationsId, projectsId" /> | Retrieves the specified Changelog. |
| <CopyableCode code="projects_locations_agents_changelogs_list" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Returns the list of Changelogs. |

## `SELECT` examples

Returns the list of Changelogs.

```sql
SELECT
name,
action,
createTime,
displayName,
languageCode,
resource,
type,
userEmail
FROM google.dialogflow.changelogs
WHERE agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

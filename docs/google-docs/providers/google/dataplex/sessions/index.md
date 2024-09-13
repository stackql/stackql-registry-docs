---
title: sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - sessions
  - dataplex
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

Creates, updates, deletes, gets or lists a <code>sessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.sessions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the content, of the form: projects/{project_id}/locations/{location_id}/lakes/{lake_id}/environment/{environment_id}/sessions/{session_id} |
| <CopyableCode code="createTime" /> | `string` | Output only. Session start time. |
| <CopyableCode code="state" /> | `string` | Output only. State of Session |
| <CopyableCode code="userId" /> | `string` | Output only. Email of user running the session. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_lakes_environments_sessions_list" /> | `SELECT` | <CopyableCode code="environmentsId, lakesId, locationsId, projectsId" /> | Lists session resources in an environment. |

## `SELECT` examples

Lists session resources in an environment.

```sql
SELECT
name,
createTime,
state,
userId
FROM google.dataplex.sessions
WHERE environmentsId = '{{ environmentsId }}'
AND lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

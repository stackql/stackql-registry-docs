---
title: workspaces_git_ahead_behind
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces_git_ahead_behind
  - dataform
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

Creates, updates, deletes, gets or lists a <code>workspaces_git_ahead_behind</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces_git_ahead_behind</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataform.workspaces_git_ahead_behind" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="commitsAhead" /> | `integer` | The number of commits in the remote branch that are not in the workspace. |
| <CopyableCode code="commitsBehind" /> | `integer` | The number of commits in the workspace that are not in the remote branch. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_git_ahead_behind" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Fetches Git ahead/behind against a remote branch. |

## `SELECT` examples

Fetches Git ahead/behind against a remote branch.

```sql
SELECT
commitsAhead,
commitsBehind
FROM google.dataform.workspaces_git_ahead_behind
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'
AND workspacesId = '{{ workspacesId }}'; 
```

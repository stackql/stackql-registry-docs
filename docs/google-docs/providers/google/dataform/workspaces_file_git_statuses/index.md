---
title: workspaces_file_git_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces_file_git_statuses
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

Creates, updates, deletes, gets or lists a <code>workspaces_file_git_statuses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces_file_git_statuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataform.workspaces_file_git_statuses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="uncommittedFileChanges" /> | `array` | A list of all files which have uncommitted Git changes. There will only be a single entry for any given file. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_file_git_statuses" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Fetches Git statuses for the files in a Workspace. |

## `SELECT` examples

Fetches Git statuses for the files in a Workspace.

```sql
SELECT
uncommittedFileChanges
FROM google.dataform.workspaces_file_git_statuses
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'
AND workspacesId = '{{ workspacesId }}'; 
```

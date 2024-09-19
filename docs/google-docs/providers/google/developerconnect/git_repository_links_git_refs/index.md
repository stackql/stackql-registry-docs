---
title: git_repository_links_git_refs
hide_title: false
hide_table_of_contents: false
keywords:
  - git_repository_links_git_refs
  - developerconnect
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

Creates, updates, deletes, gets or lists a <code>git_repository_links_git_refs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>git_repository_links_git_refs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.developerconnect.git_repository_links_git_refs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextPageToken" /> | `string` | A token identifying a page of results the server should return. |
| <CopyableCode code="refNames" /> | `array` | Name of the refs fetched. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_git_refs" /> | `SELECT` | <CopyableCode code="connectionsId, gitRepositoryLinksId, locationsId, projectsId" /> | Fetch the list of branches or tags for a given repository. |

## `SELECT` examples

Fetch the list of branches or tags for a given repository.

```sql
SELECT
nextPageToken,
refNames
FROM google.developerconnect.git_repository_links_git_refs
WHERE connectionsId = '{{ connectionsId }}'
AND gitRepositoryLinksId = '{{ gitRepositoryLinksId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

---
title: repositories_git_refs
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories_git_refs
  - cloudbuild
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

Creates, updates, deletes, gets or lists a <code>repositories_git_refs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repositories_git_refs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudbuild.repositories_git_refs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextPageToken" /> | `string` | A token identifying a page of results the server should return. |
| <CopyableCode code="refNames" /> | `array` | Name of the refs fetched. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_connections_repositories_fetch_git_refs" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId, repositoriesId" /> | Fetch the list of branches or tags for a given repository. |

## `SELECT` examples

Fetch the list of branches or tags for a given repository.

```sql
SELECT
nextPageToken,
refNames
FROM google.cloudbuild.repositories_git_refs
WHERE connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}';
```

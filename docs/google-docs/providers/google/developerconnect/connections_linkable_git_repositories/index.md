
---
title: connections_linkable_git_repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - connections_linkable_git_repositories
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

Creates, updates, deletes or gets an <code>connections_linkable_git_repository</code> resource or lists <code>connections_linkable_git_repositories</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections_linkable_git_repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.developerconnect.connections_linkable_git_repositories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="linkableGitRepositories" /> | `array` | The git repositories that can be linked to the connection. |
| <CopyableCode code="nextPageToken" /> | `string` | A token identifying a page of results the server should return. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_linkable_git_repositories" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | FetchLinkableGitRepositories returns a list of git repositories from an SCM that are available to be added to a Connection. |

## `SELECT` examples

FetchLinkableGitRepositories returns a list of git repositories from an SCM that are available to be added to a Connection.

```sql
SELECT
linkableGitRepositories,
nextPageToken
FROM google.developerconnect.connections_linkable_git_repositories
WHERE connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

---
title: git_repository_links_read_write_token
hide_title: false
hide_table_of_contents: false
keywords:
  - git_repository_links_read_write_token
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

Creates, updates, deletes or gets an <code>git_repository_links_read_write_token</code> resource or lists <code>git_repository_links_read_write_token</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>git_repository_links_read_write_token</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.developerconnect.git_repository_links_read_write_token" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="expirationTime" /> | `string` | Expiration timestamp. Can be empty if unknown or non-expiring. |
| <CopyableCode code="gitUsername" /> | `string` | The git_username to specify when making a git clone with the token. For example, for GitHub GitRepositoryLinks, this would be "x-access-token" |
| <CopyableCode code="token" /> | `string` | The token content. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_read_write_token" /> | `SELECT` | <CopyableCode code="connectionsId, gitRepositoryLinksId, locationsId, projectsId" /> | Fetches read/write token of a given gitRepositoryLink. |

## `SELECT` examples

Fetches read/write token of a given gitRepositoryLink.

```sql
SELECT
expirationTime,
gitUsername,
token
FROM google.developerconnect.git_repository_links_read_write_token
WHERE connectionsId = '{{ connectionsId }}'
AND gitRepositoryLinksId = '{{ gitRepositoryLinksId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

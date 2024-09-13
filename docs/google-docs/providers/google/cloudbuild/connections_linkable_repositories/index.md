---
title: connections_linkable_repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - connections_linkable_repositories
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

Creates, updates, deletes or gets an <code>connections_linkable_repository</code> resource or lists <code>connections_linkable_repositories</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections_linkable_repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudbuild.connections_linkable_repositories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextPageToken" /> | `string` | A token identifying a page of results the server should return. |
| <CopyableCode code="repositories" /> | `array` | repositories ready to be created. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_connections_fetch_linkable_repositories" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | FetchLinkableRepositories get repositories from SCM that are accessible and could be added to the connection. |

## `SELECT` examples

FetchLinkableRepositories get repositories from SCM that are accessible and could be added to the connection.

```sql
SELECT
nextPageToken,
repositories
FROM google.cloudbuild.connections_linkable_repositories
WHERE connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

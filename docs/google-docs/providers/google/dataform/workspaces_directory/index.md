---
title: workspaces_directory
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces_directory
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

Creates, updates, deletes or gets an <code>workspaces_directory</code> resource or lists <code>workspaces_directory</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces_directory</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataform.workspaces_directory" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="remove_directory" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Deletes a directory (inside a Workspace) and all of its contents. |

## `DELETE` example

Deletes the specified workspaces_directory resource.

```sql
DELETE FROM google.dataform.workspaces_directory
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'
AND workspacesId = '{{ workspacesId }}';
```

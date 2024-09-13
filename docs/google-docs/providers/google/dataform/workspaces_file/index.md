---
title: workspaces_file
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces_file
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

Creates, updates, deletes or gets an <code>workspaces_file</code> resource or lists <code>workspaces_file</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces_file</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataform.workspaces_file" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="remove_file" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Deletes a file (inside a Workspace). |

## `DELETE` example

Deletes the specified workspaces_file resource.

```sql
DELETE FROM google.dataform.workspaces_file
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'
AND workspacesId = '{{ workspacesId }}';
```

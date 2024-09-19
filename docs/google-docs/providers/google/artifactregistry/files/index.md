---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
  - artifactregistry
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

Creates, updates, deletes, gets or lists a <code>files</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.artifactregistry.files" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the file, for example: `projects/p1/locations/us-central1/repositories/repo1/files/a%2Fb%2Fc.txt`. If the file ID part contains slashes, they are escaped. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the File was created. |
| <CopyableCode code="fetchTime" /> | `string` | Output only. The time when the last attempt to refresh the file's data was made. Only set when the repository is remote. |
| <CopyableCode code="hashes" /> | `array` | The hashes of the file content. |
| <CopyableCode code="owner" /> | `string` | The name of the Package or Version that owns this file, if any. |
| <CopyableCode code="sizeBytes" /> | `string` | The size of the File in bytes. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the File was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="filesId, locationsId, projectsId, repositoriesId" /> | Gets a file. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Lists files. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="filesId, locationsId, projectsId, repositoriesId" /> | Deletes a file and all of its content. It is only allowed on generic repositories. The returned operation will complete once the file has been deleted. |
| <CopyableCode code="download" /> | `EXEC` | <CopyableCode code="filesId, locationsId, projectsId, repositoriesId" /> | Download a file. |

## `SELECT` examples

Lists files.

```sql
SELECT
name,
createTime,
fetchTime,
hashes,
owner,
sizeBytes,
updateTime
FROM google.artifactregistry.files
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}';
```

## `DELETE` example

Deletes the specified <code>files</code> resource.

```sql
/*+ delete */
DELETE FROM google.artifactregistry.files
WHERE filesId = '{{ filesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}';
```

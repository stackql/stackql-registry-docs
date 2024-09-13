---
title: packages
hide_title: false
hide_table_of_contents: false
keywords:
  - packages
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

Creates, updates, deletes, gets or lists a <code>packages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.artifactregistry.packages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the package, for example: `projects/p1/locations/us-central1/repositories/repo1/packages/pkg1`. If the package ID part contains slashes, the slashes are escaped. |
| <CopyableCode code="annotations" /> | `object` | Optional. Client specified annotations. |
| <CopyableCode code="createTime" /> | `string` | The time when the package was created. |
| <CopyableCode code="displayName" /> | `string` | The display name of the package. |
| <CopyableCode code="updateTime" /> | `string` | The time when the package was last updated. This includes publishing a new version of the package. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId" /> | Gets a package. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Lists packages. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId" /> | Deletes a package and all of its versions and tags. The returned operation will complete once the package has been deleted. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId" /> | Updates a package. |

## `SELECT` examples

Lists packages.

```sql
SELECT
name,
annotations,
createTime,
displayName,
updateTime
FROM google.artifactregistry.packages
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'; 
```

## `UPDATE` example

Updates a <code>packages</code> resource.

```sql
/*+ update */
UPDATE google.artifactregistry.packages
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
annotations = '{{ annotations }}'
WHERE 
locationsId = '{{ locationsId }}'
AND packagesId = '{{ packagesId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}';
```

## `DELETE` example

Deletes the specified <code>packages</code> resource.

```sql
/*+ delete */
DELETE FROM google.artifactregistry.packages
WHERE locationsId = '{{ locationsId }}'
AND packagesId = '{{ packagesId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}';
```

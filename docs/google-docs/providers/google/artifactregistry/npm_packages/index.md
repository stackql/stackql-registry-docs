---
title: npm_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - npm_packages
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

Creates, updates, deletes, gets or lists a <code>npm_packages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>npm_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.artifactregistry.npm_packages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. registry_location, project_id, repository_name and npm_package forms a unique package For example, "projects/test-project/locations/us-west4/repositories/test-repo/npmPackages/ npm_test:1.0.0", where "us-west4" is the registry_location, "test-project" is the project_id, "test-repo" is the repository_name and npm_test:1.0.0" is the npm package. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time the package was created. |
| <CopyableCode code="packageName" /> | `string` | Package for the artifact. |
| <CopyableCode code="tags" /> | `array` | Tags attached to this package. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time the package was updated. |
| <CopyableCode code="version" /> | `string` | Version of this package. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, npmPackagesId, projectsId, repositoriesId" /> | Gets a npm package. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Lists npm packages. |

## `SELECT` examples

Lists npm packages.

```sql
SELECT
name,
createTime,
packageName,
tags,
updateTime,
version
FROM google.artifactregistry.npm_packages
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'; 
```

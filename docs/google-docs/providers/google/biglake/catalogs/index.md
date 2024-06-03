---
title: catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs
  - biglake
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.biglake.catalogs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name. Format: projects/&#123;project_id_or_number&#125;/locations/&#123;location_id&#125;/catalogs/&#123;catalog_id&#125; |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time of the catalog. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The deletion time of the catalog. Only set after the catalog is deleted. |
| <CopyableCode code="expireTime" /> | `string` | Output only. The time when this catalog is considered expired. Only set after the catalog is deleted. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last modification time of the catalog. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Gets the catalog specified by the resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List all catalogs in a specified project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new catalog. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Deletes an existing catalog specified by the catalog ID. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | List all catalogs in a specified project. |

---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
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
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="biglake.databases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name. Format: projects/&#123;project_id_or_number&#125;/locations/&#123;location_id&#125;/catalogs/&#123;catalog_id&#125;/databases/&#123;database_id&#125; |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time of the database. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The deletion time of the database. Only set after the database is deleted. |
| <CopyableCode code="expireTime" /> | `string` | Output only. The time when this database is considered expired. Only set after the database is deleted. |
| <CopyableCode code="hiveOptions" /> | `object` | Options of a Hive database. |
| <CopyableCode code="type" /> | `string` | The database type. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last modification time of the database. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId" /> | Gets the database specified by the resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | List all databases in a specified catalog. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Creates a new database. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId" /> | Deletes an existing database specified by the database ID. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | List all databases in a specified catalog. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId" /> | Updates an existing database specified by the database ID. |

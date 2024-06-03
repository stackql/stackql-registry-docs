---
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
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
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.biglake.tables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name. Format: projects/&#123;project_id_or_number&#125;/locations/&#123;location_id&#125;/catalogs/&#123;catalog_id&#125;/databases/&#123;database_id&#125;/tables/&#123;table_id&#125; |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time of the table. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. The deletion time of the table. Only set after the table is deleted. |
| <CopyableCode code="etag" /> | `string` | The checksum of a table object computed by the server based on the value of other fields. It may be sent on update requests to ensure the client has an up-to-date value before proceeding. It is only checked for update table operations. |
| <CopyableCode code="expireTime" /> | `string` | Output only. The time when this table is considered expired. Only set after the table is deleted. |
| <CopyableCode code="hiveOptions" /> | `object` | Options of a Hive table. |
| <CopyableCode code="type" /> | `string` | The table type. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last modification time of the table. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId, tablesId" /> | Gets the table specified by the resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId" /> | List all tables in a specified database. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId" /> | Creates a new table. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId, tablesId" /> | Deletes an existing table specified by the table ID. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId, tablesId" /> | Updates an existing table specified by the table ID. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId" /> | List all tables in a specified database. |
| <CopyableCode code="rename" /> | `EXEC` | <CopyableCode code="catalogsId, databasesId, locationsId, projectsId, tablesId" /> | Renames an existing table specified by the table ID. |

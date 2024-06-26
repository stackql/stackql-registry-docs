---
title: migrations
hide_title: false
hide_table_of_contents: false
keywords:
  - migrations
  - databases
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>migrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.migrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the most recent migration. |
| <CopyableCode code="created_at" /> | `string` | The time the migration was initiated, in ISO 8601 format. |
| <CopyableCode code="status" /> | `string` | The current status of the migration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_migrationStatus" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | To retrieve the status of the most recent online migration, send a GET request to `/v2/databases/$DATABASE_ID/online-migration`.  |
| <CopyableCode code="delete_onlineMigration" /> | `DELETE` | <CopyableCode code="database_cluster_uuid, migration_id" /> | To stop an online migration, send a DELETE request to `/v2/databases/$DATABASE_ID/online-migration/$MIGRATION_ID`.<br /><br />A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed.<br /> |
| <CopyableCode code="update_onlineMigration" /> | `EXEC` | <CopyableCode code="database_cluster_uuid" /> | To start an online migration, send a PUT request to `/v2/databases/$DATABASE_ID/online-migration` endpoint. Migrating a cluster establishes a connection with an existing cluster and replicates its contents to the target cluster. Online migration is only available for MySQL, PostgreSQL, and Redis clusters. |
| <CopyableCode code="update_region" /> | `EXEC` | <CopyableCode code="database_cluster_uuid, data__region" /> | To migrate a database cluster to a new region, send a `PUT` request to<br />`/v2/databases/$DATABASE_ID/migrate`. The body of the request must specify a<br />`region` attribute.<br /><br />A successful request will receive a 202 Accepted status code with no body in<br />response. Querying the database cluster will show that its `status` attribute<br />will now be set to `migrating`. This will transition back to `online` when the<br />migration has completed.<br /> |

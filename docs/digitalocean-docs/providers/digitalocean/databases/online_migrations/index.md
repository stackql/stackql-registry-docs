---
title: online_migrations
hide_title: false
hide_table_of_contents: false
keywords:
  - online_migrations
  - databases
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>online_migrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>online_migrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.online_migrations" /></td></tr>
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
| <CopyableCode code="databases_get_migration_status" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | To retrieve the status of the most recent online migration, send a GET request to `/v2/databases/$DATABASE_ID/online-migration`. |
| <CopyableCode code="databases_delete_online_migration" /> | `DELETE` | <CopyableCode code="database_cluster_uuid, migration_id" /> | To stop an online migration, send a DELETE request to `/v2/databases/$DATABASE_ID/online-migration/$MIGRATION_ID`. A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. |
| <CopyableCode code="databases_update_online_migration" /> | `EXEC` | <CopyableCode code="database_cluster_uuid" /> | To start an online migration, send a PUT request to `/v2/databases/$DATABASE_ID/online-migration` endpoint. Migrating a cluster establishes a connection with an existing cluster and replicates its contents to the target cluster. Online migration is only available for MySQL, PostgreSQL, and Redis clusters. |

## `SELECT` examples

To retrieve the status of the most recent online migration, send a GET request to `/v2/databases/$DATABASE_ID/online-migration`.


```sql
SELECT
id,
created_at,
status
FROM digitalocean.databases.online_migrations
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}';
```
## `DELETE` example

Deletes the specified <code>online_migrations</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.databases.online_migrations
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}'
AND migration_id = '{{ migration_id }}';
```

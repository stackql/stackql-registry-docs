---
title: indexes
hide_title: false
hide_table_of_contents: false
keywords:
  - indexes
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

Creates, updates, deletes, gets or lists a <code>indexes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>indexes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.indexes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="databases_list_opeasearch_indexes" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | To list all of a OpenSearch cluster's indexes, send a GET request to `/v2/databases/$DATABASE_ID/indexes`. The result will be a JSON object with a `indexes` key. |
| <CopyableCode code="databases_delete_opensearch_index" /> | `DELETE` | <CopyableCode code="database_cluster_uuid, index_name" /> | To delete a single index within OpenSearch cluster, send a DELETE request to `/v2/databases/$DATABASE_ID/indexes/$INDEX_NAME`. A status of 204 will be given. This indicates that the request was processed successfully, but that no response body is needed. |

## `SELECT` examples

To list all of a OpenSearch cluster's indexes, send a GET request to `/v2/databases/$DATABASE_ID/indexes`. The result will be a JSON object with a `indexes` key.


```sql
SELECT
column_anon
FROM digitalocean.databases.indexes
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}';
```
## `DELETE` example

Deletes the specified <code>indexes</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.databases.indexes
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}'
AND index_name = '{{ index_name }}';
```

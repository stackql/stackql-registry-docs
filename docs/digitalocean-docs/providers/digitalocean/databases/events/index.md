---
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
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

Creates, updates, deletes, gets or lists a <code>events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.databases.events" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="databases_list_events_logs" /> | `SELECT` | <CopyableCode code="database_cluster_uuid" /> | To list all of the cluster events, send a GET request to `/v2/databases/$DATABASE_ID/events`. The result will be a JSON object with a `events` key. |

## `SELECT` examples

To list all of the cluster events, send a GET request to `/v2/databases/$DATABASE_ID/events`. The result will be a JSON object with a `events` key.


```sql
SELECT
column_anon
FROM digitalocean.databases.events
WHERE database_cluster_uuid = '{{ database_cluster_uuid }}';
```
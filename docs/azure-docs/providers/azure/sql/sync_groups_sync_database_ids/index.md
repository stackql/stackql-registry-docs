---
title: sync_groups_sync_database_ids
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_groups_sync_database_ids
  - sql
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

Creates, updates, deletes, gets or lists a <code>sync_groups_sync_database_ids</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_groups_sync_database_ids</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.sync_groups_sync_database_ids" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ARM resource id of sync database. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> | Gets a collection of sync database ids. |

## `SELECT` examples

Gets a collection of sync database ids.


```sql
SELECT
id
FROM azure.sql.sync_groups_sync_database_ids
WHERE locationName = '{{ locationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
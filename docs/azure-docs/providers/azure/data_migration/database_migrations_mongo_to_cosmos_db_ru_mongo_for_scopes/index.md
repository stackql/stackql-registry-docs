---
title: database_migrations_mongo_to_cosmos_db_ru_mongo_for_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - database_migrations_mongo_to_cosmos_db_ru_mongo_for_scopes
  - data_migration
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

Creates, updates, deletes, gets or lists a <code>database_migrations_mongo_to_cosmos_db_ru_mongo_for_scopes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_migrations_mongo_to_cosmos_db_ru_mongo_for_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.database_migrations_mongo_to_cosmos_db_ru_mongo_for_scopes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | Database Migration Resource properties for CosmosDb for Mongo. |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="type" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, targetResourceName" /> | Get Database Migration resources for the scope. |

## `SELECT` examples

Get Database Migration resources for the scope.


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_migration.database_migrations_mongo_to_cosmos_db_ru_mongo_for_scopes
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND targetResourceName = '{{ targetResourceName }}';
```
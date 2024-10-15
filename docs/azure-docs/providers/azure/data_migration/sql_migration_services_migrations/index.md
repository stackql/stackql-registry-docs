---
title: sql_migration_services_migrations
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_migration_services_migrations
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

Creates, updates, deletes, gets or lists a <code>sql_migration_services_migrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_migration_services_migrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.sql_migration_services_migrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | Database Migration Resource properties. |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="type" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlMigrationServiceName, subscriptionId" /> | Retrieve the List of database migrations attached to the service. |

## `SELECT` examples

Retrieve the List of database migrations attached to the service.


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_migration.sql_migration_services_migrations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlMigrationServiceName = '{{ sqlMigrationServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
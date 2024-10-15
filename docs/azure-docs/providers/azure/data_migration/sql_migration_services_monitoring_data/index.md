---
title: sql_migration_services_monitoring_data
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_migration_services_monitoring_data
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

Creates, updates, deletes, gets or lists a <code>sql_migration_services_monitoring_data</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_migration_services_monitoring_data</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.sql_migration_services_monitoring_data" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of Integration Runtime. |
| <CopyableCode code="nodes" /> | `array` | Integration Runtime node monitoring data. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlMigrationServiceName, subscriptionId" /> | Retrieve the registered Integration Runtime nodes and their monitoring data for a given Database Migration Service. |

## `SELECT` examples

Retrieve the registered Integration Runtime nodes and their monitoring data for a given Database Migration Service.


```sql
SELECT
name,
nodes
FROM azure.data_migration.sql_migration_services_monitoring_data
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlMigrationServiceName = '{{ sqlMigrationServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
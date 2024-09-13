---
title: migration_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - migration_executions
  - metastore
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

Creates, updates, deletes, gets or lists a <code>migration_executions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>migration_executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.metastore.migration_executions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the migration execution, in the following form: projects/{project_number}/locations/{location_id}/services/{service_id}/migrationExecutions/{migration_execution_id} |
| <CopyableCode code="cloudSqlMigrationConfig" /> | `object` | Configuration information for migrating from self-managed hive metastore on Google Cloud using Cloud SQL as the backend database to Dataproc Metastore. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the migration execution was started. |
| <CopyableCode code="endTime" /> | `string` | Output only. The time when the migration execution finished. |
| <CopyableCode code="phase" /> | `string` | Output only. The current phase of the migration execution. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the migration execution. |
| <CopyableCode code="stateMessage" /> | `string` | Output only. Additional information about the current state of the migration execution. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, migrationExecutionsId, projectsId, servicesId" /> | Gets details of a single migration execution. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Lists migration executions on a service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, migrationExecutionsId, projectsId, servicesId" /> | Deletes a single migration execution. |

## `SELECT` examples

Lists migration executions on a service.

```sql
SELECT
name,
cloudSqlMigrationConfig,
createTime,
endTime,
phase,
state,
stateMessage
FROM google.metastore.migration_executions
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}'; 
```

## `DELETE` example

Deletes the specified <code>migration_executions</code> resource.

```sql
/*+ delete */
DELETE FROM google.metastore.migration_executions
WHERE locationsId = '{{ locationsId }}'
AND migrationExecutionsId = '{{ migrationExecutionsId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```

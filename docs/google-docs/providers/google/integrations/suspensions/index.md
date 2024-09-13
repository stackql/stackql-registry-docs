---
title: suspensions
hide_title: false
hide_table_of_contents: false
keywords:
  - suspensions
  - integrations
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

Creates, updates, deletes, gets or lists a <code>suspensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>suspensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.suspensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name for suspensions suspension/{suspension_id} |
| <CopyableCode code="approvalConfig" /> | `object` | Configurations for approving the Suspension. |
| <CopyableCode code="audit" /> | `object` | Contains when and by whom the suspension was resolved. |
| <CopyableCode code="createTime" /> | `string` | Output only. Auto-generated. |
| <CopyableCode code="eventExecutionInfoId" /> | `string` | Required. ID of the associated execution. |
| <CopyableCode code="integration" /> | `string` | Required. The name of the originating integration. |
| <CopyableCode code="lastModifyTime" /> | `string` | Output only. Auto-generated. |
| <CopyableCode code="state" /> | `string` | Required. State of this suspension, indicating what action a resolver has taken. |
| <CopyableCode code="suspensionConfig" /> | `object` |  |
| <CopyableCode code="taskId" /> | `string` | Required. Task id of the associated SuspensionTask. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_integrations_executions_suspensions_list" /> | `SELECT` | <CopyableCode code="executionsId, integrationsId, locationsId, projectsId" /> | * Lists suspensions associated with a specific execution. Only those with permissions to resolve the relevant suspensions will be able to view them. |
| <CopyableCode code="projects_locations_products_integrations_executions_suspensions_list" /> | `SELECT` | <CopyableCode code="executionsId, integrationsId, locationsId, productsId, projectsId" /> | * Lists suspensions associated with a specific execution. Only those with permissions to resolve the relevant suspensions will be able to view them. |
| <CopyableCode code="projects_locations_integrations_executions_suspensions_lift" /> | `EXEC` | <CopyableCode code="executionsId, integrationsId, locationsId, projectsId, suspensionsId" /> | * Lifts suspension for the Suspension task. Fetch corresponding suspension with provided suspension Id, resolve suspension, and set up suspension result for the Suspension Task. |
| <CopyableCode code="projects_locations_integrations_executions_suspensions_resolve" /> | `EXEC` | <CopyableCode code="executionsId, integrationsId, locationsId, projectsId, suspensionsId" /> | * Resolves (lifts/rejects) any number of suspensions. If the integration is already running, only the status of the suspension is updated. Otherwise, the suspended integration will begin execution again. |
| <CopyableCode code="projects_locations_products_integrations_executions_suspensions_lift" /> | `EXEC` | <CopyableCode code="executionsId, integrationsId, locationsId, productsId, projectsId, suspensionsId" /> | * Lifts suspension for the Suspension task. Fetch corresponding suspension with provided suspension Id, resolve suspension, and set up suspension result for the Suspension Task. |
| <CopyableCode code="projects_locations_products_integrations_executions_suspensions_resolve" /> | `EXEC` | <CopyableCode code="executionsId, integrationsId, locationsId, productsId, projectsId, suspensionsId" /> | * Resolves (lifts/rejects) any number of suspensions. If the integration is already running, only the status of the suspension is updated. Otherwise, the suspended integration will begin execution again. |

## `SELECT` examples

* Lists suspensions associated with a specific execution. Only those with permissions to resolve the relevant suspensions will be able to view them.

```sql
SELECT
name,
approvalConfig,
audit,
createTime,
eventExecutionInfoId,
integration,
lastModifyTime,
state,
suspensionConfig,
taskId
FROM google.integrations.suspensions
WHERE executionsId = '{{ executionsId }}'
AND integrationsId = '{{ integrationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

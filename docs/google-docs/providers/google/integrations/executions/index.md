---
title: executions
hide_title: false
hide_table_of_contents: false
keywords:
  - executions
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

Creates, updates, deletes, gets or lists a <code>executions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.executions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Auto-generated primary key. |
| <CopyableCode code="cloudLoggingDetails" /> | `object` | Cloud Logging details for execution info |
| <CopyableCode code="createTime" /> | `string` | Output only. Created time of the execution. |
| <CopyableCode code="directSubExecutions" /> | `array` | Direct sub executions of the following Execution. |
| <CopyableCode code="eventExecutionDetails" /> | `object` | Contains the details of the execution info of this event: this includes the tasks execution details plus the event execution statistics. Next available id: 12 |
| <CopyableCode code="executionDetails" /> | `object` | Contains the details of the execution info: this includes the tasks execution details plus the event execution statistics. |
| <CopyableCode code="executionMethod" /> | `string` | The ways user posts this event. |
| <CopyableCode code="integrationVersionState" /> | `string` | Output only. State of the integration version |
| <CopyableCode code="replayInfo" /> | `object` | Contains the details of the execution info: this includes the replay reason and replay tree connecting executions in a parent-child relationship |
| <CopyableCode code="requestParameters" /> | `object` | Event parameters come in as part of the request. |
| <CopyableCode code="requestParams" /> | `array` | Event parameters come in as part of the request. |
| <CopyableCode code="responseParameters" /> | `object` | Event parameters returned as part of the response. |
| <CopyableCode code="responseParams" /> | `array` | Event parameters come out as part of the response. |
| <CopyableCode code="snapshotNumber" /> | `string` | Output only. An increasing sequence that is set when a new snapshot is created |
| <CopyableCode code="triggerId" /> | `string` | The trigger id of the integration trigger config. If both trigger_id and client_id is present, the integration is executed from the start tasks provided by the matching trigger config otherwise it is executed from the default start tasks. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last modified time of the execution. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_integrations_executions_get" /> | `SELECT` | <CopyableCode code="executionsId, integrationsId, locationsId, projectsId" /> | Get an execution in the specified project. |
| <CopyableCode code="projects_locations_integrations_executions_list" /> | `SELECT` | <CopyableCode code="integrationsId, locationsId, projectsId" /> | Lists the results of all the integration executions. The response includes the same information as the [execution log](https://cloud.google.com/application-integration/docs/viewing-logs) in the Integration UI. |
| <CopyableCode code="projects_locations_products_integrations_executions_get" /> | `SELECT` | <CopyableCode code="executionsId, integrationsId, locationsId, productsId, projectsId" /> | Get an execution in the specified project. |
| <CopyableCode code="projects_locations_products_integrations_executions_list" /> | `SELECT` | <CopyableCode code="integrationsId, locationsId, productsId, projectsId" /> | Lists the results of all the integration executions. The response includes the same information as the [execution log](https://cloud.google.com/application-integration/docs/viewing-logs) in the Integration UI. |
| <CopyableCode code="projects_locations_integrations_executions_download" /> | `EXEC` | <CopyableCode code="executionsId, integrationsId, locationsId, projectsId" /> | Download the execution. |
| <CopyableCode code="projects_locations_products_integrations_executions_download" /> | `EXEC` | <CopyableCode code="executionsId, integrationsId, locationsId, productsId, projectsId" /> | Download the execution. |

## `SELECT` examples

Lists the results of all the integration executions. The response includes the same information as the [execution log](https://cloud.google.com/application-integration/docs/viewing-logs) in the Integration UI.

```sql
SELECT
name,
cloudLoggingDetails,
createTime,
directSubExecutions,
eventExecutionDetails,
executionDetails,
executionMethod,
integrationVersionState,
replayInfo,
requestParameters,
requestParams,
responseParameters,
responseParams,
snapshotNumber,
triggerId,
updateTime
FROM google.integrations.executions
WHERE integrationsId = '{{ integrationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

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
| <CopyableCode code="createTime" /> | `string` | Output only. Created time of the execution. |
| <CopyableCode code="directSubExecutions" /> | `array` | Direct sub executions of the following Execution. |
| <CopyableCode code="eventExecutionDetails" /> | `object` | Contains the details of the execution info of this event: this includes the tasks execution details plus the event execution statistics. Next available id: 10 |
| <CopyableCode code="executionDetails" /> | `object` | Contains the details of the execution info: this includes the tasks execution details plus the event execution statistics. |
| <CopyableCode code="executionMethod" /> | `string` | The ways user posts this event. |
| <CopyableCode code="requestParameters" /> | `object` | Event parameters come in as part of the request. |
| <CopyableCode code="requestParams" /> | `array` | Event parameters come in as part of the request. |
| <CopyableCode code="responseParameters" /> | `object` | Event parameters returned as part of the response. |
| <CopyableCode code="responseParams" /> | `array` | Event parameters come out as part of the response. |
| <CopyableCode code="triggerId" /> | `string` | The trigger id of the integration trigger config. If both trigger_id and client_id is present, the integration is executed from the start tasks provided by the matching trigger config otherwise it is executed from the default start tasks. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last modified time of the execution. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_integrations_executions_list" /> | `SELECT` | <CopyableCode code="integrationsId, locationsId, projectsId" /> | Lists the results of all the integration executions. The response includes the same information as the [execution log](https://cloud.google.com/application-integration/docs/viewing-logs) in the Integration UI. |
| <CopyableCode code="projects_locations_products_integrations_executions_get" /> | `SELECT` | <CopyableCode code="executionsId, integrationsId, locationsId, productsId, projectsId" /> | Get an execution in the specified project. |
| <CopyableCode code="projects_locations_products_integrations_executions_list" /> | `SELECT` | <CopyableCode code="integrationsId, locationsId, productsId, projectsId" /> | Lists the results of all the integration executions. The response includes the same information as the [execution log](https://cloud.google.com/application-integration/docs/viewing-logs) in the Integration UI. |
| <CopyableCode code="_projects_locations_integrations_executions_list" /> | `EXEC` | <CopyableCode code="integrationsId, locationsId, projectsId" /> | Lists the results of all the integration executions. The response includes the same information as the [execution log](https://cloud.google.com/application-integration/docs/viewing-logs) in the Integration UI. |
| <CopyableCode code="_projects_locations_products_integrations_executions_list" /> | `EXEC` | <CopyableCode code="integrationsId, locationsId, productsId, projectsId" /> | Lists the results of all the integration executions. The response includes the same information as the [execution log](https://cloud.google.com/application-integration/docs/viewing-logs) in the Integration UI. |
| <CopyableCode code="projects_locations_products_integrations_executions_cancel" /> | `EXEC` | <CopyableCode code="executionsId, integrationsId, locationsId, productsId, projectsId" /> | Cancellation of an execution |

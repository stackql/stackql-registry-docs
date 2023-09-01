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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.integrations.executions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Auto-generated primary key. |
| `requestParams` | `array` | Event parameters come in as part of the request. |
| `responseParams` | `array` | Event parameters come out as part of the response. |
| `responseParameters` | `object` | Event parameters returned as part of the response. |
| `executionMethod` | `string` | The ways user posts this event. |
| `updateTime` | `string` | Output only. Last modified time of the execution. |
| `directSubExecutions` | `array` | Direct sub executions of the following Execution. |
| `eventExecutionDetails` | `object` | Contains the details of the execution info of this event: this includes the tasks execution details plus the event execution statistics. Next available id: 10 |
| `executionDetails` | `object` | Contains the details of the execution info: this includes the tasks execution details plus the event execution statistics. |
| `requestParameters` | `object` | Event parameters come in as part of the request. |
| `triggerId` | `string` | The trigger id of the integration trigger config. If both trigger_id and client_id is present, the integration is executed from the start tasks provided by the matching trigger config otherwise it is executed from the default start tasks. |
| `createTime` | `string` | Output only. Created time of the execution. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_integrations_executions_list` | `SELECT` | `integrationsId, locationsId, projectsId` | Lists the results of all the integration executions. The response includes the same information as the [execution log](https://cloud.google.com/application-integration/docs/viewing-logs) in the Integration UI. |
| `projects_locations_products_integrations_executions_get` | `SELECT` | `executionsId, integrationsId, locationsId, productsId, projectsId` | Get an execution in the specified project. |
| `projects_locations_products_integrations_executions_list` | `SELECT` | `integrationsId, locationsId, productsId, projectsId` | Lists the results of all the integration executions. The response includes the same information as the [execution log](https://cloud.google.com/application-integration/docs/viewing-logs) in the Integration UI. |
| `_projects_locations_integrations_executions_list` | `EXEC` | `integrationsId, locationsId, projectsId` | Lists the results of all the integration executions. The response includes the same information as the [execution log](https://cloud.google.com/application-integration/docs/viewing-logs) in the Integration UI. |
| `_projects_locations_products_integrations_executions_list` | `EXEC` | `integrationsId, locationsId, productsId, projectsId` | Lists the results of all the integration executions. The response includes the same information as the [execution log](https://cloud.google.com/application-integration/docs/viewing-logs) in the Integration UI. |
| `projects_locations_products_integrations_executions_cancel` | `EXEC` | `executionsId, integrationsId, locationsId, productsId, projectsId` | Cancellation of an execution |

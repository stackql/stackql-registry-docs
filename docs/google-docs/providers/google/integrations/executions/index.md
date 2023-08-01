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
| `executionInfos` | `array` | Required. The detailed information of requested executions. |
| `executions` | `array` | The detailed information of requested executions |
| `nextPageToken` | `string` | The token used to retrieve the next page results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_integrations_executions_list` | `SELECT` | `integrationsId, locationsId, projectsId` | Lists the results of all the integration executions. The response includes the same information as the [execution log](https://cloud.google.com/application-integration/docs/viewing-logs) in the Integration UI. |
| `projects_locations_products_integrations_executions_list` | `SELECT` | `integrationsId, locationsId, productsId, projectsId` | Lists the results of all the integration executions. The response includes the same information as the [execution log](https://cloud.google.com/application-integration/docs/viewing-logs) in the Integration UI. |
| `projects_locations_products_integrations_executions_cancel` | `EXEC` | `executionsId, integrationsId, locationsId, productsId, projectsId` | Cancellation of an execution |
| `projects_locations_products_integrations_executions_get` | `EXEC` | `executionsId, integrationsId, locationsId, productsId, projectsId` | Get an execution in the specified project. |

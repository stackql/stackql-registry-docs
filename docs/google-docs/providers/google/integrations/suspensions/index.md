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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>suspensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.integrations.suspensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name for suspensions suspension/&#123;suspension_id&#125; |
| `approvalConfig` | `object` | Configurations for approving the Suspension. |
| `lastModifyTime` | `string` | Output only. Auto-generated. |
| `taskId` | `string` | Required. Task id of the associated SuspensionTask. |
| `state` | `string` | Required. State of this suspension, indicating what action a resolver has taken. |
| `eventExecutionInfoId` | `string` | Required. ID of the associated execution. |
| `suspensionConfig` | `object` |  |
| `createTime` | `string` | Output only. Auto-generated. |
| `integration` | `string` | Required. The name of the originating integration. |
| `audit` | `object` | Contains when and by whom the suspension was resolved. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_integrations_executions_suspensions_list` | `SELECT` | `executionsId, integrationsId, locationsId, projectsId` | * Lists suspensions associated with a specific execution. Only those with permissions to resolve the relevant suspensions will be able to view them. |
| `projects_locations_products_integrations_executions_suspensions_list` | `SELECT` | `executionsId, integrationsId, locationsId, productsId, projectsId` | * Lists suspensions associated with a specific execution. Only those with permissions to resolve the relevant suspensions will be able to view them. |
| `_projects_locations_integrations_executions_suspensions_list` | `EXEC` | `executionsId, integrationsId, locationsId, projectsId` | * Lists suspensions associated with a specific execution. Only those with permissions to resolve the relevant suspensions will be able to view them. |
| `_projects_locations_products_integrations_executions_suspensions_list` | `EXEC` | `executionsId, integrationsId, locationsId, productsId, projectsId` | * Lists suspensions associated with a specific execution. Only those with permissions to resolve the relevant suspensions will be able to view them. |
| `projects_locations_integrations_executions_suspensions_lift` | `EXEC` | `executionsId, integrationsId, locationsId, projectsId, suspensionsId` | * Lifts suspension for advanced suspension task. Fetch corresponding suspension with provided suspension Id, resolve suspension, and set up suspension result for the Suspension Task. |
| `projects_locations_integrations_executions_suspensions_resolve` | `EXEC` | `executionsId, integrationsId, locationsId, projectsId, suspensionsId` | * Resolves (lifts/rejects) any number of suspensions. If the integration is already running, only the status of the suspension is updated. Otherwise, the suspended integration will begin execution again. |
| `projects_locations_products_integrations_executions_suspensions_lift` | `EXEC` | `executionsId, integrationsId, locationsId, productsId, projectsId, suspensionsId` | * Lifts suspension for advanced suspension task. Fetch corresponding suspension with provided suspension Id, resolve suspension, and set up suspension result for the Suspension Task. |
| `projects_locations_products_integrations_executions_suspensions_resolve` | `EXEC` | `executionsId, integrationsId, locationsId, productsId, projectsId, suspensionsId` | * Resolves (lifts/rejects) any number of suspensions. If the integration is already running, only the status of the suspension is updated. Otherwise, the suspended integration will begin execution again. |

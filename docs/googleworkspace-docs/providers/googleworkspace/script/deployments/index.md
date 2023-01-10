---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - script
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.script.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `updateTime` | `string` | Last modified date time stamp. |
| `deploymentConfig` | `object` | Metadata the defines how a deployment is configured. |
| `deploymentId` | `string` | The deployment ID for this deployment. |
| `entryPoints` | `array` | The deployment's entry points. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_deployments_get` | `SELECT` | `deploymentId, scriptId` | Gets a deployment of an Apps Script project. |
| `projects_deployments_list` | `SELECT` | `scriptId` | Lists the deployments of an Apps Script project. |
| `projects_deployments_create` | `INSERT` | `scriptId` | Creates a deployment of an Apps Script project. |
| `projects_deployments_delete` | `DELETE` | `deploymentId, scriptId` | Deletes a deployment of an Apps Script project. |
| `projects_deployments_update` | `EXEC` | `deploymentId, scriptId` | Updates a deployment of an Apps Script project. |

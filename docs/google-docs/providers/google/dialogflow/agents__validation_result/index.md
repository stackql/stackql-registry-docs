---
title: agents__validation_result
hide_title: false
hide_table_of_contents: false
keywords:
  - agents__validation_result
  - dialogflow
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
<tr><td><b>Name</b></td><td><code>agents__validation_result</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.agents__validation_result</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique identifier of the agent validation result. Format: `projects//locations//agents//validationResult`. |
| `flowValidationResults` | `array` | Contains all flow validation results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_agents_getValidationResult` | `SELECT` | `agentsId, locationsId, projectsId` |

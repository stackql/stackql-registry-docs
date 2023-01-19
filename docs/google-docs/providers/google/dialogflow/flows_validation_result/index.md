---
title: flows_validation_result
hide_title: false
hide_table_of_contents: false
keywords:
  - flows_validation_result
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
<tr><td><b>Name</b></td><td><code>flows_validation_result</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.flows_validation_result</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique identifier of the flow validation result. Format: `projects//locations//agents//flows//validationResult`. |
| `validationMessages` | `array` | Contains all validation messages. |
| `updateTime` | `string` | Last time the flow was validated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_agents_flows_getValidationResult` | `SELECT` | `agentsId, flowsId, locationsId, projectsId` |

---
title: results
hide_title: false
hide_table_of_contents: false
keywords:
  - results
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
<tr><td><b>Name</b></td><td><code>results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name for the test case result. Format: `projects//locations//agents//testCases/ /results/`. |
| `testTime` | `string` | The time that the test was run. |
| `conversationTurns` | `array` | The conversation turns uttered during the test case replay in chronological order. |
| `environment` | `string` | Environment where the test was run. If not set, it indicates the draft environment. |
| `testResult` | `string` | Whether the test case passed in the agent environment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_test_cases_results_get` | `SELECT` | `agentsId, locationsId, projectsId, resultsId, testCasesId` | Gets a test case result. |
| `projects_locations_agents_test_cases_results_list` | `SELECT` | `agentsId, locationsId, projectsId, testCasesId` | Fetches the list of run results for the given test case. A maximum of 100 results are kept for each test case. |
| `_projects_locations_agents_test_cases_results_list` | `EXEC` | `agentsId, locationsId, projectsId, testCasesId` | Fetches the list of run results for the given test case. A maximum of 100 results are kept for each test case. |

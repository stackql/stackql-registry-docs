---
title: test_cases
hide_title: false
hide_table_of_contents: false
keywords:
  - test_cases
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>test_cases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.test_cases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique identifier of the test case. TestCases.CreateTestCase will populate the name automatically. Otherwise use format: `projects//locations//agents/ /testCases/`. |
| <CopyableCode code="creationTime" /> | `string` | Output only. When the test was created. |
| <CopyableCode code="displayName" /> | `string` | Required. The human-readable name of the test case, unique within the agent. Limit of 200 characters. |
| <CopyableCode code="lastTestResult" /> | `object` | Represents a result from running a test case in an agent environment. |
| <CopyableCode code="notes" /> | `string` | Additional freeform notes about the test case. Limit of 400 characters. |
| <CopyableCode code="tags" /> | `array` | Tags are short descriptions that users may apply to test cases for organizational and filtering purposes. Each tag should start with "#" and has a limit of 30 characters. |
| <CopyableCode code="testCaseConversationTurns" /> | `array` | The conversation turns uttered when the test case was created, in chronological order. These include the canonical set of agent utterances that should occur when the agent is working properly. |
| <CopyableCode code="testConfig" /> | `object` | Represents configurations for a test case. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_test_cases_get" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId, testCasesId" /> | Gets a test case. |
| <CopyableCode code="projects_locations_agents_test_cases_list" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Fetches a list of test cases for a given agent. |
| <CopyableCode code="projects_locations_agents_test_cases_create" /> | `INSERT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Creates a test case for the given agent. |
| <CopyableCode code="projects_locations_agents_test_cases_patch" /> | `UPDATE` | <CopyableCode code="agentsId, locationsId, projectsId, testCasesId" /> | Updates the specified test case. |
| <CopyableCode code="_projects_locations_agents_test_cases_list" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Fetches a list of test cases for a given agent. |
| <CopyableCode code="projects_locations_agents_test_cases_batch_delete" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Batch deletes test cases. |
| <CopyableCode code="projects_locations_agents_test_cases_batch_run" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Kicks off a batch run of test cases. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: BatchRunTestCasesMetadata - `response`: BatchRunTestCasesResponse |
| <CopyableCode code="projects_locations_agents_test_cases_calculate_coverage" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Calculates the test coverage for an agent. |
| <CopyableCode code="projects_locations_agents_test_cases_export" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Exports the test cases under the agent to a Cloud Storage bucket or a local file. Filter can be applied to export a subset of test cases. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: ExportTestCasesMetadata - `response`: ExportTestCasesResponse |
| <CopyableCode code="projects_locations_agents_test_cases_import" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Imports the test cases from a Cloud Storage bucket or a local file. It always creates new test cases and won't overwrite any existing ones. The provided ID in the imported test case is neglected. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: ImportTestCasesMetadata - `response`: ImportTestCasesResponse |
| <CopyableCode code="projects_locations_agents_test_cases_run" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId, testCasesId" /> | Kicks off a test case run. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: RunTestCaseMetadata - `response`: RunTestCaseResponse |

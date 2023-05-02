---
title: test_matrices
hide_title: false
hide_table_of_contents: false
keywords:
  - test_matrices
  - testing
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
<tr><td><b>Name</b></td><td><code>test_matrices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.testing.test_matrices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `outcomeSummary` | `string` | Output Only. The overall outcome of the test. Only set when the test matrix state is FINISHED. |
| `clientInfo` | `object` | Information about the client which invoked the test. |
| `testExecutions` | `array` | Output only. The list of test executions that the service creates for this matrix. |
| `testSpecification` | `object` | A description of how to run the test. |
| `failFast` | `boolean` | If true, only a single attempt at most will be made to run each execution/shard in the matrix. Flaky test attempts are not affected. Normally, 2 or more attempts are made if a potential infrastructure issue is detected. This feature is for latency sensitive workloads. The incidence of execution failures may be significantly greater for fail-fast matrices and support is more limited because of that expectation. |
| `flakyTestAttempts` | `integer` | The number of times a TestExecution should be re-attempted if one or more of its test cases fail for any reason. The maximum number of reruns allowed is 10. Default is 0, which implies no reruns. |
| `timestamp` | `string` | Output only. The time this test matrix was initially created. |
| `resultStorage` | `object` | Locations where the results of running the test are stored. |
| `invalidMatrixDetails` | `string` | Output only. Describes why the matrix is considered invalid. Only useful for matrices in the INVALID state. |
| `environmentMatrix` | `object` | The matrix of environments in which the test is to be executed. |
| `state` | `string` | Output only. Indicates the current progress of the test matrix. |
| `testMatrixId` | `string` | Output only. Unique id set by the service. |
| `projectId` | `string` | The cloud project that owns the test matrix. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_testMatrices_get` | `SELECT` | `projectId, testMatrixId` | Checks the status of a test matrix. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the Test Matrix does not exist |
| `projects_testMatrices_create` | `INSERT` | `projectId` | Creates and runs a matrix of tests according to the given specifications. Unsupported environments will be returned in the state UNSUPPORTED. A test matrix is limited to use at most 2000 devices in parallel. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to write to project - INVALID_ARGUMENT - if the request is malformed or if the matrix tries to use too many simultaneous devices. |
| `projects_testMatrices_cancel` | `EXEC` | `projectId, testMatrixId` | Cancels unfinished test executions in a test matrix. This call returns immediately and cancellation proceeds asynchronously. If the matrix is already final, this operation will have no effect. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the Test Matrix does not exist |

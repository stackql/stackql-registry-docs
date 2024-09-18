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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>test_matrices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>test_matrices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.testing.test_matrices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clientInfo" /> | `object` | Information about the client which invoked the test. |
| <CopyableCode code="environmentMatrix" /> | `object` | The matrix of environments in which the test is to be executed. |
| <CopyableCode code="extendedInvalidMatrixDetails" /> | `array` | Output only. Details about why a matrix was deemed invalid. If multiple checks can be safely performed, they will be reported but no assumptions should be made about the length of this list. |
| <CopyableCode code="failFast" /> | `boolean` | If true, only a single attempt at most will be made to run each execution/shard in the matrix. Flaky test attempts are not affected. Normally, 2 or more attempts are made if a potential infrastructure issue is detected. This feature is for latency sensitive workloads. The incidence of execution failures may be significantly greater for fail-fast matrices and support is more limited because of that expectation. |
| <CopyableCode code="flakyTestAttempts" /> | `integer` | The number of times a TestExecution should be re-attempted if one or more of its test cases fail for any reason. The maximum number of reruns allowed is 10. Default is 0, which implies no reruns. |
| <CopyableCode code="invalidMatrixDetails" /> | `string` | Output only. Describes why the matrix is considered invalid. Only useful for matrices in the INVALID state. |
| <CopyableCode code="outcomeSummary" /> | `string` | Output Only. The overall outcome of the test. Only set when the test matrix state is FINISHED. |
| <CopyableCode code="projectId" /> | `string` | The cloud project that owns the test matrix. |
| <CopyableCode code="resultStorage" /> | `object` | Locations where the results of running the test are stored. |
| <CopyableCode code="state" /> | `string` | Output only. Indicates the current progress of the test matrix. |
| <CopyableCode code="testExecutions" /> | `array` | Output only. The list of test executions that the service creates for this matrix. |
| <CopyableCode code="testMatrixId" /> | `string` | Output only. Unique id set by the service. |
| <CopyableCode code="testSpecification" /> | `object` | A description of how to run the test. |
| <CopyableCode code="timestamp" /> | `string` | Output only. The time this test matrix was initially created. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="projectId, testMatrixId" /> | Checks the status of a test matrix and the executions once they are created. The test matrix will contain the list of test executions to run if and only if the resultStorage.toolResultsExecution fields have been populated. Note: Flaky test executions may be added to the matrix at a later stage. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the Test Matrix does not exist |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectId" /> | Creates and runs a matrix of tests according to the given specifications. Unsupported environments will be returned in the state UNSUPPORTED. A test matrix is limited to use at most 2000 devices in parallel. The returned matrix will not yet contain the executions that will be created for this matrix. Execution creation happens later on and will require a call to GetTestMatrix. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to write to project - INVALID_ARGUMENT - if the request is malformed or if the matrix tries to use too many simultaneous devices. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="projectId, testMatrixId" /> | Cancels unfinished test executions in a test matrix. This call returns immediately and cancellation proceeds asynchronously. If the matrix is already final, this operation will have no effect. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the Test Matrix does not exist |

## `SELECT` examples

Checks the status of a test matrix and the executions once they are created. The test matrix will contain the list of test executions to run if and only if the resultStorage.toolResultsExecution fields have been populated. Note: Flaky test executions may be added to the matrix at a later stage. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the Test Matrix does not exist

```sql
SELECT
clientInfo,
environmentMatrix,
extendedInvalidMatrixDetails,
failFast,
flakyTestAttempts,
invalidMatrixDetails,
outcomeSummary,
projectId,
resultStorage,
state,
testExecutions,
testMatrixId,
testSpecification,
timestamp
FROM google.testing.test_matrices
WHERE projectId = '{{ projectId }}'
AND testMatrixId = '{{ testMatrixId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>test_matrices</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.testing.test_matrices (
projectId,
testMatrixId,
projectId,
clientInfo,
testSpecification,
environmentMatrix,
testExecutions,
resultStorage,
state,
timestamp,
invalidMatrixDetails,
flakyTestAttempts,
outcomeSummary,
failFast
)
SELECT 
'{{ projectId }}',
'{{ testMatrixId }}',
'{{ projectId }}',
'{{ clientInfo }}',
'{{ testSpecification }}',
'{{ environmentMatrix }}',
'{{ testExecutions }}',
'{{ resultStorage }}',
'{{ state }}',
'{{ timestamp }}',
'{{ invalidMatrixDetails }}',
'{{ flakyTestAttempts }}',
'{{ outcomeSummary }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
testMatrixId: string
projectId: string
clientInfo:
  name: string
  clientInfoDetails:
    - key: string
      value: string
testSpecification:
  testTimeout: string
  testSetup:
    filesToPush:
      - obbFile:
          obbFileName: string
          obb:
            gcsPath: string
        regularFile:
          devicePath: string
    directoriesToPull:
      - type: string
    initialSetupApks:
      - packageName: string
    additionalApks:
      - packageName: string
    account:
      googleAuto: {}
    networkProfile: string
    environmentVariables:
      - key: string
        value: string
    systrace:
      durationSeconds: integer
    dontAutograntPermissions: boolean
  iosTestSetup:
    networkProfile: string
    additionalIpas:
      - gcsPath: string
    pushFiles:
      - bundleId: string
        devicePath: string
    pullDirectories:
      - bundleId: string
        devicePath: string
  androidInstrumentationTest:
    appBundle: {}
    appPackageId: string
    testPackageId: string
    testRunnerClass: string
    testTargets:
      - type: string
    orchestratorOption: string
    shardingOption:
      uniformSharding:
        numShards: integer
      manualSharding:
        testTargetsForShard:
          - testTargets:
              - type: string
      smartSharding:
        targetedShardDuration: string
  androidRoboTest:
    appPackageId: string
    appInitialActivity: string
    maxDepth: integer
    maxSteps: integer
    roboDirectives:
      - resourceName: string
        inputText: string
        actionType: string
    roboMode: string
    startingIntents:
      - launcherActivity: {}
        startActivity:
          action: string
          uri: string
          categories:
            - type: string
        noActivity: {}
        timeout: string
  androidTestLoop:
    appPackageId: string
    scenarios:
      - type: string
        format: string
    scenarioLabels:
      - type: string
  iosXcTest:
    xcodeVersion: string
    appBundleId: string
    testSpecialEntitlements: boolean
  iosTestLoop:
    scenarios:
      - type: string
        format: string
    appBundleId: string
  iosRoboTest:
    appBundleId: string
  disableVideoRecording: boolean
  disablePerformanceMetrics: boolean
environmentMatrix:
  androidMatrix:
    androidModelIds:
      - type: string
    androidVersionIds:
      - type: string
    locales:
      - type: string
    orientations:
      - type: string
  androidDeviceList:
    androidDevices:
      - androidModelId: string
        androidVersionId: string
        locale: string
        orientation: string
  iosDeviceList:
    iosDevices:
      - iosModelId: string
        iosVersionId: string
        locale: string
        orientation: string
testExecutions:
  - id: string
    matrixId: string
    projectId: string
    shard:
      shardIndex: integer
      numShards: integer
      testTargetsForShard:
        testTargets:
          - type: string
      estimatedShardDuration: string
    environment:
      androidDevice:
        androidModelId: string
        androidVersionId: string
        locale: string
        orientation: string
      iosDevice:
        iosModelId: string
        iosVersionId: string
        locale: string
        orientation: string
    state: string
    toolResultsStep:
      projectId: string
      historyId: string
      executionId: string
      stepId: string
    timestamp: string
    testDetails:
      progressMessages:
        - type: string
      errorMessage: string
resultStorage:
  googleCloudStorage:
    gcsPath: string
  toolResultsHistory:
    projectId: string
    historyId: string
  toolResultsExecution:
    projectId: string
    historyId: string
    executionId: string
  resultsUrl: string
state: string
timestamp: string
invalidMatrixDetails: string
extendedInvalidMatrixDetails:
  - reason: string
    message: string
flakyTestAttempts: integer
outcomeSummary: string
failFast: boolean

```
</TabItem>
</Tabs>

---
title: dlp_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - dlp_jobs
  - dlp
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

Creates, updates, deletes, gets or lists a <code>dlp_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dlp_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dlp.dlp_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The server-assigned name. |
| <CopyableCode code="actionDetails" /> | `array` | Events that should occur after the job has completed. |
| <CopyableCode code="createTime" /> | `string` | Time when the job was created. |
| <CopyableCode code="endTime" /> | `string` | Time when the job finished. |
| <CopyableCode code="errors" /> | `array` | A stream of errors encountered running the job. |
| <CopyableCode code="inspectDetails" /> | `object` | The results of an inspect DataSource job. |
| <CopyableCode code="jobTriggerName" /> | `string` | If created by a job trigger, the resource name of the trigger that instantiated the job. |
| <CopyableCode code="lastModified" /> | `string` | Time when the job was last modified by the system. |
| <CopyableCode code="riskDetails" /> | `object` | Result of a risk analysis operation request. |
| <CopyableCode code="startTime" /> | `string` | Time when the job started. |
| <CopyableCode code="state" /> | `string` | State of a job. |
| <CopyableCode code="type" /> | `string` | The type of job. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_dlp_jobs_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_dlp_jobs_get" /> | `SELECT` | <CopyableCode code="dlpJobsId, projectsId" /> | Gets the latest state of a long-running DlpJob. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_dlp_jobs_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_locations_dlp_jobs_get" /> | `SELECT` | <CopyableCode code="dlpJobsId, locationsId, projectsId" /> | Gets the latest state of a long-running DlpJob. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_locations_dlp_jobs_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_dlp_jobs_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new job to inspect storage or calculate risk metrics. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. When no InfoTypes or CustomInfoTypes are specified in inspect jobs, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated. |
| <CopyableCode code="projects_locations_dlp_jobs_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new job to inspect storage or calculate risk metrics. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. When no InfoTypes or CustomInfoTypes are specified in inspect jobs, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated. |
| <CopyableCode code="projects_dlp_jobs_delete" /> | `DELETE` | <CopyableCode code="dlpJobsId, projectsId" /> | Deletes a long-running DlpJob. This method indicates that the client is no longer interested in the DlpJob result. The job will be canceled if possible. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_locations_dlp_jobs_delete" /> | `DELETE` | <CopyableCode code="dlpJobsId, locationsId, projectsId" /> | Deletes a long-running DlpJob. This method indicates that the client is no longer interested in the DlpJob result. The job will be canceled if possible. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_dlp_jobs_cancel" /> | `EXEC` | <CopyableCode code="dlpJobsId, projectsId" /> | Starts asynchronous cancellation on a long-running DlpJob. The server makes a best effort to cancel the DlpJob, but success is not guaranteed. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_locations_dlp_jobs_cancel" /> | `EXEC` | <CopyableCode code="dlpJobsId, locationsId, projectsId" /> | Starts asynchronous cancellation on a long-running DlpJob. The server makes a best effort to cancel the DlpJob, but success is not guaranteed. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_locations_dlp_jobs_finish" /> | `EXEC` | <CopyableCode code="dlpJobsId, locationsId, projectsId" /> | Finish a running hybrid DlpJob. Triggers the finalization steps and running of any enabled actions that have not yet run. |
| <CopyableCode code="projects_locations_dlp_jobs_hybrid_inspect" /> | `EXEC` | <CopyableCode code="dlpJobsId, locationsId, projectsId" /> | Inspect hybrid content and store findings to a job. To review the findings, inspect the job. Inspection will occur asynchronously. |

## `SELECT` examples

Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more.

```sql
SELECT
name,
actionDetails,
createTime,
endTime,
errors,
inspectDetails,
jobTriggerName,
lastModified,
riskDetails,
startTime,
state,
type
FROM google.dlp.dlp_jobs
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dlp_jobs</code> resource.

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
INSERT INTO google.dlp.dlp_jobs (
projectsId,
jobId,
inspectJob,
locationId,
riskJob
)
SELECT 
'{{ projectsId }}',
'{{ jobId }}',
'{{ inspectJob }}',
'{{ locationId }}',
'{{ riskJob }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
jobId: string
inspectJob:
  inspectConfig:
    contentOptions:
      - type: string
        enum: string
        enumDescriptions: string
    infoTypes:
      - sensitivityScore:
          score: string
        version: string
        name: string
    minLikelihood: string
    includeQuote: boolean
    minLikelihoodPerInfoType:
      - minLikelihood: string
        infoType:
          version: string
          name: string
    limits:
      maxFindingsPerRequest: integer
      maxFindingsPerItem: integer
      maxFindingsPerInfoType:
        - maxFindings: integer
    customInfoTypes:
      - exclusionType: string
        storedType:
          createTime: string
          name: string
        surrogateType: {}
        regex:
          groupIndexes:
            - format: string
              type: string
          pattern: string
        detectionRules:
          - hotwordRule:
              proximity:
                windowBefore: integer
                windowAfter: integer
              likelihoodAdjustment:
                relativeLikelihood: integer
                fixedLikelihood: string
        dictionary:
          wordList:
            words:
              - type: string
          cloudStoragePath:
            path: string
        likelihood: string
    excludeInfoTypes: boolean
    ruleSet:
      - rules:
          - exclusionRule:
              matchingType: string
              excludeInfoTypes:
                infoTypes:
                  - version: string
                    name: string
              excludeByHotword: {}
        infoTypes:
          - version: string
            name: string
  actions:
    - pubSub:
        topic: string
      jobNotificationEmails: {}
      deidentify:
        fileTypesToTransform:
          - enumDescriptions: string
            enum: string
            type: string
        transformationDetailsStorageConfig:
          table:
            projectId: string
            datasetId: string
            tableId: string
        transformationConfig:
          deidentifyTemplate: string
          structuredDeidentifyTemplate: string
          imageRedactTemplate: string
        cloudStorageOutput: string
      publishFindingsToCloudDataCatalog: {}
      publishToStackdriver: {}
      publishSummaryToCscc: {}
      saveFindings:
        outputConfig:
          outputSchema: string
  storageConfig:
    cloudStorageOptions:
      fileTypes:
        - enum: string
          enumDescriptions: string
          type: string
      bytesLimitPerFile: string
      filesLimitPercent: integer
      bytesLimitPerFilePercent: integer
      fileSet:
        regexFileSet:
          excludeRegex:
            - type: string
          bucketName: string
          includeRegex:
            - type: string
        url: string
      sampleMethod: string
    hybridOptions:
      description: string
      labels: object
      tableOptions:
        identifyingFields:
          - name: string
      requiredFindingLabelKeys:
        - type: string
    datastoreOptions:
      partitionId:
        namespaceId: string
        projectId: string
      kind:
        name: string
    bigQueryOptions:
      rowsLimit: string
      includedFields:
        - name: string
      sampleMethod: string
      identifyingFields:
        - name: string
      excludedFields:
        - name: string
      rowsLimitPercent: integer
    timespanConfig:
      startTime: string
      timestampField:
        name: string
      endTime: string
      enableAutoPopulationOfTimespanConfig: boolean
  inspectTemplateName: string
locationId: string
riskJob:
  actions:
    - {}
  privacyMetric:
    categoricalStatsConfig: {}
    numericalStatsConfig: {}
    deltaPresenceEstimationConfig:
      auxiliaryTables:
        - quasiIds:
            - customTag: string
      quasiIds:
        - customTag: string
          inferred: {}
      regionCode: string
    lDiversityConfig:
      quasiIds:
        - name: string
    kMapEstimationConfig:
      quasiIds:
        - customTag: string
      regionCode: string
      auxiliaryTables:
        - quasiIds:
            - customTag: string
    kAnonymityConfig:
      entityId: {}
      quasiIds:
        - name: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>dlp_jobs</code> resource.

```sql
/*+ delete */
DELETE FROM google.dlp.dlp_jobs
WHERE dlpJobsId = '{{ dlpJobsId }}'
AND projectsId = '{{ projectsId }}';
```

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
- name: your_resource_model_name
  props:
    - name: jobId
      value: string
    - name: inspectJob
      value:
        - name: inspectConfig
          value:
            - name: contentOptions
              value:
                - string
            - name: infoTypes
              value:
                - - name: sensitivityScore
                    value:
                      - name: score
                        value: string
                  - name: version
                    value: string
                  - name: name
                    value: string
            - name: minLikelihood
              value: string
            - name: includeQuote
              value: boolean
            - name: minLikelihoodPerInfoType
              value:
                - - name: minLikelihood
                    value: string
                  - name: infoType
                    value:
                      - name: version
                        value: string
                      - name: name
                        value: string
            - name: limits
              value:
                - name: maxFindingsPerRequest
                  value: integer
                - name: maxFindingsPerItem
                  value: integer
                - name: maxFindingsPerInfoType
                  value:
                    - - name: maxFindings
                        value: integer
            - name: customInfoTypes
              value:
                - - name: exclusionType
                    value: string
                  - name: storedType
                    value:
                      - name: createTime
                        value: string
                      - name: name
                        value: string
                  - name: surrogateType
                    value: []
                  - name: regex
                    value:
                      - name: groupIndexes
                        value:
                          - integer
                      - name: pattern
                        value: string
                  - name: detectionRules
                    value:
                      - - name: hotwordRule
                          value:
                            - name: proximity
                              value:
                                - name: windowBefore
                                  value: integer
                                - name: windowAfter
                                  value: integer
                            - name: likelihoodAdjustment
                              value:
                                - name: relativeLikelihood
                                  value: integer
                                - name: fixedLikelihood
                                  value: string
                  - name: dictionary
                    value:
                      - name: wordList
                        value:
                          - name: words
                            value:
                              - string
                      - name: cloudStoragePath
                        value:
                          - name: path
                            value: string
                  - name: likelihood
                    value: string
            - name: excludeInfoTypes
              value: boolean
            - name: ruleSet
              value:
                - - name: rules
                    value:
                      - - name: exclusionRule
                          value:
                            - name: matchingType
                              value: string
                            - name: excludeInfoTypes
                              value:
                                - name: infoTypes
                                  value:
                                    - - name: version
                                        value: string
                                      - name: name
                                        value: string
                            - name: excludeByHotword
                              value: []
                  - name: infoTypes
                    value:
                      - - name: version
                          value: string
                        - name: name
                          value: string
        - name: actions
          value:
            - - name: pubSub
                value:
                  - name: topic
                    value: string
              - name: jobNotificationEmails
                value: []
              - name: deidentify
                value:
                  - name: fileTypesToTransform
                    value:
                      - string
                  - name: transformationDetailsStorageConfig
                    value:
                      - name: table
                        value:
                          - name: projectId
                            value: string
                          - name: datasetId
                            value: string
                          - name: tableId
                            value: string
                  - name: transformationConfig
                    value:
                      - name: deidentifyTemplate
                        value: string
                      - name: structuredDeidentifyTemplate
                        value: string
                      - name: imageRedactTemplate
                        value: string
                  - name: cloudStorageOutput
                    value: string
              - name: publishFindingsToCloudDataCatalog
                value: []
              - name: publishToStackdriver
                value: []
              - name: publishSummaryToCscc
                value: []
              - name: saveFindings
                value:
                  - name: outputConfig
                    value:
                      - name: outputSchema
                        value: string
        - name: storageConfig
          value:
            - name: cloudStorageOptions
              value:
                - name: fileTypes
                  value:
                    - string
                - name: bytesLimitPerFile
                  value: string
                - name: filesLimitPercent
                  value: integer
                - name: bytesLimitPerFilePercent
                  value: integer
                - name: fileSet
                  value:
                    - name: regexFileSet
                      value:
                        - name: excludeRegex
                          value:
                            - string
                        - name: bucketName
                          value: string
                        - name: includeRegex
                          value:
                            - string
                    - name: url
                      value: string
                - name: sampleMethod
                  value: string
            - name: hybridOptions
              value:
                - name: description
                  value: string
                - name: labels
                  value: object
                - name: tableOptions
                  value:
                    - name: identifyingFields
                      value:
                        - - name: name
                            value: string
                - name: requiredFindingLabelKeys
                  value:
                    - string
            - name: datastoreOptions
              value:
                - name: partitionId
                  value:
                    - name: namespaceId
                      value: string
                    - name: projectId
                      value: string
                - name: kind
                  value:
                    - name: name
                      value: string
            - name: bigQueryOptions
              value:
                - name: rowsLimit
                  value: string
                - name: includedFields
                  value:
                    - - name: name
                        value: string
                - name: sampleMethod
                  value: string
                - name: identifyingFields
                  value:
                    - - name: name
                        value: string
                - name: excludedFields
                  value:
                    - - name: name
                        value: string
                - name: rowsLimitPercent
                  value: integer
            - name: timespanConfig
              value:
                - name: startTime
                  value: string
                - name: timestampField
                  value:
                    - name: name
                      value: string
                - name: endTime
                  value: string
                - name: enableAutoPopulationOfTimespanConfig
                  value: boolean
        - name: inspectTemplateName
          value: string
    - name: locationId
      value: string
    - name: riskJob
      value:
        - name: actions
          value:
            - []
        - name: privacyMetric
          value:
            - name: categoricalStatsConfig
              value: []
            - name: numericalStatsConfig
              value: []
            - name: deltaPresenceEstimationConfig
              value:
                - name: auxiliaryTables
                  value:
                    - - name: quasiIds
                        value:
                          - - name: customTag
                              value: string
                - name: quasiIds
                  value:
                    - - name: customTag
                        value: string
                      - name: inferred
                        value: []
                - name: regionCode
                  value: string
            - name: lDiversityConfig
              value:
                - name: quasiIds
                  value:
                    - - name: name
                        value: string
            - name: kMapEstimationConfig
              value:
                - name: quasiIds
                  value:
                    - - name: customTag
                        value: string
                - name: regionCode
                  value: string
                - name: auxiliaryTables
                  value:
                    - - name: quasiIds
                        value:
                          - - name: customTag
                              value: string
            - name: kAnonymityConfig
              value:
                - name: entityId
                  value: []
                - name: quasiIds
                  value:
                    - - name: name
                        value: string

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

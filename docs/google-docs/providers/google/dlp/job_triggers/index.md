---
title: job_triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - job_triggers
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

Creates, updates, deletes, gets or lists a <code>job_triggers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dlp.job_triggers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Unique resource name for the triggeredJob, assigned by the service when the triggeredJob is created, for example `projects/dlp-test-project/jobTriggers/53234423`. |
| <CopyableCode code="description" /> | `string` | User provided description (max 256 chars) |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of a triggeredJob. |
| <CopyableCode code="displayName" /> | `string` | Display name (max 100 chars) |
| <CopyableCode code="errors" /> | `array` | Output only. A stream of errors encountered when the trigger was activated. Repeated errors may result in the JobTrigger automatically being paused. Will return the last 100 errors. Whenever the JobTrigger is modified this list will be cleared. |
| <CopyableCode code="inspectJob" /> | `object` | Controls what and how to inspect for findings. |
| <CopyableCode code="lastRunTime" /> | `string` | Output only. The timestamp of the last time this trigger executed. |
| <CopyableCode code="status" /> | `string` | Required. A status for this trigger. |
| <CopyableCode code="triggers" /> | `array` | A list of triggers which will be OR'ed together. Only one in the list needs to trigger for a job to be started. The list may contain only a single Schedule trigger and must have at least one object. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of a triggeredJob. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_job_triggers_get" /> | `SELECT` | <CopyableCode code="jobTriggersId, locationsId, organizationsId" /> | Gets a job trigger. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more. |
| <CopyableCode code="organizations_locations_job_triggers_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists job triggers. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more. |
| <CopyableCode code="projects_job_triggers_get" /> | `SELECT` | <CopyableCode code="jobTriggersId, projectsId" /> | Gets a job trigger. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more. |
| <CopyableCode code="projects_job_triggers_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists job triggers. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more. |
| <CopyableCode code="projects_locations_job_triggers_get" /> | `SELECT` | <CopyableCode code="jobTriggersId, locationsId, projectsId" /> | Gets a job trigger. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more. |
| <CopyableCode code="projects_locations_job_triggers_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists job triggers. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more. |
| <CopyableCode code="organizations_locations_job_triggers_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more. |
| <CopyableCode code="projects_job_triggers_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more. |
| <CopyableCode code="projects_locations_job_triggers_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more. |
| <CopyableCode code="organizations_locations_job_triggers_delete" /> | `DELETE` | <CopyableCode code="jobTriggersId, locationsId, organizationsId" /> | Deletes a job trigger. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more. |
| <CopyableCode code="projects_job_triggers_delete" /> | `DELETE` | <CopyableCode code="jobTriggersId, projectsId" /> | Deletes a job trigger. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more. |
| <CopyableCode code="projects_locations_job_triggers_delete" /> | `DELETE` | <CopyableCode code="jobTriggersId, locationsId, projectsId" /> | Deletes a job trigger. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more. |
| <CopyableCode code="organizations_locations_job_triggers_patch" /> | `UPDATE` | <CopyableCode code="jobTriggersId, locationsId, organizationsId" /> | Updates a job trigger. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more. |
| <CopyableCode code="projects_job_triggers_patch" /> | `UPDATE` | <CopyableCode code="jobTriggersId, projectsId" /> | Updates a job trigger. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more. |
| <CopyableCode code="projects_locations_job_triggers_patch" /> | `UPDATE` | <CopyableCode code="jobTriggersId, locationsId, projectsId" /> | Updates a job trigger. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more. |
| <CopyableCode code="projects_job_triggers_activate" /> | `EXEC` | <CopyableCode code="jobTriggersId, projectsId" /> | Activate a job trigger. Causes the immediate execute of a trigger instead of waiting on the trigger event to occur. |
| <CopyableCode code="projects_locations_job_triggers_activate" /> | `EXEC` | <CopyableCode code="jobTriggersId, locationsId, projectsId" /> | Activate a job trigger. Causes the immediate execute of a trigger instead of waiting on the trigger event to occur. |
| <CopyableCode code="projects_locations_job_triggers_hybrid_inspect" /> | `EXEC` | <CopyableCode code="jobTriggersId, locationsId, projectsId" /> | Inspect hybrid content and store findings to a trigger. The inspection will be processed asynchronously. To review the findings monitor the jobs within the trigger. |

## `SELECT` examples

Lists job triggers. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more.

```sql
SELECT
name,
description,
createTime,
displayName,
errors,
inspectJob,
lastRunTime,
status,
triggers,
updateTime
FROM google.dlp.job_triggers
WHERE projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>job_triggers</code> resource.

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
INSERT INTO google.dlp.job_triggers (
projectsId,
triggerId,
locationId,
jobTrigger
)
SELECT 
'{{ projectsId }}',
'{{ triggerId }}',
'{{ locationId }}',
'{{ jobTrigger }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: triggerId
      value: string
    - name: locationId
      value: string
    - name: jobTrigger
      value:
        - name: errors
          value:
            - - name: details
                value:
                  - name: details
                    value:
                      - object
                  - name: code
                    value: integer
                  - name: message
                    value: string
              - name: timestamps
                value:
                  - string
              - name: extraInfo
                value: string
        - name: status
          value: string
        - name: lastRunTime
          value: string
        - name: name
          value: string
        - name: createTime
          value: string
        - name: updateTime
          value: string
        - name: triggers
          value:
            - - name: manual
                value: []
              - name: schedule
                value:
                  - name: recurrencePeriodDuration
                    value: string
        - name: description
          value: string
        - name: displayName
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>job_triggers</code> resource.

```sql
/*+ update */
UPDATE google.dlp.job_triggers
SET 
jobTrigger = '{{ jobTrigger }}',
updateMask = '{{ updateMask }}'
WHERE 
jobTriggersId = '{{ jobTriggersId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>job_triggers</code> resource.

```sql
/*+ delete */
DELETE FROM google.dlp.job_triggers
WHERE jobTriggersId = '{{ jobTriggersId }}'
AND projectsId = '{{ projectsId }}';
```

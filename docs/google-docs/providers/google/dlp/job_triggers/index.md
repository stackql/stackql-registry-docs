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
jobTrigger,
triggerId,
locationId
)
SELECT 
'{{ projectsId }}',
'{{ jobTrigger }}',
'{{ triggerId }}',
'{{ locationId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
jobTrigger:
  createTime: string
  name: string
  errors:
    - details:
        message: string
        code: integer
        details:
          - additionalProperties: any
            type: string
      timestamps:
        - format: string
          type: string
      extraInfo: string
  triggers:
    - schedule:
        recurrencePeriodDuration: string
      manual: {}
  lastRunTime: string
  status: string
  displayName: string
  description: string
  inspectJob:
    storageConfig:
      hybridOptions:
        requiredFindingLabelKeys:
          - type: string
        labels: object
        description: string
        tableOptions:
          identifyingFields:
            - name: string
      timespanConfig:
        startTime: string
        timestampField:
          name: string
        endTime: string
        enableAutoPopulationOfTimespanConfig: boolean
      datastoreOptions:
        kind:
          name: string
        partitionId:
          namespaceId: string
          projectId: string
      cloudStorageOptions:
        bytesLimitPerFilePercent: integer
        filesLimitPercent: integer
        fileSet:
          regexFileSet:
            excludeRegex:
              - type: string
            includeRegex:
              - type: string
            bucketName: string
          url: string
        bytesLimitPerFile: string
        fileTypes:
          - enumDescriptions: string
            enum: string
            type: string
        sampleMethod: string
      bigQueryOptions:
        includedFields:
          - name: string
        identifyingFields:
          - name: string
        tableReference:
          tableId: string
          projectId: string
          datasetId: string
        excludedFields:
          - name: string
        rowsLimitPercent: integer
        rowsLimit: string
        sampleMethod: string
    inspectTemplateName: string
    actions:
      - publishSummaryToCscc: {}
        saveFindings:
          outputConfig:
            outputSchema: string
        jobNotificationEmails: {}
        publishFindingsToCloudDataCatalog: {}
        pubSub:
          topic: string
        deidentify:
          cloudStorageOutput: string
          transformationConfig:
            structuredDeidentifyTemplate: string
            imageRedactTemplate: string
            deidentifyTemplate: string
          transformationDetailsStorageConfig: {}
          fileTypesToTransform:
            - enumDescriptions: string
              type: string
              enum: string
        publishToStackdriver: {}
    inspectConfig:
      limits:
        maxFindingsPerItem: integer
        maxFindingsPerRequest: integer
        maxFindingsPerInfoType:
          - maxFindings: integer
            infoType:
              version: string
              name: string
              sensitivityScore:
                score: string
      contentOptions:
        - enum: string
          type: string
          enumDescriptions: string
      includeQuote: boolean
      customInfoTypes:
        - regex:
            pattern: string
            groupIndexes:
              - type: string
                format: string
          exclusionType: string
          likelihood: string
          dictionary:
            cloudStoragePath:
              path: string
            wordList:
              words:
                - type: string
          surrogateType: {}
          detectionRules:
            - hotwordRule:
                proximity:
                  windowAfter: integer
                  windowBefore: integer
                likelihoodAdjustment:
                  relativeLikelihood: integer
                  fixedLikelihood: string
          storedType:
            createTime: string
            name: string
      minLikelihoodPerInfoType:
        - minLikelihood: string
      infoTypes:
        - version: string
          name: string
      minLikelihood: string
      excludeInfoTypes: boolean
      ruleSet:
        - infoTypes:
            - version: string
              name: string
          rules:
            - exclusionRule:
                excludeInfoTypes:
                  infoTypes:
                    - version: string
                      name: string
                matchingType: string
                excludeByHotword: {}
  updateTime: string
triggerId: string
locationId: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>job_triggers</code> resource.

```sql
/*+ update */
UPDATE google.dlp.job_triggers
SET 
updateMask = '{{ updateMask }}',
jobTrigger = '{{ jobTrigger }}'
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

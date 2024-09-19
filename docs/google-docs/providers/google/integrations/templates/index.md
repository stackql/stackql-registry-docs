---
title: templates
hide_title: false
hide_table_of_contents: false
keywords:
  - templates
  - integrations
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

Creates, updates, deletes, gets or lists a <code>templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name of the template. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the template. The length should not be more than 255 characters |
| <CopyableCode code="author" /> | `string` | Optional. Creator of the template. |
| <CopyableCode code="categories" /> | `array` | Required. Categories associated with the Template. The categories listed below will be utilized for the Template listing. |
| <CopyableCode code="components" /> | `array` | Optional. Components being used in the template. This could be used to categorize and filter. |
| <CopyableCode code="createTime" /> | `string` | Output only. Auto-generated. |
| <CopyableCode code="displayName" /> | `string` | Required. The name of the template |
| <CopyableCode code="docLink" /> | `string` | Optional. Link to template documentation. |
| <CopyableCode code="lastUsedTime" /> | `string` | Optional. Time the template was last used. |
| <CopyableCode code="sharedWith" /> | `array` | Required. Resource names with which the template is shared for example ProjectNumber/Ord id |
| <CopyableCode code="tags" /> | `array` | Required. Tags which are used to identify templates. These tags could be for business use case, connectors etc. |
| <CopyableCode code="templateBundle" /> | `object` | Define the bundle of the template. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Auto-generated |
| <CopyableCode code="usageCount" /> | `string` | Optional. Number of template usages. |
| <CopyableCode code="usageInfo" /> | `string` | Optional. Information on how to use the template. This should contain detailed information about usage of the template. |
| <CopyableCode code="visibility" /> | `string` | Required. Visibility of the template. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_templates_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, templatesId" /> | Get a template in the specified project. |
| <CopyableCode code="projects_locations_templates_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all templates matching the filter. |
| <CopyableCode code="projects_locations_templates_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new template |
| <CopyableCode code="projects_locations_templates_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, templatesId" /> | Deletes a template |
| <CopyableCode code="projects_locations_templates_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, templatesId" /> | Updates the template by given id. |
| <CopyableCode code="projects_locations_templates_download" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, templatesId" /> | Downloads a template. Retrieves the `Template` and returns the response as a string. |
| <CopyableCode code="projects_locations_templates_import" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, templatesId" /> | Import the template to an existing integration. This api would keep track of usage_count and last_used_time. PERMISSION_DENIED would be thrown if template is not accessible by client. |
| <CopyableCode code="projects_locations_templates_search" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Search templates based on user query and filters. This api would query the templates and return a list of templates based on the user filter. |
| <CopyableCode code="projects_locations_templates_share" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, templatesId" /> | Share a template with other clients. Only the template owner can share the templates with other projects. PERMISSION_DENIED would be thrown if the request is not from the owner. |
| <CopyableCode code="projects_locations_templates_unshare" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, templatesId" /> | Unshare a template from given clients. Owner of the template can unshare template with clients. Shared client can only unshare the template from itself. PERMISSION_DENIED would be thrown if request is not from owner or for unsharing itself. |
| <CopyableCode code="projects_locations_templates_upload" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Uploads a template. The content can be a previously downloaded template. Performs the same function as CreateTemplate, but accepts input in a string format, which holds the complete representation of the Template content. |
| <CopyableCode code="projects_locations_templates_use" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, templatesId" /> | Use the template to create integration. This api would keep track of usage_count and last_used_time. PERMISSION_DENIED would be thrown if template is not accessible by client. |

## `SELECT` examples

Lists all templates matching the filter.

```sql
SELECT
name,
description,
author,
categories,
components,
createTime,
displayName,
docLink,
lastUsedTime,
sharedWith,
tags,
templateBundle,
updateTime,
usageCount,
usageInfo,
visibility
FROM google.integrations.templates
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>templates</code> resource.

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
INSERT INTO google.integrations.templates (
locationsId,
projectsId,
tags,
sharedWith,
components,
lastUsedTime,
docLink,
displayName,
description,
usageInfo,
categories,
templateBundle,
visibility,
author,
usageCount,
name
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ tags }}',
'{{ sharedWith }}',
'{{ components }}',
'{{ lastUsedTime }}',
'{{ docLink }}',
'{{ displayName }}',
'{{ description }}',
'{{ usageInfo }}',
'{{ categories }}',
'{{ templateBundle }}',
'{{ visibility }}',
'{{ author }}',
'{{ usageCount }}',
'{{ name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
tags:
  - type: string
sharedWith:
  - type: string
components:
  - type: string
    name: string
lastUsedTime: string
createTime: string
docLink: string
updateTime: string
displayName: string
description: string
usageInfo: string
categories:
  - type: string
    enumDescriptions: string
    enum: string
templateBundle:
  subIntegrationVersionTemplates:
    - integrationVersion:
        origin: string
        userLabel: string
        triggerConfigs:
          - startTasks:
              - displayName: string
                taskId: string
                taskConfigId: string
                description: string
                condition: string
            alertConfig:
              - alertThreshold: integer
                thresholdType: string
                durationThreshold: string
                thresholdValue:
                  absolute: string
                  percentage: integer
                metricType: string
                aggregationPeriod: string
                disableAlert: boolean
                displayName: string
                onlyFinalAttempt: boolean
            properties: object
            triggerId: string
            nextTasksExecutionPolicy: string
            label: string
            position:
              x: integer
              'y': integer
            cloudSchedulerConfig:
              cronTab: string
              location: string
              serviceAccountEmail: string
              errorMessage: string
            description: string
            trigger: string
            triggerNumber: string
            errorCatcherId: string
            triggerType: string
        taskConfigs:
          - taskTemplate: string
            failurePolicy:
              condition: string
              intervalTime: string
              maxRetries: integer
              retryStrategy: string
            taskId: string
            nextTasksExecutionPolicy: string
            description: string
            conditionalFailurePolicies:
              failurePolicies:
                - condition: string
                  intervalTime: string
                  maxRetries: integer
                  retryStrategy: string
            successPolicy:
              finalState: string
            parameters: object
            taskExecutionStrategy: string
            errorCatcherId: string
            nextTasks:
              - displayName: string
                taskId: string
                taskConfigId: string
                description: string
                condition: string
            externalTaskType: string
            displayName: string
            jsonValidationOption: string
            task: string
        triggerConfigsInternal:
          - nextTasksExecutionPolicy: string
            position:
              'y': integer
              x: integer
            triggerName: string
            startTasks:
              - combinedConditions:
                  - conditions:
                      - value:
                          stringValue: string
                          intValue: string
                          stringArray:
                            values:
                              - type: string
                          intArray:
                            values:
                              - type: string
                                format: string
                          doubleValue: number
                          booleanValue: boolean
                          doubleArray:
                            values:
                              - type: string
                                format: string
                          protoValue: object
                        eventPropertyKey: string
                        operator: string
                condition: string
                taskNumber: string
                taskConfigId: string
                label: string
                description: string
            triggerNumber: string
            triggerCriteria:
              triggerCriteriaTaskImplementationClassName: string
              parameters:
                parameters:
                  - value:
                      protoArray:
                        protoValues:
                          - type: string
                            additionalProperties: any
                      doubleArray:
                        doubleValues:
                          - type: string
                            format: string
                      stringValue: string
                      intValue: string
                      doubleValue: number
                      booleanValue: boolean
                      serializedObjectValue:
                        objectValue: string
                      intArray:
                        intValues:
                          - format: string
                            type: string
                      booleanArray:
                        booleanValues:
                          - type: string
                      stringArray:
                        stringValues:
                          - type: string
                      protoValue: object
                    key: string
                    masked: boolean
              condition: string
            description: string
            properties: object
            pauseWorkflowExecutions: boolean
            triggerType: string
            alertConfig:
              - alertName: string
                durationThresholdMs: string
                playbookUrl: string
                warningEnumList:
                  filterType: string
                  enumStrings:
                    - type: string
                onlyFinalAttempt: boolean
                aggregationPeriod: string
                metricType: string
                numAggregationPeriods: integer
                thresholdType: string
                clientId: string
                thresholdValue:
                  percentage: integer
                  absolute: string
                alertDisabled: boolean
            triggerId: string
            enabledClients:
              - type: string
            errorCatcherId: string
            cloudSchedulerConfig:
              errorMessage: string
              cronTab: string
              location: string
              serviceAccountEmail: string
            label: string
        createTime: string
        createdFromTemplate: string
        description: string
        teardown:
          teardownTaskConfigs:
            - teardownTaskImplementationClassName: string
              name: string
              properties:
                properties:
                  - key: string
              creatorEmail: string
              nextTeardownTask:
                name: string
        enableVariableMasking: boolean
        snapshotNumber: string
        parentTemplateId: string
        lastModifierEmail: string
        state: string
        cloudLoggingDetails:
          enableCloudLogging: boolean
          cloudLoggingSeverity: string
        updateTime: string
        runAsServiceAccount: string
        integrationConfigParameters:
          - value:
              intArray:
                intValues:
                  - format: string
                    type: string
              doubleArray:
                doubleValues:
                  - format: string
                    type: string
              intValue: string
              stringArray:
                stringValues:
                  - type: string
              doubleValue: number
              stringValue: string
              jsonValue: string
              booleanArray:
                booleanValues:
                  - type: string
              booleanValue: boolean
            parameter:
              description: string
              inputOutputType: string
              isTransient: boolean
              producer: string
              dataType: string
              jsonSchema: string
              searchable: boolean
              containsLargeData: boolean
              masked: boolean
              key: string
              displayName: string
        errorCatcherConfigs:
          - description: string
            startErrorTasks:
              - displayName: string
                taskId: string
                taskConfigId: string
                description: string
                condition: string
            label: string
            errorCatcherNumber: string
            errorCatcherId: string
        status: string
        name: string
        databasePersistencePolicy: string
        lockHolder: string
        taskConfigsInternal:
          - taskNumber: string
            lastModifiedTime: string
            taskType: string
            nextTasks:
              - combinedConditions:
                  - conditions:
                      - eventPropertyKey: string
                        operator: string
                condition: string
                taskNumber: string
                taskConfigId: string
                label: string
                description: string
            disableStrictTypeValidation: boolean
            taskExecutionStrategy: string
            errorCatcherId: string
            failurePolicy:
              retryStrategy: string
              retryCondition: string
              maxNumRetries: integer
              intervalInSeconds: string
            taskEntity:
              taskType: string
              stats:
                dimensions:
                  triggerId: string
                  taskName: string
                  warningEnumString: string
                  clientId: string
                  errorEnumString: string
                  retryAttempt: string
                  workflowName: string
                  enumFilterType: string
                  taskNumber: string
                  workflowId: string
                warningRate: number
                qps: number
                durationInSeconds: number
                errorRate: number
              paramSpecs:
                parameters:
                  - config:
                      helpText: string
                      isHidden: boolean
                      label: string
                      uiPlaceholderText: string
                      subSectionLabel: string
                      parameterNameOption: string
                      inputDisplayOption: string
                      descriptivePhrase: string
                      hideDefaultValue: boolean
                    validationRule:
                      doubleRange:
                        max: number
                        min: number
                      intRange:
                        min: string
                        max: string
                      stringRegex:
                        regex: string
                        exclusive: boolean
                    protoDef:
                      fullName: string
                      path: string
                    isOutput: boolean
                    jsonSchema: string
                    key: string
                    dataType: string
                    collectionElementClassName: string
                    required: boolean
                    className: string
                    isDeprecated: boolean
                    defaultValue:
                      stringValue: string
                      doubleValue: number
                      protoValue: object
                      stringArray:
                        stringValues:
                          - type: string
                      booleanValue: boolean
                      intArray:
                        intValues:
                          - type: string
                            format: string
                      jsonValue: string
                      serializedObjectValue:
                        objectValue: string
                      doubleArray:
                        doubleValues:
                          - format: string
                            type: string
                      booleanArray:
                        booleanValues:
                          - type: string
                      protoArray:
                        protoValues:
                          - type: string
                            additionalProperties: any
                      intValue: string
              uiConfig:
                taskUiModuleConfigs:
                  - moduleId: string
              metadata:
                activeTaskName: string
                externalDocHtml: string
                isDeprecated: boolean
                externalDocMarkdown: string
                tags:
                  - type: string
                externalDocLink: string
                admins:
                  - googleGroupEmail: string
                    userEmail: string
                externalCategorySequence: integer
                iconLink: string
                docMarkdown: string
                descriptiveName: string
                system: string
                standaloneExternalDocHtml: string
                defaultSpec: string
                name: string
                g3DocLink: string
                category: string
                externalCategory: string
                codeSearchLink: string
                defaultJsonValidationOption: string
                status: string
                description: string
              disabledForVpcSc: boolean
            jsonValidationOption: string
            taskName: string
            externalTaskType: string
            alertConfigs:
              - numAggregationPeriods: integer
                alertName: string
                thresholdType: string
                alertDisabled: boolean
                playbookUrl: string
                aggregationPeriod: string
                clientId: string
                onlyFinalAttempt: boolean
                metricType: string
                durationThresholdMs: string
            preconditionLabel: string
            label: string
            parameters: object
            precondition: string
            createTime: string
            creatorEmail: string
            conditionalFailurePolicies:
              failurePolicies:
                - retryStrategy: string
                  retryCondition: string
                  maxNumRetries: integer
                  intervalInSeconds: string
            description: string
            incomingEdgeCount: integer
            successPolicy:
              finalState: string
            nextTasksExecutionPolicy: string
            rollbackStrategy:
              rollbackTaskImplementationClassName: string
              parameters:
                parameters:
                  - key: string
                    dataType: string
                    masked: boolean
              taskNumbersToRollback:
                - type: string
            taskTemplateName: string
            taskSpec: string
        integrationParametersInternal:
          parameters:
            - producer: string
              producedBy:
                elementIdentifier: string
                elementType: string
              containsLargeData: boolean
              inOutType: string
              required: boolean
              key: string
              dataType: string
              attributes:
                readOnly: boolean
                dataType: string
                searchable: string
                isRequired: boolean
                masked: boolean
                isSearchable: boolean
                logSettings:
                  seedPeriod: string
                  seedScope: string
                  logFieldName: string
                taskVisibility:
                  - type: string
              protoDefName: string
              jsonSchema: string
              protoDefPath: string
              name: string
              description: string
              children:
                - producer: string
                  containsLargeData: boolean
                  inOutType: string
                  required: boolean
                  key: string
                  dataType: string
                  protoDefName: string
                  jsonSchema: string
                  protoDefPath: string
                  name: string
                  description: string
                  children:
                    - producer: string
                      containsLargeData: boolean
                      inOutType: string
                      required: boolean
                      key: string
                      dataType: string
                      protoDefName: string
                      jsonSchema: string
                      protoDefPath: string
                      name: string
                      description: string
                      children:
                        - producer: string
                          containsLargeData: boolean
                          inOutType: string
                          required: boolean
                          key: string
                          dataType: string
                          protoDefName: string
                          jsonSchema: string
                          protoDefPath: string
                          name: string
                          description: string
                          children:
                            - producer: string
                              containsLargeData: boolean
                              inOutType: string
                              required: boolean
                              key: string
                              dataType: string
                              protoDefName: string
                              jsonSchema: string
                              protoDefPath: string
                              name: string
                              description: string
                              children:
                                - producer: string
                                  containsLargeData: boolean
                                  inOutType: string
                                  required: boolean
                                  key: string
                                  dataType: string
                                  protoDefName: string
                                  jsonSchema: string
                                  protoDefPath: string
                                  name: string
                                  description: string
                                  children:
                                    - {}
                                  isTransient: boolean
                              isTransient: boolean
                          isTransient: boolean
                      isTransient: boolean
                  isTransient: boolean
              isTransient: boolean
        integrationParameters:
          - description: string
            inputOutputType: string
            isTransient: boolean
            producer: string
            dataType: string
            jsonSchema: string
            searchable: boolean
            containsLargeData: boolean
            masked: boolean
            key: string
            displayName: string
      key: string
  integrationVersionTemplate:
    key: string
visibility: string
author: string
usageCount: string
name: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>templates</code> resource.

```sql
/*+ update */
UPDATE google.integrations.templates
SET 
tags = '{{ tags }}',
sharedWith = '{{ sharedWith }}',
components = '{{ components }}',
lastUsedTime = '{{ lastUsedTime }}',
docLink = '{{ docLink }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
usageInfo = '{{ usageInfo }}',
categories = '{{ categories }}',
templateBundle = '{{ templateBundle }}',
visibility = '{{ visibility }}',
author = '{{ author }}',
usageCount = '{{ usageCount }}',
name = '{{ name }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND templatesId = '{{ templatesId }}';
```

## `DELETE` example

Deletes the specified <code>templates</code> resource.

```sql
/*+ delete */
DELETE FROM google.integrations.templates
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND templatesId = '{{ templatesId }}';
```

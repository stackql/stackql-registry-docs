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
- name: your_resource_model_name
  props:
    - name: tags
      value:
        - string
    - name: sharedWith
      value:
        - string
    - name: components
      value:
        - - name: type
            value: string
          - name: name
            value: string
    - name: lastUsedTime
      value: string
    - name: createTime
      value: string
    - name: docLink
      value: string
    - name: updateTime
      value: string
    - name: displayName
      value: string
    - name: description
      value: string
    - name: usageInfo
      value: string
    - name: categories
      value:
        - string
    - name: templateBundle
      value:
        - name: subIntegrationVersionTemplates
          value:
            - - name: integrationVersion
                value:
                  - name: origin
                    value: string
                  - name: userLabel
                    value: string
                  - name: triggerConfigs
                    value:
                      - - name: startTasks
                          value:
                            - - name: displayName
                                value: string
                              - name: taskId
                                value: string
                              - name: taskConfigId
                                value: string
                              - name: description
                                value: string
                              - name: condition
                                value: string
                        - name: alertConfig
                          value:
                            - - name: alertThreshold
                                value: integer
                              - name: thresholdType
                                value: string
                              - name: durationThreshold
                                value: string
                              - name: thresholdValue
                                value:
                                  - name: absolute
                                    value: string
                                  - name: percentage
                                    value: integer
                              - name: metricType
                                value: string
                              - name: aggregationPeriod
                                value: string
                              - name: disableAlert
                                value: boolean
                              - name: displayName
                                value: string
                              - name: onlyFinalAttempt
                                value: boolean
                        - name: properties
                          value: object
                        - name: triggerId
                          value: string
                        - name: nextTasksExecutionPolicy
                          value: string
                        - name: label
                          value: string
                        - name: position
                          value:
                            - name: x
                              value: integer
                            - name: 'y'
                              value: integer
                        - name: cloudSchedulerConfig
                          value:
                            - name: cronTab
                              value: string
                            - name: location
                              value: string
                            - name: serviceAccountEmail
                              value: string
                            - name: errorMessage
                              value: string
                        - name: description
                          value: string
                        - name: trigger
                          value: string
                        - name: triggerNumber
                          value: string
                        - name: errorCatcherId
                          value: string
                        - name: triggerType
                          value: string
                  - name: taskConfigs
                    value:
                      - - name: taskTemplate
                          value: string
                        - name: failurePolicy
                          value:
                            - name: condition
                              value: string
                            - name: intervalTime
                              value: string
                            - name: maxRetries
                              value: integer
                            - name: retryStrategy
                              value: string
                        - name: taskId
                          value: string
                        - name: nextTasksExecutionPolicy
                          value: string
                        - name: description
                          value: string
                        - name: conditionalFailurePolicies
                          value:
                            - name: failurePolicies
                              value:
                                - - name: condition
                                    value: string
                                  - name: intervalTime
                                    value: string
                                  - name: maxRetries
                                    value: integer
                                  - name: retryStrategy
                                    value: string
                        - name: successPolicy
                          value:
                            - name: finalState
                              value: string
                        - name: parameters
                          value: object
                        - name: taskExecutionStrategy
                          value: string
                        - name: errorCatcherId
                          value: string
                        - name: nextTasks
                          value:
                            - - name: displayName
                                value: string
                              - name: taskId
                                value: string
                              - name: taskConfigId
                                value: string
                              - name: description
                                value: string
                              - name: condition
                                value: string
                        - name: externalTaskType
                          value: string
                        - name: displayName
                          value: string
                        - name: jsonValidationOption
                          value: string
                        - name: task
                          value: string
                  - name: triggerConfigsInternal
                    value:
                      - - name: nextTasksExecutionPolicy
                          value: string
                        - name: position
                          value:
                            - name: 'y'
                              value: integer
                            - name: x
                              value: integer
                        - name: triggerName
                          value: string
                        - name: startTasks
                          value:
                            - - name: combinedConditions
                                value:
                                  - - name: conditions
                                      value:
                                        - - name: value
                                            value:
                                              - name: stringValue
                                                value: string
                                              - name: intValue
                                                value: string
                                              - name: stringArray
                                                value:
                                                  - name: values
                                                    value:
                                                      - string
                                              - name: intArray
                                                value:
                                                  - name: values
                                                    value:
                                                      - string
                                              - name: doubleValue
                                                value: number
                                              - name: booleanValue
                                                value: boolean
                                              - name: doubleArray
                                                value:
                                                  - name: values
                                                    value:
                                                      - number
                                              - name: protoValue
                                                value: object
                                          - name: eventPropertyKey
                                            value: string
                                          - name: operator
                                            value: string
                              - name: condition
                                value: string
                              - name: taskNumber
                                value: string
                              - name: taskConfigId
                                value: string
                              - name: label
                                value: string
                              - name: description
                                value: string
                        - name: triggerNumber
                          value: string
                        - name: triggerCriteria
                          value:
                            - name: triggerCriteriaTaskImplementationClassName
                              value: string
                            - name: parameters
                              value:
                                - name: parameters
                                  value:
                                    - - name: value
                                        value:
                                          - name: protoArray
                                            value:
                                              - name: protoValues
                                                value:
                                                  - object
                                          - name: doubleArray
                                            value:
                                              - name: doubleValues
                                                value:
                                                  - number
                                          - name: stringValue
                                            value: string
                                          - name: intValue
                                            value: string
                                          - name: doubleValue
                                            value: number
                                          - name: booleanValue
                                            value: boolean
                                          - name: serializedObjectValue
                                            value:
                                              - name: objectValue
                                                value: string
                                          - name: intArray
                                            value:
                                              - name: intValues
                                                value:
                                                  - string
                                          - name: booleanArray
                                            value:
                                              - name: booleanValues
                                                value:
                                                  - boolean
                                          - name: stringArray
                                            value:
                                              - name: stringValues
                                                value:
                                                  - string
                                          - name: protoValue
                                            value: object
                                      - name: key
                                        value: string
                                      - name: masked
                                        value: boolean
                            - name: condition
                              value: string
                        - name: description
                          value: string
                        - name: properties
                          value: object
                        - name: pauseWorkflowExecutions
                          value: boolean
                        - name: triggerType
                          value: string
                        - name: alertConfig
                          value:
                            - - name: alertName
                                value: string
                              - name: durationThresholdMs
                                value: string
                              - name: playbookUrl
                                value: string
                              - name: warningEnumList
                                value:
                                  - name: filterType
                                    value: string
                                  - name: enumStrings
                                    value:
                                      - string
                              - name: onlyFinalAttempt
                                value: boolean
                              - name: aggregationPeriod
                                value: string
                              - name: metricType
                                value: string
                              - name: numAggregationPeriods
                                value: integer
                              - name: thresholdType
                                value: string
                              - name: clientId
                                value: string
                              - name: thresholdValue
                                value:
                                  - name: percentage
                                    value: integer
                                  - name: absolute
                                    value: string
                              - name: alertDisabled
                                value: boolean
                        - name: triggerId
                          value: string
                        - name: enabledClients
                          value:
                            - string
                        - name: errorCatcherId
                          value: string
                        - name: cloudSchedulerConfig
                          value:
                            - name: errorMessage
                              value: string
                            - name: cronTab
                              value: string
                            - name: location
                              value: string
                            - name: serviceAccountEmail
                              value: string
                        - name: label
                          value: string
                  - name: createTime
                    value: string
                  - name: createdFromTemplate
                    value: string
                  - name: description
                    value: string
                  - name: teardown
                    value:
                      - name: teardownTaskConfigs
                        value:
                          - - name: teardownTaskImplementationClassName
                              value: string
                            - name: name
                              value: string
                            - name: properties
                              value:
                                - name: properties
                                  value:
                                    - - name: key
                                        value: string
                            - name: creatorEmail
                              value: string
                            - name: nextTeardownTask
                              value:
                                - name: name
                                  value: string
                  - name: enableVariableMasking
                    value: boolean
                  - name: snapshotNumber
                    value: string
                  - name: parentTemplateId
                    value: string
                  - name: lastModifierEmail
                    value: string
                  - name: state
                    value: string
                  - name: cloudLoggingDetails
                    value:
                      - name: enableCloudLogging
                        value: boolean
                      - name: cloudLoggingSeverity
                        value: string
                  - name: updateTime
                    value: string
                  - name: runAsServiceAccount
                    value: string
                  - name: integrationConfigParameters
                    value:
                      - - name: value
                          value:
                            - name: intArray
                              value:
                                - name: intValues
                                  value:
                                    - string
                            - name: doubleArray
                              value:
                                - name: doubleValues
                                  value:
                                    - number
                            - name: intValue
                              value: string
                            - name: stringArray
                              value:
                                - name: stringValues
                                  value:
                                    - string
                            - name: doubleValue
                              value: number
                            - name: stringValue
                              value: string
                            - name: jsonValue
                              value: string
                            - name: booleanArray
                              value:
                                - name: booleanValues
                                  value:
                                    - boolean
                            - name: booleanValue
                              value: boolean
                        - name: parameter
                          value:
                            - name: description
                              value: string
                            - name: inputOutputType
                              value: string
                            - name: isTransient
                              value: boolean
                            - name: producer
                              value: string
                            - name: dataType
                              value: string
                            - name: jsonSchema
                              value: string
                            - name: searchable
                              value: boolean
                            - name: containsLargeData
                              value: boolean
                            - name: masked
                              value: boolean
                            - name: key
                              value: string
                            - name: displayName
                              value: string
                  - name: errorCatcherConfigs
                    value:
                      - - name: description
                          value: string
                        - name: startErrorTasks
                          value:
                            - - name: displayName
                                value: string
                              - name: taskId
                                value: string
                              - name: taskConfigId
                                value: string
                              - name: description
                                value: string
                              - name: condition
                                value: string
                        - name: label
                          value: string
                        - name: errorCatcherNumber
                          value: string
                        - name: errorCatcherId
                          value: string
                  - name: status
                    value: string
                  - name: name
                    value: string
                  - name: databasePersistencePolicy
                    value: string
                  - name: lockHolder
                    value: string
                  - name: taskConfigsInternal
                    value:
                      - - name: taskNumber
                          value: string
                        - name: lastModifiedTime
                          value: string
                        - name: taskType
                          value: string
                        - name: nextTasks
                          value:
                            - - name: combinedConditions
                                value:
                                  - - name: conditions
                                      value:
                                        - - name: eventPropertyKey
                                            value: string
                                          - name: operator
                                            value: string
                              - name: condition
                                value: string
                              - name: taskNumber
                                value: string
                              - name: taskConfigId
                                value: string
                              - name: label
                                value: string
                              - name: description
                                value: string
                        - name: disableStrictTypeValidation
                          value: boolean
                        - name: taskExecutionStrategy
                          value: string
                        - name: errorCatcherId
                          value: string
                        - name: failurePolicy
                          value:
                            - name: retryStrategy
                              value: string
                            - name: retryCondition
                              value: string
                            - name: maxNumRetries
                              value: integer
                            - name: intervalInSeconds
                              value: string
                        - name: taskEntity
                          value:
                            - name: taskType
                              value: string
                            - name: stats
                              value:
                                - name: dimensions
                                  value:
                                    - name: triggerId
                                      value: string
                                    - name: taskName
                                      value: string
                                    - name: warningEnumString
                                      value: string
                                    - name: clientId
                                      value: string
                                    - name: errorEnumString
                                      value: string
                                    - name: retryAttempt
                                      value: string
                                    - name: workflowName
                                      value: string
                                    - name: enumFilterType
                                      value: string
                                    - name: taskNumber
                                      value: string
                                    - name: workflowId
                                      value: string
                                - name: warningRate
                                  value: number
                                - name: qps
                                  value: number
                                - name: durationInSeconds
                                  value: number
                                - name: errorRate
                                  value: number
                            - name: paramSpecs
                              value:
                                - name: parameters
                                  value:
                                    - - name: config
                                        value:
                                          - name: helpText
                                            value: string
                                          - name: isHidden
                                            value: boolean
                                          - name: label
                                            value: string
                                          - name: uiPlaceholderText
                                            value: string
                                          - name: subSectionLabel
                                            value: string
                                          - name: parameterNameOption
                                            value: string
                                          - name: inputDisplayOption
                                            value: string
                                          - name: descriptivePhrase
                                            value: string
                                          - name: hideDefaultValue
                                            value: boolean
                                      - name: validationRule
                                        value:
                                          - name: doubleRange
                                            value:
                                              - name: max
                                                value: number
                                              - name: min
                                                value: number
                                          - name: intRange
                                            value:
                                              - name: min
                                                value: string
                                              - name: max
                                                value: string
                                          - name: stringRegex
                                            value:
                                              - name: regex
                                                value: string
                                              - name: exclusive
                                                value: boolean
                                      - name: protoDef
                                        value:
                                          - name: fullName
                                            value: string
                                          - name: path
                                            value: string
                                      - name: isOutput
                                        value: boolean
                                      - name: jsonSchema
                                        value: string
                                      - name: key
                                        value: string
                                      - name: dataType
                                        value: string
                                      - name: collectionElementClassName
                                        value: string
                                      - name: required
                                        value: boolean
                                      - name: className
                                        value: string
                                      - name: isDeprecated
                                        value: boolean
                                      - name: defaultValue
                                        value:
                                          - name: stringValue
                                            value: string
                                          - name: doubleValue
                                            value: number
                                          - name: protoValue
                                            value: object
                                          - name: stringArray
                                            value:
                                              - name: stringValues
                                                value:
                                                  - string
                                          - name: booleanValue
                                            value: boolean
                                          - name: intArray
                                            value:
                                              - name: intValues
                                                value:
                                                  - string
                                          - name: jsonValue
                                            value: string
                                          - name: serializedObjectValue
                                            value:
                                              - name: objectValue
                                                value: string
                                          - name: doubleArray
                                            value:
                                              - name: doubleValues
                                                value:
                                                  - number
                                          - name: booleanArray
                                            value:
                                              - name: booleanValues
                                                value:
                                                  - boolean
                                          - name: protoArray
                                            value:
                                              - name: protoValues
                                                value:
                                                  - object
                                          - name: intValue
                                            value: string
                            - name: uiConfig
                              value:
                                - name: taskUiModuleConfigs
                                  value:
                                    - - name: moduleId
                                        value: string
                            - name: metadata
                              value:
                                - name: activeTaskName
                                  value: string
                                - name: externalDocHtml
                                  value: string
                                - name: isDeprecated
                                  value: boolean
                                - name: externalDocMarkdown
                                  value: string
                                - name: tags
                                  value:
                                    - string
                                - name: externalDocLink
                                  value: string
                                - name: admins
                                  value:
                                    - - name: googleGroupEmail
                                        value: string
                                      - name: userEmail
                                        value: string
                                - name: externalCategorySequence
                                  value: integer
                                - name: iconLink
                                  value: string
                                - name: docMarkdown
                                  value: string
                                - name: descriptiveName
                                  value: string
                                - name: system
                                  value: string
                                - name: standaloneExternalDocHtml
                                  value: string
                                - name: defaultSpec
                                  value: string
                                - name: name
                                  value: string
                                - name: g3DocLink
                                  value: string
                                - name: category
                                  value: string
                                - name: externalCategory
                                  value: string
                                - name: codeSearchLink
                                  value: string
                                - name: defaultJsonValidationOption
                                  value: string
                                - name: status
                                  value: string
                                - name: description
                                  value: string
                            - name: disabledForVpcSc
                              value: boolean
                        - name: jsonValidationOption
                          value: string
                        - name: taskName
                          value: string
                        - name: externalTaskType
                          value: string
                        - name: alertConfigs
                          value:
                            - - name: numAggregationPeriods
                                value: integer
                              - name: alertName
                                value: string
                              - name: thresholdType
                                value: string
                              - name: alertDisabled
                                value: boolean
                              - name: playbookUrl
                                value: string
                              - name: aggregationPeriod
                                value: string
                              - name: clientId
                                value: string
                              - name: onlyFinalAttempt
                                value: boolean
                              - name: metricType
                                value: string
                              - name: durationThresholdMs
                                value: string
                        - name: preconditionLabel
                          value: string
                        - name: label
                          value: string
                        - name: parameters
                          value: object
                        - name: precondition
                          value: string
                        - name: createTime
                          value: string
                        - name: creatorEmail
                          value: string
                        - name: conditionalFailurePolicies
                          value:
                            - name: failurePolicies
                              value:
                                - - name: retryStrategy
                                    value: string
                                  - name: retryCondition
                                    value: string
                                  - name: maxNumRetries
                                    value: integer
                                  - name: intervalInSeconds
                                    value: string
                        - name: description
                          value: string
                        - name: incomingEdgeCount
                          value: integer
                        - name: successPolicy
                          value:
                            - name: finalState
                              value: string
                        - name: nextTasksExecutionPolicy
                          value: string
                        - name: rollbackStrategy
                          value:
                            - name: rollbackTaskImplementationClassName
                              value: string
                            - name: parameters
                              value:
                                - name: parameters
                                  value:
                                    - - name: key
                                        value: string
                                      - name: dataType
                                        value: string
                                      - name: masked
                                        value: boolean
                            - name: taskNumbersToRollback
                              value:
                                - string
                        - name: taskTemplateName
                          value: string
                        - name: taskSpec
                          value: string
                  - name: integrationParametersInternal
                    value:
                      - name: parameters
                        value:
                          - - name: producer
                              value: string
                            - name: producedBy
                              value:
                                - name: elementIdentifier
                                  value: string
                                - name: elementType
                                  value: string
                            - name: containsLargeData
                              value: boolean
                            - name: inOutType
                              value: string
                            - name: required
                              value: boolean
                            - name: key
                              value: string
                            - name: dataType
                              value: string
                            - name: attributes
                              value:
                                - name: readOnly
                                  value: boolean
                                - name: dataType
                                  value: string
                                - name: searchable
                                  value: string
                                - name: isRequired
                                  value: boolean
                                - name: masked
                                  value: boolean
                                - name: isSearchable
                                  value: boolean
                                - name: logSettings
                                  value:
                                    - name: seedPeriod
                                      value: string
                                    - name: seedScope
                                      value: string
                                    - name: logFieldName
                                      value: string
                                - name: taskVisibility
                                  value:
                                    - string
                            - name: protoDefName
                              value: string
                            - name: jsonSchema
                              value: string
                            - name: protoDefPath
                              value: string
                            - name: name
                              value: string
                            - name: description
                              value: string
                            - name: children
                              value:
                                - - name: producer
                                    value: string
                                  - name: containsLargeData
                                    value: boolean
                                  - name: inOutType
                                    value: string
                                  - name: required
                                    value: boolean
                                  - name: key
                                    value: string
                                  - name: dataType
                                    value: string
                                  - name: protoDefName
                                    value: string
                                  - name: jsonSchema
                                    value: string
                                  - name: protoDefPath
                                    value: string
                                  - name: name
                                    value: string
                                  - name: description
                                    value: string
                                  - name: children
                                    value:
                                      - - name: producer
                                          value: string
                                        - name: containsLargeData
                                          value: boolean
                                        - name: inOutType
                                          value: string
                                        - name: required
                                          value: boolean
                                        - name: key
                                          value: string
                                        - name: dataType
                                          value: string
                                        - name: protoDefName
                                          value: string
                                        - name: jsonSchema
                                          value: string
                                        - name: protoDefPath
                                          value: string
                                        - name: name
                                          value: string
                                        - name: description
                                          value: string
                                        - name: children
                                          value:
                                            - - name: producer
                                                value: string
                                              - name: containsLargeData
                                                value: boolean
                                              - name: inOutType
                                                value: string
                                              - name: required
                                                value: boolean
                                              - name: key
                                                value: string
                                              - name: dataType
                                                value: string
                                              - name: protoDefName
                                                value: string
                                              - name: jsonSchema
                                                value: string
                                              - name: protoDefPath
                                                value: string
                                              - name: name
                                                value: string
                                              - name: description
                                                value: string
                                              - name: children
                                                value:
                                                  - - name: producer
                                                      value: string
                                                    - name: containsLargeData
                                                      value: boolean
                                                    - name: inOutType
                                                      value: string
                                                    - name: required
                                                      value: boolean
                                                    - name: key
                                                      value: string
                                                    - name: dataType
                                                      value: string
                                                    - name: protoDefName
                                                      value: string
                                                    - name: jsonSchema
                                                      value: string
                                                    - name: protoDefPath
                                                      value: string
                                                    - name: name
                                                      value: string
                                                    - name: description
                                                      value: string
                                                    - name: children
                                                      value:
                                                        - - name: producer
                                                            value: string
                                                          - name: containsLargeData
                                                            value: boolean
                                                          - name: inOutType
                                                            value: string
                                                          - name: required
                                                            value: boolean
                                                          - name: key
                                                            value: string
                                                          - name: dataType
                                                            value: string
                                                          - name: protoDefName
                                                            value: string
                                                          - name: jsonSchema
                                                            value: string
                                                          - name: protoDefPath
                                                            value: string
                                                          - name: name
                                                            value: string
                                                          - name: description
                                                            value: string
                                                          - name: children
                                                            value:
                                                              - []
                                                          - name: isTransient
                                                            value: boolean
                                                    - name: isTransient
                                                      value: boolean
                                              - name: isTransient
                                                value: boolean
                                        - name: isTransient
                                          value: boolean
                                  - name: isTransient
                                    value: boolean
                            - name: isTransient
                              value: boolean
                  - name: integrationParameters
                    value:
                      - - name: description
                          value: string
                        - name: inputOutputType
                          value: string
                        - name: isTransient
                          value: boolean
                        - name: producer
                          value: string
                        - name: dataType
                          value: string
                        - name: jsonSchema
                          value: string
                        - name: searchable
                          value: boolean
                        - name: containsLargeData
                          value: boolean
                        - name: masked
                          value: boolean
                        - name: key
                          value: string
                        - name: displayName
                          value: string
              - name: key
                value: string
        - name: integrationVersionTemplate
          value:
            - name: key
              value: string
    - name: visibility
      value: string
    - name: author
      value: string
    - name: usageCount
      value: string
    - name: name
      value: string

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

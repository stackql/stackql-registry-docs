---
title: software_update_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - software_update_configurations
  - automation
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

Creates, updates, deletes, gets or lists a <code>software_update_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>software_update_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.software_update_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_software_update_configurations', value: 'view', },
        { label: 'software_update_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schedule_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="softwareUpdateConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tasks" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `string` | Resource type |
| <CopyableCode code="update_configuration" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | Software update configuration properties. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_name" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, softwareUpdateConfigurationName, subscriptionId" /> | Get a single software update configuration by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Get all software update configurations for the account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="automationAccountName, resourceGroupName, softwareUpdateConfigurationName, subscriptionId, data__properties" /> | Create a new software update configuration with the name given in the URI. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, resourceGroupName, softwareUpdateConfigurationName, subscriptionId" /> | delete a specific software update configuration. |

## `SELECT` examples

Get all software update configurations for the account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_software_update_configurations', value: 'view', },
        { label: 'software_update_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
automationAccountName,
created_by,
creation_time,
error,
last_modified_by,
last_modified_time,
provisioning_state,
resourceGroupName,
schedule_info,
softwareUpdateConfigurationName,
subscriptionId,
tasks,
type,
update_configuration
FROM azure.automation.vw_software_update_configurations
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.automation.software_update_configurations
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>software_update_configurations</code> resource.

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
INSERT INTO azure.automation.software_update_configurations (
automationAccountName,
resourceGroupName,
softwareUpdateConfigurationName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ automationAccountName }}',
'{{ resourceGroupName }}',
'{{ softwareUpdateConfigurationName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: id
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: updateConfiguration
          value:
            - name: operatingSystem
              value: []
            - name: windows
              value:
                - name: includedUpdateClassifications
                  value: string
                - name: excludedKbNumbers
                  value:
                    - string
                - name: includedKbNumbers
                  value:
                    - string
                - name: rebootSetting
                  value: string
            - name: linux
              value:
                - name: includedPackageClassifications
                  value: string
                - name: excludedPackageNameMasks
                  value:
                    - string
                - name: includedPackageNameMasks
                  value:
                    - string
                - name: rebootSetting
                  value: string
            - name: duration
              value: string
            - name: azureVirtualMachines
              value:
                - string
            - name: nonAzureComputerNames
              value:
                - string
            - name: targets
              value:
                - name: azureQueries
                  value:
                    - - name: scope
                        value:
                          - string
                      - name: locations
                        value:
                          - string
                      - name: tagSettings
                        value:
                          - name: tags
                            value: object
                          - name: filterOperator
                            value: string
                - name: nonAzureQueries
                  value:
                    - - name: functionAlias
                        value: string
                      - name: workspaceId
                        value: string
        - name: scheduleInfo
          value:
            - name: startTime
              value: string
            - name: startTimeOffsetMinutes
              value: number
            - name: expiryTime
              value: string
            - name: expiryTimeOffsetMinutes
              value: number
            - name: isEnabled
              value: boolean
            - name: nextRun
              value: string
            - name: nextRunOffsetMinutes
              value: number
            - name: interval
              value: integer
            - name: frequency
              value: []
            - name: timeZone
              value: string
            - name: advancedSchedule
              value:
                - name: weekDays
                  value:
                    - string
                - name: monthDays
                  value:
                    - integer
                - name: monthlyOccurrences
                  value:
                    - - name: occurrence
                        value: integer
                      - name: day
                        value: string
            - name: creationTime
              value: string
            - name: lastModifiedTime
              value: string
            - name: description
              value: string
        - name: provisioningState
          value: string
        - name: error
          value:
            - name: error
              value:
                - name: code
                  value: string
                - name: message
                  value: string
                - name: target
                  value: string
                - name: details
                  value:
                    - - name: code
                        value: string
                      - name: message
                        value: string
                      - name: target
                        value: string
                      - name: details
                        value:
                          - - name: code
                              value: string
                            - name: message
                              value: string
                            - name: target
                              value: string
                            - name: details
                              value:
                                - - name: code
                                    value: string
                                  - name: message
                                    value: string
                                  - name: target
                                    value: string
                                  - name: details
                                    value:
                                      - - name: code
                                          value: string
                                        - name: message
                                          value: string
                                        - name: target
                                          value: string
                                        - name: details
                                          value:
                                            - - name: code
                                                value: string
                                              - name: message
                                                value: string
                                              - name: target
                                                value: string
                                              - name: details
                                                value:
                                                  - - name: code
                                                      value: string
                                                    - name: message
                                                      value: string
                                                    - name: target
                                                      value: string
                                                    - name: details
                                                      value:
                                                        - - name: code
                                                            value: string
                                                          - name: message
                                                            value: string
                                                          - name: target
                                                            value: string
                                                          - name: details
                                                            value:
                                                              - []
                                                          - name: additionalInfo
                                                            value:
                                                              - []
                                                    - name: additionalInfo
                                                      value:
                                                        - - name: type
                                                            value: string
                                                          - name: info
                                                            value: object
                                              - name: additionalInfo
                                                value:
                                                  - - name: type
                                                      value: string
                                                    - name: info
                                                      value: object
                                        - name: additionalInfo
                                          value:
                                            - - name: type
                                                value: string
                                              - name: info
                                                value: object
                                  - name: additionalInfo
                                    value:
                                      - - name: type
                                          value: string
                                        - name: info
                                          value: object
                            - name: additionalInfo
                              value:
                                - - name: type
                                    value: string
                                  - name: info
                                    value: object
                      - name: additionalInfo
                        value:
                          - - name: type
                              value: string
                            - name: info
                              value: object
                - name: additionalInfo
                  value:
                    - - name: type
                        value: string
                      - name: info
                        value: object
        - name: creationTime
          value: string
        - name: createdBy
          value: string
        - name: lastModifiedTime
          value: string
        - name: lastModifiedBy
          value: string
        - name: tasks
          value:
            - name: preTask
              value:
                - name: parameters
                  value: object
                - name: source
                  value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>software_update_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automation.software_update_configurations
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND softwareUpdateConfigurationName = '{{ softwareUpdateConfigurationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

---
title: configuration_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_slots
  - app_service
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

Creates, updates, deletes, gets or lists a <code>configuration_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.configuration_slots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | Configuration of an App Service app. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for List the configurations of an app |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Updates the configuration of an app. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Updates the configuration of an app. |

## `SELECT` examples

Description for Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.configuration_slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration_slots</code> resource.

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
INSERT INTO azure.app_service.configuration_slots (
name,
resourceGroupName,
slot,
subscriptionId,
kind,
properties
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ slot }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: numberOfWorkers
          value: integer
        - name: defaultDocuments
          value:
            - string
        - name: netFrameworkVersion
          value: string
        - name: phpVersion
          value: string
        - name: pythonVersion
          value: string
        - name: nodeVersion
          value: string
        - name: powerShellVersion
          value: string
        - name: linuxFxVersion
          value: string
        - name: windowsFxVersion
          value: string
        - name: requestTracingEnabled
          value: boolean
        - name: requestTracingExpirationTime
          value: string
        - name: remoteDebuggingEnabled
          value: boolean
        - name: remoteDebuggingVersion
          value: string
        - name: httpLoggingEnabled
          value: boolean
        - name: acrUseManagedIdentityCreds
          value: boolean
        - name: acrUserManagedIdentityID
          value: string
        - name: logsDirectorySizeLimit
          value: integer
        - name: detailedErrorLoggingEnabled
          value: boolean
        - name: publishingUsername
          value: string
        - name: appSettings
          value:
            - - name: name
                value: string
              - name: value
                value: string
        - name: metadata
          value:
            - - name: name
                value: string
              - name: value
                value: string
        - name: connectionStrings
          value:
            - - name: name
                value: string
              - name: connectionString
                value: string
              - name: type
                value: string
        - name: machineKey
          value:
            - name: validation
              value: string
            - name: validationKey
              value: string
            - name: decryption
              value: string
            - name: decryptionKey
              value: string
        - name: handlerMappings
          value:
            - - name: extension
                value: string
              - name: scriptProcessor
                value: string
              - name: arguments
                value: string
        - name: documentRoot
          value: string
        - name: scmType
          value: string
        - name: use32BitWorkerProcess
          value: boolean
        - name: webSocketsEnabled
          value: boolean
        - name: alwaysOn
          value: boolean
        - name: javaVersion
          value: string
        - name: javaContainer
          value: string
        - name: javaContainerVersion
          value: string
        - name: appCommandLine
          value: string
        - name: managedPipelineMode
          value: string
        - name: virtualApplications
          value:
            - - name: virtualPath
                value: string
              - name: physicalPath
                value: string
              - name: preloadEnabled
                value: boolean
              - name: virtualDirectories
                value:
                  - - name: virtualPath
                      value: string
                    - name: physicalPath
                      value: string
        - name: loadBalancing
          value: string
        - name: experiments
          value:
            - name: rampUpRules
              value:
                - - name: actionHostName
                    value: string
                  - name: reroutePercentage
                    value: number
                  - name: changeStep
                    value: number
                  - name: changeIntervalInMinutes
                    value: integer
                  - name: minReroutePercentage
                    value: number
                  - name: maxReroutePercentage
                    value: number
                  - name: changeDecisionCallbackUrl
                    value: string
                  - name: name
                    value: string
        - name: limits
          value:
            - name: maxPercentageCpu
              value: number
            - name: maxMemoryInMb
              value: integer
            - name: maxDiskSizeInMb
              value: integer
        - name: autoHealEnabled
          value: boolean
        - name: autoHealRules
          value:
            - name: triggers
              value:
                - name: requests
                  value:
                    - name: count
                      value: integer
                    - name: timeInterval
                      value: string
                - name: privateBytesInKB
                  value: integer
                - name: statusCodes
                  value:
                    - - name: status
                        value: integer
                      - name: subStatus
                        value: integer
                      - name: win32Status
                        value: integer
                      - name: count
                        value: integer
                      - name: timeInterval
                        value: string
                      - name: path
                        value: string
                - name: slowRequests
                  value:
                    - name: timeTaken
                      value: string
                    - name: path
                      value: string
                    - name: count
                      value: integer
                    - name: timeInterval
                      value: string
                - name: slowRequestsWithPath
                  value:
                    - - name: timeTaken
                        value: string
                      - name: path
                        value: string
                      - name: count
                        value: integer
                      - name: timeInterval
                        value: string
                - name: statusCodesRange
                  value:
                    - - name: statusCodes
                        value: string
                      - name: path
                        value: string
                      - name: count
                        value: integer
                      - name: timeInterval
                        value: string
            - name: actions
              value:
                - name: actionType
                  value: string
                - name: customAction
                  value:
                    - name: exe
                      value: string
                    - name: parameters
                      value: string
                - name: minProcessExecutionTime
                  value: string
        - name: tracingOptions
          value: string
        - name: vnetName
          value: string
        - name: vnetRouteAllEnabled
          value: boolean
        - name: vnetPrivatePortsCount
          value: integer
        - name: cors
          value:
            - name: allowedOrigins
              value:
                - string
            - name: supportCredentials
              value: boolean
        - name: push
          value:
            - name: id
              value: string
            - name: name
              value: string
            - name: kind
              value: string
            - name: type
              value: string
            - name: properties
              value:
                - name: isPushEnabled
                  value: boolean
                - name: tagWhitelistJson
                  value: string
                - name: tagsRequiringAuth
                  value: string
                - name: dynamicTagsJson
                  value: string
        - name: apiDefinition
          value:
            - name: url
              value: string
        - name: apiManagementConfig
          value:
            - name: id
              value: string
        - name: autoSwapSlotName
          value: string
        - name: localMySqlEnabled
          value: boolean
        - name: managedServiceIdentityId
          value: integer
        - name: xManagedServiceIdentityId
          value: integer
        - name: keyVaultReferenceIdentity
          value: string
        - name: ipSecurityRestrictions
          value:
            - - name: ipAddress
                value: string
              - name: subnetMask
                value: string
              - name: vnetSubnetResourceId
                value: string
              - name: vnetTrafficTag
                value: integer
              - name: subnetTrafficTag
                value: integer
              - name: action
                value: string
              - name: tag
                value: string
              - name: priority
                value: integer
              - name: name
                value: string
              - name: description
                value: string
              - name: headers
                value: object
        - name: ipSecurityRestrictionsDefaultAction
          value: string
        - name: scmIpSecurityRestrictions
          value:
            - - name: ipAddress
                value: string
              - name: subnetMask
                value: string
              - name: vnetSubnetResourceId
                value: string
              - name: vnetTrafficTag
                value: integer
              - name: subnetTrafficTag
                value: integer
              - name: action
                value: string
              - name: tag
                value: string
              - name: priority
                value: integer
              - name: name
                value: string
              - name: description
                value: string
              - name: headers
                value: object
        - name: scmIpSecurityRestrictionsDefaultAction
          value: string
        - name: scmIpSecurityRestrictionsUseMain
          value: boolean
        - name: http20Enabled
          value: boolean
        - name: minTlsVersion
          value: string
        - name: minTlsCipherSuite
          value: string
        - name: scmMinTlsVersion
          value: string
        - name: ftpsState
          value: string
        - name: preWarmedInstanceCount
          value: integer
        - name: functionAppScaleLimit
          value: integer
        - name: elasticWebAppScaleLimit
          value: integer
        - name: healthCheckPath
          value: string
        - name: functionsRuntimeScaleMonitoringEnabled
          value: boolean
        - name: websiteTimeZone
          value: string
        - name: minimumElasticInstanceCount
          value: integer
        - name: azureStorageAccounts
          value: object
        - name: publicNetworkAccess
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>configuration_slots</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.configuration_slots
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```

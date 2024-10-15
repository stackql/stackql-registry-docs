---
title: slots
hide_title: false
hide_table_of_contents: false
keywords:
  - slots
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

Creates, updates, deletes, gets or lists a <code>slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.slots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="extendedLocation" /> | `object` | Extended Location. |
| <CopyableCode code="identity" /> | `object` | Managed service identity. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | Site resource specific properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Gets the details of a web, mobile, or API app. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Gets an app's deployment slots. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Deletes a web, mobile, or API app, or one of the deployment slots. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. |

## `SELECT` examples

Description for Gets an app's deployment slots.


```sql
SELECT
id,
name,
extendedLocation,
identity,
kind,
location,
properties,
tags,
type
FROM azure.app_service.slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>slots</code> resource.

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
INSERT INTO azure.app_service.slots (
name,
resourceGroupName,
slot,
subscriptionId,
kind,
location,
tags,
properties,
identity,
extendedLocation
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ slot }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ identity }}',
'{{ extendedLocation }}'
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
    - name: location
      value: string
    - name: type
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: state
          value: string
        - name: hostNames
          value:
            - string
        - name: repositorySiteName
          value: string
        - name: usageState
          value: string
        - name: enabled
          value: boolean
        - name: enabledHostNames
          value:
            - string
        - name: availabilityState
          value: string
        - name: hostNameSslStates
          value:
            - - name: name
                value: string
              - name: sslState
                value: string
              - name: virtualIP
                value: string
              - name: thumbprint
                value: string
              - name: toUpdate
                value: boolean
              - name: hostType
                value: string
        - name: serverFarmId
          value: string
        - name: reserved
          value: boolean
        - name: isXenon
          value: boolean
        - name: hyperV
          value: boolean
        - name: lastModifiedTimeUtc
          value: string
        - name: dnsConfiguration
          value:
            - name: dnsServers
              value:
                - string
            - name: dnsAltServer
              value: string
            - name: dnsRetryAttemptTimeout
              value: integer
            - name: dnsRetryAttemptCount
              value: integer
            - name: dnsMaxCacheTimeout
              value: integer
            - name: dnsLegacySortOrder
              value: boolean
        - name: vnetRouteAllEnabled
          value: boolean
        - name: vnetImagePullEnabled
          value: boolean
        - name: vnetContentShareEnabled
          value: boolean
        - name: vnetBackupRestoreEnabled
          value: boolean
        - name: siteConfig
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
        - name: functionAppConfig
          value:
            - name: deployment
              value:
                - name: storage
                  value:
                    - name: type
                      value: string
                    - name: value
                      value: string
                    - name: authentication
                      value:
                        - name: type
                          value: string
                        - name: userAssignedIdentityResourceId
                          value: string
                        - name: storageAccountConnectionStringName
                          value: string
            - name: runtime
              value:
                - name: name
                  value: string
                - name: version
                  value: string
            - name: scaleAndConcurrency
              value:
                - name: alwaysReady
                  value:
                    - - name: name
                        value: string
                      - name: instanceCount
                        value: integer
                - name: maximumInstanceCount
                  value: integer
                - name: instanceMemoryMB
                  value: integer
                - name: triggers
                  value:
                    - name: http
                      value:
                        - name: perInstanceConcurrency
                          value: integer
        - name: daprConfig
          value:
            - name: enabled
              value: boolean
            - name: appId
              value: string
            - name: appPort
              value: integer
            - name: httpReadBufferSize
              value: integer
            - name: httpMaxRequestSize
              value: integer
            - name: logLevel
              value: string
            - name: enableApiLogging
              value: boolean
        - name: workloadProfileName
          value: string
        - name: resourceConfig
          value:
            - name: cpu
              value: number
            - name: memory
              value: string
        - name: trafficManagerHostNames
          value:
            - string
        - name: scmSiteAlsoStopped
          value: boolean
        - name: targetSwapSlot
          value: string
        - name: hostingEnvironmentProfile
          value:
            - name: id
              value: string
            - name: name
              value: string
            - name: type
              value: string
        - name: clientAffinityEnabled
          value: boolean
        - name: clientCertEnabled
          value: boolean
        - name: clientCertMode
          value: string
        - name: clientCertExclusionPaths
          value: string
        - name: hostNamesDisabled
          value: boolean
        - name: customDomainVerificationId
          value: string
        - name: outboundIpAddresses
          value: string
        - name: possibleOutboundIpAddresses
          value: string
        - name: containerSize
          value: integer
        - name: dailyMemoryTimeQuota
          value: integer
        - name: suspendedTill
          value: string
        - name: maxNumberOfWorkers
          value: integer
        - name: cloningInfo
          value:
            - name: correlationId
              value: string
            - name: overwrite
              value: boolean
            - name: cloneCustomHostNames
              value: boolean
            - name: cloneSourceControl
              value: boolean
            - name: sourceWebAppId
              value: string
            - name: sourceWebAppLocation
              value: string
            - name: hostingEnvironment
              value: string
            - name: appSettingsOverrides
              value: object
            - name: configureLoadBalancing
              value: boolean
            - name: trafficManagerProfileId
              value: string
            - name: trafficManagerProfileName
              value: string
        - name: resourceGroup
          value: string
        - name: isDefaultContainer
          value: boolean
        - name: defaultHostName
          value: string
        - name: slotSwapStatus
          value:
            - name: timestampUtc
              value: string
            - name: sourceSlotName
              value: string
            - name: destinationSlotName
              value: string
        - name: httpsOnly
          value: boolean
        - name: redundancyMode
          value: string
        - name: inProgressOperationId
          value: string
        - name: publicNetworkAccess
          value: string
        - name: storageAccountRequired
          value: boolean
        - name: keyVaultReferenceIdentity
          value: string
        - name: virtualNetworkSubnetId
          value: string
        - name: managedEnvironmentId
          value: string
    - name: identity
      value:
        - name: type
          value: string
        - name: tenantId
          value: string
        - name: principalId
          value: string
        - name: userAssignedIdentities
          value: object
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>slots</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.slots
SET 
kind = '{{ kind }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>slots</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```

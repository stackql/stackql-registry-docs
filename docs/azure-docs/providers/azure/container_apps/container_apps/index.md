---
title: container_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>container_apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.container_apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="kind" /> | `string` | Metadata used to render different experiences for resources of the same type; e.g. WorkflowApp is a kind of Microsoft.App/ContainerApps type. If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="managedBy" /> | `string` | The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource. |
| <CopyableCode code="properties" /> | `object` | ContainerApp resource specific properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> | Create or update a Container App. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> | Delete a Container App. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> | Patches a Container App using JSON Merge Patch |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
extendedLocation,
identity,
kind,
location,
managedBy,
properties,
tags
FROM azure.container_apps.container_apps
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>container_apps</code> resource.

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
INSERT INTO azure.container_apps.container_apps (
containerAppName,
resourceGroupName,
subscriptionId,
tags,
location,
extendedLocation,
identity,
managedBy,
kind,
properties
)
SELECT 
'{{ containerAppName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ extendedLocation }}',
'{{ identity }}',
'{{ managedBy }}',
'{{ kind }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: managedBy
      value: string
    - name: kind
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: managedEnvironmentId
          value: string
        - name: environmentId
          value: string
        - name: workloadProfileName
          value: []
        - name: patchingConfiguration
          value:
            - name: patchingMode
              value: string
        - name: latestRevisionName
          value: string
        - name: latestReadyRevisionName
          value: string
        - name: latestRevisionFqdn
          value: string
        - name: customDomainVerificationId
          value: string
        - name: configuration
          value:
            - name: secrets
              value:
                - - name: name
                    value: string
                  - name: value
                    value: string
                  - name: identity
                    value: string
                  - name: keyVaultUrl
                    value: string
            - name: activeRevisionsMode
              value: string
            - name: ingress
              value:
                - name: fqdn
                  value: string
                - name: external
                  value: boolean
                - name: targetPort
                  value: integer
                - name: exposedPort
                  value: integer
                - name: transport
                  value: string
                - name: traffic
                  value:
                    - - name: revisionName
                        value: string
                      - name: weight
                        value: integer
                      - name: latestRevision
                        value: boolean
                      - name: label
                        value: string
                - name: customDomains
                  value:
                    - - name: name
                        value: string
                      - name: bindingType
                        value: string
                      - name: certificateId
                        value: string
                - name: allowInsecure
                  value: boolean
                - name: ipSecurityRestrictions
                  value:
                    - - name: name
                        value: string
                      - name: description
                        value: string
                      - name: ipAddressRange
                        value: string
                      - name: action
                        value: string
                - name: stickySessions
                  value:
                    - name: affinity
                      value: string
                - name: clientCertificateMode
                  value: string
                - name: corsPolicy
                  value:
                    - name: allowedOrigins
                      value:
                        - string
                    - name: allowedMethods
                      value:
                        - string
                    - name: allowedHeaders
                      value:
                        - string
                    - name: exposeHeaders
                      value:
                        - string
                    - name: maxAge
                      value: integer
                    - name: allowCredentials
                      value: boolean
                - name: additionalPortMappings
                  value:
                    - - name: external
                        value: boolean
                      - name: targetPort
                        value: integer
                      - name: exposedPort
                        value: integer
                - name: targetPortHttpScheme
                  value: string
            - name: registries
              value:
                - - name: server
                    value: string
                  - name: username
                    value: string
                  - name: passwordSecretRef
                    value: string
                  - name: identity
                    value: string
            - name: dapr
              value:
                - name: enabled
                  value: boolean
                - name: appId
                  value: string
                - name: appProtocol
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
            - name: runtime
              value:
                - name: java
                  value:
                    - name: enableMetrics
                      value: boolean
                    - name: javaAgent
                      value:
                        - name: enabled
                          value: boolean
                        - name: logging
                          value:
                            - name: loggerSettings
                              value:
                                - - name: logger
                                    value: string
                                  - name: level
                                    value: string
                - name: dotnet
                  value:
                    - name: autoConfigureDataProtection
                      value: boolean
            - name: maxInactiveRevisions
              value: integer
            - name: service
              value:
                - name: type
                  value: string
            - name: identitySettings
              value:
                - - name: identity
                    value: string
                  - name: lifecycle
                    value: string
        - name: template
          value:
            - name: revisionSuffix
              value: string
            - name: terminationGracePeriodSeconds
              value: integer
            - name: initContainers
              value:
                - - name: image
                    value: string
                  - name: imageType
                    value: string
                  - name: name
                    value: string
                  - name: command
                    value:
                      - string
                  - name: args
                    value:
                      - string
                  - name: env
                    value:
                      - - name: name
                          value: string
                        - name: value
                          value: string
                        - name: secretRef
                          value: string
                  - name: resources
                    value:
                      - name: cpu
                        value: number
                      - name: memory
                        value: string
                      - name: ephemeralStorage
                        value: string
                  - name: volumeMounts
                    value:
                      - - name: volumeName
                          value: string
                        - name: mountPath
                          value: string
                        - name: subPath
                          value: string
            - name: containers
              value:
                - - name: image
                    value: string
                  - name: imageType
                    value: string
                  - name: name
                    value: string
                  - name: command
                    value:
                      - string
                  - name: args
                    value:
                      - string
                  - name: env
                    value:
                      - - name: name
                          value: string
                        - name: value
                          value: string
                        - name: secretRef
                          value: string
                  - name: volumeMounts
                    value:
                      - - name: volumeName
                          value: string
                        - name: mountPath
                          value: string
                        - name: subPath
                          value: string
                  - name: probes
                    value:
                      - - name: failureThreshold
                          value: integer
                        - name: httpGet
                          value:
                            - name: host
                              value: string
                            - name: httpHeaders
                              value:
                                - - name: name
                                    value: string
                                  - name: value
                                    value: string
                            - name: path
                              value: string
                            - name: port
                              value: integer
                            - name: scheme
                              value: string
                        - name: initialDelaySeconds
                          value: integer
                        - name: periodSeconds
                          value: integer
                        - name: successThreshold
                          value: integer
                        - name: tcpSocket
                          value:
                            - name: host
                              value: string
                            - name: port
                              value: integer
                        - name: terminationGracePeriodSeconds
                          value: integer
                        - name: timeoutSeconds
                          value: integer
                        - name: type
                          value: string
            - name: scale
              value:
                - name: minReplicas
                  value: integer
                - name: maxReplicas
                  value: integer
                - name: rules
                  value:
                    - - name: name
                        value: string
                      - name: azureQueue
                        value:
                          - name: accountName
                            value: string
                          - name: queueName
                            value: string
                          - name: queueLength
                            value: integer
                          - name: auth
                            value:
                              - - name: secretRef
                                  value: string
                                - name: triggerParameter
                                  value: string
                          - name: identity
                            value: string
                      - name: custom
                        value:
                          - name: type
                            value: string
                          - name: metadata
                            value: object
                          - name: auth
                            value:
                              - - name: secretRef
                                  value: string
                                - name: triggerParameter
                                  value: string
                          - name: identity
                            value: string
                      - name: http
                        value:
                          - name: metadata
                            value: object
                          - name: auth
                            value:
                              - - name: secretRef
                                  value: string
                                - name: triggerParameter
                                  value: string
                          - name: identity
                            value: string
                      - name: tcp
                        value:
                          - name: metadata
                            value: object
                          - name: auth
                            value:
                              - - name: secretRef
                                  value: string
                                - name: triggerParameter
                                  value: string
                          - name: identity
                            value: string
            - name: volumes
              value:
                - - name: name
                    value: string
                  - name: storageType
                    value: string
                  - name: storageName
                    value: string
                  - name: secrets
                    value:
                      - - name: secretRef
                          value: string
                        - name: path
                          value: string
                  - name: mountOptions
                    value: string
            - name: serviceBinds
              value:
                - - name: serviceId
                    value: string
                  - name: name
                    value: string
                  - name: clientType
                    value: string
                  - name: customizedKeys
                    value: object
        - name: outboundIpAddresses
          value:
            - string
        - name: eventStreamEndpoint
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>container_apps</code> resource.

```sql
/*+ update */
UPDATE azure.container_apps.container_apps
SET 
tags = '{{ tags }}',
location = '{{ location }}',
extendedLocation = '{{ extendedLocation }}',
identity = '{{ identity }}',
managedBy = '{{ managedBy }}',
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
containerAppName = '{{ containerAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>container_apps</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.container_apps
WHERE containerAppName = '{{ containerAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

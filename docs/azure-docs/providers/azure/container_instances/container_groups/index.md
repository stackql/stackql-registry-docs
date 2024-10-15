---
title: container_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - container_groups
  - container_instances
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

Creates, updates, deletes, gets or lists a <code>container_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_instances.container_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="identity" /> | `object` | Identity for the container group. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The container group properties |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The resource type. |
| <CopyableCode code="zones" /> | `array` | The zones for the container group. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerGroupName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified container group in the specified subscription and resource group. The operation returns the properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of container groups in the specified subscription. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of container groups in a specified subscription and resource group. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="containerGroupName, resourceGroupName, subscriptionId" /> | Create or update container groups with specified configurations. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="containerGroupName, resourceGroupName, subscriptionId" /> | Delete the specified container group in the specified subscription and resource group. The operation does not delete other resources provided by the user, such as volumes. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="containerGroupName, resourceGroupName, subscriptionId" /> | Updates container group tags with specified values. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="containerGroupName, resourceGroupName, subscriptionId" /> | Restarts all containers in a container group in place. If container image has updates, new image will be downloaded. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="containerGroupName, resourceGroupName, subscriptionId" /> | Starts all containers in a container group. Compute resources will be allocated and billing will start. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="containerGroupName, resourceGroupName, subscriptionId" /> | Stops all containers in a container group. Compute resources will be deallocated and billing will stop. |

## `SELECT` examples

Get a list of container groups in the specified subscription. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.


```sql
SELECT
id,
name,
identity,
location,
properties,
tags,
type,
zones
FROM azure.container_instances.container_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>container_groups</code> resource.

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
INSERT INTO azure.container_instances.container_groups (
containerGroupName,
resourceGroupName,
subscriptionId,
location,
tags,
zones,
identity,
properties
)
SELECT 
'{{ containerGroupName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ zones }}',
'{{ identity }}',
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
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object
    - name: zones
      value:
        - string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: containers
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: image
                    value: string
                  - name: command
                    value:
                      - string
                  - name: ports
                    value:
                      - - name: protocol
                          value: string
                        - name: port
                          value: integer
                  - name: environmentVariables
                    value:
                      - - name: name
                          value: string
                        - name: value
                          value: string
                        - name: secureValue
                          value: string
                  - name: instanceView
                    value:
                      - name: restartCount
                        value: integer
                      - name: currentState
                        value:
                          - name: state
                            value: string
                          - name: startTime
                            value: string
                          - name: exitCode
                            value: integer
                          - name: finishTime
                            value: string
                          - name: detailStatus
                            value: string
                      - name: events
                        value:
                          - - name: count
                              value: integer
                            - name: firstTimestamp
                              value: string
                            - name: lastTimestamp
                              value: string
                            - name: name
                              value: string
                            - name: message
                              value: string
                            - name: type
                              value: string
                  - name: resources
                    value:
                      - name: requests
                        value:
                          - name: memoryInGB
                            value: number
                          - name: cpu
                            value: number
                          - name: gpu
                            value:
                              - name: count
                                value: integer
                              - name: sku
                                value: string
                      - name: limits
                        value:
                          - name: memoryInGB
                            value: number
                          - name: cpu
                            value: number
                  - name: volumeMounts
                    value:
                      - - name: name
                          value: string
                        - name: mountPath
                          value: string
                        - name: readOnly
                          value: boolean
                  - name: livenessProbe
                    value:
                      - name: exec
                        value:
                          - name: command
                            value:
                              - string
                      - name: httpGet
                        value:
                          - name: path
                            value: string
                          - name: port
                            value: integer
                          - name: scheme
                            value: string
                          - name: httpHeaders
                            value:
                              - - name: name
                                  value: string
                                - name: value
                                  value: string
                      - name: initialDelaySeconds
                        value: integer
                      - name: periodSeconds
                        value: integer
                      - name: failureThreshold
                        value: integer
                      - name: successThreshold
                        value: integer
                      - name: timeoutSeconds
                        value: integer
                  - name: securityContext
                    value:
                      - name: privileged
                        value: boolean
                      - name: allowPrivilegeEscalation
                        value: boolean
                      - name: capabilities
                        value:
                          - name: add
                            value:
                              - string
                          - name: drop
                            value:
                              - string
                      - name: runAsGroup
                        value: integer
                      - name: runAsUser
                        value: integer
                      - name: seccompProfile
                        value: string
                  - name: configMap
                    value:
                      - name: keyValuePairs
                        value: object
        - name: imageRegistryCredentials
          value:
            - - name: server
                value: string
              - name: username
                value: string
              - name: password
                value: string
              - name: identity
                value: string
              - name: identityUrl
                value: string
        - name: restartPolicy
          value: string
        - name: ipAddress
          value:
            - name: ports
              value:
                - - name: protocol
                    value: string
                  - name: port
                    value: integer
            - name: type
              value: string
            - name: ip
              value: string
            - name: dnsNameLabel
              value: string
            - name: autoGeneratedDomainNameLabelScope
              value: string
            - name: fqdn
              value: string
        - name: osType
          value: string
        - name: volumes
          value:
            - - name: name
                value: string
              - name: azureFile
                value:
                  - name: shareName
                    value: string
                  - name: readOnly
                    value: boolean
                  - name: storageAccountName
                    value: string
                  - name: storageAccountKey
                    value: string
              - name: emptyDir
                value: []
              - name: secret
                value: []
              - name: gitRepo
                value:
                  - name: directory
                    value: string
                  - name: repository
                    value: string
                  - name: revision
                    value: string
        - name: instanceView
          value:
            - name: events
              value:
                - - name: count
                    value: integer
                  - name: firstTimestamp
                    value: string
                  - name: lastTimestamp
                    value: string
                  - name: name
                    value: string
                  - name: message
                    value: string
                  - name: type
                    value: string
            - name: state
              value: string
        - name: diagnostics
          value:
            - name: logAnalytics
              value:
                - name: workspaceId
                  value: string
                - name: workspaceKey
                  value: string
                - name: logType
                  value: string
                - name: metadata
                  value: object
                - name: workspaceResourceId
                  value: string
        - name: subnetIds
          value:
            - - name: id
                value: string
              - name: name
                value: string
        - name: dnsConfig
          value:
            - name: nameServers
              value:
                - string
            - name: searchDomains
              value: string
            - name: options
              value: string
        - name: sku
          value: []
        - name: encryptionProperties
          value:
            - name: vaultBaseUrl
              value: string
            - name: keyName
              value: string
            - name: keyVersion
              value: string
            - name: identity
              value: string
        - name: initContainers
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: image
                    value: string
                  - name: command
                    value:
                      - string
                  - name: environmentVariables
                    value:
                      - - name: name
                          value: string
                        - name: value
                          value: string
                        - name: secureValue
                          value: string
                  - name: instanceView
                    value:
                      - name: restartCount
                        value: integer
                      - name: events
                        value:
                          - - name: count
                              value: integer
                            - name: firstTimestamp
                              value: string
                            - name: lastTimestamp
                              value: string
                            - name: name
                              value: string
                            - name: message
                              value: string
                            - name: type
                              value: string
                  - name: volumeMounts
                    value:
                      - - name: name
                          value: string
                        - name: mountPath
                          value: string
                        - name: readOnly
                          value: boolean
        - name: extensions
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: extensionType
                    value: string
                  - name: version
                    value: string
                  - name: settings
                    value: object
                  - name: protectedSettings
                    value: object
        - name: confidentialComputeProperties
          value:
            - name: ccePolicy
              value: string
        - name: priority
          value: string
        - name: containerGroupProfile
          value:
            - name: id
              value: string
            - name: revision
              value: integer
        - name: standbyPoolProfile
          value:
            - name: id
              value: string
            - name: failContainerGroupCreateOnReuseFailure
              value: boolean
        - name: isCreatedFromStandbyPool
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>container_groups</code> resource.

```sql
/*+ update */
UPDATE azure.container_instances.container_groups
SET 
location = '{{ location }}',
tags = '{{ tags }}',
zones = '{{ zones }}'
WHERE 
containerGroupName = '{{ containerGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>container_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_instances.container_groups
WHERE containerGroupName = '{{ containerGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

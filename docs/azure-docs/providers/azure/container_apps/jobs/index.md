---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Container Apps Job resource specific properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Create or Update a Container Apps Job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Delete a Container Apps Job. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Patches a Container Apps Job using JSON Merge Patch |
| <CopyableCode code="proxy_get" /> | `EXEC` | <CopyableCode code="apiName, jobName, resourceGroupName, subscriptionId" /> | Get the properties of a Container App Job. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="stop_execution" /> | `EXEC` | <CopyableCode code="jobExecutionName, jobName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="stop_multiple_executions" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
extendedLocation,
identity,
location,
properties,
tags
FROM azure.container_apps.jobs
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>jobs</code> resource.

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
INSERT INTO azure.container_apps.jobs (
jobName,
resourceGroupName,
subscriptionId,
tags,
location,
extendedLocation,
identity,
properties
)
SELECT 
'{{ jobName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ extendedLocation }}',
'{{ identity }}',
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
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: environmentId
          value: string
        - name: workloadProfileName
          value: []
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
            - name: triggerType
              value: string
            - name: replicaTimeout
              value: integer
            - name: replicaRetryLimit
              value: integer
            - name: manualTriggerConfig
              value:
                - name: replicaCompletionCount
                  value: []
                - name: parallelism
                  value: []
            - name: scheduleTriggerConfig
              value:
                - name: cronExpression
                  value: string
            - name: eventTriggerConfig
              value:
                - name: scale
                  value:
                    - name: pollingInterval
                      value: []
                    - name: minExecutions
                      value: integer
                    - name: maxExecutions
                      value: integer
                    - name: rules
                      value:
                        - - name: name
                            value: string
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
            - name: identitySettings
              value:
                - - name: identity
                    value: string
                  - name: lifecycle
                    value: string
        - name: template
          value:
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
        - name: outboundIpAddresses
          value:
            - string
        - name: eventStreamEndpoint
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>jobs</code> resource.

```sql
/*+ update */
UPDATE azure.container_apps.jobs
SET 
extendedLocation = '{{ extendedLocation }}',
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>jobs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.jobs
WHERE jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

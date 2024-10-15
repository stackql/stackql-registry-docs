---
title: container_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>container_apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.container_apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | ContainerApp resource specific properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Create or update a Container App. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Delete a Container App. |

## `SELECT` examples




```sql
SELECT
id,
name,
kind,
location,
properties,
tags,
type
FROM azure.app_service.container_apps
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
INSERT INTO azure.app_service.container_apps (
name,
resourceGroupName,
subscriptionId,
kind,
location,
tags,
properties
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ location }}',
'{{ tags }}',
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
    - name: location
      value: string
    - name: type
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: kubeEnvironmentId
          value: string
        - name: latestRevisionName
          value: string
        - name: latestRevisionFqdn
          value: string
        - name: configuration
          value:
            - name: secrets
              value:
                - - name: name
                    value: string
                  - name: value
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
                - name: allowInsecure
                  value: boolean
            - name: registries
              value:
                - - name: server
                    value: string
                  - name: username
                    value: string
                  - name: passwordSecretRef
                    value: string
        - name: template
          value:
            - name: revisionSuffix
              value: string
            - name: containers
              value:
                - - name: image
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
            - name: dapr
              value:
                - name: enabled
                  value: boolean
                - name: appId
                  value: string
                - name: appPort
                  value: integer
                - name: components
                  value:
                    - - name: name
                        value: string
                      - name: type
                        value: string
                      - name: version
                        value: string
                      - name: metadata
                        value:
                          - - name: name
                              value: string
                            - name: value
                              value: string
                            - name: secretRef
                              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>container_apps</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.container_apps
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

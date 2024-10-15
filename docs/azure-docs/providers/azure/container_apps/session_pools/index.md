---
title: session_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - session_pools
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

Creates, updates, deletes, gets or lists a <code>session_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>session_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.session_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Container App session pool resource specific properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sessionPoolName, subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, sessionPoolName, subscriptionId" /> | Create or update a session pool with the given properties. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sessionPoolName, subscriptionId" /> | Delete the session pool with the given name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, sessionPoolName, subscriptionId" /> | Patches a session pool using JSON merge patch |

## `SELECT` examples




```sql
SELECT
location,
properties,
tags
FROM azure.container_apps.session_pools
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>session_pools</code> resource.

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
INSERT INTO azure.container_apps.session_pools (
resourceGroupName,
sessionPoolName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ sessionPoolName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
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
    - name: properties
      value:
        - name: environmentId
          value: string
        - name: containerType
          value: string
        - name: poolManagementType
          value: string
        - name: nodeCount
          value: integer
        - name: scaleConfiguration
          value:
            - name: maxConcurrentSessions
              value: integer
            - name: readySessionInstances
              value: integer
        - name: secrets
          value:
            - - name: name
                value: string
              - name: value
                value: string
        - name: dynamicPoolConfiguration
          value:
            - name: executionType
              value: string
            - name: cooldownPeriodInSeconds
              value: integer
        - name: customContainerTemplate
          value:
            - name: registryCredentials
              value:
                - name: registryServer
                  value: string
                - name: username
                  value: string
                - name: passwordSecretRef
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
            - name: ingress
              value:
                - name: targetPort
                  value: integer
        - name: sessionNetworkConfiguration
          value:
            - name: status
              value: string
        - name: poolManagementEndpoint
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>session_pools</code> resource.

```sql
/*+ update */
UPDATE azure.container_apps.session_pools
SET 
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND sessionPoolName = '{{ sessionPoolName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>session_pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.session_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sessionPoolName = '{{ sessionPoolName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

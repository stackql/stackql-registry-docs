---
title: app_resiliencies
hide_title: false
hide_table_of_contents: false
keywords:
  - app_resiliencies
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

Creates, updates, deletes, gets or lists a <code>app_resiliencies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_resiliencies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.app_resiliencies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | App Resiliency resource specific properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appName, name, resourceGroupName, subscriptionId" /> | Get container app resiliency policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appName, resourceGroupName, subscriptionId" /> | List container app resiliency policies. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="appName, name, resourceGroupName, subscriptionId" /> | Create or update container app resiliency policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appName, name, resourceGroupName, subscriptionId" /> | Delete container app resiliency policy. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="appName, name, resourceGroupName, subscriptionId" /> | Update container app resiliency policy. |

## `SELECT` examples

List container app resiliency policies.


```sql
SELECT
properties
FROM azure.container_apps.app_resiliencies
WHERE appName = '{{ appName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>app_resiliencies</code> resource.

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
INSERT INTO azure.container_apps.app_resiliencies (
appName,
name,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ appName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: timeoutPolicy
          value:
            - name: responseTimeoutInSeconds
              value: integer
            - name: connectionTimeoutInSeconds
              value: integer
        - name: httpRetryPolicy
          value:
            - name: maxRetries
              value: integer
            - name: retryBackOff
              value:
                - name: initialDelayInMilliseconds
                  value: integer
                - name: maxIntervalInMilliseconds
                  value: integer
            - name: matches
              value:
                - name: headers
                  value:
                    - - name: header
                        value: string
                      - name: match
                        value:
                          - name: exactMatch
                            value: string
                          - name: prefixMatch
                            value: string
                          - name: suffixMatch
                            value: string
                          - name: regexMatch
                            value: string
                - name: httpStatusCodes
                  value:
                    - integer
                - name: errors
                  value:
                    - string
        - name: tcpRetryPolicy
          value:
            - name: maxConnectAttempts
              value: integer
        - name: circuitBreakerPolicy
          value:
            - name: consecutiveErrors
              value: integer
            - name: intervalInSeconds
              value: integer
            - name: maxEjectionPercent
              value: integer
        - name: httpConnectionPool
          value:
            - name: http1MaxPendingRequests
              value: integer
            - name: http2MaxRequests
              value: integer
        - name: tcpConnectionPool
          value:
            - name: maxConnections
              value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>app_resiliencies</code> resource.

```sql
/*+ update */
UPDATE azure.container_apps.app_resiliencies
SET 
properties = '{{ properties }}'
WHERE 
appName = '{{ appName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>app_resiliencies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.app_resiliencies
WHERE appName = '{{ appName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

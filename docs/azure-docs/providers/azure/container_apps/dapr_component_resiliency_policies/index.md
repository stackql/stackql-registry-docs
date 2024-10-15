---
title: dapr_component_resiliency_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - dapr_component_resiliency_policies
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

Creates, updates, deletes, gets or lists a <code>dapr_component_resiliency_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dapr_component_resiliency_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.dapr_component_resiliency_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Dapr Component Resiliency Policy resource specific properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="componentName, environmentName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="componentName, environmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="componentName, environmentName, name, resourceGroupName, subscriptionId" /> | Creates or updates a resiliency policy for a Dapr component. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="componentName, environmentName, name, resourceGroupName, subscriptionId" /> | Delete a resiliency policy for a Dapr component. |

## `SELECT` examples




```sql
SELECT
properties
FROM azure.container_apps.dapr_component_resiliency_policies
WHERE componentName = '{{ componentName }}'
AND environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dapr_component_resiliency_policies</code> resource.

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
INSERT INTO azure.container_apps.dapr_component_resiliency_policies (
componentName,
environmentName,
name,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ componentName }}',
'{{ environmentName }}',
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
        - name: inboundPolicy
          value:
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
            - name: timeoutPolicy
              value:
                - name: responseTimeoutInSeconds
                  value: integer
            - name: circuitBreakerPolicy
              value:
                - name: consecutiveErrors
                  value: integer
                - name: timeoutInSeconds
                  value: integer
                - name: intervalInSeconds
                  value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>dapr_component_resiliency_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.dapr_component_resiliency_policies
WHERE componentName = '{{ componentName }}'
AND environmentName = '{{ environmentName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

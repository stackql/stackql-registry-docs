---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.deployments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deployments', value: 'view', },
        { label: 'deployments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="active" /> | `text` | field from the `properties` object |
| <CopyableCode code="appName" /> | `text` | field from the `properties` object |
| <CopyableCode code="deploymentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="instances" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Sku of Azure Spring Apps |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Deployment resource properties payload |
| <CopyableCode code="sku" /> | `object` | Sku of Azure Spring Apps |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Get a Deployment and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in an App. |
| <CopyableCode code="list_for_cluster" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | List deployments for a certain service |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Create a new Deployment or update an exiting Deployment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Operation to delete a Deployment. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Operation to update an exiting Deployment. |
| <CopyableCode code="disable_remote_debugging" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Disable remote debugging. |
| <CopyableCode code="enable_remote_debugging" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Enable remote debugging. |
| <CopyableCode code="generate_heap_dump" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Generate Heap Dump |
| <CopyableCode code="generate_thread_dump" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Generate Thread Dump |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Restart the deployment. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Start the deployment. |
| <CopyableCode code="start_jfr" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Start JFR |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Stop the deployment. |

## `SELECT` examples

List deployments for a certain service

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deployments', value: 'view', },
        { label: 'deployments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
active,
appName,
deploymentName,
deployment_settings,
instances,
provisioning_state,
resourceGroupName,
serviceName,
sku,
source,
status,
subscriptionId
FROM azure.spring_apps.vw_deployments
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
sku
FROM azure.spring_apps.deployments
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployments</code> resource.

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
INSERT INTO azure.spring_apps.deployments (
appName,
deploymentName,
resourceGroupName,
serviceName,
subscriptionId,
properties,
sku
)
SELECT 
'{{ appName }}',
'{{ deploymentName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ sku }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: source
          value:
            - name: type
              value: string
            - name: version
              value: string
        - name: deploymentSettings
          value:
            - name: resourceRequests
              value:
                - name: cpu
                  value: string
                - name: memory
                  value: string
            - name: environmentVariables
              value: object
            - name: apms
              value: []
            - name: addonConfigs
              value: object
            - name: livenessProbe
              value:
                - name: probeAction
                  value:
                    - name: type
                      value: string
                - name: disableProbe
                  value: boolean
                - name: initialDelaySeconds
                  value: integer
                - name: periodSeconds
                  value: integer
                - name: timeoutSeconds
                  value: integer
                - name: failureThreshold
                  value: integer
                - name: successThreshold
                  value: integer
            - name: terminationGracePeriodSeconds
              value: integer
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
            - name: containerProbeSettings
              value:
                - name: disableProbe
                  value: boolean
        - name: provisioningState
          value: string
        - name: status
          value: string
        - name: active
          value: boolean
        - name: instances
          value:
            - - name: name
                value: string
              - name: status
                value: string
              - name: reason
                value: string
              - name: discoveryStatus
                value: string
              - name: startTime
                value: string
              - name: zone
                value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: capacity
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>deployments</code> resource.

```sql
/*+ update */
UPDATE azure.spring_apps.deployments
SET 
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
appName = '{{ appName }}'
AND deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>deployments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.deployments
WHERE appName = '{{ appName }}'
AND deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

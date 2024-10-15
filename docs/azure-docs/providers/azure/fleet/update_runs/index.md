---
title: update_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - update_runs
  - fleet
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

Creates, updates, deletes, gets or lists a <code>update_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>update_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fleet.update_runs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_update_runs', value: 'view', },
        { label: 'update_runs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="fleetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_cluster_update" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="strategy" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="updateRunName" /> | `text` | field from the `properties` object |
| <CopyableCode code="update_strategy_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="eTag" /> | `string` | If eTag is provided in the response body, it may also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. |
| <CopyableCode code="properties" /> | `object` | The properties of the UpdateRun. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId, updateRunName" /> | Get a UpdateRun |
| <CopyableCode code="list_by_fleet" /> | `SELECT` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId" /> | List UpdateRun resources by Fleet |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId, updateRunName" /> | Create a UpdateRun |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId, updateRunName" /> | Delete a UpdateRun |
| <CopyableCode code="skip" /> | `EXEC` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId, updateRunName, data__targets" /> | Skips one or a combination of member/group/stage/afterStageWait(s) of an update run. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId, updateRunName" /> | Starts an UpdateRun. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId, updateRunName" /> | Stops an UpdateRun. |

## `SELECT` examples

List UpdateRun resources by Fleet

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_update_runs', value: 'view', },
        { label: 'update_runs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
e_tag,
fleetName,
managed_cluster_update,
provisioning_state,
resourceGroupName,
status,
strategy,
subscriptionId,
updateRunName,
update_strategy_id
FROM azure.fleet.vw_update_runs
WHERE fleetName = '{{ fleetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
eTag,
properties
FROM azure.fleet.update_runs
WHERE fleetName = '{{ fleetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>update_runs</code> resource.

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
INSERT INTO azure.fleet.update_runs (
fleetName,
resourceGroupName,
subscriptionId,
updateRunName,
properties
)
SELECT 
'{{ fleetName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ updateRunName }}',
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
        - name: provisioningState
          value: []
        - name: updateStrategyId
          value: []
        - name: strategy
          value:
            - name: stages
              value:
                - - name: name
                    value: string
                  - name: groups
                    value:
                      - - name: name
                          value: string
                  - name: afterStageWaitInSeconds
                    value: integer
        - name: managedClusterUpdate
          value:
            - name: upgrade
              value:
                - name: type
                  value: []
                - name: kubernetesVersion
                  value: []
            - name: nodeImageSelection
              value:
                - name: type
                  value: []
        - name: status
          value:
            - name: status
              value:
                - name: startTime
                  value: string
                - name: completedTime
                  value: string
                - name: state
                  value: []
                - name: error
                  value:
                    - name: code
                      value: string
                    - name: message
                      value: string
                    - name: target
                      value: string
                    - name: details
                      value:
                        - - name: code
                            value: string
                          - name: message
                            value: string
                          - name: target
                            value: string
                          - name: details
                            value:
                              - - name: code
                                  value: string
                                - name: message
                                  value: string
                                - name: target
                                  value: string
                                - name: details
                                  value:
                                    - - name: code
                                        value: string
                                      - name: message
                                        value: string
                                      - name: target
                                        value: string
                                      - name: details
                                        value:
                                          - - name: code
                                              value: string
                                            - name: message
                                              value: string
                                            - name: target
                                              value: string
                                            - name: details
                                              value:
                                                - - name: code
                                                    value: string
                                                  - name: message
                                                    value: string
                                                  - name: target
                                                    value: string
                                                  - name: details
                                                    value:
                                                      - - name: code
                                                          value: string
                                                        - name: message
                                                          value: string
                                                        - name: target
                                                          value: string
                                                        - name: details
                                                          value:
                                                            - []
                                                        - name: additionalInfo
                                                          value:
                                                            - []
                                                  - name: additionalInfo
                                                    value:
                                                      - - name: type
                                                          value: string
                                                        - name: info
                                                          value: object
                                            - name: additionalInfo
                                              value:
                                                - - name: type
                                                    value: string
                                                  - name: info
                                                    value: object
                                      - name: additionalInfo
                                        value:
                                          - - name: type
                                              value: string
                                            - name: info
                                              value: object
                                - name: additionalInfo
                                  value:
                                    - - name: type
                                        value: string
                                      - name: info
                                        value: object
                          - name: additionalInfo
                            value:
                              - - name: type
                                  value: string
                                - name: info
                                  value: object
                    - name: additionalInfo
                      value:
                        - - name: type
                            value: string
                          - name: info
                            value: object
            - name: stages
              value:
                - - name: name
                    value: string
                  - name: groups
                    value:
                      - - name: name
                          value: string
                        - name: members
                          value:
                            - - name: name
                                value: string
                              - name: clusterResourceId
                                value: string
                              - name: operationId
                                value: string
                              - name: message
                                value: string
                  - name: afterStageWaitStatus
                    value:
                      - name: waitDurationInSeconds
                        value: integer
            - name: nodeImageSelection
              value:
                - name: selectedNodeImageVersions
                  value:
                    - - name: version
                        value: string
    - name: eTag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>update_runs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.fleet.update_runs
WHERE fleetName = '{{ fleetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND updateRunName = '{{ updateRunName }}';
```

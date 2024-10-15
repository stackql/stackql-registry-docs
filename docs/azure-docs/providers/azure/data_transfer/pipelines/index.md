---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - data_transfer
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

Creates, updates, deletes, gets or lists a <code>pipelines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_transfer.pipelines" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pipelines', value: 'view', },
        { label: 'pipelines', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="flow_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="pipelineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_cloud" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscribers" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of pipeline |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId" /> | Gets pipeline resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets pipelines in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets pipelines in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId, data__location" /> | Creates or updates the pipeline resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId" /> | Deletes the pipeline resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId" /> | Updates the pipeline resource. |
| <CopyableCode code="approve_connection" /> | `EXEC` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId, data__id" /> | Approves the specified connection in a pipeline. |
| <CopyableCode code="reject_connection" /> | `EXEC` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId, data__id" /> | Rejects the specified connection in a pipeline. |

## `SELECT` examples

Gets pipelines in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pipelines', value: 'view', },
        { label: 'pipelines', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
connections,
display_name,
flow_types,
location,
pipelineName,
policies,
provisioning_state,
remote_cloud,
resourceGroupName,
subscribers,
subscriptionId,
tags
FROM azure.data_transfer.vw_pipelines
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.data_transfer.pipelines
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pipelines</code> resource.

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
INSERT INTO azure.data_transfer.pipelines (
pipelineName,
resourceGroupName,
subscriptionId,
data__location,
properties,
tags,
location
)
SELECT 
'{{ pipelineName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: remoteCloud
          value: string
        - name: displayName
          value: string
        - name: connections
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: location
                value: string
              - name: etag
                value: string
              - name: systemData
                value:
                  - name: createdBy
                    value: string
                  - name: createdByType
                    value: string
                  - name: createdAt
                    value: string
                  - name: lastModifiedBy
                    value: string
                  - name: lastModifiedByType
                    value: string
                  - name: lastModifiedAt
                    value: string
              - name: properties
                value:
                  - name: internalMetadata
                    value:
                      - name: operationStatus
                        value:
                          - name: status
                            value: string
                          - name: id
                            value: string
                          - name: message
                            value: string
                      - name: statusSetBy
                        value: string
        - name: subscribers
          value:
            - - name: email
                value: string
              - name: notifications
                value: integer
        - name: provisioningState
          value: string
        - name: policies
          value:
            - string
        - name: flowTypes
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>pipelines</code> resource.

```sql
/*+ update */
UPDATE azure.data_transfer.pipelines
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
pipelineName = '{{ pipelineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>pipelines</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_transfer.pipelines
WHERE pipelineName = '{{ pipelineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

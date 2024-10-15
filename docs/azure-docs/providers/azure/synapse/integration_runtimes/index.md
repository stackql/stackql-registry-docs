---
title: integration_runtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtimes
  - synapse
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

Creates, updates, deletes, gets or lists a <code>integration_runtimes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_runtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.integration_runtimes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_runtimes', value: 'view', },
        { label: 'integration_runtimes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="integrationRuntimeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Azure Synapse nested object which serves as a compute resource for activities. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Get an integration runtime |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | List all integration runtimes |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName, data__properties" /> | Create an integration runtime |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Delete an integration runtime |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Update an integration runtime |
| <CopyableCode code="disable_interactive_query" /> | `EXEC` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Disable interactive query in integration runtime |
| <CopyableCode code="enable_interactive_query" /> | `EXEC` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Enable interactive query in integration runtime |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Start an integration runtime |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Stop an integration runtime |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Upgrade an integration runtime |

## `SELECT` examples

List all integration runtimes

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_runtimes', value: 'view', },
        { label: 'integration_runtimes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
integrationRuntimeName,
resourceGroupName,
subscriptionId,
type,
workspaceName
FROM azure.synapse.vw_integration_runtimes
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.synapse.integration_runtimes
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>integration_runtimes</code> resource.

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
INSERT INTO azure.synapse.integration_runtimes (
integrationRuntimeName,
resourceGroupName,
subscriptionId,
workspaceName,
data__properties,
properties
)
SELECT 
'{{ integrationRuntimeName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__properties }}',
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
        - name: type
          value: []
        - name: description
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>integration_runtimes</code> resource.

```sql
/*+ update */
UPDATE azure.synapse.integration_runtimes
SET 
autoUpdate = '{{ autoUpdate }}',
updateDelayOffset = '{{ updateDelayOffset }}'
WHERE 
integrationRuntimeName = '{{ integrationRuntimeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>integration_runtimes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.synapse.integration_runtimes
WHERE integrationRuntimeName = '{{ integrationRuntimeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

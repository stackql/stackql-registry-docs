---
title: integration_runtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtimes
  - data_factory
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.integration_runtimes" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag identifies change in the resource. |
| <CopyableCode code="factoryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="integrationRuntimeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | Etag identifies change in the resource. |
| <CopyableCode code="properties" /> | `object` | Azure Data Factory nested object which serves as a compute resource for activities. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Gets an integration runtime. |
| <CopyableCode code="list_by_factory" /> | `SELECT` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Lists integration runtimes. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="factoryName, integrationRuntimeName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an integration runtime. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Deletes an integration runtime. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Updates an integration runtime. |
| <CopyableCode code="regenerate_auth_key" /> | `EXEC` | <CopyableCode code="factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Regenerates the authentication key for an integration runtime. |
| <CopyableCode code="remove_links" /> | `EXEC` | <CopyableCode code="factoryName, integrationRuntimeName, resourceGroupName, subscriptionId, data__factoryName" /> | Remove all linked integration runtimes under specific data factory in a self-hosted integration runtime. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Starts a ManagedReserved type integration runtime. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Stops a ManagedReserved type integration runtime. |
| <CopyableCode code="sync_credentials" /> | `EXEC` | <CopyableCode code="factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Force the integration runtime to synchronize credentials across integration runtime nodes, and this will override the credentials across all worker nodes with those available on the dispatcher node. If you already have the latest credential backup file, you should manually import it (preferred) on any self-hosted integration runtime node than using this API directly. |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Upgrade self-hosted integration runtime to latest version if availability. |

## `SELECT` examples

Lists integration runtimes.

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
id,
name,
description,
etag,
factoryName,
integrationRuntimeName,
resourceGroupName,
subscriptionId,
type
FROM azure.data_factory.vw_integration_runtimes
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.data_factory.integration_runtimes
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
INSERT INTO azure.data_factory.integration_runtimes (
factoryName,
integrationRuntimeName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ factoryName }}',
'{{ integrationRuntimeName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
    - name: etag
      value: string
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
UPDATE azure.data_factory.integration_runtimes
SET 
autoUpdate = '{{ autoUpdate }}',
updateDelayOffset = '{{ updateDelayOffset }}'
WHERE 
factoryName = '{{ factoryName }}'
AND integrationRuntimeName = '{{ integrationRuntimeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>integration_runtimes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_factory.integration_runtimes
WHERE factoryName = '{{ factoryName }}'
AND integrationRuntimeName = '{{ integrationRuntimeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

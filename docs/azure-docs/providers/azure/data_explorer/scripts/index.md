---
title: scripts
hide_title: false
hide_table_of_contents: false
keywords:
  - scripts
  - data_explorer
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

Creates, updates, deletes, gets or lists a <code>scripts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scripts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.scripts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scripts', value: 'view', },
        { label: 'scripts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="continue_on_errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="force_update_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scriptName" /> | `text` | field from the `properties` object |
| <CopyableCode code="script_content" /> | `text` | field from the `properties` object |
| <CopyableCode code="script_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="script_url_sas_token" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A class representing database script property. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, scriptName, subscriptionId" /> | Gets a Kusto cluster database script. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Returns the list of database scripts for given database. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, scriptName, subscriptionId" /> | Creates a Kusto database script. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, databaseName, resourceGroupName, scriptName, subscriptionId" /> | Deletes a Kusto database script. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, databaseName, resourceGroupName, scriptName, subscriptionId" /> | Updates a database script. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__name, data__type" /> | Checks that the script name is valid and is not already in use. |

## `SELECT` examples

Returns the list of database scripts for given database.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scripts', value: 'view', },
        { label: 'scripts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
clusterName,
continue_on_errors,
databaseName,
force_update_tag,
provisioning_state,
resourceGroupName,
scriptName,
script_content,
script_url,
script_url_sas_token,
subscriptionId,
system_data
FROM azure.data_explorer.vw_scripts
WHERE clusterName = '{{ clusterName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.data_explorer.scripts
WHERE clusterName = '{{ clusterName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scripts</code> resource.

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
INSERT INTO azure.data_explorer.scripts (
clusterName,
databaseName,
resourceGroupName,
scriptName,
subscriptionId,
properties
)
SELECT 
'{{ clusterName }}',
'{{ databaseName }}',
'{{ resourceGroupName }}',
'{{ scriptName }}',
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
        - name: scriptUrl
          value: string
        - name: scriptUrlSasToken
          value: string
        - name: scriptContent
          value: string
        - name: forceUpdateTag
          value: string
        - name: continueOnErrors
          value: boolean
        - name: provisioningState
          value: []
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>scripts</code> resource.

```sql
/*+ update */
UPDATE azure.data_explorer.scripts
SET 
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND scriptName = '{{ scriptName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>scripts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_explorer.scripts
WHERE clusterName = '{{ clusterName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND scriptName = '{{ scriptName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

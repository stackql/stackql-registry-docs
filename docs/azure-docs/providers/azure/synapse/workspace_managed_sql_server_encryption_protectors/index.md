---
title: workspace_managed_sql_server_encryption_protectors
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_managed_sql_server_encryption_protectors
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

Creates, updates, deletes, gets or lists a <code>workspace_managed_sql_server_encryption_protectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_managed_sql_server_encryption_protectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.workspace_managed_sql_server_encryption_protectors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_managed_sql_server_encryption_protectors', value: 'view', },
        { label: 'workspace_managed_sql_server_encryption_protectors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="encryptionProtectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_key_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_key_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subregion" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="thumbprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties for an encryption protector execution. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="encryptionProtectorName, resourceGroupName, subscriptionId, workspaceName" /> | Get workspace managed sql server's encryption protector. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Get list of encryption protectors for workspace managed sql server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="encryptionProtectorName, resourceGroupName, subscriptionId, workspaceName" /> | Updates workspace managed sql server's encryption protector. |
| <CopyableCode code="revalidate" /> | `EXEC` | <CopyableCode code="encryptionProtectorName, resourceGroupName, subscriptionId, workspaceName" /> | Revalidates workspace managed sql server's existing encryption protector. |

## `SELECT` examples

Get list of encryption protectors for workspace managed sql server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_managed_sql_server_encryption_protectors', value: 'view', },
        { label: 'workspace_managed_sql_server_encryption_protectors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
encryptionProtectorName,
kind,
location,
resourceGroupName,
server_key_name,
server_key_type,
subregion,
subscriptionId,
thumbprint,
uri,
workspaceName
FROM azure.synapse.vw_workspace_managed_sql_server_encryption_protectors
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
location,
properties
FROM azure.synapse.workspace_managed_sql_server_encryption_protectors
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_managed_sql_server_encryption_protectors</code> resource.

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
INSERT INTO azure.synapse.workspace_managed_sql_server_encryption_protectors (
encryptionProtectorName,
resourceGroupName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ encryptionProtectorName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: string
    - name: location
      value: string
    - name: properties
      value:
        - name: subregion
          value: string
        - name: serverKeyName
          value: string
        - name: serverKeyType
          value: string
        - name: uri
          value: string
        - name: thumbprint
          value: string

```
</TabItem>
</Tabs>

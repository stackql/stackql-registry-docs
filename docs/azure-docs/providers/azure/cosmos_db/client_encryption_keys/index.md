---
title: client_encryption_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - client_encryption_keys
  - cosmos_db
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

Creates, updates, deletes, gets or lists a <code>client_encryption_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>client_encryption_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.client_encryption_keys" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_client_encryption_keys', value: 'view', },
        { label: 'client_encryption_keys', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `text` | The name of the database account. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="clientEncryptionKeyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of Azure resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `string` | The name of the database account. |
| <CopyableCode code="properties" /> | `object` | The properties of a ClientEncryptionKey resource |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, clientEncryptionKeyName, databaseName, resourceGroupName, subscriptionId" /> | Gets the ClientEncryptionKey under an existing Azure Cosmos DB SQL database. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, databaseName, resourceGroupName, subscriptionId" /> | Lists the ClientEncryptionKeys under an existing Azure Cosmos DB SQL database. |
| <CopyableCode code="create_update" /> | `INSERT` | <CopyableCode code="accountName, clientEncryptionKeyName, databaseName, resourceGroupName, subscriptionId, data__properties" /> | Create or update a ClientEncryptionKey. This API is meant to be invoked via tools such as the Azure Powershell (instead of directly). |

## `SELECT` examples

Lists the ClientEncryptionKeys under an existing Azure Cosmos DB SQL database.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_client_encryption_keys', value: 'view', },
        { label: 'client_encryption_keys', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
clientEncryptionKeyName,
databaseName,
resource,
resourceGroupName,
subscriptionId,
type
FROM azure.cosmos_db.vw_client_encryption_keys
WHERE accountName = '{{ accountName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.cosmos_db.client_encryption_keys
WHERE accountName = '{{ accountName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>client_encryption_keys</code> resource.

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
INSERT INTO azure.cosmos_db.client_encryption_keys (
accountName,
clientEncryptionKeyName,
databaseName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ accountName }}',
'{{ clientEncryptionKeyName }}',
'{{ databaseName }}',
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
    - name: properties
      value:
        - name: resource
          value:
            - name: id
              value: string
            - name: encryptionAlgorithm
              value: string
            - name: wrappedDataEncryptionKey
              value: string
            - name: keyWrapMetadata
              value:
                - name: name
                  value: string
                - name: type
                  value: string
                - name: value
                  value: string
                - name: algorithm
                  value: string

```
</TabItem>
</Tabs>

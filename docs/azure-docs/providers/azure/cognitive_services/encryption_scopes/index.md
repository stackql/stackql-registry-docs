---
title: encryption_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - encryption_scopes
  - cognitive_services
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

Creates, updates, deletes, gets or lists a <code>encryption_scopes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>encryption_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.encryption_scopes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_encryption_scopes', value: 'view', },
        { label: 'encryption_scopes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryptionScopeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource Etag. |
| <CopyableCode code="key_source" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource Etag. |
| <CopyableCode code="properties" /> | `object` | Properties to EncryptionScope |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, encryptionScopeName, resourceGroupName, subscriptionId" /> | Gets the specified EncryptionScope associated with the Cognitive Services account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the content filters associated with the Azure OpenAI account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, encryptionScopeName, resourceGroupName, subscriptionId" /> | Update the state of specified encryptionScope associated with the Cognitive Services account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, encryptionScopeName, resourceGroupName, subscriptionId" /> | Deletes the specified encryptionScope associated with the Cognitive Services account. |

## `SELECT` examples

Gets the content filters associated with the Azure OpenAI account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_encryption_scopes', value: 'view', },
        { label: 'encryption_scopes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
encryptionScopeName,
etag,
key_source,
key_vault_properties,
provisioning_state,
resourceGroupName,
state,
subscriptionId,
system_data,
tags
FROM azure.cognitive_services.vw_encryption_scopes
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties,
systemData,
tags
FROM azure.cognitive_services.encryption_scopes
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>encryption_scopes</code> resource.

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
INSERT INTO azure.cognitive_services.encryption_scopes (
accountName,
encryptionScopeName,
resourceGroupName,
subscriptionId,
tags,
properties
)
SELECT 
'{{ accountName }}',
'{{ encryptionScopeName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
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
    - name: etag
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: state
          value: string
        - name: keyVaultProperties
          value:
            - name: keyIdentifier
              value: string
            - name: identity
              value: string
        - name: keySource
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>encryption_scopes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cognitive_services.encryption_scopes
WHERE accountName = '{{ accountName }}'
AND encryptionScopeName = '{{ encryptionScopeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

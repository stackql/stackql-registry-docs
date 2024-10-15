---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
  - key_vault
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

Creates, updates, deletes, gets or lists a <code>secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.secrets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_secrets', value: 'view', },
        { label: 'secrets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified identifier of the key vault resource. |
| <CopyableCode code="name" /> | `text` | Name of the key vault resource. |
| <CopyableCode code="attributes" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Azure location of the key vault resource. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secretName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secret_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="secret_uri_with_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Tags assigned to the key vault resource. |
| <CopyableCode code="type" /> | `text` | Resource type of the key vault resource. |
| <CopyableCode code="value" /> | `text` | field from the `properties` object |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier of the key vault resource. |
| <CopyableCode code="name" /> | `string` | Name of the key vault resource. |
| <CopyableCode code="location" /> | `string` | Azure location of the key vault resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the secret |
| <CopyableCode code="tags" /> | `object` | Tags assigned to the key vault resource. |
| <CopyableCode code="type" /> | `string` | Resource type of the key vault resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, secretName, subscriptionId, vaultName" /> | Gets the specified secret.  NOTE: This API is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | The List operation gets information about the secrets in a vault.  NOTE: This API is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, secretName, subscriptionId, vaultName, data__properties" /> | Create or update a secret in a key vault in the specified subscription.  NOTE: This API is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, secretName, subscriptionId, vaultName" /> | Update a secret in the specified subscription.  NOTE: This API is intended for internal use in ARM deployments.  Users should use the data-plane REST service for interaction with vault secrets. |

## `SELECT` examples

The List operation gets information about the secrets in a vault.  NOTE: This API is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_secrets', value: 'view', },
        { label: 'secrets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
attributes,
content_type,
location,
resourceGroupName,
secretName,
secret_uri,
secret_uri_with_version,
subscriptionId,
tags,
type,
value,
vaultName
FROM azure.key_vault.vw_secrets
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.key_vault.secrets
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>secrets</code> resource.

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
INSERT INTO azure.key_vault.secrets (
resourceGroupName,
secretName,
subscriptionId,
vaultName,
data__properties,
tags,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ secretName }}',
'{{ subscriptionId }}',
'{{ vaultName }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: properties
      value:
        - name: value
          value: string
        - name: contentType
          value: string
        - name: attributes
          value:
            - name: enabled
              value: boolean
            - name: nbf
              value: integer
            - name: exp
              value: integer
            - name: created
              value: integer
            - name: updated
              value: integer
        - name: secretUri
          value: string
        - name: secretUriWithVersion
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>secrets</code> resource.

```sql
/*+ update */
UPDATE azure.key_vault.secrets
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND secretName = '{{ secretName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```

---
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - tokens
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.tokens" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tokens', value: 'view', },
        { label: 'tokens', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope_map_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tokenName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a token. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, tokenName" /> | Gets the properties of the specified token. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all the tokens for the specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, tokenName" /> | Creates a token for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, tokenName" /> | Deletes a token from a container registry. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, tokenName" /> | Updates a token with the specified parameters. |

## `SELECT` examples

Lists all the tokens for the specified container registry.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tokens', value: 'view', },
        { label: 'tokens', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
creation_date,
credentials,
provisioning_state,
registryName,
resourceGroupName,
scope_map_id,
status,
subscriptionId,
tokenName
FROM azure.container_registry.vw_tokens
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.container_registry.tokens
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tokens</code> resource.

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
INSERT INTO azure.container_registry.tokens (
registryName,
resourceGroupName,
subscriptionId,
tokenName,
properties
)
SELECT 
'{{ registryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tokenName }}',
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
        - name: creationDate
          value: string
        - name: provisioningState
          value: string
        - name: scopeMapId
          value: string
        - name: credentials
          value:
            - name: certificates
              value:
                - - name: name
                    value: string
                  - name: expiry
                    value: string
                  - name: thumbprint
                    value: string
                  - name: encodedPemCertificate
                    value: string
            - name: passwords
              value:
                - - name: creationTime
                    value: string
                  - name: expiry
                    value: string
                  - name: name
                    value: string
                  - name: value
                    value: string
        - name: status
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tokens</code> resource.

```sql
/*+ update */
UPDATE azure.container_registry.tokens
SET 
properties = '{{ properties }}'
WHERE 
registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tokenName = '{{ tokenName }}';
```

## `DELETE` example

Deletes the specified <code>tokens</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_registry.tokens
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tokenName = '{{ tokenName }}';
```

---
title: custom_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_certificates
  - web_pubsub
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

Creates, updates, deletes, gets or lists a <code>custom_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web_pubsub.custom_certificates" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_certificates', value: 'view', },
        { label: 'custom_certificates', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="certificateName" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault_base_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault_secret_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault_secret_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Custom certificate properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateName, resourceGroupName, resourceName, subscriptionId" /> | Get a custom certificate. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | List all custom certificates. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Create or update a custom certificate. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificateName, resourceGroupName, resourceName, subscriptionId" /> | Delete a custom certificate. |

## `SELECT` examples

List all custom certificates.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_certificates', value: 'view', },
        { label: 'custom_certificates', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
certificateName,
key_vault_base_uri,
key_vault_secret_name,
key_vault_secret_version,
provisioning_state,
resourceGroupName,
resourceName,
subscriptionId
FROM azure.web_pubsub.vw_custom_certificates
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.web_pubsub.custom_certificates
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_certificates</code> resource.

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
INSERT INTO azure.web_pubsub.custom_certificates (
certificateName,
resourceGroupName,
resourceName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ certificateName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
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
        - name: provisioningState
          value: []
        - name: keyVaultBaseUri
          value: string
        - name: keyVaultSecretName
          value: string
        - name: keyVaultSecretVersion
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>custom_certificates</code> resource.

```sql
/*+ delete */
DELETE FROM azure.web_pubsub.custom_certificates
WHERE certificateName = '{{ certificateName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

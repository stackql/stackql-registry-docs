---
title: federated_identity_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - federated_identity_credentials
  - managed_identity
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

Creates, updates, deletes, gets or lists a <code>federated_identity_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>federated_identity_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_identity.federated_identity_credentials" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_federated_identity_credentials', value: 'view', },
        { label: 'federated_identity_credentials', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="audiences" /> | `text` | field from the `properties` object |
| <CopyableCode code="federatedIdentityCredentialResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="issuer" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subject" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties associated with a federated identity credential. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="federatedIdentityCredentialResourceName, resourceGroupName, resourceName, subscriptionId" /> | Gets the federated identity credential. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Lists all the federated identity credentials under the specified user assigned identity. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="federatedIdentityCredentialResourceName, resourceGroupName, resourceName, subscriptionId" /> | Create or update a federated identity credential under the specified user assigned identity. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="federatedIdentityCredentialResourceName, resourceGroupName, resourceName, subscriptionId" /> | Deletes the federated identity credential. |

## `SELECT` examples

Lists all the federated identity credentials under the specified user assigned identity.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_federated_identity_credentials', value: 'view', },
        { label: 'federated_identity_credentials', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
audiences,
federatedIdentityCredentialResourceName,
issuer,
resourceGroupName,
resourceName,
subject,
subscriptionId
FROM azure.managed_identity.vw_federated_identity_credentials
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.managed_identity.federated_identity_credentials
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>federated_identity_credentials</code> resource.

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
INSERT INTO azure.managed_identity.federated_identity_credentials (
federatedIdentityCredentialResourceName,
resourceGroupName,
resourceName,
subscriptionId,
properties
)
SELECT 
'{{ federatedIdentityCredentialResourceName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
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
        - name: issuer
          value: string
        - name: subject
          value: string
        - name: audiences
          value:
            - string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>federated_identity_credentials</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_identity.federated_identity_credentials
WHERE federatedIdentityCredentialResourceName = '{{ federatedIdentityCredentialResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

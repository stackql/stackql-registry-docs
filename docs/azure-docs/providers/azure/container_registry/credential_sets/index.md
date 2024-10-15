---
title: credential_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - credential_sets
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

Creates, updates, deletes, gets or lists a <code>credential_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>credential_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.credential_sets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_credential_sets', value: 'view', },
        { label: 'credential_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="auth_credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="credentialSetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed identity for the resource. |
| <CopyableCode code="login_server" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed identity for the resource. |
| <CopyableCode code="properties" /> | `object` | The properties of a credential set resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="credentialSetName, registryName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified credential set resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all credential set resources for the specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="credentialSetName, registryName, resourceGroupName, subscriptionId" /> | Creates a credential set for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="credentialSetName, registryName, resourceGroupName, subscriptionId" /> | Deletes a credential set from a container registry. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="credentialSetName, registryName, resourceGroupName, subscriptionId" /> | Updates a credential set for a container registry with the specified parameters. |

## `SELECT` examples

Lists all credential set resources for the specified container registry.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_credential_sets', value: 'view', },
        { label: 'credential_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
auth_credentials,
creation_date,
credentialSetName,
identity,
login_server,
provisioning_state,
registryName,
resourceGroupName,
subscriptionId
FROM azure.container_registry.vw_credential_sets
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
properties
FROM azure.container_registry.credential_sets
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>credential_sets</code> resource.

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
INSERT INTO azure.container_registry.credential_sets (
credentialSetName,
registryName,
resourceGroupName,
subscriptionId,
identity,
properties
)
SELECT 
'{{ credentialSetName }}',
'{{ registryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ identity }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
    - name: properties
      value:
        - name: loginServer
          value: string
        - name: authCredentials
          value:
            - - name: name
                value: string
              - name: usernameSecretIdentifier
                value: string
              - name: passwordSecretIdentifier
                value: string
              - name: credentialHealth
                value:
                  - name: status
                    value: string
                  - name: errorCode
                    value: string
                  - name: errorMessage
                    value: string
        - name: creationDate
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>credential_sets</code> resource.

```sql
/*+ update */
UPDATE azure.container_registry.credential_sets
SET 
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
credentialSetName = '{{ credentialSetName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>credential_sets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_registry.credential_sets
WHERE credentialSetName = '{{ credentialSetName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

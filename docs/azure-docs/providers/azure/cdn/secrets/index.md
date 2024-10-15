---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
  - cdn
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.secrets" /></td></tr>
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
| <CopyableCode code="deployment_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="profile_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secretName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties of the Secret to create. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, secretName, subscriptionId" /> | Gets an existing Secret within a profile. |
| <CopyableCode code="list_by_profile" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Lists existing AzureFrontDoor secrets. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="profileName, resourceGroupName, secretName, subscriptionId" /> | Creates a new Secret within the specified profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="profileName, resourceGroupName, secretName, subscriptionId" /> | Deletes an existing Secret within profile. |

## `SELECT` examples

Lists existing AzureFrontDoor secrets.

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
deployment_status,
parameters,
profileName,
profile_name,
provisioning_state,
resourceGroupName,
secretName,
subscriptionId
FROM azure.cdn.vw_secrets
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.cdn.secrets
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
INSERT INTO azure.cdn.secrets (
profileName,
resourceGroupName,
secretName,
subscriptionId,
properties
)
SELECT 
'{{ profileName }}',
'{{ resourceGroupName }}',
'{{ secretName }}',
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
        - name: provisioningState
          value: string
        - name: deploymentStatus
          value: string
        - name: profileName
          value: string
        - name: parameters
          value:
            - name: type
              value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>secrets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cdn.secrets
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND secretName = '{{ secretName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

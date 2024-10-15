---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - nginx
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

Creates, updates, deletes, gets or lists a <code>certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.nginx.certificates" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_certificates', value: 'view', },
        { label: 'certificates', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | field from the `properties` object |
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificateName" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificate_error" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificate_virtual_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="deploymentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault_secret_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault_secret_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault_secret_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_virtual_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sha1_thumbprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="location" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateName, deploymentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateName, deploymentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificateName, deploymentName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_certificates', value: 'view', },
        { label: 'certificates', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
certificateName,
certificate_error,
certificate_virtual_path,
deploymentName,
key_vault_secret_created,
key_vault_secret_id,
key_vault_secret_version,
key_virtual_path,
location,
provisioning_state,
resourceGroupName,
sha1_thumbprint,
subscriptionId,
system_data,
type
FROM azure_isv.nginx.vw_certificates
WHERE deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
systemData,
type
FROM azure_isv.nginx.certificates
WHERE deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>certificates</code> resource.

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
INSERT INTO azure_isv.nginx.certificates (
certificateName,
deploymentName,
resourceGroupName,
subscriptionId,
properties,
location
)
SELECT 
'{{ certificateName }}',
'{{ deploymentName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: keyVirtualPath
          value: string
        - name: certificateVirtualPath
          value: string
        - name: keyVaultSecretId
          value: string
        - name: sha1Thumbprint
          value: string
        - name: keyVaultSecretVersion
          value: string
        - name: keyVaultSecretCreated
          value: string
        - name: certificateError
          value:
            - name: code
              value: string
            - name: message
              value: string
    - name: location
      value: string
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

## `DELETE` example

Deletes the specified <code>certificates</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.nginx.certificates
WHERE certificateName = '{{ certificateName }}'
AND deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

---
title: managed_instance_encryption_protectors
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_encryption_protectors
  - sql
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

Creates, updates, deletes, gets or lists a <code>managed_instance_encryption_protectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_instance_encryption_protectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instance_encryption_protectors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_instance_encryption_protectors', value: 'view', },
        { label: 'managed_instance_encryption_protectors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="auto_rotation_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryptionProtectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_key_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_key_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="thumbprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="uri" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| <CopyableCode code="properties" /> | `object` | Properties for an encryption protector execution. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="encryptionProtectorName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a managed instance encryption protector. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="encryptionProtectorName, managedInstanceName, resourceGroupName, subscriptionId" /> | Updates an existing encryption protector. |
| <CopyableCode code="revalidate" /> | `EXEC` | <CopyableCode code="encryptionProtectorName, managedInstanceName, resourceGroupName, subscriptionId" /> | Revalidates an existing encryption protector. |

## `SELECT` examples

Gets a managed instance encryption protector.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_instance_encryption_protectors', value: 'view', },
        { label: 'managed_instance_encryption_protectors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
auto_rotation_enabled,
encryptionProtectorName,
kind,
managedInstanceName,
resourceGroupName,
server_key_name,
server_key_type,
subscriptionId,
thumbprint,
uri
FROM azure.sql.vw_managed_instance_encryption_protectors
WHERE encryptionProtectorName = '{{ encryptionProtectorName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
properties
FROM azure.sql.managed_instance_encryption_protectors
WHERE encryptionProtectorName = '{{ encryptionProtectorName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_instance_encryption_protectors</code> resource.

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
INSERT INTO azure.sql.managed_instance_encryption_protectors (
encryptionProtectorName,
managedInstanceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ encryptionProtectorName }}',
'{{ managedInstanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
    - name: properties
      value:
        - name: serverKeyName
          value: string
        - name: serverKeyType
          value: string
        - name: uri
          value: string
        - name: thumbprint
          value: string
        - name: autoRotationEnabled
          value: boolean

```
</TabItem>
</Tabs>

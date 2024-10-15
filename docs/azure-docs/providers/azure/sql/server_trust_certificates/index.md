---
title: server_trust_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - server_trust_certificates
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

Creates, updates, deletes, gets or lists a <code>server_trust_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_trust_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_trust_certificates" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_trust_certificates', value: 'view', },
        { label: 'server_trust_certificates', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="certificateName" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificate_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_blob" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="thumbprint" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a server trust certificate. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a server trust certificate that was uploaded from box to Sql Managed Instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateName, managedInstanceName, resourceGroupName, subscriptionId" /> | Uploads a server trust certificate from box to Sql Managed Instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificateName, managedInstanceName, resourceGroupName, subscriptionId" /> | Deletes a server trust certificate that was uploaded from box to Sql Managed Instance. |

## `SELECT` examples

Gets a server trust certificate that was uploaded from box to Sql Managed Instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_trust_certificates', value: 'view', },
        { label: 'server_trust_certificates', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
certificateName,
certificate_name,
managedInstanceName,
public_blob,
resourceGroupName,
subscriptionId,
thumbprint
FROM azure.sql.vw_server_trust_certificates
WHERE certificateName = '{{ certificateName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.server_trust_certificates
WHERE certificateName = '{{ certificateName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>server_trust_certificates</code> resource.

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
INSERT INTO azure.sql.server_trust_certificates (
certificateName,
managedInstanceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ certificateName }}',
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
    - name: properties
      value:
        - name: publicBlob
          value: string
        - name: thumbprint
          value: string
        - name: certificateName
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>server_trust_certificates</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.server_trust_certificates
WHERE certificateName = '{{ certificateName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

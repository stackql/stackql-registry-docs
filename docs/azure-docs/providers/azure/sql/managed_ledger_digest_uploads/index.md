---
title: managed_ledger_digest_uploads
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_ledger_digest_uploads
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

Creates, updates, deletes, gets or lists a <code>managed_ledger_digest_uploads</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_ledger_digest_uploads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_ledger_digest_uploads" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_ledger_digest_uploads', value: 'view', },
        { label: 'managed_ledger_digest_uploads', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="digest_storage_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="ledgerDigestUploads" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a database ledger digest upload settings. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, ledgerDigestUploads, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets the current ledger digest upload configuration for a database. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets all ledger digest upload settings on a database. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, ledgerDigestUploads, managedInstanceName, resourceGroupName, subscriptionId" /> | Enables upload ledger digests to an Azure Storage account or an Azure Confidential Ledger instance. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="databaseName, ledgerDigestUploads, managedInstanceName, resourceGroupName, subscriptionId" /> | Disables uploading ledger digests to an Azure Storage account or an Azure Confidential Ledger instance. |

## `SELECT` examples

Gets all ledger digest upload settings on a database.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_ledger_digest_uploads', value: 'view', },
        { label: 'managed_ledger_digest_uploads', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
databaseName,
digest_storage_endpoint,
ledgerDigestUploads,
managedInstanceName,
resourceGroupName,
state,
subscriptionId
FROM azure.sql.vw_managed_ledger_digest_uploads
WHERE databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.managed_ledger_digest_uploads
WHERE databaseName = '{{ databaseName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_ledger_digest_uploads</code> resource.

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
INSERT INTO azure.sql.managed_ledger_digest_uploads (
databaseName,
ledgerDigestUploads,
managedInstanceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ databaseName }}',
'{{ ledgerDigestUploads }}',
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
        - name: digestStorageEndpoint
          value: string
        - name: state
          value: string

```
</TabItem>
</Tabs>

---
title: ledgers
hide_title: false
hide_table_of_contents: false
keywords:
  - ledgers
  - confidential_ledger
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

Creates, updates, deletes, gets or lists a <code>ledgers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ledgers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidential_ledger.ledgers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ledgers', value: 'view', },
        { label: 'ledgers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aad_based_security_principals" /> | `text` | field from the `properties` object |
| <CopyableCode code="cert_based_security_principals" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity_service_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="ledgerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ledger_internal_namespace" /> | `text` | field from the `properties` object |
| <CopyableCode code="ledger_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="ledger_sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="ledger_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="ledger_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="max_body_size_in_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="running_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subject_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="worker_threads" /> | `text` | field from the `properties` object |
| <CopyableCode code="write_lb_address_prefix" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Additional Confidential Ledger properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ledgerName, resourceGroupName, subscriptionId" /> | Retrieves the properties of a Confidential Ledger. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieves the properties of all Confidential Ledgers. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieves the properties of all Confidential Ledgers. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="ledgerName, resourceGroupName, subscriptionId" /> | Creates a  Confidential Ledger with the specified ledger parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="ledgerName, resourceGroupName, subscriptionId" /> | Deletes an existing Confidential Ledger. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="ledgerName, resourceGroupName, subscriptionId" /> | Updates properties of Confidential Ledger |
| <CopyableCode code="backup" /> | `EXEC` | <CopyableCode code="ledgerName, resourceGroupName, subscriptionId, data__uri" /> | Backs up a Confidential Ledger Resource. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="ledgerName, resourceGroupName, subscriptionId, data__fileShareName, data__restoreRegion, data__uri" /> | Restores a Confidential Ledger Resource. |

## `SELECT` examples

Retrieves the properties of all Confidential Ledgers.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ledgers', value: 'view', },
        { label: 'ledgers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
aad_based_security_principals,
cert_based_security_principals,
host_level,
identity_service_uri,
ledgerName,
ledger_internal_namespace,
ledger_name,
ledger_sku,
ledger_type,
ledger_uri,
location,
max_body_size_in_mb,
node_count,
provisioning_state,
resourceGroupName,
running_state,
subject_name,
subscriptionId,
tags,
worker_threads,
write_lb_address_prefix
FROM azure.confidential_ledger.vw_ledgers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.confidential_ledger.ledgers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ledgers</code> resource.

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
INSERT INTO azure.confidential_ledger.ledgers (
ledgerName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ ledgerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
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
    - name: location
      value: string
    - name: properties
      value:
        - name: ledgerName
          value: string
        - name: ledgerUri
          value: string
        - name: identityServiceUri
          value: string
        - name: ledgerInternalNamespace
          value: string
        - name: runningState
          value: []
        - name: ledgerType
          value: []
        - name: provisioningState
          value: []
        - name: ledgerSku
          value: []
        - name: aadBasedSecurityPrincipals
          value:
            - - name: principalId
                value: string
              - name: tenantId
                value: string
              - name: ledgerRoleName
                value: []
        - name: certBasedSecurityPrincipals
          value:
            - - name: cert
                value: string
        - name: hostLevel
          value: string
        - name: maxBodySizeInMb
          value: []
        - name: subjectName
          value: string
        - name: nodeCount
          value: []
        - name: writeLBAddressPrefix
          value: string
        - name: workerThreads
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>ledgers</code> resource.

```sql
/*+ update */
UPDATE azure.confidential_ledger.ledgers
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
ledgerName = '{{ ledgerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>ledgers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.confidential_ledger.ledgers
WHERE ledgerName = '{{ ledgerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

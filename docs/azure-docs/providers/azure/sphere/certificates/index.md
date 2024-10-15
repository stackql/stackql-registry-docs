---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - sphere
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sphere.certificates" /></td></tr>
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
| <CopyableCode code="catalogName" /> | `text` | field from the `properties` object |
| <CopyableCode code="certificate" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiry_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="not_before_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serialNumber" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subject" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="thumbprint" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of certificate |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, resourceGroupName, serialNumber, subscriptionId" /> | Get a Certificate |
| <CopyableCode code="list_by_catalog" /> | `SELECT` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | List Certificate resources by Catalog |
| <CopyableCode code="retrieve_cert_chain" /> | `EXEC` | <CopyableCode code="catalogName, resourceGroupName, serialNumber, subscriptionId" /> | Retrieves cert chain. |
| <CopyableCode code="retrieve_proof_of_possession_nonce" /> | `EXEC` | <CopyableCode code="catalogName, resourceGroupName, serialNumber, subscriptionId, data__proofOfPossessionNonce" /> | Gets the proof of possession nonce. |

## `SELECT` examples

List Certificate resources by Catalog

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
catalogName,
certificate,
expiry_utc,
not_before_utc,
provisioning_state,
resourceGroupName,
serialNumber,
status,
subject,
subscriptionId,
thumbprint
FROM azure.sphere.vw_certificates
WHERE catalogName = '{{ catalogName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sphere.certificates
WHERE catalogName = '{{ catalogName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


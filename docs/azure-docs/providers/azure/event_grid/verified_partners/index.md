---
title: verified_partners
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_partners
  - event_grid
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

Creates, updates, deletes, gets or lists a <code>verified_partners</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_partners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.verified_partners" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_verified_partners', value: 'view', },
        { label: 'verified_partners', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="organization_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_destination_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_registration_immutable_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_topic_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="verifiedPartnerName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the verified partner. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="verifiedPartnerName" /> | Get properties of a verified partner. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Get a list of all verified partners. |

## `SELECT` examples

Get a list of all verified partners.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_verified_partners', value: 'view', },
        { label: 'verified_partners', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
organization_name,
partner_destination_details,
partner_display_name,
partner_registration_immutable_id,
partner_topic_details,
provisioning_state,
system_data,
type,
verifiedPartnerName
FROM azure.event_grid.vw_verified_partners
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.event_grid.verified_partners
;
```
</TabItem></Tabs>


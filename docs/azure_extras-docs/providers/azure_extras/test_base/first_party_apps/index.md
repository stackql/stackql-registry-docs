---
title: first_party_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - first_party_apps
  - test_base
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

Creates, updates, deletes, gets or lists a <code>first_party_apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>first_party_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.first_party_apps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_first_party_apps', value: 'view', },
        { label: 'first_party_apps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="architecture" /> | `text` | field from the `properties` object |
| <CopyableCode code="channel" /> | `text` | field from the `properties` object |
| <CopyableCode code="firstPartyAppResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="media_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ring" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_products" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a first party application. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firstPartyAppResourceName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a first party application to prepare a test run for a Test Base Account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all first party applications currently available for test runs under a Test Base Account. |

## `SELECT` examples

Lists all first party applications currently available for test runs under a Test Base Account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_first_party_apps', value: 'view', },
        { label: 'first_party_apps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
architecture,
channel,
firstPartyAppResourceName,
media_type,
provisioning_state,
resourceGroupName,
ring,
subscriptionId,
supported_products,
testBaseAccountName
FROM azure_extras.test_base.vw_first_party_apps
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.first_party_apps
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>


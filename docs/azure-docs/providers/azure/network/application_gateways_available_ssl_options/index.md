---
title: application_gateways_available_ssl_options
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateways_available_ssl_options
  - network
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

Creates, updates, deletes, gets or lists a <code>application_gateways_available_ssl_options</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_gateways_available_ssl_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.application_gateways_available_ssl_options" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_gateways_available_ssl_options', value: 'view', },
        { label: 'application_gateways_available_ssl_options', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="available_cipher_suites" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_protocols" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="predefined_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of ApplicationGatewayAvailableSslOptions. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists available Ssl options for configuring Ssl policy. |

## `SELECT` examples

Lists available Ssl options for configuring Ssl policy.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_gateways_available_ssl_options', value: 'view', },
        { label: 'application_gateways_available_ssl_options', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
available_cipher_suites,
available_protocols,
default_policy,
location,
predefined_policies,
subscriptionId,
tags,
type
FROM azure.network.vw_application_gateways_available_ssl_options
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.network.application_gateways_available_ssl_options
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


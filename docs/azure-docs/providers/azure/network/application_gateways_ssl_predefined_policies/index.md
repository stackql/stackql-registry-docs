---
title: application_gateways_ssl_predefined_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateways_ssl_predefined_policies
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

Creates, updates, deletes, gets or lists a <code>application_gateways_ssl_predefined_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_gateways_ssl_predefined_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.application_gateways_ssl_predefined_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_gateways_ssl_predefined_policies', value: 'view', },
        { label: 'application_gateways_ssl_predefined_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Name of the Ssl predefined policy. |
| <CopyableCode code="cipher_suites" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_protocol_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="predefinedPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Name of the Ssl predefined policy. |
| <CopyableCode code="properties" /> | `object` | Properties of ApplicationGatewaySslPredefinedPolicy. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="predefinedPolicyName, subscriptionId" /> | Gets Ssl predefined policy with the specified policy name. |

## `SELECT` examples

Gets Ssl predefined policy with the specified policy name.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_gateways_ssl_predefined_policies', value: 'view', },
        { label: 'application_gateways_ssl_predefined_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
cipher_suites,
min_protocol_version,
predefinedPolicyName,
subscriptionId
FROM azure.network.vw_application_gateways_ssl_predefined_policies
WHERE predefinedPolicyName = '{{ predefinedPolicyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties
FROM azure.network.application_gateways_ssl_predefined_policies
WHERE predefinedPolicyName = '{{ predefinedPolicyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


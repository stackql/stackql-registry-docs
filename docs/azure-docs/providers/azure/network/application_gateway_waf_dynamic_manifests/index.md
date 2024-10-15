---
title: application_gateway_waf_dynamic_manifests
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateway_waf_dynamic_manifests
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

Creates, updates, deletes, gets or lists a <code>application_gateway_waf_dynamic_manifests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_gateway_waf_dynamic_manifests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.application_gateway_waf_dynamic_manifests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | Properties of ApplicationGatewayWafDynamicManifest. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Gets the regional application gateway waf manifest. |

## `SELECT` examples

Gets the regional application gateway waf manifest.


```sql
SELECT
id,
name,
properties,
type
FROM azure.network.application_gateway_waf_dynamic_manifests
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
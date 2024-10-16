---
title: managed_rule_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_rule_sets
  - cdn
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

Creates, updates, deletes, gets or lists a <code>managed_rule_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_rule_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.managed_rule_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | Properties for a managed rule set definition. |
| <CopyableCode code="sku" /> | `object` | Standard_Verizon = The SKU name for a Standard Verizon CDN profile.
Premium_Verizon = The SKU name for a Premium Verizon CDN profile.
Custom_Verizon = The SKU name for a Custom Verizon CDN profile.
Standard_Akamai = The SKU name for an Akamai CDN profile.
Standard_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using GB based billing model.
Standard_Microsoft = The SKU name for a Standard Microsoft CDN profile.
Standard_AzureFrontDoor =  The SKU name for an Azure Front Door Standard profile.
Premium_AzureFrontDoor = The SKU name for an Azure Front Door Premium profile.
Standard_955BandWidth_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using 95-5 peak bandwidth billing model.
Standard_AvgBandWidth_ChinaCdn = The SKU name for a China CDN profile for VOD, Web and download scenarios using monthly average peak bandwidth billing model.
StandardPlus_ChinaCdn = The SKU name for a China CDN profile for live-streaming using GB based billing model.
StandardPlus_955BandWidth_ChinaCdn = The SKU name for a China CDN live-streaming profile using 95-5 peak bandwidth billing model.
StandardPlus_AvgBandWidth_ChinaCdn = The SKU name for a China CDN live-streaming profile using monthly average peak bandwidth billing model. |
| <CopyableCode code="systemData" /> | `object` | Read only system data |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all available managed rule sets. |

## `SELECT` examples

Lists all available managed rule sets.


```sql
SELECT
id,
name,
properties,
sku,
systemData,
type
FROM azure.cdn.managed_rule_sets
WHERE subscriptionId = '{{ subscriptionId }}';
```
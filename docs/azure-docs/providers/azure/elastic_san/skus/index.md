---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - elastic_san
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

Creates, updates, deletes, gets or lists a <code>skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.elastic_san.skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The sku name. |
| <CopyableCode code="capabilities" /> | `array` | The capability information in the specified SKU. |
| <CopyableCode code="locationInfo" /> | `array` | Availability of the SKU for the location/zone |
| <CopyableCode code="locations" /> | `array` | The set of locations that the SKU is available. This will be supported and registered Azure Geo Regions (e.g. West US, East US, Southeast Asia, etc.). |
| <CopyableCode code="resourceType" /> | `string` | The type of the resource. |
| <CopyableCode code="tier" /> | `string` | This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
name,
capabilities,
locationInfo,
locations,
resourceType,
tier
FROM azure.elastic_san.skus
WHERE subscriptionId = '{{ subscriptionId }}';
```
---
title: available_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - available_skus
  - data_box_edge
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

Creates, updates, deletes, gets or lists a <code>available_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>available_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.available_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The Sku name. |
| <CopyableCode code="apiVersions" /> | `array` | The API versions in which Sku is available. |
| <CopyableCode code="availability" /> | `string` | Links to the next set of results |
| <CopyableCode code="capabilities" /> | `array` | The capability info of the SKU. |
| <CopyableCode code="costs" /> | `array` | The pricing info of the Sku. |
| <CopyableCode code="family" /> | `string` | The Sku family. |
| <CopyableCode code="kind" /> | `string` | The Sku kind. |
| <CopyableCode code="locationInfo" /> | `array` | Availability of the Sku for the location/zone/site. |
| <CopyableCode code="locations" /> | `array` | Availability of the Sku for the region. |
| <CopyableCode code="resourceType" /> | `string` | The type of the resource. |
| <CopyableCode code="shipmentTypes" /> | `array` | List of Shipment Types supported by this SKU |
| <CopyableCode code="signupOption" /> | `string` | Sku can be signed up by customer or not. |
| <CopyableCode code="size" /> | `string` | The Sku kind. |
| <CopyableCode code="tier" /> | `string` | The Sku tier. |
| <CopyableCode code="version" /> | `string` | Availability of the Sku as preview/stable. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
name,
apiVersions,
availability,
capabilities,
costs,
family,
kind,
locationInfo,
locations,
resourceType,
shipmentTypes,
signupOption,
size,
tier,
version
FROM azure.data_box_edge.available_skus
WHERE subscriptionId = '{{ subscriptionId }}';
```
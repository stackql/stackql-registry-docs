---
title: resource_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_skus
  - compute
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

Creates, updates, deletes, gets or lists a <code>resource_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.resource_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of SKU. |
| <CopyableCode code="apiVersions" /> | `array` | The api versions that support this SKU. |
| <CopyableCode code="capabilities" /> | `array` | A name value pair to describe the capability. |
| <CopyableCode code="capacity" /> | `object` | Describes scaling information of a SKU. |
| <CopyableCode code="costs" /> | `array` | Metadata for retrieving price info. |
| <CopyableCode code="family" /> | `string` | The Family of this particular SKU. |
| <CopyableCode code="kind" /> | `string` | The Kind of resources that are supported in this SKU. |
| <CopyableCode code="locationInfo" /> | `array` | A list of locations and availability zones in those locations where the SKU is available. |
| <CopyableCode code="locations" /> | `array` | The set of locations that the SKU is available. |
| <CopyableCode code="resourceType" /> | `string` | The type of resource the SKU applies to. |
| <CopyableCode code="restrictions" /> | `array` | The restrictions because of which SKU cannot be used. This is empty if there are no restrictions. |
| <CopyableCode code="size" /> | `string` | The Size of the SKU. |
| <CopyableCode code="tier" /> | `string` | Specifies the tier of virtual machines in a scale set.   Possible Values:   **Standard**   **Basic** |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the list of Microsoft.Compute SKUs available for your Subscription. |

## `SELECT` examples

Gets the list of Microsoft.Compute SKUs available for your Subscription.


```sql
SELECT
name,
apiVersions,
capabilities,
capacity,
costs,
family,
kind,
locationInfo,
locations,
resourceType,
restrictions,
size,
tier
FROM azure.compute.resource_skus
WHERE subscriptionId = '{{ subscriptionId }}';
```
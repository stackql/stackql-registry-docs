---
title: profiles_resource_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles_resource_usages
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

Creates, updates, deletes, gets or lists a <code>profiles_resource_usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles_resource_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.profiles_resource_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="currentValue" /> | `integer` | Actual value of usage on the specified resource type. |
| <CopyableCode code="limit" /> | `integer` | Quota of the specified resource type. |
| <CopyableCode code="resourceType" /> | `string` | Resource type for which the usage is provided. |
| <CopyableCode code="unit" /> | `string` | Unit of the usage. e.g. count. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Checks the quota and actual usage of endpoints under the given Azure Front Door Standard or Azure Front Door Premium or CDN profile. |

## `SELECT` examples

Checks the quota and actual usage of endpoints under the given Azure Front Door Standard or Azure Front Door Premium or CDN profile.


```sql
SELECT
currentValue,
limit,
resourceType,
unit
FROM azure.cdn.profiles_resource_usages
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
---
title: afd_origin_groups_resource_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_origin_groups_resource_usages
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

Creates, updates, deletes, gets or lists a <code>afd_origin_groups_resource_usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>afd_origin_groups_resource_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.afd_origin_groups_resource_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource identifier. |
| <CopyableCode code="name" /> | `object` | The usage names. |
| <CopyableCode code="currentValue" /> | `integer` | The current value of the usage. |
| <CopyableCode code="limit" /> | `integer` | The limit of usage. |
| <CopyableCode code="unit" /> | `string` | An enum describing the unit of measurement. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="originGroupName, profileName, resourceGroupName, subscriptionId" /> | Checks the quota and actual usage of endpoints under the given Azure Front Door profile.. |

## `SELECT` examples

Checks the quota and actual usage of endpoints under the given Azure Front Door profile..


```sql
SELECT
id,
name,
currentValue,
limit,
unit
FROM azure.cdn.afd_origin_groups_resource_usages
WHERE originGroupName = '{{ originGroupName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
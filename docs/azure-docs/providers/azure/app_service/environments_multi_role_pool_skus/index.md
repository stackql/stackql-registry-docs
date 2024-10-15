---
title: environments_multi_role_pool_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_multi_role_pool_skus
  - app_service
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

Creates, updates, deletes, gets or lists a <code>environments_multi_role_pool_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments_multi_role_pool_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.environments_multi_role_pool_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capacity" /> | `object` | Description of the App Service plan scale options. |
| <CopyableCode code="resourceType" /> | `string` | Resource type that this SKU applies to. |
| <CopyableCode code="sku" /> | `object` | Description of a SKU for a scalable resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Get available SKUs for scaling a multi-role pool. |

## `SELECT` examples

Description for Get available SKUs for scaling a multi-role pool.


```sql
SELECT
capacity,
resourceType,
sku
FROM azure.app_service.environments_multi_role_pool_skus
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
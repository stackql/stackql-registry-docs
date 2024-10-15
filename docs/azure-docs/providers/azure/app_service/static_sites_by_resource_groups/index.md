---
title: static_sites_by_resource_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - static_sites_by_resource_groups
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

Creates, updates, deletes, gets or lists a <code>static_sites_by_resource_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>static_sites_by_resource_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.static_sites_by_resource_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="identity" /> | `object` | Managed service identity. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | A static site. |
| <CopyableCode code="sku" /> | `object` | Description of a SKU for a scalable resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for Gets all static sites in the specified resource group. |

## `SELECT` examples

Description for Gets all static sites in the specified resource group.


```sql
SELECT
id,
name,
identity,
kind,
location,
properties,
sku,
tags,
type
FROM azure.app_service.static_sites_by_resource_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
---
title: services_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - services_skus
  - data_migration
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

Creates, updates, deletes, gets or lists a <code>services_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.services_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capacity" /> | `object` | A description of the scaling capacities of the SKU |
| <CopyableCode code="resourceType" /> | `string` | The resource type, including the provider namespace |
| <CopyableCode code="sku" /> | `object` | SKU name, tier, etc. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupName, serviceName, subscriptionId" /> | The services resource is the top-level resource that represents the Database Migration Service (classic). The skus action returns the list of SKUs that a service resource can be updated to. |

## `SELECT` examples

The services resource is the top-level resource that represents the Database Migration Service (classic). The skus action returns the list of SKUs that a service resource can be updated to.


```sql
SELECT
capacity,
resourceType,
sku
FROM azure.data_migration.services_skus
WHERE groupName = '{{ groupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
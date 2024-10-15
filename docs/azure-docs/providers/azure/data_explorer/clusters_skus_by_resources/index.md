---
title: clusters_skus_by_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_skus_by_resources
  - data_explorer
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

Creates, updates, deletes, gets or lists a <code>clusters_skus_by_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_skus_by_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.clusters_skus_by_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capacity" /> | `object` | Azure capacity definition. |
| <CopyableCode code="resourceType" /> | `string` | Resource Namespace and Type. |
| <CopyableCode code="sku" /> | `object` | Azure SKU definition. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Returns the SKUs available for the provided resource. |

## `SELECT` examples

Returns the SKUs available for the provided resource.


```sql
SELECT
capacity,
resourceType,
sku
FROM azure.data_explorer.clusters_skus_by_resources
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
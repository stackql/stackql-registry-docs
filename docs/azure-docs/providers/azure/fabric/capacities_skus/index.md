---
title: capacities_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - capacities_skus
  - fabric
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

Creates, updates, deletes, gets or lists a <code>capacities_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacities_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fabric.capacities_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The SKU's name |
| <CopyableCode code="locations" /> | `array` | The list of available locations for the SKU |
| <CopyableCode code="resourceType" /> | `string` | The resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List eligible SKUs for Microsoft Fabric resource provider |

## `SELECT` examples

List eligible SKUs for Microsoft Fabric resource provider


```sql
SELECT
name,
locations,
resourceType
FROM azure.fabric.capacities_skus
WHERE subscriptionId = '{{ subscriptionId }}';
```
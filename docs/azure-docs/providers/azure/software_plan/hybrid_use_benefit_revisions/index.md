---
title: hybrid_use_benefit_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_use_benefit_revisions
  - software_plan
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

Creates, updates, deletes, gets or lists a <code>hybrid_use_benefit_revisions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hybrid_use_benefit_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.software_plan.hybrid_use_benefit_revisions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="etag" /> | `integer` | Indicates the revision of the hybrid use benefit |
| <CopyableCode code="properties" /> | `object` | Hybrid use benefit properties |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="planId, scope" /> | Gets the version history of a hybrid use benefit |

## `SELECT` examples

Gets the version history of a hybrid use benefit


```sql
SELECT
id,
name,
etag,
properties,
sku,
type
FROM azure.software_plan.hybrid_use_benefit_revisions
WHERE planId = '{{ planId }}'
AND scope = '{{ scope }}';
```
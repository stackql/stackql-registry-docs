---
title: usage_models
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_models
  - storage_cache
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

Creates, updates, deletes, gets or lists a <code>usage_models</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usage_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.usage_models" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="display" /> | `object` | Localized information describing this usage model. |
| <CopyableCode code="modelName" /> | `string` | Non-localized keyword name for this usage model. |
| <CopyableCode code="targetType" /> | `string` | The type of Storage Target to which this model is applicable (only nfs3 as of this version). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get the list of cache usage models available to this subscription. |

## `SELECT` examples

Get the list of cache usage models available to this subscription.


```sql
SELECT
display,
modelName,
targetType
FROM azure.storage_cache.usage_models
WHERE subscriptionId = '{{ subscriptionId }}';
```
---
title: accounts_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_skus
  - cognitive_services
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

Creates, updates, deletes, gets or lists a <code>accounts_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.accounts_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="resourceType" /> | `string` | Resource Namespace and Type |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List available SKUs for the requested Cognitive Services account |

## `SELECT` examples

List available SKUs for the requested Cognitive Services account


```sql
SELECT
resourceType,
sku
FROM azure.cognitive_services.accounts_skus
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
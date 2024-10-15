---
title: deployments_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments_skus
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

Creates, updates, deletes, gets or lists a <code>deployments_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.deployments_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capacity" /> | `object` | The capacity configuration. |
| <CopyableCode code="resourceType" /> | `string` | The resource type name. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, deploymentName, resourceGroupName, subscriptionId" /> | Lists the specified deployments skus associated with the Cognitive Services account. |

## `SELECT` examples

Lists the specified deployments skus associated with the Cognitive Services account.


```sql
SELECT
capacity,
resourceType,
sku
FROM azure.cognitive_services.deployments_skus
WHERE accountName = '{{ accountName }}'
AND deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
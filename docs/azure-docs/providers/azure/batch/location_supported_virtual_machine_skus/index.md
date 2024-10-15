---
title: location_supported_virtual_machine_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - location_supported_virtual_machine_skus
  - batch
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

Creates, updates, deletes, gets or lists a <code>location_supported_virtual_machine_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_supported_virtual_machine_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch.location_supported_virtual_machine_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the SKU. |
| <CopyableCode code="batchSupportEndOfLife" /> | `string` | The time when Azure Batch service will retire this SKU. |
| <CopyableCode code="capabilities" /> | `array` | A collection of capabilities which this SKU supports. |
| <CopyableCode code="familyName" /> | `string` | The family name of the SKU. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> | Gets the list of Batch supported Virtual Machine VM sizes available at the given location. |

## `SELECT` examples

Gets the list of Batch supported Virtual Machine VM sizes available at the given location.


```sql
SELECT
name,
batchSupportEndOfLife,
capabilities,
familyName
FROM azure.batch.location_supported_virtual_machine_skus
WHERE locationName = '{{ locationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
---
title: registries_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - registries_usages
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>registries_usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registries_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.registries_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the usage. |
| <CopyableCode code="currentValue" /> | `integer` | The current value of the usage. |
| <CopyableCode code="limit" /> | `integer` | The limit of the usage. |
| <CopyableCode code="unit" /> | `string` | The unit of measurement. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Gets the quota usages for the specified container registry. |

## `SELECT` examples

Gets the quota usages for the specified container registry.


```sql
SELECT
name,
currentValue,
limit,
unit
FROM azure.container_registry.registries_usages
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
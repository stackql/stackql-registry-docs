---
title: target_compute_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - target_compute_sizes
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>target_compute_sizes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_compute_sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.target_compute_sizes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Id. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | Represents applicable recovery vm sizes properties. |
| <CopyableCode code="type" /> | `string` | The Type of the object. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_replication_protected_items" /> | `SELECT` | <CopyableCode code="fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId" /> | Lists the available target compute sizes for a replication protected item. |

## `SELECT` examples

Lists the available target compute sizes for a replication protected item.


```sql
SELECT
id,
name,
properties,
type
FROM azure.recovery_services_site_recovery.target_compute_sizes
WHERE fabricName = '{{ fabricName }}'
AND protectionContainerName = '{{ protectionContainerName }}'
AND replicatedProtectedItemName = '{{ replicatedProtectedItemName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
---
title: mhsm_regions
hide_title: false
hide_table_of_contents: false
keywords:
  - mhsm_regions
  - key_vault
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

Creates, updates, deletes, gets or lists a <code>mhsm_regions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mhsm_regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.mhsm_regions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the geo replicated region. |
| <CopyableCode code="isPrimary" /> | `boolean` | A boolean value that indicates whether the region is the primary region or a secondary region. |
| <CopyableCode code="provisioningState" /> | `string` | The current provisioning state. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_resource" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | The List operation gets information about the regions associated with the managed HSM Pool. |

## `SELECT` examples

The List operation gets information about the regions associated with the managed HSM Pool.


```sql
SELECT
name,
isPrimary,
provisioningState
FROM azure.key_vault.mhsm_regions
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
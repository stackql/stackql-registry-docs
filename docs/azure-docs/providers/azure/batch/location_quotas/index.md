---
title: location_quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - location_quotas
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

Creates, updates, deletes, gets or lists a <code>location_quotas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch.location_quotas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountQuota" /> | `integer` | The number of Batch accounts that may be created under the subscription in the specified region. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> | Gets the Batch service quotas for the specified subscription at the given location. |

## `SELECT` examples

Gets the Batch service quotas for the specified subscription at the given location.


```sql
SELECT
accountQuota
FROM azure.batch.location_quotas
WHERE locationName = '{{ locationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
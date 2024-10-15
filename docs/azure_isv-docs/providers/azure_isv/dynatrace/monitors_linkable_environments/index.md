---
title: monitors_linkable_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_linkable_environments
  - dynatrace
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

Creates, updates, deletes, gets or lists a <code>monitors_linkable_environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitors_linkable_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.dynatrace.monitors_linkable_environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="environmentId" /> | `string` | environment id for which user is an admin |
| <CopyableCode code="environmentName" /> | `string` | Name of the environment |
| <CopyableCode code="planData" /> | `object` | Billing plan information. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId, data__region, data__tenantId, data__userPrincipal" /> |  |

## `SELECT` examples




```sql
SELECT
environmentId,
environmentName,
planData
FROM azure_isv.dynatrace.monitors_linkable_environments
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__region = '{{ data__region }}'
AND data__tenantId = '{{ data__tenantId }}'
AND data__userPrincipal = '{{ data__userPrincipal }}';
```
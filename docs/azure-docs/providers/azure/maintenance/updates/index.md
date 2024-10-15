---
title: updates
hide_title: false
hide_table_of_contents: false
keywords:
  - updates
  - maintenance
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

Creates, updates, deletes, gets or lists a <code>updates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>updates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maintenance.updates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="impactDurationInSec" /> | `integer` | Duration of impact in seconds |
| <CopyableCode code="impactType" /> | `string` | The impact type |
| <CopyableCode code="maintenanceScope" /> | `string` | The impact area |
| <CopyableCode code="notBefore" /> | `string` | Time when Azure will start force updates if not self-updated by customer before this time |
| <CopyableCode code="properties" /> | `object` | Properties for update |
| <CopyableCode code="status" /> | `string` | The status |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="providerName, resourceGroupName, resourceName, resourceType, subscriptionId" /> | Get updates to resources. |

## `SELECT` examples

Get updates to resources.


```sql
SELECT
impactDurationInSec,
impactType,
maintenanceScope,
notBefore,
properties,
status
FROM azure.maintenance.updates
WHERE providerName = '{{ providerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND resourceType = '{{ resourceType }}'
AND subscriptionId = '{{ subscriptionId }}';
```
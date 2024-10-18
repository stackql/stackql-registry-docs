---
title: subscriptions_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions_locations
  - resources
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>subscriptions_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.subscriptions_locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified ID of the location. For example, /subscriptions/00000000-0000-0000-0000-000000000000/locations/westus. |
| <CopyableCode code="name" /> | `string` | The location name. |
| <CopyableCode code="displayName" /> | `string` | The display name of the location. |
| <CopyableCode code="metadata" /> | `object` | Location metadata information |
| <CopyableCode code="regionalDisplayName" /> | `string` | The display name of the location and its region. |
| <CopyableCode code="subscriptionId" /> | `string` | The subscription ID. |
| <CopyableCode code="type" /> | `string` | The location type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | This operation provides all the locations that are available for resource providers; however, each resource provider may support a subset of this list. |

## `SELECT` examples

This operation provides all the locations that are available for resource providers; however, each resource provider may support a subset of this list.


```sql
SELECT
id,
name,
displayName,
metadata,
regionalDisplayName,
subscriptionId,
type
FROM azure.resources.subscriptions_locations
WHERE subscriptionId = '{{ subscriptionId }}';
```
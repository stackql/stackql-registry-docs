---
title: available_resource_group_delegations
hide_title: false
hide_table_of_contents: false
keywords:
  - available_resource_group_delegations
  - network
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

Creates, updates, deletes, gets or lists a <code>available_resource_group_delegations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>available_resource_group_delegations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.available_resource_group_delegations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique identifier of the AvailableDelegation resource. |
| <CopyableCode code="name" /> | `string` | The name of the AvailableDelegation resource. |
| <CopyableCode code="actions" /> | `array` | The actions permitted to the service upon delegation. |
| <CopyableCode code="serviceName" /> | `string` | The name of the service and resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Gets all of the available subnet delegations for this resource group in this region. |

## `SELECT` examples

Gets all of the available subnet delegations for this resource group in this region.


```sql
SELECT
id,
name,
actions,
serviceName,
type
FROM azure.network.available_resource_group_delegations
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
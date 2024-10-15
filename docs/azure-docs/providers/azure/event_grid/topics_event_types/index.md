---
title: topics_event_types
hide_title: false
hide_table_of_contents: false
keywords:
  - topics_event_types
  - event_grid
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

Creates, updates, deletes, gets or lists a <code>topics_event_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topics_event_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.topics_event_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the event type |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="providerNamespace, resourceGroupName, resourceName, resourceTypeName, subscriptionId" /> | List event types for a topic. |

## `SELECT` examples

List event types for a topic.


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.event_grid.topics_event_types
WHERE providerNamespace = '{{ providerNamespace }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND resourceTypeName = '{{ resourceTypeName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
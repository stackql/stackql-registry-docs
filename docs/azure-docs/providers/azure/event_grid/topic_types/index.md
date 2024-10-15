---
title: topic_types
hide_title: false
hide_table_of_contents: false
keywords:
  - topic_types
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

Creates, updates, deletes, gets or lists a <code>topic_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.topic_types" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_topic_types', value: 'view', },
        { label: 'topic_types', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="additional_enforced_permissions" /> | `text` | field from the `properties` object |
| <CopyableCode code="are_regional_and_global_sources_supported" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_region_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_resource_format" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_locations" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_scopes_for_source" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="topicTypeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of a topic type. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="topicTypeName" /> | Get information about a topic type. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | List all registered topic types. |

## `SELECT` examples

List all registered topic types.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_topic_types', value: 'view', },
        { label: 'topic_types', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
additional_enforced_permissions,
are_regional_and_global_sources_supported,
display_name,
provider,
provisioning_state,
resource_region_type,
source_resource_format,
supported_locations,
supported_scopes_for_source,
system_data,
topicTypeName,
type
FROM azure.event_grid.vw_topic_types
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.event_grid.topic_types
;
```
</TabItem></Tabs>


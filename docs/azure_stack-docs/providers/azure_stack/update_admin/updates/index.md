---
title: updates
hide_title: false
hide_table_of_contents: false
keywords:
  - updates
  - update_admin
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.update_admin.updates" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_updates', value: 'view', },
        { label: 'updates', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="additional_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="installed_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="kb_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Region location of resource. |
| <CopyableCode code="min_oem_version_required" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_version_required" /> | `text` | field from the `properties` object |
| <CopyableCode code="oem_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_size_in_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher" /> | `text` | field from the `properties` object |
| <CopyableCode code="release_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key-value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
| <CopyableCode code="updateLocation" /> | `text` | field from the `properties` object |
| <CopyableCode code="updateName" /> | `text` | field from the `properties` object |
| <CopyableCode code="update_prerequisites" /> | `text` | field from the `properties` object |
| <CopyableCode code="update_state_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Region location of resource. |
| <CopyableCode code="properties" /> | `object` | Properties of an update. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, updateLocation, updateName" /> | Get a specific update at an update location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, updateLocation" /> | Get the list of updates at an update locations |
| <CopyableCode code="apply" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, updateLocation, updateName" /> | Apply a specific update at an update location. |
| <CopyableCode code="health_check" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, updateLocation, updateName" /> | Run health check for a specified update at an update location. |
| <CopyableCode code="prepare" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, updateLocation, updateName" /> | Prepare a specified update at an update location. |

## `SELECT` examples

Get the list of updates at an update locations

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_updates', value: 'view', },
        { label: 'updates', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
additional_properties,
availability_type,
display_name,
installed_date,
kb_link,
location,
min_oem_version_required,
min_version_required,
oem_version,
package_path,
package_size_in_mb,
package_type,
publisher,
release_link,
resourceGroupName,
state,
subscriptionId,
tags,
type,
updateLocation,
updateName,
update_prerequisites,
update_state_properties,
version
FROM azure_stack.update_admin.vw_updates
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND updateLocation = '{{ updateLocation }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure_stack.update_admin.updates
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND updateLocation = '{{ updateLocation }}';
```
</TabItem></Tabs>


---
title: updates
hide_title: false
hide_table_of_contents: false
keywords:
  - updates
  - azure_stack_hci
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.updates" /></td></tr>
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
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="additional_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="component_versions" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_check_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_check_result" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="installed_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="package_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_size_in_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="package_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="prerequisites" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher" /> | `text` | field from the `properties` object |
| <CopyableCode code="reboot_required" /> | `text` | field from the `properties` object |
| <CopyableCode code="release_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="updateName" /> | `text` | field from the `properties` object |
| <CopyableCode code="update_state_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Details of a singular Update in HCI Cluster |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, updateName" /> | Get specified Update |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | List all Updates |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, updateName" /> | Delete specified Update |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, updateName" /> | Put specified Update |
| <CopyableCode code="post" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, updateName" /> | Apply Update |

## `SELECT` examples

List all Updates

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
description,
additional_properties,
availability_type,
clusterName,
component_versions,
display_name,
health_check_date,
health_check_result,
health_state,
installed_date,
location,
package_path,
package_size_in_mb,
package_type,
prerequisites,
provisioning_state,
publisher,
reboot_required,
release_link,
resourceGroupName,
state,
subscriptionId,
updateName,
update_state_properties,
version
FROM azure_stack.azure_stack_hci.vw_updates
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties
FROM azure_stack.azure_stack_hci.updates
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>updates</code> resource.

```sql
/*+ update */
REPLACE azure_stack.azure_stack_hci.updates
SET 
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND updateName = '{{ updateName }}';
```

## `DELETE` example

Deletes the specified <code>updates</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack_hci.updates
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND updateName = '{{ updateName }}';
```

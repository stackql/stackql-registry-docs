---
title: private_link_resources_secs
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources_secs
  - security_and_compliance
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

Creates, updates, deletes, gets or lists a <code>private_link_resources_secs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_link_resources_secs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_and_compliance.private_link_resources_secs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_link_resources_secs', value: 'view', },
        { label: 'private_link_resources_secs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="groupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="required_members" /> | `text` | field from the `properties` object |
| <CopyableCode code="required_zone_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of a private link resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupName, resourceGroupName, resourceName, subscriptionId" /> | Gets a private link resource that need to be created for a service. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets the private link resources that need to be created for a service. |

## `SELECT` examples

Gets the private link resources that need to be created for a service.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_link_resources_secs', value: 'view', },
        { label: 'private_link_resources_secs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
groupName,
group_id,
required_members,
required_zone_names,
resourceGroupName,
resourceName,
subscriptionId,
system_data,
type
FROM azure.security_and_compliance.vw_private_link_resources_secs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
FROM azure.security_and_compliance.private_link_resources_secs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


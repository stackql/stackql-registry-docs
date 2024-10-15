---
title: network_security_perimeter_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter_configurations
  - search
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

Creates, updates, deletes, gets or lists a <code>network_security_perimeter_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_security_perimeter_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search.network_security_perimeter_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_security_perimeter_configurations', value: 'view', },
        { label: 'network_security_perimeter_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="network_security_perimeter" /> | `text` | field from the `properties` object |
| <CopyableCode code="nspConfigName" /> | `text` | field from the `properties` object |
| <CopyableCode code="profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_issues" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_association" /> | `text` | field from the `properties` object |
| <CopyableCode code="searchServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a network security perimeter configuration. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="nspConfigName, resourceGroupName, searchServiceName, subscriptionId" /> | Gets a network security perimeter configuration. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, searchServiceName, subscriptionId" /> | Gets a list of network security perimeter configurations for a search service. |
| <CopyableCode code="reconcile" /> | `EXEC` | <CopyableCode code="nspConfigName, resourceGroupName, searchServiceName, subscriptionId" /> | Reconcile network security perimeter configuration for the Azure AI Search resource provider. This triggers a manual resync with network security perimeter configurations by ensuring the search service carries the latest configuration. |

## `SELECT` examples

Gets a list of network security perimeter configurations for a search service.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_security_perimeter_configurations', value: 'view', },
        { label: 'network_security_perimeter_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
network_security_perimeter,
nspConfigName,
profile,
provisioning_issues,
provisioning_state,
resourceGroupName,
resource_association,
searchServiceName,
subscriptionId
FROM azure.search.vw_network_security_perimeter_configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND searchServiceName = '{{ searchServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.search.network_security_perimeter_configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND searchServiceName = '{{ searchServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


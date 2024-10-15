---
title: business_process_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - business_process_versions
  - integration_environment
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

Creates, updates, deletes, gets or lists a <code>business_process_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>business_process_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.integration_environment.business_process_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_business_process_versions', value: 'view', },
        { label: 'business_process_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="businessProcessName" /> | `text` | field from the `properties` object |
| <CopyableCode code="businessProcessVersion" /> | `text` | field from the `properties` object |
| <CopyableCode code="business_process_mapping" /> | `text` | field from the `properties` object |
| <CopyableCode code="business_process_stages" /> | `text` | field from the `properties` object |
| <CopyableCode code="identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="spaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="table_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="tracking_data_store_reference_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of business process. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationName, businessProcessName, businessProcessVersion, resourceGroupName, spaceName, subscriptionId" /> | Get a BusinessProcessVersion |
| <CopyableCode code="list_by_business_process" /> | `SELECT` | <CopyableCode code="applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId" /> | List BusinessProcessVersion resources by BusinessProcess |

## `SELECT` examples

List BusinessProcessVersion resources by BusinessProcess

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_business_process_versions', value: 'view', },
        { label: 'business_process_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
applicationName,
businessProcessName,
businessProcessVersion,
business_process_mapping,
business_process_stages,
identifier,
provisioning_state,
resourceGroupName,
spaceName,
subscriptionId,
table_name,
tracking_data_store_reference_name,
version
FROM azure.integration_environment.vw_business_process_versions
WHERE applicationName = '{{ applicationName }}'
AND businessProcessName = '{{ businessProcessName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND spaceName = '{{ spaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.integration_environment.business_process_versions
WHERE applicationName = '{{ applicationName }}'
AND businessProcessName = '{{ businessProcessName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND spaceName = '{{ spaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


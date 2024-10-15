---
title: endpoint_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_certificates
  - sql
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

Creates, updates, deletes, gets or lists a <code>endpoint_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.endpoint_certificates" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_endpoint_certificates', value: 'view', },
        { label: 'endpoint_certificates', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endpointType" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_blob" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of an endpoint certificate. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointType, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a certificate used on the endpoint with the given id. |

## `SELECT` examples

Gets a certificate used on the endpoint with the given id.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_endpoint_certificates', value: 'view', },
        { label: 'endpoint_certificates', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
endpointType,
managedInstanceName,
public_blob,
resourceGroupName,
subscriptionId
FROM azure.sql.vw_endpoint_certificates
WHERE endpointType = '{{ endpointType }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.endpoint_certificates
WHERE endpointType = '{{ endpointType }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


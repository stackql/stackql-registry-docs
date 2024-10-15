---
title: dedicated_cloud_services
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_cloud_services
  - vmware_cloud_simple
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

Creates, updates, deletes, gets or lists a <code>dedicated_cloud_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dedicated_cloud_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.dedicated_cloud_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dedicated_cloud_services', value: 'view', },
        { label: 'dedicated_cloud_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedCloudServices/{dedicatedCloudServiceName} |
| <CopyableCode code="name" /> | `text` | {dedicatedCloudServiceName} |
| <CopyableCode code="dedicatedCloudServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_subnet" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_account_onboarded" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Azure region |
| <CopyableCode code="nodes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Tags model |
| <CopyableCode code="type" /> | `text` | {resourceProviderNamespace}/{resourceType} |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/dedicatedCloudServices/{dedicatedCloudServiceName} |
| <CopyableCode code="name" /> | `string` | {dedicatedCloudServiceName} |
| <CopyableCode code="location" /> | `string` | Azure region |
| <CopyableCode code="properties" /> | `object` | Properties of dedicated cloud service |
| <CopyableCode code="tags" /> | `object` | Tags model |
| <CopyableCode code="type" /> | `string` | {resourceProviderNamespace}/{resourceType} |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dedicatedCloudServiceName, resourceGroupName, subscriptionId" /> | Returns Dedicate Cloud Service |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns list of dedicated cloud services within a resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns list of dedicated cloud services within a subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dedicatedCloudServiceName, resourceGroupName, subscriptionId, data__location" /> | Create dedicate cloud service |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dedicatedCloudServiceName, resourceGroupName, subscriptionId" /> | Delete dedicate cloud service |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dedicatedCloudServiceName, resourceGroupName, subscriptionId" /> | Patch dedicated cloud service's properties |

## `SELECT` examples

Returns list of dedicated cloud services within a subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dedicated_cloud_services', value: 'view', },
        { label: 'dedicated_cloud_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
dedicatedCloudServiceName,
gateway_subnet,
is_account_onboarded,
location,
nodes,
resourceGroupName,
service_url,
subscriptionId,
tags,
type
FROM azure_isv.vmware_cloud_simple.vw_dedicated_cloud_services
WHERE subscriptionId = '{{ subscriptionId }}';
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
FROM azure_isv.vmware_cloud_simple.dedicated_cloud_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dedicated_cloud_services</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure_isv.vmware_cloud_simple.dedicated_cloud_services (
dedicatedCloudServiceName,
resourceGroupName,
subscriptionId,
data__location,
location,
properties,
tags
)
SELECT 
'{{ dedicatedCloudServiceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ location }}',
'{{ properties }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: location
      value: string
    - name: name
      value: string
    - name: properties
      value:
        - name: gatewaySubnet
          value: string
        - name: isAccountOnboarded
          value: string
        - name: nodes
          value: integer
        - name: serviceURL
          value: string
    - name: tags
      value: []
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dedicated_cloud_services</code> resource.

```sql
/*+ update */
UPDATE azure_isv.vmware_cloud_simple.dedicated_cloud_services
SET 
tags = '{{ tags }}'
WHERE 
dedicatedCloudServiceName = '{{ dedicatedCloudServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>dedicated_cloud_services</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.vmware_cloud_simple.dedicated_cloud_services
WHERE dedicatedCloudServiceName = '{{ dedicatedCloudServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

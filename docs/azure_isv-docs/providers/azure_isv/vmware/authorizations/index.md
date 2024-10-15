---
title: authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - authorizations
  - vmware
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

Creates, updates, deletes, gets or lists a <code>authorizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware.authorizations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_authorizations', value: 'view', },
        { label: 'authorizations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="authorizationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="express_route_authorization_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="express_route_authorization_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateCloudName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The properties of an ExpressRoute Circuit Authorization resource |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizationName, privateCloudName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorizationName, privateCloudName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authorizationName, privateCloudName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_authorizations', value: 'view', },
        { label: 'authorizations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
authorizationName,
express_route_authorization_id,
express_route_authorization_key,
privateCloudName,
provisioning_state,
resourceGroupName,
subscriptionId,
type
FROM azure_isv.vmware.vw_authorizations
WHERE privateCloudName = '{{ privateCloudName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure_isv.vmware.authorizations
WHERE privateCloudName = '{{ privateCloudName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>authorizations</code> resource.

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
INSERT INTO azure_isv.vmware.authorizations (
authorizationName,
privateCloudName,
resourceGroupName,
subscriptionId
)
SELECT 
'{{ authorizationName }}',
'{{ privateCloudName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: expressRouteAuthorizationId
          value: string
        - name: expressRouteAuthorizationKey
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>authorizations</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.vmware.authorizations
WHERE authorizationName = '{{ authorizationName }}'
AND privateCloudName = '{{ privateCloudName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

---
title: load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers
  - k8s_runtime
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

Creates, updates, deletes, gets or lists a <code>load_balancers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.k8s_runtime.load_balancers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_load_balancers', value: 'view', },
        { label: 'load_balancers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="advertise_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="loadBalancerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_selector" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Details of the LoadBalancer. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="loadBalancerName, resourceUri" /> | Get a LoadBalancer |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | List LoadBalancer resources by parent |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="loadBalancerName, resourceUri" /> | Create a LoadBalancer |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="loadBalancerName, resourceUri" /> | Delete a LoadBalancer |

## `SELECT` examples

List LoadBalancer resources by parent

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_load_balancers', value: 'view', },
        { label: 'load_balancers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
addresses,
advertise_mode,
loadBalancerName,
provisioning_state,
resourceUri,
service_selector
FROM azure.k8s_runtime.vw_load_balancers
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.k8s_runtime.load_balancers
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>load_balancers</code> resource.

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
INSERT INTO azure.k8s_runtime.load_balancers (
loadBalancerName,
resourceUri,
properties
)
SELECT 
'{{ loadBalancerName }}',
'{{ resourceUri }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: addresses
          value:
            - string
        - name: serviceSelector
          value: object
        - name: advertiseMode
          value: []
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>load_balancers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.k8s_runtime.load_balancers
WHERE loadBalancerName = '{{ loadBalancerName }}'
AND resourceUri = '{{ resourceUri }}';
```

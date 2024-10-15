---
title: security_policies_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - security_policies_interfaces
  - service_networking
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

Creates, updates, deletes, gets or lists a <code>security_policies_interfaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_policies_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_networking.security_policies_interfaces" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_security_policies_interfaces', value: 'view', },
        { label: 'security_policies_interfaces', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="policy_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="securityPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="trafficControllerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="waf_policy" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | SecurityPolicy Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, securityPolicyName, subscriptionId, trafficControllerName" /> | Get a SecurityPolicy |
| <CopyableCode code="list_by_traffic_controller" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, trafficControllerName" /> | List SecurityPolicy resources by TrafficController |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, securityPolicyName, subscriptionId, trafficControllerName" /> | Create a SecurityPolicy |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, securityPolicyName, subscriptionId, trafficControllerName" /> | Delete a SecurityPolicy |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, securityPolicyName, subscriptionId, trafficControllerName" /> | Update a SecurityPolicy |

## `SELECT` examples

List SecurityPolicy resources by TrafficController

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_security_policies_interfaces', value: 'view', },
        { label: 'security_policies_interfaces', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
location,
policy_type,
provisioning_state,
resourceGroupName,
securityPolicyName,
subscriptionId,
tags,
trafficControllerName,
waf_policy
FROM azure.service_networking.vw_security_policies_interfaces
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trafficControllerName = '{{ trafficControllerName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.service_networking.security_policies_interfaces
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trafficControllerName = '{{ trafficControllerName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_policies_interfaces</code> resource.

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
INSERT INTO azure.service_networking.security_policies_interfaces (
resourceGroupName,
securityPolicyName,
subscriptionId,
trafficControllerName,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ securityPolicyName }}',
'{{ subscriptionId }}',
'{{ trafficControllerName }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: policyType
          value: []
        - name: wafPolicy
          value:
            - name: id
              value: string
        - name: provisioningState
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>security_policies_interfaces</code> resource.

```sql
/*+ update */
UPDATE azure.service_networking.security_policies_interfaces
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND securityPolicyName = '{{ securityPolicyName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trafficControllerName = '{{ trafficControllerName }}';
```

## `DELETE` example

Deletes the specified <code>security_policies_interfaces</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_networking.security_policies_interfaces
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND securityPolicyName = '{{ securityPolicyName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trafficControllerName = '{{ trafficControllerName }}';
```

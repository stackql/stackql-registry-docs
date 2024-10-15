---
title: sim_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - sim_policies
  - mobile_network
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

Creates, updates, deletes, gets or lists a <code>sim_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sim_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.sim_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sim_policies', value: 'view', },
        { label: 'sim_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="default_slice" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="mobileNetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_timer" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rfsp_index" /> | `text` | field from the `properties` object |
| <CopyableCode code="simPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="site_provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="slice_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="ue_ambr" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | SIM policy properties. Must be created in the same location as its parent mobile network. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="mobileNetworkName, resourceGroupName, simPolicyName, subscriptionId" /> | Gets information about the specified SIM policy. |
| <CopyableCode code="list_by_mobile_network" /> | `SELECT` | <CopyableCode code="mobileNetworkName, resourceGroupName, subscriptionId" /> | Gets all the SIM policies in a mobile network. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="mobileNetworkName, resourceGroupName, simPolicyName, subscriptionId, data__properties" /> | Creates or updates a SIM policy. Must be created in the same location as its parent mobile network. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="mobileNetworkName, resourceGroupName, simPolicyName, subscriptionId" /> | Deletes the specified SIM policy. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="mobileNetworkName, resourceGroupName, simPolicyName, subscriptionId" /> | Updates SIM policy tags. |

## `SELECT` examples

Gets all the SIM policies in a mobile network.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sim_policies', value: 'view', },
        { label: 'sim_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
default_slice,
location,
mobileNetworkName,
provisioning_state,
registration_timer,
resourceGroupName,
rfsp_index,
simPolicyName,
site_provisioning_state,
slice_configurations,
subscriptionId,
tags,
ue_ambr
FROM azure.mobile_network.vw_sim_policies
WHERE mobileNetworkName = '{{ mobileNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.mobile_network.sim_policies
WHERE mobileNetworkName = '{{ mobileNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sim_policies</code> resource.

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
INSERT INTO azure.mobile_network.sim_policies (
mobileNetworkName,
resourceGroupName,
simPolicyName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ mobileNetworkName }}',
'{{ resourceGroupName }}',
'{{ simPolicyName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: provisioningState
          value: []
        - name: siteProvisioningState
          value: []
        - name: ueAmbr
          value:
            - name: uplink
              value: []
        - name: defaultSlice
          value:
            - name: id
              value: string
        - name: rfspIndex
          value: []
        - name: registrationTimer
          value: integer
        - name: sliceConfigurations
          value:
            - - name: defaultDataNetwork
                value:
                  - name: id
                    value: string
              - name: dataNetworkConfigurations
                value:
                  - - name: 5qi
                      value: []
                    - name: allocationAndRetentionPriorityLevel
                      value: []
                    - name: preemptionCapability
                      value: []
                    - name: preemptionVulnerability
                      value: []
                    - name: defaultSessionType
                      value: []
                    - name: additionalAllowedSessionTypes
                      value:
                        - []
                    - name: allowedServices
                      value:
                        - - name: id
                            value: string
                    - name: maximumNumberOfBufferedPackets
                      value: integer
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sim_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.mobile_network.sim_policies
WHERE mobileNetworkName = '{{ mobileNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND simPolicyName = '{{ simPolicyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

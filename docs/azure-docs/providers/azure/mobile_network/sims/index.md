---
title: sims
hide_title: false
hide_table_of_contents: false
keywords:
  - sims
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

Creates, updates, deletes, gets or lists a <code>sims</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sims</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.sims" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sims', value: 'view', },
        { label: 'sims', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authentication_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="integrated_circuit_card_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="international_mobile_subscriber_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="operator_key_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="simGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="simName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sim_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="sim_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="site_provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="static_ip_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="vendor_key_fingerprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="vendor_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | SIM properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, simGroupName, simName, subscriptionId" /> | Gets information about the specified SIM. |
| <CopyableCode code="list_by_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, simGroupName, subscriptionId" /> | Gets all the SIMs in a SIM group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, simGroupName, simName, subscriptionId, data__properties" /> | Creates or updates a SIM. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, simGroupName, simName, subscriptionId" /> | Deletes the specified SIM. |
| <CopyableCode code="bulk_delete" /> | `EXEC` | <CopyableCode code="resourceGroupName, simGroupName, subscriptionId, data__sims" /> | Bulk delete SIMs from a SIM group. |
| <CopyableCode code="bulk_upload" /> | `EXEC` | <CopyableCode code="resourceGroupName, simGroupName, subscriptionId, data__sims" /> | Bulk upload SIMs to a SIM group. |
| <CopyableCode code="bulk_upload_encrypted" /> | `EXEC` | <CopyableCode code="resourceGroupName, simGroupName, subscriptionId, data__azureKeyIdentifier, data__encryptedTransportKey, data__signedTransportKey, data__sims, data__vendorKeyFingerprint, data__version" /> | Bulk upload SIMs in encrypted form to a SIM group. The SIM credentials must be encrypted. |
| <CopyableCode code="clone" /> | `EXEC` | <CopyableCode code="resourceGroupName, simGroupName, subscriptionId" /> | Clone SIMs to another SIM Group |
| <CopyableCode code="move" /> | `EXEC` | <CopyableCode code="resourceGroupName, simGroupName, subscriptionId" /> | Move SIMs to another SIM Group |

## `SELECT` examples

Gets all the SIMs in a SIM group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sims', value: 'view', },
        { label: 'sims', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
authentication_key,
device_type,
integrated_circuit_card_identifier,
international_mobile_subscriber_identity,
operator_key_code,
provisioning_state,
resourceGroupName,
simGroupName,
simName,
sim_policy,
sim_state,
site_provisioning_state,
static_ip_configuration,
subscriptionId,
vendor_key_fingerprint,
vendor_name
FROM azure.mobile_network.vw_sims
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND simGroupName = '{{ simGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.mobile_network.sims
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND simGroupName = '{{ simGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sims</code> resource.

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
INSERT INTO azure.mobile_network.sims (
resourceGroupName,
simGroupName,
simName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ simGroupName }}',
'{{ simName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: authenticationKey
          value: string
        - name: operatorKeyCode
          value: string
        - name: provisioningState
          value: []
        - name: simState
          value: []
        - name: siteProvisioningState
          value: []
        - name: internationalMobileSubscriberIdentity
          value: string
        - name: integratedCircuitCardIdentifier
          value: string
        - name: deviceType
          value: string
        - name: simPolicy
          value:
            - name: id
              value: string
        - name: staticIpConfiguration
          value:
            - - name: attachedDataNetwork
                value:
                  - name: id
                    value: string
              - name: slice
                value:
                  - name: id
                    value: string
              - name: staticIp
                value:
                  - name: ipv4Address
                    value: []
        - name: vendorName
          value: string
        - name: vendorKeyFingerprint
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sims</code> resource.

```sql
/*+ delete */
DELETE FROM azure.mobile_network.sims
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND simGroupName = '{{ simGroupName }}'
AND simName = '{{ simName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

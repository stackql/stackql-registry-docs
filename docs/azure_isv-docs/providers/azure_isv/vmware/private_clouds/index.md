---
title: private_clouds
hide_title: false
hide_table_of_contents: false
keywords:
  - private_clouds
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

Creates, updates, deletes, gets or lists a <code>private_clouds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_clouds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware.private_clouds" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_clouds', value: 'view', },
        { label: 'private_clouds', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="circuit" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity_sources" /> | `text` | field from the `properties` object |
| <CopyableCode code="internet" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="management_cluster" /> | `text` | field from the `properties` object |
| <CopyableCode code="management_network" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_block" /> | `text` | field from the `properties` object |
| <CopyableCode code="nsxt_certificate_thumbprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="nsxt_password" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateCloudName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_network" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="vcenter_certificate_thumbprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="vcenter_password" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmotion_network" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | The properties of a private cloud resource |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_in_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId, data__location, data__properties, data__sku" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_clouds', value: 'view', },
        { label: 'private_clouds', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
circuit,
endpoints,
identity_sources,
internet,
location,
management_cluster,
management_network,
network_block,
nsxt_certificate_thumbprint,
nsxt_password,
privateCloudName,
provisioning_network,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
tags,
vcenter_certificate_thumbprint,
vcenter_password,
vmotion_network
FROM azure_isv.vmware.vw_private_clouds
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
tags
FROM azure_isv.vmware.private_clouds
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_clouds</code> resource.

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
INSERT INTO azure_isv.vmware.private_clouds (
privateCloudName,
resourceGroupName,
subscriptionId,
data__location,
data__properties,
data__sku,
location,
tags,
sku,
properties
)
SELECT 
'{{ privateCloudName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ data__sku }}',
'{{ location }}',
'{{ tags }}',
'{{ sku }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: sku
      value:
        - name: name
          value: string
    - name: properties
      value:
        - name: managementCluster
          value:
            - name: clusterSize
              value: integer
            - name: provisioningState
              value: []
            - name: clusterId
              value: integer
            - name: hosts
              value:
                - string
        - name: internet
          value: string
        - name: identitySources
          value:
            - - name: name
                value: string
              - name: alias
                value: string
              - name: domain
                value: string
              - name: baseUserDN
                value: string
              - name: baseGroupDN
                value: string
              - name: primaryServer
                value: string
              - name: secondaryServer
                value: string
              - name: ssl
                value: string
              - name: username
                value: string
              - name: password
                value: string
        - name: provisioningState
          value: string
        - name: circuit
          value:
            - name: primarySubnet
              value: string
            - name: secondarySubnet
              value: string
            - name: expressRouteID
              value: string
            - name: expressRoutePrivatePeeringID
              value: string
        - name: endpoints
          value:
            - name: nsxtManager
              value: string
            - name: vcsa
              value: string
            - name: hcxCloudManager
              value: string
        - name: networkBlock
          value: string
        - name: managementNetwork
          value: string
        - name: provisioningNetwork
          value: string
        - name: vmotionNetwork
          value: string
        - name: vcenterPassword
          value: string
        - name: nsxtPassword
          value: string
        - name: vcenterCertificateThumbprint
          value: string
        - name: nsxtCertificateThumbprint
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>private_clouds</code> resource.

```sql
/*+ update */
UPDATE azure_isv.vmware.private_clouds
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
privateCloudName = '{{ privateCloudName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>private_clouds</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.vmware.private_clouds
WHERE privateCloudName = '{{ privateCloudName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

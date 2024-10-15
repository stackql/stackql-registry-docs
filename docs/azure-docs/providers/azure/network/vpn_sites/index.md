---
title: vpn_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_sites
  - network
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

Creates, updates, deletes, gets or lists a <code>vpn_sites</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vpn_sites" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vpn_sites', value: 'view', },
        { label: 'vpn_sites', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="address_space" /> | `text` | field from the `properties` object |
| <CopyableCode code="bgp_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_security_site" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="o365_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="site_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtual_wan" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpnSiteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vpn_site_links" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Parameters for VpnSite. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vpnSiteName" /> | Retrieves the details of a VPN site. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the VpnSites in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the vpnSites in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, vpnSiteName, data__location" /> | Creates a VpnSite resource if it doesn't exist else updates the existing VpnSite. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, vpnSiteName" /> | Deletes a VpnSite. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vpnSiteName" /> | Updates VpnSite tags. |

## `SELECT` examples

Lists all the VpnSites in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vpn_sites', value: 'view', },
        { label: 'vpn_sites', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
address_space,
bgp_properties,
device_properties,
etag,
ip_address,
is_security_site,
location,
o365_policy,
provisioning_state,
resourceGroupName,
site_key,
subscriptionId,
tags,
type,
virtual_wan,
vpnSiteName,
vpn_site_links
FROM azure.network.vw_vpn_sites
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
tags,
type
FROM azure.network.vpn_sites
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpn_sites</code> resource.

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
INSERT INTO azure.network.vpn_sites (
resourceGroupName,
subscriptionId,
vpnSiteName,
data__location,
properties,
id,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vpnSiteName }}',
'{{ data__location }}',
'{{ properties }}',
'{{ id }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: virtualWan
          value:
            - name: id
              value: string
        - name: deviceProperties
          value:
            - name: deviceVendor
              value: string
            - name: deviceModel
              value: string
            - name: linkSpeedInMbps
              value: integer
        - name: ipAddress
          value: string
        - name: siteKey
          value: string
        - name: addressSpace
          value:
            - name: addressPrefixes
              value:
                - string
        - name: bgpProperties
          value:
            - name: asn
              value: integer
            - name: bgpPeeringAddress
              value: string
            - name: peerWeight
              value: integer
            - name: bgpPeeringAddresses
              value:
                - - name: ipconfigurationId
                    value: string
                  - name: defaultBgpIpAddresses
                    value:
                      - string
                  - name: customBgpIpAddresses
                    value:
                      - string
                  - name: tunnelIpAddresses
                    value:
                      - string
        - name: provisioningState
          value: []
        - name: isSecuritySite
          value: boolean
        - name: vpnSiteLinks
          value:
            - - name: properties
                value:
                  - name: linkProperties
                    value:
                      - name: linkProviderName
                        value: string
                      - name: linkSpeedInMbps
                        value: integer
                  - name: ipAddress
                    value: string
                  - name: fqdn
                    value: string
                  - name: bgpProperties
                    value:
                      - name: asn
                        value: integer
                      - name: bgpPeeringAddress
                        value: string
              - name: etag
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: id
                value: string
        - name: o365Policy
          value:
            - name: breakOutCategories
              value:
                - name: allow
                  value: boolean
                - name: optimize
                  value: boolean
                - name: default
                  value: boolean
    - name: etag
      value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>vpn_sites</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.vpn_sites
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vpnSiteName = '{{ vpnSiteName }}';
```

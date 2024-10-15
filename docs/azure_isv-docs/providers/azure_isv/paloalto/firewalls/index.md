---
title: firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls
  - paloalto
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

Creates, updates, deletes, gets or lists a <code>firewalls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.firewalls" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_firewalls', value: 'view', },
        { label: 'firewalls', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="associated_rulestack" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="firewallName" /> | `text` | field from the `properties` object |
| <CopyableCode code="front_end_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | The properties of the managed service identities assigned to this resource. |
| <CopyableCode code="is_panorama_managed" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_strata_cloud_managed" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="marketplace_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="pan_etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="panorama_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="strata_cloud_manager_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | The properties of the managed service identities assigned to this resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties specific to the Firewall resource deployment. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewallName, resourceGroupName, subscriptionId" /> | Get a FirewallResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List FirewallResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List FirewallResource resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="firewallName, resourceGroupName, subscriptionId, data__properties" /> | Create a FirewallResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="firewallName, resourceGroupName, subscriptionId" /> | Delete a FirewallResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="firewallName, resourceGroupName, subscriptionId" /> | Update a FirewallResource |
| <CopyableCode code="save_log_profile" /> | `EXEC` | <CopyableCode code="firewallName, resourceGroupName, subscriptionId" /> | Log Profile for Firewall |

## `SELECT` examples

List FirewallResource resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_firewalls', value: 'view', },
        { label: 'firewalls', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
associated_rulestack,
dns_settings,
firewallName,
front_end_settings,
identity,
is_panorama_managed,
is_strata_cloud_managed,
location,
marketplace_details,
network_profile,
pan_etag,
panorama_config,
plan_data,
provisioning_state,
resourceGroupName,
strata_cloud_manager_config,
subscriptionId,
system_data,
tags
FROM azure_isv.paloalto.vw_firewalls
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
systemData,
tags
FROM azure_isv.paloalto.firewalls
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>firewalls</code> resource.

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
INSERT INTO azure_isv.paloalto.firewalls (
firewallName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
identity,
tags,
location
)
SELECT 
'{{ firewallName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ identity }}',
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
        - name: panEtag
          value: string
        - name: networkProfile
          value:
            - name: vnetConfiguration
              value:
                - name: vnet
                  value:
                    - name: resourceId
                      value: string
                    - name: addressSpace
                      value: string
                - name: ipOfTrustSubnetForUdr
                  value:
                    - name: resourceId
                      value: string
                    - name: address
                      value: string
            - name: vwanConfiguration
              value:
                - name: networkVirtualApplianceId
                  value: string
            - name: networkType
              value: []
            - name: publicIps
              value:
                - - name: resourceId
                    value: string
                  - name: address
                    value: string
            - name: enableEgressNat
              value: []
            - name: egressNatIp
              value:
                - - name: resourceId
                    value: string
                  - name: address
                    value: string
            - name: trustedRanges
              value:
                - string
            - name: privateSourceNatRulesDestination
              value:
                - string
        - name: isPanoramaManaged
          value: []
        - name: panoramaConfig
          value:
            - name: configString
              value: string
            - name: vmAuthKey
              value: string
            - name: panoramaServer
              value: string
            - name: panoramaServer2
              value: string
            - name: dgName
              value: string
            - name: tplName
              value: string
            - name: cgName
              value: string
            - name: hostName
              value: string
        - name: strataCloudManagerConfig
          value:
            - name: cloudManagerName
              value: string
        - name: associatedRulestack
          value:
            - name: resourceId
              value: string
            - name: rulestackId
              value: string
            - name: location
              value: string
        - name: dnsSettings
          value:
            - name: enableDnsProxy
              value: []
            - name: enabledDnsType
              value: []
            - name: dnsServers
              value:
                - - name: resourceId
                    value: string
                  - name: address
                    value: string
        - name: frontEndSettings
          value:
            - - name: name
                value: string
              - name: protocol
                value: []
              - name: frontendConfiguration
                value:
                  - name: port
                    value: string
        - name: provisioningState
          value: []
        - name: planData
          value:
            - name: usageType
              value: []
            - name: billingCycle
              value: []
            - name: planId
              value: string
            - name: effectiveDate
              value: string
        - name: marketplaceDetails
          value:
            - name: marketplaceSubscriptionId
              value: string
            - name: offerId
              value: string
            - name: publisherId
              value: string
            - name: marketplaceSubscriptionStatus
              value: []
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: identity
      value:
        - name: tenantId
          value: string
        - name: principalId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: object
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>firewalls</code> resource.

```sql
/*+ update */
UPDATE azure_isv.paloalto.firewalls
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
firewallName = '{{ firewallName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>firewalls</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.paloalto.firewalls
WHERE firewallName = '{{ firewallName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

---
title: firewall_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policies
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

Creates, updates, deletes, gets or lists a <code>firewall_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.firewall_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_firewall_policies', value: 'view', },
        { label: 'firewall_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="base_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="child_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="explicit_proxy" /> | `text` | field from the `properties` object |
| <CopyableCode code="firewallPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="firewalls" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="insights" /> | `text` | field from the `properties` object |
| <CopyableCode code="intrusion_detection" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rule_collection_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="size" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="snat" /> | `text` | field from the `properties` object |
| <CopyableCode code="sql" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="threat_intel_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="threat_intel_whitelist" /> | `text` | field from the `properties` object |
| <CopyableCode code="transport_security" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Firewall Policy definition. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Gets the specified Firewall Policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Firewall Policies in a resource group. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the Firewall Policies in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Creates or updates the specified Firewall Policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Deletes the specified Firewall Policy. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Updates tags of a Azure Firewall Policy resource. |

## `SELECT` examples

Gets all the Firewall Policies in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_firewall_policies', value: 'view', },
        { label: 'firewall_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
base_policy,
child_policies,
dns_settings,
etag,
explicit_proxy,
firewallPolicyName,
firewalls,
identity,
insights,
intrusion_detection,
location,
provisioning_state,
resourceGroupName,
rule_collection_groups,
size,
sku,
snat,
sql,
subscriptionId,
tags,
threat_intel_mode,
threat_intel_whitelist,
transport_security,
type
FROM azure.network.vw_firewall_policies
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
identity,
location,
properties,
tags,
type
FROM azure.network.firewall_policies
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>firewall_policies</code> resource.

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
INSERT INTO azure.network.firewall_policies (
firewallPolicyName,
resourceGroupName,
subscriptionId,
properties,
identity,
id,
location,
tags
)
SELECT 
'{{ firewallPolicyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
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
        - name: size
          value: string
        - name: ruleCollectionGroups
          value:
            - - name: id
                value: string
        - name: provisioningState
          value: []
        - name: basePolicy
          value:
            - name: id
              value: string
        - name: firewalls
          value:
            - - name: id
                value: string
        - name: childPolicies
          value:
            - - name: id
                value: string
        - name: threatIntelMode
          value: []
        - name: threatIntelWhitelist
          value:
            - name: ipAddresses
              value:
                - string
            - name: fqdns
              value:
                - string
        - name: insights
          value:
            - name: isEnabled
              value: boolean
            - name: retentionDays
              value: integer
            - name: logAnalyticsResources
              value:
                - name: workspaces
                  value:
                    - - name: region
                        value: string
        - name: snat
          value:
            - name: privateRanges
              value:
                - string
            - name: autoLearnPrivateRanges
              value: string
        - name: sql
          value:
            - name: allowSqlRedirect
              value: boolean
        - name: dnsSettings
          value:
            - name: servers
              value:
                - string
            - name: enableProxy
              value: boolean
            - name: requireProxyForNetworkRules
              value: boolean
        - name: explicitProxy
          value:
            - name: enableExplicitProxy
              value: boolean
            - name: httpPort
              value: integer
            - name: httpsPort
              value: integer
            - name: enablePacFile
              value: boolean
            - name: pacFilePort
              value: integer
            - name: pacFile
              value: string
        - name: intrusionDetection
          value:
            - name: mode
              value: []
            - name: profile
              value: []
            - name: configuration
              value:
                - name: signatureOverrides
                  value:
                    - - name: id
                        value: string
                - name: bypassTrafficSettings
                  value:
                    - - name: name
                        value: string
                      - name: description
                        value: string
                      - name: protocol
                        value: []
                      - name: sourceAddresses
                        value:
                          - string
                      - name: destinationAddresses
                        value:
                          - string
                      - name: destinationPorts
                        value:
                          - string
                      - name: sourceIpGroups
                        value:
                          - string
                      - name: destinationIpGroups
                        value:
                          - string
                - name: privateRanges
                  value:
                    - string
        - name: transportSecurity
          value:
            - name: certificateAuthority
              value:
                - name: keyVaultSecretId
                  value: string
                - name: name
                  value: string
        - name: sku
          value:
            - name: tier
              value: string
    - name: etag
      value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
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

Deletes the specified <code>firewall_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.firewall_policies
WHERE firewallPolicyName = '{{ firewallPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

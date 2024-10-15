---
title: firewall_policy_drafts
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policy_drafts
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

Creates, updates, deletes, gets or lists a <code>firewall_policy_drafts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_policy_drafts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.firewall_policy_drafts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_firewall_policy_drafts', value: 'view', },
        { label: 'firewall_policy_drafts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="base_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="explicit_proxy" /> | `text` | field from the `properties` object |
| <CopyableCode code="firewallPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="insights" /> | `text` | field from the `properties` object |
| <CopyableCode code="intrusion_detection" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="snat" /> | `text` | field from the `properties` object |
| <CopyableCode code="sql" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="threat_intel_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="threat_intel_whitelist" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Get a draft Firewall Policy. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Create or update a draft Firewall Policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Delete a draft policy. |

## `SELECT` examples

Get a draft Firewall Policy.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_firewall_policy_drafts', value: 'view', },
        { label: 'firewall_policy_drafts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
base_policy,
dns_settings,
explicit_proxy,
firewallPolicyName,
insights,
intrusion_detection,
location,
resourceGroupName,
snat,
sql,
subscriptionId,
tags,
threat_intel_mode,
threat_intel_whitelist,
type
FROM azure.network.vw_firewall_policy_drafts
WHERE firewallPolicyName = '{{ firewallPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
FROM azure.network.firewall_policy_drafts
WHERE firewallPolicyName = '{{ firewallPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>firewall_policy_drafts</code> resource.

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
INSERT INTO azure.network.firewall_policy_drafts (
firewallPolicyName,
resourceGroupName,
subscriptionId,
properties,
id,
location,
tags
)
SELECT 
'{{ firewallPolicyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: basePolicy
          value:
            - name: id
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

Deletes the specified <code>firewall_policy_drafts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.firewall_policy_drafts
WHERE firewallPolicyName = '{{ firewallPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

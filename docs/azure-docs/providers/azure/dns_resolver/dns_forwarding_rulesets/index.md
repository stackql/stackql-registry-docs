---
title: dns_forwarding_rulesets
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_forwarding_rulesets
  - dns_resolver
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

Creates, updates, deletes, gets or lists a <code>dns_forwarding_rulesets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dns_forwarding_rulesets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns_resolver.dns_forwarding_rulesets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dns_forwarding_rulesets', value: 'view', },
        { label: 'dns_forwarding_rulesets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dnsForwardingRulesetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_resolver_outbound_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | ETag of the DNS forwarding ruleset. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | ETag of the DNS forwarding ruleset. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Represents the properties of a DNS forwarding ruleset. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsForwardingRulesetName, resourceGroupName, subscriptionId" /> | Gets a DNS forwarding ruleset properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists DNS forwarding rulesets in all resource groups of a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists DNS forwarding rulesets within a resource group. |
| <CopyableCode code="list_by_virtual_network" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName" /> | Lists DNS forwarding ruleset resource IDs attached to a virtual network. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dnsForwardingRulesetName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a DNS forwarding ruleset. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dnsForwardingRulesetName, resourceGroupName, subscriptionId" /> | Deletes a DNS forwarding ruleset. WARNING: This operation cannot be undone. All forwarding rules within the ruleset will be deleted. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dnsForwardingRulesetName, resourceGroupName, subscriptionId" /> | Updates a DNS forwarding ruleset. |

## `SELECT` examples

Lists DNS forwarding rulesets in all resource groups of a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dns_forwarding_rulesets', value: 'view', },
        { label: 'dns_forwarding_rulesets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dnsForwardingRulesetName,
dns_resolver_outbound_endpoints,
etag,
location,
provisioning_state,
resourceGroupName,
resource_guid,
subscriptionId,
system_data,
tags
FROM azure.dns_resolver.vw_dns_forwarding_rulesets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
systemData,
tags
FROM azure.dns_resolver.dns_forwarding_rulesets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dns_forwarding_rulesets</code> resource.

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
INSERT INTO azure.dns_resolver.dns_forwarding_rulesets (
dnsForwardingRulesetName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ dnsForwardingRulesetName }}',
'{{ resourceGroupName }}',
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
    - name: etag
      value: string
    - name: properties
      value:
        - name: dnsResolverOutboundEndpoints
          value:
            - - name: id
                value: string
        - name: provisioningState
          value: []
        - name: resourceGuid
          value: string
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
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dns_forwarding_rulesets</code> resource.

```sql
/*+ update */
UPDATE azure.dns_resolver.dns_forwarding_rulesets
SET 
dnsResolverOutboundEndpoints = '{{ dnsResolverOutboundEndpoints }}',
tags = '{{ tags }}'
WHERE 
dnsForwardingRulesetName = '{{ dnsForwardingRulesetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>dns_forwarding_rulesets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dns_resolver.dns_forwarding_rulesets
WHERE dnsForwardingRulesetName = '{{ dnsForwardingRulesetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

---
title: virtual_network_links
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_links
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

Creates, updates, deletes, gets or lists a <code>virtual_network_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_network_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns_resolver.virtual_network_links" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_network_links', value: 'view', },
        { label: 'virtual_network_links', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dnsForwardingRulesetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | ETag of the virtual network link. |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualNetworkLinkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_network" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | ETag of the virtual network link. |
| <CopyableCode code="properties" /> | `object` | Represents the properties of a virtual network link. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsForwardingRulesetName, resourceGroupName, subscriptionId, virtualNetworkLinkName" /> | Gets properties of a virtual network link to a DNS forwarding ruleset. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="dnsForwardingRulesetName, resourceGroupName, subscriptionId" /> | Lists virtual network links to a DNS forwarding ruleset. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dnsForwardingRulesetName, resourceGroupName, subscriptionId, virtualNetworkLinkName, data__properties" /> | Creates or updates a virtual network link to a DNS forwarding ruleset. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dnsForwardingRulesetName, resourceGroupName, subscriptionId, virtualNetworkLinkName" /> | Deletes a virtual network link to a DNS forwarding ruleset. WARNING: This operation cannot be undone. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dnsForwardingRulesetName, resourceGroupName, subscriptionId, virtualNetworkLinkName" /> | Updates a virtual network link to a DNS forwarding ruleset. |

## `SELECT` examples

Lists virtual network links to a DNS forwarding ruleset.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_network_links', value: 'view', },
        { label: 'virtual_network_links', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dnsForwardingRulesetName,
etag,
metadata,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
virtualNetworkLinkName,
virtual_network
FROM azure.dns_resolver.vw_virtual_network_links
WHERE dnsForwardingRulesetName = '{{ dnsForwardingRulesetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties,
systemData
FROM azure.dns_resolver.virtual_network_links
WHERE dnsForwardingRulesetName = '{{ dnsForwardingRulesetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_network_links</code> resource.

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
INSERT INTO azure.dns_resolver.virtual_network_links (
dnsForwardingRulesetName,
resourceGroupName,
subscriptionId,
virtualNetworkLinkName,
data__properties,
properties
)
SELECT 
'{{ dnsForwardingRulesetName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualNetworkLinkName }}',
'{{ data__properties }}',
'{{ properties }}'
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
        - name: virtualNetwork
          value:
            - name: id
              value: string
        - name: metadata
          value: object
        - name: provisioningState
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_network_links</code> resource.

```sql
/*+ update */
UPDATE azure.dns_resolver.virtual_network_links
SET 
properties = '{{ properties }}'
WHERE 
dnsForwardingRulesetName = '{{ dnsForwardingRulesetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkLinkName = '{{ virtualNetworkLinkName }}';
```

## `DELETE` example

Deletes the specified <code>virtual_network_links</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dns_resolver.virtual_network_links
WHERE dnsForwardingRulesetName = '{{ dnsForwardingRulesetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkLinkName = '{{ virtualNetworkLinkName }}';
```

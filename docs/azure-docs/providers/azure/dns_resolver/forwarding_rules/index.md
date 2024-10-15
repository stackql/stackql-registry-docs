---
title: forwarding_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - forwarding_rules
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

Creates, updates, deletes, gets or lists a <code>forwarding_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>forwarding_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns_resolver.forwarding_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_forwarding_rules', value: 'view', },
        { label: 'forwarding_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dnsForwardingRulesetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | ETag of the forwarding rule. |
| <CopyableCode code="forwardingRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="forwarding_rule_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_dns_servers" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | ETag of the forwarding rule. |
| <CopyableCode code="properties" /> | `object` | Represents the properties of a forwarding rule within a DNS forwarding ruleset. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsForwardingRulesetName, forwardingRuleName, resourceGroupName, subscriptionId" /> | Gets properties of a forwarding rule in a DNS forwarding ruleset. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="dnsForwardingRulesetName, resourceGroupName, subscriptionId" /> | Lists forwarding rules in a DNS forwarding ruleset. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dnsForwardingRulesetName, forwardingRuleName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a forwarding rule in a DNS forwarding ruleset. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dnsForwardingRulesetName, forwardingRuleName, resourceGroupName, subscriptionId" /> | Deletes a forwarding rule in a DNS forwarding ruleset. WARNING: This operation cannot be undone. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dnsForwardingRulesetName, forwardingRuleName, resourceGroupName, subscriptionId" /> | Updates a forwarding rule in a DNS forwarding ruleset. |

## `SELECT` examples

Lists forwarding rules in a DNS forwarding ruleset.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_forwarding_rules', value: 'view', },
        { label: 'forwarding_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dnsForwardingRulesetName,
domain_name,
etag,
forwardingRuleName,
forwarding_rule_state,
metadata,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
target_dns_servers
FROM azure.dns_resolver.vw_forwarding_rules
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
FROM azure.dns_resolver.forwarding_rules
WHERE dnsForwardingRulesetName = '{{ dnsForwardingRulesetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>forwarding_rules</code> resource.

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
INSERT INTO azure.dns_resolver.forwarding_rules (
dnsForwardingRulesetName,
forwardingRuleName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ dnsForwardingRulesetName }}',
'{{ forwardingRuleName }}',
'{{ resourceGroupName }}',
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
    - name: etag
      value: string
    - name: properties
      value:
        - name: domainName
          value: string
        - name: targetDnsServers
          value:
            - - name: ipAddress
                value: string
              - name: port
                value: integer
        - name: metadata
          value: object
        - name: forwardingRuleState
          value: string
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

Updates a <code>forwarding_rules</code> resource.

```sql
/*+ update */
UPDATE azure.dns_resolver.forwarding_rules
SET 
properties = '{{ properties }}'
WHERE 
dnsForwardingRulesetName = '{{ dnsForwardingRulesetName }}'
AND forwardingRuleName = '{{ forwardingRuleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>forwarding_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dns_resolver.forwarding_rules
WHERE dnsForwardingRulesetName = '{{ dnsForwardingRulesetName }}'
AND forwardingRuleName = '{{ forwardingRuleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

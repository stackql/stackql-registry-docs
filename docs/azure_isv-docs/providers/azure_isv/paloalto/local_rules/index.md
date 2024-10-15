---
title: local_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - local_rules
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

Creates, updates, deletes, gets or lists a <code>local_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.local_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_local_rules', value: 'view', },
        { label: 'local_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="action_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="applications" /> | `text` | field from the `properties` object |
| <CopyableCode code="audit_comment" /> | `text` | field from the `properties` object |
| <CopyableCode code="category" /> | `text` | field from the `properties` object |
| <CopyableCode code="decryption_rule_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_logging" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="inbound_inspection_certificate" /> | `text` | field from the `properties` object |
| <CopyableCode code="localRulestackName" /> | `text` | field from the `properties` object |
| <CopyableCode code="negate_destination" /> | `text` | field from the `properties` object |
| <CopyableCode code="negate_source" /> | `text` | field from the `properties` object |
| <CopyableCode code="priority" /> | `text` | field from the `properties` object |
| <CopyableCode code="protocol" /> | `text` | field from the `properties` object |
| <CopyableCode code="protocol_port_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rule_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="rule_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | definition of rule |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="localRulestackName, priority, resourceGroupName, subscriptionId" /> | Get a LocalRulesResource |
| <CopyableCode code="list_by_local_rulestacks" /> | `SELECT` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | List LocalRulesResource resources by LocalRulestacks |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="localRulestackName, priority, resourceGroupName, subscriptionId, data__properties" /> | Create a LocalRulesResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="localRulestackName, priority, resourceGroupName, subscriptionId" /> | Delete a LocalRulesResource |
| <CopyableCode code="refresh_counters" /> | `EXEC` | <CopyableCode code="localRulestackName, priority, resourceGroupName, subscriptionId" /> | Refresh counters |
| <CopyableCode code="reset_counters" /> | `EXEC` | <CopyableCode code="localRulestackName, priority, resourceGroupName, subscriptionId" /> | Reset counters |

## `SELECT` examples

List LocalRulesResource resources by LocalRulestacks

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_local_rules', value: 'view', },
        { label: 'local_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
action_type,
applications,
audit_comment,
category,
decryption_rule_type,
destination,
enable_logging,
etag,
inbound_inspection_certificate,
localRulestackName,
negate_destination,
negate_source,
priority,
protocol,
protocol_port_list,
provisioning_state,
resourceGroupName,
rule_name,
rule_state,
source,
subscriptionId,
system_data,
tags
FROM azure_isv.paloalto.vw_local_rules
WHERE localRulestackName = '{{ localRulestackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure_isv.paloalto.local_rules
WHERE localRulestackName = '{{ localRulestackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>local_rules</code> resource.

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
INSERT INTO azure_isv.paloalto.local_rules (
localRulestackName,
priority,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ localRulestackName }}',
'{{ priority }}',
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
    - name: properties
      value:
        - name: etag
          value: string
        - name: ruleName
          value: string
        - name: priority
          value: integer
        - name: description
          value: string
        - name: ruleState
          value: []
        - name: source
          value:
            - name: cidrs
              value:
                - string
            - name: countries
              value:
                - string
            - name: feeds
              value:
                - string
            - name: prefixLists
              value:
                - string
        - name: negateSource
          value: []
        - name: destination
          value:
            - name: cidrs
              value:
                - string
            - name: countries
              value:
                - string
            - name: feeds
              value:
                - string
            - name: prefixLists
              value:
                - string
            - name: fqdnLists
              value:
                - string
        - name: applications
          value:
            - string
        - name: category
          value:
            - name: urlCustom
              value:
                - string
            - name: feeds
              value:
                - string
        - name: protocol
          value: string
        - name: protocolPortList
          value:
            - string
        - name: inboundInspectionCertificate
          value: string
        - name: auditComment
          value: string
        - name: actionType
          value: []
        - name: decryptionRuleType
          value: []
        - name: tags
          value:
            - - name: key
                value: string
              - name: value
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

## `DELETE` example

Deletes the specified <code>local_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.paloalto.local_rules
WHERE localRulestackName = '{{ localRulestackName }}'
AND priority = '{{ priority }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

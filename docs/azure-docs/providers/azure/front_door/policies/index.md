---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - front_door
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

Creates, updates, deletes, gets or lists a <code>policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.front_door.policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_policies', value: 'view', },
        { label: 'policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="custom_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Gets a unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="frontend_endpoint_links" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="managed_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="policyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="routing_rule_links" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_policy_links" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The pricing tier of the web application firewall policy. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | Gets a unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Defines web application firewall policy properties. |
| <CopyableCode code="sku" /> | `object` | The pricing tier of the web application firewall policy. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Retrieve protection policy with specified name within a resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the protection policies within a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the protection policies within a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Create or update policy with specified rule set name within a resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Deletes Policy |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Patch a specific frontdoor webApplicationFirewall policy for tags update under the specified subscription and resource group. |

## `SELECT` examples

Lists all of the protection policies within a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_policies', value: 'view', },
        { label: 'policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
custom_rules,
etag,
frontend_endpoint_links,
location,
managed_rules,
policyName,
policy_settings,
provisioning_state,
resourceGroupName,
resource_state,
routing_rule_links,
security_policy_links,
sku,
subscriptionId,
tags,
type
FROM azure.front_door.vw_policies
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
sku,
tags,
type
FROM azure.front_door.policies
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policies</code> resource.

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
INSERT INTO azure.front_door.policies (
policyName,
resourceGroupName,
subscriptionId,
properties,
etag,
sku,
location,
tags
)
SELECT 
'{{ policyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ etag }}',
'{{ sku }}',
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
        - name: policySettings
          value:
            - name: enabledState
              value: string
            - name: mode
              value: string
            - name: redirectUrl
              value: string
            - name: customBlockResponseStatusCode
              value: integer
            - name: customBlockResponseBody
              value: string
            - name: requestBodyCheck
              value: string
            - name: javascriptChallengeExpirationInMinutes
              value: integer
            - name: logScrubbing
              value:
                - name: state
                  value: string
                - name: scrubbingRules
                  value:
                    - - name: matchVariable
                        value: string
                      - name: selectorMatchOperator
                        value: string
                      - name: selector
                        value: string
                      - name: state
                        value: string
        - name: customRules
          value:
            - name: rules
              value:
                - - name: name
                    value: string
                  - name: priority
                    value: integer
                  - name: enabledState
                    value: string
                  - name: ruleType
                    value: string
                  - name: rateLimitDurationInMinutes
                    value: integer
                  - name: rateLimitThreshold
                    value: integer
                  - name: groupBy
                    value:
                      - - name: variableName
                          value: string
                  - name: matchConditions
                    value:
                      - - name: matchVariable
                          value: string
                        - name: selector
                          value: string
                        - name: operator
                          value: string
                        - name: negateCondition
                          value: boolean
                        - name: matchValue
                          value:
                            - string
                        - name: transforms
                          value:
                            - []
                  - name: action
                    value: []
        - name: managedRules
          value:
            - name: managedRuleSets
              value:
                - - name: ruleSetType
                    value: string
                  - name: ruleSetVersion
                    value: string
                  - name: ruleSetAction
                    value: []
                  - name: exclusions
                    value:
                      - - name: matchVariable
                          value: string
                        - name: selectorMatchOperator
                          value: string
                        - name: selector
                          value: string
                  - name: ruleGroupOverrides
                    value:
                      - - name: ruleGroupName
                          value: string
                        - name: exclusions
                          value:
                            - - name: matchVariable
                                value: string
                              - name: selectorMatchOperator
                                value: string
                              - name: selector
                                value: string
                        - name: rules
                          value:
                            - - name: ruleId
                                value: string
                              - name: enabledState
                                value: []
                              - name: exclusions
                                value:
                                  - - name: matchVariable
                                      value: string
                                    - name: selectorMatchOperator
                                      value: string
                                    - name: selector
                                      value: string
        - name: frontendEndpointLinks
          value:
            - - name: id
                value: string
        - name: routingRuleLinks
          value:
            - - name: id
                value: string
        - name: securityPolicyLinks
          value:
            - - name: id
                value: string
        - name: provisioningState
          value: string
        - name: resourceState
          value: string
    - name: etag
      value: string
    - name: sku
      value:
        - name: name
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

## `UPDATE` example

Updates a <code>policies</code> resource.

```sql
/*+ update */
UPDATE azure.front_door.policies
SET 
tags = '{{ tags }}'
WHERE 
policyName = '{{ policyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.front_door.policies
WHERE policyName = '{{ policyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

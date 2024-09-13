---
title: security_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - security_actions
  - apigee
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

Creates, updates, deletes or gets an <code>security_action</code> resource or lists <code>security_actions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.security_actions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. This field is ignored during creation as per AIP-133. Please set the `security_action_id` field in the CreateSecurityActionRequest when creating a new SecurityAction. Format: organizations/{org}/environments/{env}/securityActions/{security_action} |
| <CopyableCode code="description" /> | `string` | Optional. An optional user provided description of the SecurityAction. |
| <CopyableCode code="allow" /> | `object` | Message that should be set in case of an Allow Action. This does not have any fields. |
| <CopyableCode code="apiProxies" /> | `array` | Optional. If unset, this would apply to all proxies in the environment. If set, this action is enforced only if at least one proxy in the repeated list is deployed at the time of enforcement. If set, several restrictions are enforced on SecurityActions. There can be at most 100 enabled actions with proxies set in an env. Several other restrictions apply on conditions and are detailed later. |
| <CopyableCode code="conditionConfig" /> | `object` | The following are a list of conditions. A valid SecurityAction must contain at least one condition. Within a condition, each element is ORed. Across conditions elements are ANDed. For example if a SecurityAction has the following: ip_address_ranges: ["ip1", "ip2"] and bot_reasons: ["Flooder", "Robot Abuser"] then this is interpreted as: enforce the action if the incoming request has ((ip_address_ranges = "ip1" OR ip_address_ranges = "ip2") AND (bot_reasons="Flooder" OR bot_reasons="Robot Abuser")). Conditions other than ip_address_ranges and bot_reasons cannot be ANDed. |
| <CopyableCode code="createTime" /> | `string` | Output only. The create time for this SecurityAction. |
| <CopyableCode code="deny" /> | `object` | Message that should be set in case of a Deny Action. |
| <CopyableCode code="expireTime" /> | `string` | The expiration for this SecurityAction. |
| <CopyableCode code="flag" /> | `object` | The message that should be set in the case of a Flag action. |
| <CopyableCode code="state" /> | `string` | Required. Only an ENABLED SecurityAction is enforced. An ENABLED SecurityAction past its expiration time will not be enforced. |
| <CopyableCode code="ttl" /> | `string` | Input only. The TTL for this SecurityAction. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The update time for this SecurityAction. This reflects when this SecurityAction changed states. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_security_actions_get" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId, securityActionsId" /> | Get a SecurityAction by name. |
| <CopyableCode code="organizations_environments_security_actions_list" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId" /> | Returns a list of SecurityActions. This returns both enabled and disabled actions. |
| <CopyableCode code="organizations_environments_security_actions_create" /> | `INSERT` | <CopyableCode code="environmentsId, organizationsId" /> | CreateSecurityAction creates a SecurityAction. |
| <CopyableCode code="organizations_environments_security_actions_disable" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId, securityActionsId" /> | Disable a SecurityAction. The `state` of the SecurityAction after disabling is `DISABLED`. `DisableSecurityAction` can be called on SecurityActions in the state `ENABLED`; SecurityActions in a different state (including `DISABLED`) return an error. |
| <CopyableCode code="organizations_environments_security_actions_enable" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId, securityActionsId" /> | Enable a SecurityAction. The `state` of the SecurityAction after enabling is `ENABLED`. `EnableSecurityAction` can be called on SecurityActions in the state `DISABLED`; SecurityActions in a different state (including `ENABLED) return an error. |

## `SELECT` examples

Returns a list of SecurityActions. This returns both enabled and disabled actions.

```sql
SELECT
name,
description,
allow,
apiProxies,
conditionConfig,
createTime,
deny,
expireTime,
flag,
state,
ttl,
updateTime
FROM google.apigee.security_actions
WHERE environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_actions</code> resource.

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
INSERT INTO google.apigee.security_actions (
environmentsId,
organizationsId,
apiProxies,
createTime,
updateTime,
name,
description,
conditionConfig,
deny,
state,
ttl,
allow,
flag,
expireTime
)
SELECT 
'{{ environmentsId }}',
'{{ organizationsId }}',
'{{ apiProxies }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ name }}',
'{{ description }}',
'{{ conditionConfig }}',
'{{ deny }}',
'{{ state }}',
'{{ ttl }}',
'{{ allow }}',
'{{ flag }}',
'{{ expireTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: apiProxies
        value: '{{ apiProxies }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: conditionConfig
        value: '{{ conditionConfig }}'
      - name: deny
        value: '{{ deny }}'
      - name: state
        value: '{{ state }}'
      - name: ttl
        value: '{{ ttl }}'
      - name: allow
        value: '{{ allow }}'
      - name: flag
        value: '{{ flag }}'
      - name: expireTime
        value: '{{ expireTime }}'

```
</TabItem>
</Tabs>

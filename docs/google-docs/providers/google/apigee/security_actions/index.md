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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.security_actions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. This field is ignored during creation as per AIP-133. Please set the `security_action_id` field in the CreateSecurityActionRequest when creating a new SecurityAction. Format: organizations/&#123;org&#125;/environments/&#123;env&#125;/securityActions/&#123;security_action&#125; |
| <CopyableCode code="description" /> | `string` | Optional. An optional user provided description of the SecurityAction. |
| <CopyableCode code="allow" /> | `object` | Message that should be set in case of an Allow Action. This does not have any fields. |
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
| <CopyableCode code="_organizations_environments_security_actions_list" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId" /> | Returns a list of SecurityActions. This returns both enabled and disabled actions. |
| <CopyableCode code="organizations_environments_security_actions_disable" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId, securityActionsId" /> | Disable a SecurityAction. The `state` of the SecurityAction after disabling is `DISABLED`. `DisableSecurityAction` can be called on SecurityActions in the state `ENABLED`; SecurityActions in a different state (including `DISABLED`) return an error. |
| <CopyableCode code="organizations_environments_security_actions_enable" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId, securityActionsId" /> | Enable a SecurityAction. The `state` of the SecurityAction after enabling is `ENABLED`. `EnableSecurityAction` can be called on SecurityActions in the state `DISABLED`; SecurityActions in a different state (including `ENABLED) return an error. |

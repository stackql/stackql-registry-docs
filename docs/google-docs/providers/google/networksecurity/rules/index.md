---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - networksecurity
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
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Immutable. Name of the resource. ame is the full resource name so projects/&#123;project&#125;/locations/&#123;location&#125;/gatewaySecurityPolicies/&#123;gateway_security_policy&#125;/rules/&#123;rule&#125; rule should match the pattern: (^[a-z]([a-z0-9-]&#123;0,61&#125;[a-z0-9])?$). |
| <CopyableCode code="description" /> | `string` | Optional. Free-text description of the resource. |
| <CopyableCode code="applicationMatcher" /> | `string` | Optional. CEL expression for matching on L7/application level criteria. |
| <CopyableCode code="basicProfile" /> | `string` | Required. Profile which tells what the primitive action should be. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the rule was created. |
| <CopyableCode code="enabled" /> | `boolean` | Required. Whether the rule is enforced. |
| <CopyableCode code="priority" /> | `integer` | Required. Priority of the rule. Lower number corresponds to higher precedence. |
| <CopyableCode code="sessionMatcher" /> | `string` | Required. CEL expression for matching on session criteria. |
| <CopyableCode code="tlsInspectionEnabled" /> | `boolean` | Optional. Flag to enable TLS inspection of traffic matching on , can only be true if the parent GatewaySecurityPolicy references a TLSInspectionConfig. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the rule was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_gateway_security_policies_rules_get" /> | `SELECT` | <CopyableCode code="gatewaySecurityPoliciesId, locationsId, projectsId, rulesId" /> | Gets details of a single GatewaySecurityPolicyRule. |
| <CopyableCode code="projects_locations_gateway_security_policies_rules_list" /> | `SELECT` | <CopyableCode code="gatewaySecurityPoliciesId, locationsId, projectsId" /> | Lists GatewaySecurityPolicyRules in a given project and location. |
| <CopyableCode code="projects_locations_gateway_security_policies_rules_create" /> | `INSERT` | <CopyableCode code="gatewaySecurityPoliciesId, locationsId, projectsId" /> | Creates a new GatewaySecurityPolicy in a given project and location. |
| <CopyableCode code="projects_locations_gateway_security_policies_rules_delete" /> | `DELETE` | <CopyableCode code="gatewaySecurityPoliciesId, locationsId, projectsId, rulesId" /> | Deletes a single GatewaySecurityPolicyRule. |
| <CopyableCode code="projects_locations_gateway_security_policies_rules_patch" /> | `UPDATE` | <CopyableCode code="gatewaySecurityPoliciesId, locationsId, projectsId, rulesId" /> | Updates the parameters of a single GatewaySecurityPolicyRule. |
| <CopyableCode code="_projects_locations_gateway_security_policies_rules_list" /> | `EXEC` | <CopyableCode code="gatewaySecurityPoliciesId, locationsId, projectsId" /> | Lists GatewaySecurityPolicyRules in a given project and location. |

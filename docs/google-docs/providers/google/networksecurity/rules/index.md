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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networksecurity.rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Immutable. Name of the resource. ame is the full resource name so projects/&#123;project&#125;/locations/&#123;location&#125;/gatewaySecurityPolicies/&#123;gateway_security_policy&#125;/rules/&#123;rule&#125; rule should match the pattern: (^[a-z]([a-z0-9-]&#123;0,61&#125;[a-z0-9])?$). |
| `description` | `string` | Optional. Free-text description of the resource. |
| `sessionMatcher` | `string` | Required. CEL expression for matching on session criteria. |
| `createTime` | `string` | Output only. Time when the rule was created. |
| `tlsInspectionEnabled` | `boolean` | Optional. Flag to enable TLS inspection of traffic matching on , can only be true if the parent GatewaySecurityPolicy references a TLSInspectionConfig. |
| `basicProfile` | `string` | Required. Profile which tells what the primitive action should be. |
| `updateTime` | `string` | Output only. Time when the rule was updated. |
| `priority` | `integer` | Required. Priority of the rule. Lower number corresponds to higher precedence. |
| `applicationMatcher` | `string` | Optional. CEL expression for matching on L7/application level criteria. |
| `enabled` | `boolean` | Required. Whether the rule is enforced. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_gateway_security_policies_rules_get` | `SELECT` | `gatewaySecurityPoliciesId, locationsId, projectsId, rulesId` | Gets details of a single GatewaySecurityPolicyRule. |
| `projects_locations_gateway_security_policies_rules_list` | `SELECT` | `gatewaySecurityPoliciesId, locationsId, projectsId` | Lists GatewaySecurityPolicyRules in a given project and location. |
| `projects_locations_gateway_security_policies_rules_create` | `INSERT` | `gatewaySecurityPoliciesId, locationsId, projectsId` | Creates a new GatewaySecurityPolicy in a given project and location. |
| `projects_locations_gateway_security_policies_rules_delete` | `DELETE` | `gatewaySecurityPoliciesId, locationsId, projectsId, rulesId` | Deletes a single GatewaySecurityPolicyRule. |
| `_projects_locations_gateway_security_policies_rules_list` | `EXEC` | `gatewaySecurityPoliciesId, locationsId, projectsId` | Lists GatewaySecurityPolicyRules in a given project and location. |
| `projects_locations_gateway_security_policies_rules_patch` | `EXEC` | `gatewaySecurityPoliciesId, locationsId, projectsId, rulesId` | Updates the parameters of a single GatewaySecurityPolicyRule. |

---
title: gateway_security_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_security_policies
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
<tr><td><b>Name</b></td><td><code>gateway_security_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networksecurity.gateway_security_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the resource. Name is of the form projects/&#123;project&#125;/locations/&#123;location&#125;/gatewaySecurityPolicies/&#123;gateway_security_policy&#125; gateway_security_policy should match the pattern:(^[a-z]([a-z0-9-]&#123;0,61&#125;[a-z0-9])?$). |
| `description` | `string` | Optional. Free-text description of the resource. |
| `tlsInspectionPolicy` | `string` | Optional. Name of a TLS Inspection Policy resource that defines how TLS inspection will be performed for any rule(s) which enables it. |
| `updateTime` | `string` | Output only. The timestamp when the resource was updated. |
| `createTime` | `string` | Output only. The timestamp when the resource was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_gateway_security_policies_get` | `SELECT` | `gatewaySecurityPoliciesId, locationsId, projectsId` | Gets details of a single GatewaySecurityPolicy. |
| `projects_locations_gateway_security_policies_list` | `SELECT` | `locationsId, projectsId` | Lists GatewaySecurityPolicies in a given project and location. |
| `projects_locations_gateway_security_policies_create` | `INSERT` | `locationsId, projectsId` | Creates a new GatewaySecurityPolicy in a given project and location. |
| `projects_locations_gateway_security_policies_delete` | `DELETE` | `gatewaySecurityPoliciesId, locationsId, projectsId` | Deletes a single GatewaySecurityPolicy. |
| `_projects_locations_gateway_security_policies_list` | `EXEC` | `locationsId, projectsId` | Lists GatewaySecurityPolicies in a given project and location. |
| `projects_locations_gateway_security_policies_patch` | `EXEC` | `gatewaySecurityPoliciesId, locationsId, projectsId` | Updates the parameters of a single GatewaySecurityPolicy. |

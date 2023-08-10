---
title: tls_inspection_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - tls_inspection_policies
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
<tr><td><b>Name</b></td><td><code>tls_inspection_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networksecurity.tls_inspection_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the resource. Name is of the form projects/&#123;project&#125;/locations/&#123;location&#125;/tlsInspectionPolicies/&#123;tls_inspection_policy&#125; tls_inspection_policy should match the pattern:(^[a-z]([a-z0-9-]&#123;0,61&#125;[a-z0-9])?$). |
| `description` | `string` | Optional. Free-text description of the resource. |
| `createTime` | `string` | Output only. The timestamp when the resource was created. |
| `customTlsFeatures` | `array` | Optional. List of custom TLS cipher suites selected. This field is valid only if the selected tls_feature_profile is CUSTOM. The compute.SslPoliciesService.ListAvailableFeatures method returns the set of features that can be specified in this list. Note that Secure Web Proxy does not yet honor this field. |
| `updateTime` | `string` | Output only. The timestamp when the resource was updated. |
| `minTlsVersion` | `string` | Optional. Minimum TLS version that the firewall should use when negotiating connections with both clients and servers. If this is not set, then the default value is to allow the broadest set of clients and servers (TLS 1.0 or higher). Setting this to more restrictive values may improve security, but may also prevent the firewall from connecting to some clients or servers. Note that Secure Web Proxy does not yet honor this field. |
| `excludePublicCaSet` | `boolean` | Optional. If FALSE (the default), use our default set of public CAs in addition to any CAs specified in trust_config. These public CAs are currently based on the Mozilla Root Program and are subject to change over time. If TRUE, do not accept our default set of public CAs. Only CAs specified in trust_config will be accepted. This defaults to FALSE (use public CAs in addition to trust_config) for backwards compatibility, but trusting public root CAs is *not recommended* unless the traffic in question is outbound to public web servers. When possible, prefer setting this to "false" and explicitly specifying trusted CAs and certificates in a TrustConfig. Note that Secure Web Proxy does not yet honor this field. |
| `trustConfig` | `string` | Optional. A TrustConfig resource used when making a connection to the TLS server. This is a relative resource path following the form "projects/&#123;project&#125;/locations/&#123;location&#125;/trustConfigs/&#123;trust_config&#125;". This is necessary to intercept TLS connections to servers with certificates signed by a private CA or self-signed certificates. Note that Secure Web Proxy does not yet honor this field. |
| `caPool` | `string` | Required. A CA pool resource used to issue interception certificates. The CA pool string has a relative resource path following the form "projects/&#123;project&#125;/locations/&#123;location&#125;/caPools/&#123;ca_pool&#125;". |
| `tlsFeatureProfile` | `string` | Optional. The selected Profile. If this is not set, then the default value is to allow the broadest set of clients and servers ("PROFILE_COMPATIBLE"). Setting this to more restrictive values may improve security, but may also prevent the TLS inspection proxy from connecting to some clients or servers. Note that Secure Web Proxy does not yet honor this field. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_tls_inspection_policies_get` | `SELECT` | `locationsId, projectsId, tlsInspectionPoliciesId` | Gets details of a single TlsInspectionPolicy. |
| `projects_locations_tls_inspection_policies_list` | `SELECT` | `locationsId, projectsId` | Lists TlsInspectionPolicies in a given project and location. |
| `projects_locations_tls_inspection_policies_create` | `INSERT` | `locationsId, projectsId` | Creates a new TlsInspectionPolicy in a given project and location. |
| `projects_locations_tls_inspection_policies_delete` | `DELETE` | `locationsId, projectsId, tlsInspectionPoliciesId` | Deletes a single TlsInspectionPolicy. |
| `_projects_locations_tls_inspection_policies_list` | `EXEC` | `locationsId, projectsId` | Lists TlsInspectionPolicies in a given project and location. |
| `projects_locations_tls_inspection_policies_patch` | `EXEC` | `locationsId, projectsId, tlsInspectionPoliciesId` | Updates the parameters of a single TlsInspectionPolicy. |

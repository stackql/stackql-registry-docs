---
title: inbound_saml_sso_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - inbound_saml_sso_profiles
  - cloudidentity
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
<tr><td><b>Name</b></td><td><code>inbound_saml_sso_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudidentity.inbound_saml_sso_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the SAML SSO profile. |
| `customer` | `string` | Immutable. The customer. For example: `customers/C0123abc`. |
| `displayName` | `string` | Human-readable name of the SAML SSO profile. |
| `idpConfig` | `object` | SAML IDP (identity provider) configuration. |
| `spConfig` | `object` | SAML SP (service provider) configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `inboundSamlSsoProfilesId` | Gets an InboundSamlSsoProfile. |
| `list` | `SELECT` |  | Lists InboundSamlSsoProfiles for a customer. |
| `create` | `INSERT` |  | Creates an InboundSamlSsoProfile for a customer. |
| `delete` | `DELETE` | `inboundSamlSsoProfilesId` | Deletes an InboundSamlSsoProfile. |
| `_list` | `EXEC` |  | Lists InboundSamlSsoProfiles for a customer. |
| `patch` | `EXEC` | `inboundSamlSsoProfilesId` | Updates an InboundSamlSsoProfile. |

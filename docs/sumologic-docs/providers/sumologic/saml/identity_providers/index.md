---
title: identity_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_providers
  - saml
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.saml.identity_providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier of the SAML Identity Provider. |
| `authnRequestUrl` | `string` | The URL that the identity provider has assigned for Sumo Logic to submit SAML authentication requests to the identity provider. |
| `onDemandProvisioningEnabled` | `object` |  |
| `entityId` | `string` | A unique identifier that is the intended audience of the SAML assertion. |
| `x509cert2` | `string` | The backup certificate used to verify the signature in SAML assertions when x509cert1 expires. |
| `x509cert1` | `string` | The certificate is used to verify the signature in SAML assertions. |
| `spInitiatedLoginEnabled` | `boolean` | True if Sumo Logic redirects users to your identity provider with a SAML AuthnRequest when signing in. |
| `rolesAttribute` | `string` | The role that Sumo Logic will assign to users when they sign in. |
| `disableRequestedAuthnContext` | `boolean` | True if Sumo Logic will include the RequestedAuthnContext element of the SAML AuthnRequests it sends to the identity provider. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `signAuthnRequest` | `boolean` | True if Sumo Logic will send signed Authn requests to the identity provider. |
| `issuer` | `string` | The unique URL assigned to the organization by the SAML Identity Provider. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `logoutUrl` | `string` | The URL that users will be redirected to after signing out of Sumo Logic. |
| `assertionConsumerUrl` | `string` | The URL on Sumo Logic where the IdP will redirect to with its authentication response. |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `certificate` | `string` | Authentication Request Signing Certificate for the user. |
| `x509cert3` | `string` | The backup certificate used to verify the signature in SAML assertions when x509cert1 expires and x509cert2 is empty. |
| `spInitiatedLoginPath` | `string` | This property has been deprecated and is no longer used. |
| `emailAttribute` | `string` | The email address of the new user account. |
| `debugMode` | `boolean` | True if additional details are included when a user fails to sign in. |
| `configurationName` | `string` | Name of the SSO policy or another name used to describe the policy internally. |
| `logoutEnabled` | `boolean` | True if users are redirected to a URL after signing out of Sumo Logic. |
| `isRedirectBinding` | `boolean` | True if the SAML binding is of HTTP Redirect type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getIdentityProviders` | `SELECT` | `region` | Get a list of all SAML configurations in the organization. |
| `createIdentityProvider` | `INSERT` | `data__configurationName, data__issuer, data__x509cert1, region` | Create a new SAML configuration in the organization. |
| `deleteIdentityProvider` | `DELETE` | `id, region` | Delete a SAML configuration with the given identifier from the organization. |
| `updateIdentityProvider` | `EXEC` | `id, data__configurationName, data__issuer, data__x509cert1, region` | Update an existing SAML configuration in the organization. |

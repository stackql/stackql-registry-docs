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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.saml.identity_providers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier of the SAML Identity Provider. |
| <CopyableCode code="assertionConsumerUrl" /> | `string` | The URL on Sumo Logic where the IdP will redirect to with its authentication response. |
| <CopyableCode code="authnRequestUrl" /> | `string` | The URL that the identity provider has assigned for Sumo Logic to submit SAML authentication requests to the identity provider. |
| <CopyableCode code="certificate" /> | `string` | Authentication Request Signing Certificate for the user. |
| <CopyableCode code="configurationName" /> | `string` | Name of the SSO policy or another name used to describe the policy internally. |
| <CopyableCode code="createdAt" /> | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| <CopyableCode code="createdBy" /> | `string` | Identifier of the user who created the resource. |
| <CopyableCode code="debugMode" /> | `boolean` | True if additional details are included when a user fails to sign in. |
| <CopyableCode code="disableRequestedAuthnContext" /> | `boolean` | True if Sumo Logic will include the RequestedAuthnContext element of the SAML AuthnRequests it sends to the identity provider. |
| <CopyableCode code="emailAttribute" /> | `string` | The email address of the new user account. |
| <CopyableCode code="entityId" /> | `string` | A unique identifier that is the intended audience of the SAML assertion. |
| <CopyableCode code="isRedirectBinding" /> | `boolean` | True if the SAML binding is of HTTP Redirect type. |
| <CopyableCode code="issuer" /> | `string` | The unique URL assigned to the organization by the SAML Identity Provider. |
| <CopyableCode code="logoutEnabled" /> | `boolean` | True if users are redirected to a URL after signing out of Sumo Logic. |
| <CopyableCode code="logoutUrl" /> | `string` | The URL that users will be redirected to after signing out of Sumo Logic. |
| <CopyableCode code="modifiedAt" /> | `string` | Last modification timestamp in UTC. |
| <CopyableCode code="modifiedBy" /> | `string` | Identifier of the user who last modified the resource. |
| <CopyableCode code="onDemandProvisioningEnabled" /> | `object` |  |
| <CopyableCode code="rolesAttribute" /> | `string` | The role that Sumo Logic will assign to users when they sign in. |
| <CopyableCode code="signAuthnRequest" /> | `boolean` | True if Sumo Logic will send signed Authn requests to the identity provider. |
| <CopyableCode code="spInitiatedLoginEnabled" /> | `boolean` | True if Sumo Logic redirects users to your identity provider with a SAML AuthnRequest when signing in. |
| <CopyableCode code="spInitiatedLoginPath" /> | `string` | This property has been deprecated and is no longer used. |
| <CopyableCode code="x509cert1" /> | `string` | The certificate is used to verify the signature in SAML assertions. |
| <CopyableCode code="x509cert2" /> | `string` | The backup certificate used to verify the signature in SAML assertions when x509cert1 expires. |
| <CopyableCode code="x509cert3" /> | `string` | The backup certificate used to verify the signature in SAML assertions when x509cert1 expires and x509cert2 is empty. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getIdentityProviders" /> | `SELECT` | <CopyableCode code="region" /> | Get a list of all SAML configurations in the organization. |
| <CopyableCode code="createIdentityProvider" /> | `INSERT` | <CopyableCode code="data__configurationName, data__issuer, data__x509cert1, region" /> | Create a new SAML configuration in the organization. |
| <CopyableCode code="deleteIdentityProvider" /> | `DELETE` | <CopyableCode code="id, region" /> | Delete a SAML configuration with the given identifier from the organization. |
| <CopyableCode code="updateIdentityProvider" /> | `EXEC` | <CopyableCode code="id, data__configurationName, data__issuer, data__x509cert1, region" /> | Update an existing SAML configuration in the organization. |

---
title: relyingparty__project_config
hide_title: false
hide_table_of_contents: false
keywords:
  - relyingparty__project_config
  - identitytoolkit
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
<tr><td><b>Name</b></td><td><code>relyingparty__project_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.identitytoolkit.relyingparty__project_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `changeEmailTemplate` | `object` | Template for an email template. |
| `dynamicLinksDomain` | `string` |  |
| `useEmailSending` | `boolean` | Whether to use email sending provided by Firebear. |
| `authorizedDomains` | `array` | Authorized domains. |
| `idpConfig` | `array` | OAuth2 provider configuration. |
| `apiKey` | `string` | Browser API key, needed when making http request to Apiary. |
| `resetPasswordTemplate` | `object` | Template for an email template. |
| `verifyEmailTemplate` | `object` | Template for an email template. |
| `allowPasswordUser` | `boolean` | Whether to allow password user sign in or sign up. |
| `projectId` | `string` | Project ID of the relying party. |
| `enableAnonymousUser` | `boolean` | Whether anonymous user is enabled. |
| `legacyResetPasswordTemplate` | `object` | Template for an email template. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `relyingparty_getProjectConfig` | `SELECT` |  |

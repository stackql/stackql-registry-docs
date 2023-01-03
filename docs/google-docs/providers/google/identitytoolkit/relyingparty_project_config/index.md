---
title: relyingparty_project_config
hide_title: false
hide_table_of_contents: false
keywords:
  - relyingparty_project_config
  - identitytoolkit
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>relyingparty_project_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.identitytoolkit.relyingparty_project_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `projectId` | `string` | Project ID of the relying party. |
| `dynamicLinksDomain` | `string` |  |
| `legacyResetPasswordTemplate` | `object` | Template for an email template. |
| `changeEmailTemplate` | `object` | Template for an email template. |
| `useEmailSending` | `boolean` | Whether to use email sending provided by Firebear. |
| `allowPasswordUser` | `boolean` | Whether to allow password user sign in or sign up. |
| `enableAnonymousUser` | `boolean` | Whether anonymous user is enabled. |
| `authorizedDomains` | `array` | Authorized domains. |
| `resetPasswordTemplate` | `object` | Template for an email template. |
| `verifyEmailTemplate` | `object` | Template for an email template. |
| `idpConfig` | `array` | OAuth2 provider configuration. |
| `apiKey` | `string` | Browser API key, needed when making http request to Apiary. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `relyingparty_getProjectConfig` | `SELECT` |  |

---
title: idp_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - idp_credentials
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
<tr><td><b>Name</b></td><td><code>idp_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudidentity.idp_credentials</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the credential. |
| `updateTime` | `string` | Output only. Time when the `IdpCredential` was last updated. |
| `dsaKeyInfo` | `object` | Information of a DSA public key. |
| `rsaKeyInfo` | `object` | Information of a RSA public key. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `idpCredentialsId, inboundSamlSsoProfilesId` | Gets an IdpCredential. |
| `list` | `SELECT` | `inboundSamlSsoProfilesId` | Returns a list of IdpCredentials in an InboundSamlSsoProfile. |
| `delete` | `DELETE` | `idpCredentialsId, inboundSamlSsoProfilesId` | Deletes an IdpCredential. |
| `_list` | `EXEC` | `inboundSamlSsoProfilesId` | Returns a list of IdpCredentials in an InboundSamlSsoProfile. |
| `add` | `EXEC` | `inboundSamlSsoProfilesId` | Adds an IdpCredential. Up to 2 credentials are allowed. |

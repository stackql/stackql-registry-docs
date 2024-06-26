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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>idp_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudidentity.idp_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the credential. |
| <CopyableCode code="dsaKeyInfo" /> | `object` | Information of a DSA public key. |
| <CopyableCode code="rsaKeyInfo" /> | `object` | Information of a RSA public key. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the `IdpCredential` was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="idpCredentialsId, inboundSamlSsoProfilesId" /> | Gets an IdpCredential. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="inboundSamlSsoProfilesId" /> | Returns a list of IdpCredentials in an InboundSamlSsoProfile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="idpCredentialsId, inboundSamlSsoProfilesId" /> | Deletes an IdpCredential. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="inboundSamlSsoProfilesId" /> | Returns a list of IdpCredentials in an InboundSamlSsoProfile. |
| <CopyableCode code="add" /> | `EXEC` | <CopyableCode code="inboundSamlSsoProfilesId" /> | Adds an IdpCredential. Up to 2 credentials are allowed. |

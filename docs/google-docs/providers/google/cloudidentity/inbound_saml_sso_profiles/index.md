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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inbound_saml_sso_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudidentity.inbound_saml_sso_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the SAML SSO profile. |
| <CopyableCode code="customer" /> | `string` | Immutable. The customer. For example: `customers/C0123abc`. |
| <CopyableCode code="displayName" /> | `string` | Human-readable name of the SAML SSO profile. |
| <CopyableCode code="idpConfig" /> | `object` | SAML IDP (identity provider) configuration. |
| <CopyableCode code="spConfig" /> | `object` | SAML SP (service provider) configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="inboundSamlSsoProfilesId" /> | Gets an InboundSamlSsoProfile. |
| <CopyableCode code="list" /> | `SELECT` |  | Lists InboundSamlSsoProfiles for a customer. |
| <CopyableCode code="create" /> | `INSERT` |  | Creates an InboundSamlSsoProfile for a customer. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="inboundSamlSsoProfilesId" /> | Deletes an InboundSamlSsoProfile. |
| <CopyableCode code="_list" /> | `EXEC` |  | Lists InboundSamlSsoProfiles for a customer. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="inboundSamlSsoProfilesId" /> | Updates an InboundSamlSsoProfile. |

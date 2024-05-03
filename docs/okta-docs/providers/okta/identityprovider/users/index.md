---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - identityprovider
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.identityprovider.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="_embedded" /> | `object` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="externalId" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="profile" /> | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="idpId, userId, subdomain" /> | Fetches a linked IdP user by ID |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="idpId, subdomain" /> | Find all the users linked to an identity provider |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="idpId, userId, subdomain" /> | Links an Okta user to an existing Social Identity Provider. This does not support the SAML2 Identity Provider Type |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="idpId, userId, subdomain" /> | Removes the link between the Okta user and the IdP user. |

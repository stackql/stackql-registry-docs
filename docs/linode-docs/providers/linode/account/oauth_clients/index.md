---
title: oauth_clients
hide_title: false
hide_table_of_contents: false
keywords:
  - oauth_clients
  - account
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>oauth_clients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.oauth_clients" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The OAuth Client ID.  This is used to identify the client, and is a publicly-known value (it is not a secret).<br /> |
| <CopyableCode code="label" /> | `string` | The name of this application.  This will be presented to users when they are asked to grant it access to their Account.<br /> |
| <CopyableCode code="public" /> | `boolean` | If this is a public or private OAuth Client.  Public clients have a slightly different authentication workflow than private clients.  See the &lt;a target="_top" href="https://oauth.net/2/"&gt;OAuth spec&lt;/a&gt; for more details.<br /> |
| <CopyableCode code="redirect_uri" /> | `string` | The location a successful log in from &lt;a target="_top" href="https://login.linode.com"&gt;https://login.linode.com&lt;/a&gt; should be redirected to for this client.  The receiver of this redirect should be ready to accept an OAuth exchange code and finish the OAuth exchange.<br /> |
| <CopyableCode code="secret" /> | `string` | The OAuth Client secret, used in the OAuth exchange.  This is returned as `&lt;REDACTED&gt;` except when an OAuth Client is created or its secret is reset.  This is a secret, and should not be shared or disclosed publicly.<br /> |
| <CopyableCode code="status" /> | `string` | The status of this application.  `active` by default.<br /> |
| <CopyableCode code="thumbnail_url" /> | `string` | The URL where this client's thumbnail may be viewed, or `null` if this client does not have a thumbnail set.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getClient" /> | `SELECT` | <CopyableCode code="clientId" /> | Returns information about a single OAuth client.<br /> |
| <CopyableCode code="getClients" /> | `SELECT` |  | Returns a paginated list of OAuth Clients registered to your Account.  OAuth Clients allow users to log into applications you write or host using their Linode Account, and may allow them to grant some level of access to their Linodes or other entities to your application.<br /> |
| <CopyableCode code="createClient" /> | `INSERT` | <CopyableCode code="data__label, data__redirect_uri" /> | Creates an OAuth Client, which can be used to allow users (using their Linode account) to log in to your own application, and optionally grant your application some amount of access to their Linodes or other entities.<br /> |
| <CopyableCode code="deleteClient" /> | `DELETE` | <CopyableCode code="clientId" /> | Deletes an OAuth Client registered with Linode. The Client ID and Client secret will no longer be accepted by &lt;a target="_top" href="https://login.linode.com"&gt;https://login.linode.com&lt;/a&gt;, and all tokens issued to this client will be invalidated (meaning that if your application was using a token, it will no longer work).<br /> |
| <CopyableCode code="_getClient" /> | `EXEC` | <CopyableCode code="clientId" /> | Returns information about a single OAuth client.<br /> |
| <CopyableCode code="_getClientThumbnail" /> | `EXEC` | <CopyableCode code="clientId" /> | Returns the thumbnail for this OAuth Client.  This is a publicly-viewable endpoint, and can be accessed without authentication.<br /> |
| <CopyableCode code="_getClients" /> | `EXEC` |  | Returns a paginated list of OAuth Clients registered to your Account.  OAuth Clients allow users to log into applications you write or host using their Linode Account, and may allow them to grant some level of access to their Linodes or other entities to your application.<br /> |
| <CopyableCode code="getClientThumbnail" /> | `EXEC` | <CopyableCode code="clientId" /> | Returns the thumbnail for this OAuth Client.  This is a publicly-viewable endpoint, and can be accessed without authentication.<br /> |
| <CopyableCode code="resetClientSecret" /> | `EXEC` | <CopyableCode code="clientId" /> | Resets the OAuth Client secret for a client you own, and returns the OAuth Client with the plaintext secret. This secret is not supposed to be publicly known or disclosed anywhere. This can be used to generate a new secret in case the one you have has been leaked, or to get a new secret if you lost the original. The old secret is expired immediately, and logins to your client with the old secret will fail.<br /> |
| <CopyableCode code="setClientThumbnail" /> | `EXEC` | <CopyableCode code="clientId" /> | Upload a thumbnail for a client you own.  You must upload an image file that will be returned when the thumbnail is retrieved.  This image will be publicly-viewable.<br /> |
| <CopyableCode code="updateClient" /> | `EXEC` | <CopyableCode code="clientId" /> | Update information about an OAuth Client on your Account. This can be especially useful to update the `redirect_uri` of your client in the event that the callback url changed in your application.<br /> |

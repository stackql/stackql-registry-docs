---
title: invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - invitations
  - adexchangebuyer2
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adexchangebuyer2.invitations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `clientAccountId` | `string` | Numerical account ID of the client buyer that the invited user is associated with. The value of this field is ignored in create operations. |
| `email` | `string` | The email address to which the invitation is sent. Email addresses should be unique among all client users under each sponsor buyer. |
| `invitationId` | `string` | The unique numerical ID of the invitation that is sent to the user. The value of this field is ignored in create operations. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_clients_invitations_get` | `SELECT` | `accountId, clientAccountId, invitationId` | Retrieves an existing client user invitation. |
| `accounts_clients_invitations_list` | `SELECT` | `accountId, clientAccountId` | Lists all the client users invitations for a client with a given account ID. |
| `accounts_clients_invitations_create` | `INSERT` | `accountId, clientAccountId` | Creates and sends out an email invitation to access an Ad Exchange client buyer account. |

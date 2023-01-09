---
title: invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - invitations
  - mybusinessaccountmanagement
  - googlemybusiness    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googlemybusiness/stackql-googlemybusiness-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googlemybusiness.mybusinessaccountmanagement.invitations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_invitations_list` | `SELECT` | `accountsId` | Lists pending invitations for the specified account. |
| `accounts_invitations_accept` | `EXEC` | `accountsId, invitationsId` | Accepts the specified invitation. |
| `accounts_invitations_decline` | `EXEC` | `accountsId, invitationsId` | Declines the specified invitation. |

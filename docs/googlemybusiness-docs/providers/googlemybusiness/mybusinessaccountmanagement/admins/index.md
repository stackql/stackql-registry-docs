---
title: admins
hide_title: false
hide_table_of_contents: false
keywords:
  - admins
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
<tr><td><b>Name</b></td><td><code>admins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googlemybusiness.mybusinessaccountmanagement.admins</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_admins_list` | `SELECT` | `accountsId` | Lists the admins for the specified account. |
| `locations_admins_list` | `SELECT` | `locationsId` | Lists all of the admins for the specified location. |
| `accounts_admins_create` | `INSERT` | `accountsId` | Invites the specified user to become an administrator for the specified account. The invitee must accept the invitation in order to be granted access to the account. See AcceptInvitation to programmatically accept an invitation. |
| `locations_admins_create` | `INSERT` | `locationsId` | Invites the specified user to become an administrator for the specified location. The invitee must accept the invitation in order to be granted access to the location. See AcceptInvitation to programmatically accept an invitation. |
| `accounts_admins_delete` | `DELETE` | `accountsId, adminsId` | Removes the specified admin from the specified account. |
| `locations_admins_delete` | `DELETE` | `adminsId, locationsId` | Removes the specified admin as a manager of the specified location. |
| `accounts_admins_patch` | `EXEC` | `accountsId, adminsId` | Updates the Admin for the specified Account Admin. |
| `locations_admins_patch` | `EXEC` | `adminsId, locationsId` | Updates the Admin for the specified location. Only the AdminRole of the Admin can be updated. |

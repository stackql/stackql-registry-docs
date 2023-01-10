---
title: consumer_invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - consumer_invitations
  - data_share
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consumer_invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_share.consumer_invitations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id of the azure resource |
| `name` | `string` | Name of the azure resource |
| `properties` | `object` | Properties of consumer invitation |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Type of the azure resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ConsumerInvitations_Get` | `SELECT` | `api-version, invitationId, location` | Get an invitation |
| `ConsumerInvitations_ListInvitations` | `EXEC` | `api-version` | Lists invitations |
| `ConsumerInvitations_RejectInvitation` | `EXEC` | `api-version, location, data__properties` | Reject an invitation |
